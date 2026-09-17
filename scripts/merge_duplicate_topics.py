"""Fold the duplicate/fragmented MDCAT topic tree back onto the published syllabus.

Three generations of importer each invented their own topic names, and all
three are live at once: the past-paper import's detailed units, the mock
import's coarse buckets ("Organic Chemistry"), and a later mock import's
near-misses ("Work, Energy & Power" beside "Work and Energy", "Op-Amp"
beside "Operational Amplifiers"). Students see the result on /syllabus,
where one chapter appears two or three times under slightly different names
and each copy holds a slice of the questions.

The canonical list is not invented here: it is the PMDC unit list the site
already publishes in /blog/mdcat-2026-syllabus - 16 Biology units, 20
Chemistry, 16 Physics. Anything matching a published unit wins; everything
else folds into it. A handful of real FSc topics that PMDC's list does not
name (Measurements, Optics, Environmental Chemistry, Cell Cycle & Division,
Molecular Biology, Plant Biology, Ecology, Classification & Diversity) are
kept as extra topics rather than forced into a unit they do not belong to.

Questions are never edited - they move with their subtopic, which is what
"re-tagging" means here. Where source and target already hold a subtopic of
the same name, the questions are repointed and the empty duplicate deleted.

Idempotent, and matched by name rather than id so it runs on production
unchanged. Deleting a topic changes /syllabus/<subject>/<topic> URLs, so
every merge here has a matching redirect in the frontend's next.config.ts.

    python manage.py shell -c "exec(open('scripts/merge_duplicate_topics.py').read())"
"""

import re
from django.db import transaction
from django.utils.text import slugify

from content.models import Subject, Topic, Subtopic, Question

DRY_RUN = False

# source topic name -> canonical topic name, per subject.
TOPIC_MERGES = {
    "Physics": {
        "Kinematics": "Force and Motion",
        "Motion and Force": "Force and Motion",
        "Dynamics": "Force and Motion",
        "Work, Energy & Power": "Work and Energy",
        "Circular Motion": "Rotational and Circular Motion",
        "Circular Motion & Gravitation": "Rotational and Circular Motion",
        "Gravitation": "Rotational and Circular Motion",
        "Fluid Mechanics": "Fluid Dynamics",
        "Oscillations": "Waves",
        "Oscillations & Waves": "Waves",
        "Oscillations (SHM)": "Waves",
        "Sound": "Waves",
        "Waves & Sound": "Waves",
        "Magnetism": "Electromagnetism",
        "Electromagnetic Induction & AC": "Electromagnetic Induction",
        "EM Induction and AC": "Electromagnetic Induction",
        "Modern Physics": "Dawn of Modern Physics",
        "Atomic Structure": "Dawn of Modern Physics",
        "Vectors & Equilibrium": "Vectors and Equilibrium",
        # Not PMDC units, but real chapters - one name each instead of three.
        "Measurement": "Measurements",
        "Measurements & Units": "Measurements",
        "Physical Optics": "Optics",
        "Solids": "Deformation of Solids",
    },
    "Chemistry": {
        "Stoichiometry": "Fundamental Concepts of Chemistry",
        "Acids & Bases": "Chemical Equilibrium",
        "Periodic Table": "s and p Block Elements",
        "States of Matter": "Gases",
        "Biological Molecules": "Macromolecules",
        "Coordination Chemistry": "Transition Elements",
    },
    "Biology": {
        "Biomolecules": "Biological Molecules",
        "Genetics": "Inheritance",
        "Human Physiology - Immune System": "Immunity",
        "Human Physiology - Excretion": "Homeostasis",
        "Human Physiology - Nervous & Endocrine": "Coordination and Control",
        "Human Nervous System": "Coordination and Control",
        "Human Endocrine System": "Coordination and Control",
        "Genetic Engineering": "Biotechnology",
        "Growth and Development": "Reproduction",
        "Photosynthesis": "Bioenergetics",
        "Diversity of Life": "Classification & Diversity",
        "Kingdom Plantae": "Plant Biology",
    },
}

# Subtopics filed under the wrong topic entirely - (subject, topic, subtopic)
# -> correct topic. Mostly single questions that an importer dropped into
# whatever topic it happened to be reading at the time.
SUBTOPIC_MOVES = [
    ("Physics", "Work and Energy", "Resistivity and Temperature Coefficient", "Current Electricity"),
    ("Physics", "Work and Energy", "Specific and Molar Specific Heat", "Thermodynamics"),
    ("Physics", "Work and Energy", "First Law of Thermodynamics", "Thermodynamics"),
    ("Physics", "Electromagnetism", "Electrostatics", "Electrostatics"),
    ("Physics", "Alternating Current", "Electromagnetic Spectrum", "Electromagnetism"),
    ("Physics", "Electromagnetism", "Transformer", "Electromagnetic Induction"),
    ("Biology", "Prokaryotes and Viruses", "Viruses", "Acellular Life"),
    ("Biology", "Prokaryotes and Viruses", "Bacteria", "Classification & Diversity"),
    ("Biology", "Prokaryotes and Viruses", "Bacterial Reproduction", "Classification & Diversity"),
    ("Biology", "Prokaryotes and Viruses", "Fungi", "Classification & Diversity"),
]

# Two spellings of the same subtopic inside one topic. (subject, topic,
# loser) -> winner.
SUBTOPIC_MERGES = [
    ("Physics", "Electronics", "Op-Amp", "Operational Amplifiers"),
    ("Physics", "Electronics", "Rectifier", "Rectification (Half and Full Wave)"),
    # Folding the topics above brings each chapter's two vocabularies into one
    # place, where the same subtopic is often listed twice under a short and a
    # long name. Only pairs that are the same thing are listed here - "Energy"
    # and "Kinetic Energy", or "Bacteria" and "Bacterial Reproduction", are
    # left alone.
    ("Physics", "Thermodynamics", "Isothermal", "Isothermal Process"),
    ("Physics", "Thermodynamics", "Kinetic Theory", "Kinetic Theory of Gases"),
    ("Physics", "Thermodynamics", "Specific Heat", "Specific and Molar Specific Heat"),
    ("Physics", "Thermodynamics", "Heat", "Thermal Equilibrium and Heat"),
    ("Physics", "Waves", "Doppler", "Doppler Effect"),
    ("Physics", "Waves", "Doppler Equation", "Doppler Effect"),
    ("Physics", "Waves", "SHM", "Simple Harmonic Motion (SHM)"),
    ("Physics", "Waves", "Oscillations (SHM)", "Simple Harmonic Motion (SHM)"),
    ("Physics", "Waves", "Stationary", "Stationary Waves"),
    ("Physics", "Waves", "Superposition", "Superposition of Waves"),
    ("Physics", "Waves", "Speed", "Wave Speed"),
    ("Physics", "Vectors and Equilibrium", "Equilibrium", "Conditions of Equilibrium"),
    ("Physics", "Vectors and Equilibrium", "Torque", "Torque and Moment of Force"),
    ("Physics", "Work and Energy", "Efficiency", "Energy Losses and Efficiency"),
    ("Physics", "Work and Energy", "Work-Energy Theorem", "Kinetic Energy and Work-Energy Theorem"),
    ("Chemistry", "Chemical Equilibrium", "Chemical Equilibrium (Reversible Reactions)", "Chemical Equilibrium"),
    ("Biology", "Circulation", "Lymphatic", "Lymphatic System"),
    ("Biology", "Classification & Diversity", "Bacteria", "Kingdom Prokaryotae (Bacteria)"),
    ("Biology", "Classification & Diversity", "Fungi", "Kingdom Fungi"),
    ("Biology", "Classification & Diversity", "Five Kingdoms", "Kingdoms"),
    ("Biology", "Coordination and Control", "Impulse", "Nerve Impulse and Reflexes"),
    ("Biology", "Coordination and Control", "Reflex", "Nerve Impulse and Reflexes"),
    ("Biology", "Coordination and Control", "Neuron", "Neurons"),
    ("Biology", "Ecology", "Food Chain", "Food Chain and Food Web"),
    ("Biology", "Enzymes", "Cofactors", "Co-factors of Enzymes"),
    ("Biology", "Enzymes", "Factors", "Factors Affecting Enzyme Action"),
    ("Biology", "Evolution", "Darwin", "Darwinism"),
    ("Biology", "Evolution", "Lamarck", "Lamarckism"),
    ("Biology", "Homeostasis", "Kidney", "Kidney Structure and Function"),
    ("Biology", "Inheritance", "Codominance", "Incomplete Dominance and Codominance"),
    ("Biology", "Inheritance", "Incomplete Dominance", "Incomplete Dominance and Codominance"),
    ("Biology", "Inheritance", "Linkage", "Gene Linkage and Crossing Over"),
    ("Biology", "Plant Biology", "Hormones", "Plant Hormones (Auxins, Gibberellins, etc.)"),
    ("Biology", "Plant Biology", "Photoperiodism", "Photoperiodism and Phytochrome"),
    ("Biology", "Plant Biology", "Transpiration", "Water Movement in Plants (Guttation, Transpiration)"),
    ("Biology", "Plant Biology", "Reproduction", "Reproduction in Angiosperms (Double Fertilization)"),
    ("Biology", "Support and Movement", "Contraction", "Muscle Contraction"),
    ("Biology", "Support and Movement", "Skeleton", "Human Skeleton (Cartilage, Muscle, Bone)"),
    ("Biology", "Support and Movement", "Muscles", "Muscles (Smooth, Cardiac, Skeletal)"),
]


def _norm(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())


def _free_slug(topic, base):
    slug, n = base, 2
    while topic.subtopics.filter(slug=slug).exists():
        slug, n = "%s-%d" % (base, n), n + 1
    return slug


def move_subtopic(st, target_topic, log):
    """Move one subtopic to another topic, folding it into a same-named twin."""
    twin = next((x for x in target_topic.subtopics.all() if _norm(x.name) == _norm(st.name)), None)
    if twin and twin.id == st.id:
        return 0
    if twin:
        n = Question.objects.filter(subtopic=st).update(subtopic=twin)
        log.append("      merged '%s' into %s > %s (%d questions)" % (st.name, target_topic.name, twin.name, n))
        st.delete()
        return n
    count = st.questions.count()
    st.topic = target_topic
    st.slug = _free_slug(target_topic, slugify(st.name) or ("st-%d" % st.id))
    st.save(update_fields=["topic", "slug"])
    log.append("      moved  '%s' -> %s (%d questions)" % (st.name, target_topic.name, count))
    return count


def run():
    log = []
    before = {s.id: Question.objects.filter(subtopic__topic__subject=s).count()
              for s in Subject.objects.all()}
    total_before = Question.objects.count()
    orphan_before = Question.objects.filter(subtopic__isnull=True).count()

    for subject_name, merges in TOPIC_MERGES.items():
        subject = Subject.objects.filter(exam__name="MDCAT", name=subject_name).first()
        if not subject:
            log.append("  SKIP subject %s (not on this database)" % subject_name)
            continue
        log.append("  == %s" % subject_name)
        for source_name, target_name in merges.items():
            source = subject.topics.filter(name=source_name).first()
            target = subject.topics.filter(name=target_name).first()
            if not source:
                continue  # already merged on an earlier run
            if not target:
                log.append("    !! no target topic '%s' for '%s' - left alone" % (target_name, source_name))
                continue
            log.append("    %s -> %s" % (source_name, target_name))
            for st in list(source.subtopics.all()):
                move_subtopic(st, target, log)
            if source.subtopics.count() == 0:
                source.delete()
                log.append("      deleted empty topic '%s'" % source_name)
            else:
                log.append("      !! '%s' still has subtopics - kept" % source_name)

    log.append("  == misfiled subtopics")
    for subject_name, topic_name, st_name, target_name in SUBTOPIC_MOVES:
        subject = Subject.objects.filter(exam__name="MDCAT", name=subject_name).first()
        if not subject:
            continue
        topic = subject.topics.filter(name=topic_name).first()
        target = subject.topics.filter(name=target_name).first()
        if not topic or not target:
            continue
        st = topic.subtopics.filter(name=st_name).first()
        if not st:
            continue
        log.append("    %s > %s -> %s" % (topic_name, st_name, target_name))
        move_subtopic(st, target, log)
        if topic.subtopics.count() == 0:
            topic.delete()
            log.append("      deleted empty topic '%s'" % topic_name)

    log.append("  == duplicate subtopic names inside one topic")
    for subject_name, topic_name, loser_name, winner_name in SUBTOPIC_MERGES:
        subject = Subject.objects.filter(exam__name="MDCAT", name=subject_name).first()
        if not subject:
            continue
        topic = subject.topics.filter(name=topic_name).first()
        if not topic:
            continue
        loser = topic.subtopics.filter(name=loser_name).first()
        winner = topic.subtopics.filter(name=winner_name).first()
        if not loser or not winner:
            continue
        n = Question.objects.filter(subtopic=loser).update(subtopic=winner)
        loser.delete()
        log.append("    %s: '%s' -> '%s' (%d questions)" % (topic_name, loser_name, winner_name, n))

    log.append("  == empty subtopics")
    for st in list(Subtopic.objects.all()):
        if st.questions.count() == 0:
            log.append("    deleted %s / %s > %s" % (st.topic.subject.name, st.topic.name, st.name))
            st.delete()

    # Nothing above may create or destroy a question, or leave one untagged.
    after = {s.id: Question.objects.filter(subtopic__topic__subject=s).count()
             for s in Subject.objects.all()}
    total_after = Question.objects.count()
    orphan_after = Question.objects.filter(subtopic__isnull=True).count()
    problems = ["subject %s: %s -> %s" % (sid, before.get(sid), after.get(sid))
                for sid in before if before.get(sid) != after.get(sid)]
    if total_before != total_after:
        problems.append("question count %d -> %d" % (total_before, total_after))
    if orphan_before != orphan_after:
        problems.append("untagged questions %d -> %d" % (orphan_before, orphan_after))
    return log, problems


with transaction.atomic():
    _log, _problems = run()
    print("\n".join(_log))
    print("")
    if _problems:
        print("ABORTED - question counts moved:")
        for _p in _problems:
            print("   ", _p)
        transaction.set_rollback(True)
    elif DRY_RUN:
        print("DRY RUN - rolled back")
        transaction.set_rollback(True)
    else:
        print("OK - every subject's question count is unchanged")

for _s in Subject.objects.filter(exam__name="MDCAT").order_by("name"):
    print("  %s: %d topics, %d questions" % (
        _s.name, _s.topics.count(),
        Question.objects.filter(subtopic__topic__subject=_s).count()))
