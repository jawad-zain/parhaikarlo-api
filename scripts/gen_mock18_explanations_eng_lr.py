import json
from pathlib import Path

OUT = Path(__file__).parent / "mock18_explanations_eng_lr.json"

def I(po): return po + 7944

E = []

def add(po, short, long, trick, a, b, c, d):
    E.append({
        "id": I(po), "short": short, "long": long, "trick": trick,
        "options": {"a": a, "b": b, "c": c, "d": d}
    })

add(163, "'Benevolent' means kind/well-meaning, so 'Kind' is the closest synonym.",
    "'Benevolent' derives from Latin roots meaning 'well-wishing' — describing someone who is kind, generous, and disposed to do good for others. Among the choices, 'Kind' captures this meaning most directly.",
    "Watch for words that sound similar but mean the opposite (like 'Cruel' or 'Selfish') planted as distractors for a positive-meaning word like 'benevolent'.",
    "Incorrect — 'Indifferent' means showing no particular interest or concern, not matching benevolent's warmth.",
    "Incorrect — 'Cruel' is close to the opposite of benevolent's kind, caring meaning.",
    "Correct — 'Kind' most closely matches the meaning of 'benevolent' (well-meaning, generous).",
    "Incorrect — 'Selfish' is essentially opposite to benevolent's other-focused, generous meaning.")

add(164, "'Transparent' (able to be seen through / clear) is opposite in meaning to 'Opaque' (not able to be seen through).",
    "'Transparent' describes something clear enough to see through (literally or, figuratively, easy to understand); its direct opposite is 'opaque', describing something that blocks light/vision (or, figuratively, unclear/hard to understand).",
    "'Obvious', 'Clear', and 'Visible' are actually near-SYNONYMS of transparent, not antonyms — a classic trap of listing synonyms among antonym answer choices.",
    "Incorrect — 'Obvious' is a synonym-adjacent meaning to transparent (easy to perceive), not an opposite.",
    "Incorrect — 'Clear' is essentially synonymous with transparent, not its opposite.",
    "Incorrect — 'Visible' is a related, near-synonymous idea to transparent, not an antonym.",
    "Correct — 'Opaque' is the direct opposite of transparent (blocking rather than allowing light/view through).")

add(165, "'He doesn't know the answer.' correctly pairs the third-person singular subject with 'doesn't' + base verb.",
    "With a third-person singular subject ('He'), standard English grammar requires the auxiliary 'does' (contracted 'doesn't' in the negative) paired with the base form of the main verb ('know'), not 'don't' (for plural/first/second person) or a double-marked verb like 'knows' after 'doesn't'.",
    "Third-person singular subjects (he/she/it) pair with 'does/doesn't', not 'do/don't' — and only ONE part of the sentence should carry the tense/number marking, not both the auxiliary AND the main verb.",
    "Correct — 'doesn't' (does + not) correctly matches the third-person singular subject 'He', followed by the base verb 'know'.",
    "Incorrect — 'don't' is used with plural subjects or I/you, not with the third-person singular 'He'.",
    "Incorrect — this omits the auxiliary 'does' needed to form the negative in English, an ungrammatical construction.",
    "Incorrect — this double-marks the verb (both 'doesn't' and 'knows' carry the -s/does marking), which is grammatically incorrect; only one should.")

add(166, "The subjunctive mood after 'it is essential that' calls for the bare/base verb form ('attend'), not 'attends'.",
    "Certain expressions of necessity, demand, or recommendation ('it is essential/necessary/important that...') trigger the subjunctive mood in formal English, which uses the bare infinitive form of the verb regardless of subject (e.g. 'that he attend', not 'that he attends').",
    "Subjunctive-triggering phrases ('essential that', 'suggest that', 'recommend that', 'insist that') always take the BASE verb form, even with third-person singular subjects — a rule many students overlook since it looks 'ungrammatical' at first glance.",
    "Incorrect — 'attends' incorrectly uses the regular third-person singular form instead of the subjunctive base form required after 'it is essential that'.",
    "Correct — 'attend' (the bare/base verb form) is the correct subjunctive mood usage after 'it is essential that he...'.",
    "Incorrect — besides the subjunctive verb-form issue, 'attends to the meeting' incorrectly adds 'to', which is not idiomatic with 'attend' meaning 'be present at'.",
    "Incorrect — 'will attend' uses future tense, which is not the subjunctive construction called for by 'it is essential that'.")

add(167, "'Neither of the answers is correct.' — 'neither of' takes a singular verb.",
    "'Neither' (and 'either') is grammatically singular, even when followed by a plural noun phrase like 'of the answers' — so the verb must agree in the singular ('is'), not the plural ('are').",
    "'Neither of / Either of + plural noun' still takes a SINGULAR verb — a frequently tested subject-verb agreement exception where the nearby plural noun tempts a wrong plural verb choice.",
    "Incorrect — besides the verb agreement error ('are' should be singular), 'answer' should be plural ('answers') to match 'of the...'.",
    "Incorrect — 'are' incorrectly treats 'neither' as plural; it should be the singular 'is'.",
    "Correct — 'is' correctly agrees with the singular subject 'neither', despite the plural 'answers' immediately before it.",
    "Incorrect — 'were' is both plural (wrong for 'neither') and past tense, which doesn't fit this general-truth statement.")

add(168, "'Compromise' fits a resolution that satisfies both parties in a negotiation.",
    "A compromise is an agreement reached where each side makes concessions, resulting in an outcome acceptable to both — exactly matching 'satisfied both parties'. 'Impasse', 'conflict', and 'deadlock' all describe failure to reach agreement, the opposite sense needed here.",
    "The sentence explicitly says the outcome 'satisfied both parties' — that phrase alone rules out any word implying a stalemate or disagreement (impasse, deadlock, conflict).",
    "Incorrect — an 'impasse' is a situation with no agreement/progress, the opposite of an outcome satisfying both parties.",
    "Incorrect — 'conflict' implies ongoing disagreement, not a resolution satisfying both sides.",
    "Incorrect — a 'deadlock' means negotiations are stuck with no resolution, contradicting the sentence's description of mutual satisfaction.",
    "Correct — 'compromise' is the only option describing a mutually satisfying resolution, matching the sentence's context.")

add(169, "'To bite the bullet' idiomatically means to face a difficult situation with courage/resolve, not to avoid it.",
    "This idiom originates from historical practices where a patient would literally bite on a bullet to cope with pain during surgery without anesthesia — it now figuratively means to bravely endure or confront something unpleasant or difficult that can't be avoided.",
    "The idiom is about FACING difficulty head-on (with courage), not avoiding it — a common misreading is to assume 'biting' something means rejecting/avoiding it.",
    "Incorrect — this is essentially the opposite meaning; the idiom is about confronting, not avoiding, a difficult situation.",
    "Correct — 'to bite the bullet' means to face a difficult or unpleasant situation with courage/resolve.",
    "Incorrect — the idiom has nothing to do with causing harm to another person.",
    "Incorrect — the idiom relates to enduring hardship, not celebrating success, an unrelated meaning.")

add(170, "The subject-verb agreement in 'neither...nor' follows the noun CLOSER to the verb — here 'students' (plural), so 'were' is correct.",
    "With correlative conjunctions like 'neither...nor' or 'either...or', the verb agrees with whichever subject is grammatically closer to it. Since 'students' (plural) is the nearer subject to the verb, the plural form 'were' is required, not the singular 'was' used in the original sentence.",
    "'Neither X nor Y' agreement rule: match the verb to Y (the second/nearer item), not X — the original sentence's 'was' incorrectly matched the farther singular 'teacher' instead of the nearer plural 'students'.",
    "Incorrect — this only adds 'about', an unnecessary/incorrect preposition change, while leaving the actual subject-verb agreement error ('was' with plural 'students') uncorrected.",
    "Correct — 'were' correctly agrees with the nearer plural subject 'students' in this neither...nor construction.",
    "Incorrect — needlessly pluralizes 'teacher' to 'teachers' and singularizes 'student', which doesn't fix (and actually complicates) the actual agreement issue with the original nouns.",
    "Incorrect — the original sentence does contain a real subject-verb agreement error ('was' should be 'were'), so 'no correction needed' is incorrect.")

add(171, "'Interested in' is the correct, idiomatic preposition pairing with the adjective 'interested'.",
    "English fixed prepositional phrases must often simply be memorized: 'interested IN' (a subject/topic) is the standard, correct collocation — 'interested on/at/for' are not idiomatic English.",
    "Preposition questions like this test memorized collocations rather than logic — 'interested in' is one of the most common fixed pairings to know by heart.",
    "Incorrect — 'interested on' is not standard, idiomatic English.",
    "Incorrect — 'interested at' is not the correct idiomatic preposition pairing here.",
    "Correct — 'interested in' is the standard, correct idiomatic preposition pairing.",
    "Incorrect — 'interested for' is not the correct idiomatic construction for expressing interest in a subject.")

add(172, "The series 5, 10, 15, 20 increases by a constant +5 each step, so the next term is 25.",
    "This is a simple arithmetic sequence with a common difference of +5 (5, 10, 15, 20, 25, ...) — each term is found by adding 5 to the previous one.",
    "Always find the DIFFERENCE between consecutive terms first — here it's a constant +5, an arithmetic (not geometric) progression.",
    "Incorrect — 22 doesn't follow the constant +5 pattern established by the previous terms.",
    "Incorrect — 24 doesn't match adding 5 to the previous term (20).",
    "Incorrect — 30 would be 20+10, skipping ahead by double the established step size.",
    "Correct — 20 + 5 = 25, continuing the established +5 pattern.")

add(173, "The series 2, 5, 10, 17 has increasing differences 3, 5, 7 (consecutive odd numbers), so the next difference is 9, giving 17+9=26.",
    "Looking at consecutive differences: 5-2=3, 10-5=5, 17-10=7 — these differences themselves increase by 2 each time (an odd-number pattern: 3,5,7,9,...). The next difference should be 9, so the next term is 17+9=26.",
    "When a simple constant difference doesn't work, check the SECOND-LEVEL differences (differences of the differences) — a very common trick in number series questions.",
    "Correct — following the 3,5,7,9 difference pattern, 17+9=26 is the next term.",
    "Incorrect — 24 doesn't match the established +9 next-difference pattern (17+7=24 would repeat the previous difference instead of increasing it).",
    "Incorrect — 28 overshoots the expected next difference of +9 (17+9=26, not +11=28).",
    "Incorrect — 30 significantly overshoots the pattern; it doesn't correspond to the correctly identified difference sequence.")

add(174, "Bird:Nest as Bee:Hive — each animal is paired with its characteristic dwelling/home structure.",
    "This is a classic 'animal to its home' analogy: a bird builds/lives in a nest, just as a bee builds/lives in a hive — matching the relationship type (creature -> its constructed living space).",
    "Identify the RELATIONSHIP first (animal -> its home), then find the option matching that exact relationship type, not just any bee-related word.",
    "Incorrect — a flower is a source of nectar/pollen for bees, not their home/dwelling — a different relationship than 'nest' is to 'bird'.",
    "Correct — a hive is a bee's home, exactly matching how a nest is a bird's home.",
    "Incorrect — honey is a product made by bees, not their dwelling place — doesn't match the 'creature-to-home' relationship.",
    "Incorrect — a wing is a body part of a bee, an entirely different relationship type than 'animal to its home'.")

add(175, "Doctor:Hospital as Teacher:School — each professional is paired with their characteristic workplace.",
    "This analogy pairs a profession with the institution/building where that profession is typically practiced: a doctor works in a hospital, just as a teacher works in a school.",
    "Match the relationship (profession -> workplace), not surface-level word associations like 'teacher relates to book/student' which describe a DIFFERENT kind of relationship.",
    "Incorrect — a student is who a teacher teaches, not the teacher's workplace — a different relationship (person-to-person, not person-to-place).",
    "Incorrect — a book is a tool a teacher might use, not their workplace.",
    "Correct — a school is a teacher's workplace, exactly matching how a hospital is a doctor's workplace.",
    "Incorrect — 'classroom exam' is an activity/event associated with teaching, not the institution/workplace itself.")

add(176, "The woman is the man's sister: 'my grandfather's only son' (given the man has no other siblings) refers to the man's own father, so 'daughter of my father' = sister.",
    "Since the man states he has no siblings other than possibly the woman in question, 'my grandfather's only son' must be the man's own father (there being effectively one son of the grandfather who is the man's own father, given the stated constraint). The daughter of the man's father is therefore the man's sister.",
    "Trace the relationship one careful step at a time: grandfather -> his only son (= the man's father, given the stated no-other-siblings constraint) -> that son's daughter (= the man's sister).",
    "Incorrect — 'niece' would apply if the son in question were the man's uncle rather than his own father; the constraint given points to his own father instead.",
    "Incorrect — 'cousin' would apply if the son were an uncle (a sibling of the man's father), not the man's own father as established here.",
    "Incorrect — 'aunt' would make her older/an elder relative, but the given relationship instead identifies her as the man's own generation (a sibling).",
    "Correct — given the stated constraint, 'my grandfather's only son' is the man's own father, making the pictured woman his sister.")

add(177, "APPLE -> BQQMF uses a simple +1 letter-shift cipher, so MANGO -> NBOHP.",
    "Checking each letter: A->B, P->Q, P->Q, L->M, E->F — every letter is shifted forward by exactly one position in the alphabet. Applying the same +1 shift to MANGO: M->N, A->B, N->O, G->H, O->P, giving NBOHP.",
    "Verify the cipher rule on EVERY letter of the given example (not just the first one) before applying it to the new word — a partial check can miss inconsistent letter shifts.",
    "Correct — applying the confirmed +1 shift to each letter of MANGO gives N-B-O-H-P.",
    "Incorrect — the last letter is shifted incorrectly here (O should become P under a +1 shift, not Q).",
    "Incorrect — the first letter is shifted incorrectly here (M should become N under a +1 shift, not stay as M).",
    "Incorrect — the fourth letter is shifted incorrectly here (G should become H under a +1 shift, not P).")

add(178, "All doctors are educated + no educated people are illiterate logically implies no doctors are illiterate.",
    "Since every doctor belongs to the 'educated' category (premise 1), and the 'educated' category has zero overlap with 'illiterate' (premise 2), doctors — being a subset of educated people — must also have zero overlap with 'illiterate'. This is a valid categorical syllogism (a chain of set inclusion).",
    "Draw this out as nested/overlapping circles (Venn diagram): Doctors ⊆ Educated, and Educated ∩ Illiterate = empty, so Doctors ∩ Illiterate must also be empty — a clean, valid syllogistic conclusion.",
    "Incorrect — this directly contradicts both given premises; the logic guarantees the opposite (no doctors are illiterate).",
    "Correct — since doctors are a subset of educated people, and no educated people are illiterate, no doctors can be illiterate either.",
    "Incorrect — this reverses/overgeneralizes the relationship; the premises establish doctors are a SUBSET of educated people, not that illiterate people are doctors.",
    "Incorrect — while true that some educated people are doctors, this doesn't follow as the direct LOGICAL conclusion being tested here (the more specific 'no doctors are illiterate' is the actual valid syllogistic conclusion).")

add(179, "The series 3, 6, 11, 18, 27 has increasing differences 3,5,7,9,11 (odd numbers), so the next term is 27+11=38.",
    "Consecutive differences: 6-3=3, 11-6=5, 18-11=7, 27-18=9 — each difference increases by 2 (an odd-number sequence 3,5,7,9,11,...). The next difference should be 11, giving 27+11=38.",
    "As in similar number-series questions, when the first-level differences aren't constant, check whether THOSE differences themselves form a recognizable pattern (here, consecutive odd numbers).",
    "Incorrect — 40 overshoots the correctly identified next difference of +11 (27+13=40 would use the wrong next difference).",
    "Incorrect — 36 undershoots; it corresponds to a next difference of only +9 (repeating the previous difference instead of increasing it to 11).",
    "Correct — following the 3,5,7,9,11 difference pattern, 27+11=38 is the next term.",
    "Incorrect — 34 corresponds to a next difference of only +7, two less than the correctly identified pattern's next difference of +11.")

add(180, "By the Pythagorean theorem, 6 km east + 8 km north gives a straight-line distance of sqrt(6^2+8^2)=sqrt(100)=10 km from the start.",
    "The man's path forms a right angle (east then north), so his displacement from the start is the hypotenuse of a right triangle with legs 6 km and 8 km: distance = sqrt(6^2 + 8^2) = sqrt(36+64) = sqrt(100) = 10 km. (This is the well-known 6-8-10 Pythagorean triple, a scaled-up 3-4-5 triangle.)",
    "Direction-sense problems with a 90-degree turn always reduce to the Pythagorean theorem on the two straight-line legs — recognizing 6-8-10 as a scaled 3-4-5 triple makes this instant.",
    "Incorrect — 14 km would result from simply adding the two legs (6+8) rather than correctly applying the Pythagorean theorem for the straight-line distance.",
    "Incorrect — 48 km is the product of the two legs (6x8), not the actual displacement distance.",
    "Incorrect — 2 km doesn't correspond to any correct calculation of the displacement here.",
    "Correct — sqrt(6^2+8^2) = sqrt(100) = 10 km, the straight-line distance from the starting point.")

data = E
print(f"Eng+LR batch: {len(data)} entries, ids {data[0]['id']}-{data[-1]['id']}")
assert len(data) == 18
OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print("wrote", OUT)
