import json
from pathlib import Path

EXPL = {
8467: dict(
    short="'Meticulous' means extremely careful and precise about details.",
    long="Meticulous describes someone who pays great attention to detail, being extremely careful and precise in their work.",
    trick="Don't confuse it with words describing carelessness — meticulous is the opposite of careless/impulsive.",
    options=dict(a="Impulsive means acting without thought, the opposite quality.",
                 b="Lazy is unrelated to precision or care.",
                 c="Correct — meticulous means careful and precise about detail.",
                 d="Careless is the direct opposite of meticulous.")
),
8468: dict(
    short="'Generous' means willing to give freely; its opposite is 'stingy'.",
    long="Generous describes someone who freely gives money, help, or time. The opposite quality is being unwilling to give or spend — stingy.",
    trick="Charitable, giving, and kind are all synonyms of generous, not opposites — watch for synonym distractors in an antonym question.",
    options=dict(a="Charitable is a synonym of generous, not an antonym.",
                 b="Giving is a synonym of generous, not an antonym.",
                 c="Kind is close in meaning to generous, not opposite.",
                 d="Correct — stingy (unwilling to give) is the opposite of generous.")
),
8469: dict(
    short="Subject-verb agreement: 'They were' is correct (plural subject + plural past-tense 'were').",
    long="'They' is a plural pronoun, which takes the plural verb form 'were' in the past tense, not 'was', 'is', or the bare form 'be'.",
    trick="'They was'/'they is'/'they be' are all common non-standard agreement errors — only 'they were' (or 'they are' in present tense) is grammatically correct.",
    options=dict(a="Correct — 'they were' correctly matches the plural subject with past tense.",
                 b="'Was' is singular; it doesn't agree with plural 'they'.",
                 c="'Is' is present tense singular; wrong tense and number.",
                 d="'They be' is not standard grammatical English.")
),
8470: dict(
    short="Hypothetical/subjunctive 'if': use 'were' regardless of subject in a contrary-to-fact condition.",
    long="In a hypothetical or unreal conditional ('If I were you...'), English uses the subjunctive mood, which takes 'were' for all subjects (I/he/she/it included), not 'was'.",
    trick="'If I was you' is a very common everyday error — the subjunctive 'were' is required specifically because this is a hypothetical, not a real past fact.",
    options=dict(a="'If I will be you' mixes future tense incorrectly into a hypothetical condition.",
                 b="Correct — subjunctive 'were' is required in this contrary-to-fact conditional.",
                 c="'If I am you' uses simple present, not the needed subjunctive/hypothetical form.",
                 d="'If I was you' incorrectly uses indicative 'was' instead of subjunctive 'were'.")
),
8471: dict(
    short="'Everyone' is singular and takes the singular verb 'has'.",
    long="Indefinite pronouns like 'everyone', 'everybody', 'each', and 'someone' are grammatically singular, so they take singular verb forms ('has arrived'), even though they refer to a group.",
    trick="Don't be misled by 'of the players' (plural) right before the verb — the verb must agree with 'everyone', the true subject, not the noun in the prepositional phrase.",
    options=dict(a="'Have' is plural; doesn't agree with singular 'everyone'.",
                 b="'Player' should be plural ('players') in this phrase, so this option is also ungrammatical.",
                 c="Correct — 'everyone...has arrived' correctly uses the singular verb.",
                 d="'Were arrived' is not standard English (arrive doesn't use 'were' this way).")
),
8472: dict(
    short="A decision that 'could not be appealed' is 'final'.",
    long="'Final' means conclusive, not open to further discussion or change — exactly matching a decision that cannot be appealed.",
    trick="Tentative, uncertain, and negotiable all suggest a decision that COULD still change — the opposite of what the sentence describes.",
    options=dict(a="Tentative implies the decision could still change, contradicting 'could not be appealed'.",
                 b="Uncertain also implies the decision isn't settled, contradicting the sentence.",
                 c="Negotiable directly contradicts 'could not be appealed'.",
                 d="Correct — 'final' matches a decision that cannot be appealed.")
),
8473: dict(
    short="'To hit the nail on the head' means to describe something exactly/precisely.",
    long="This idiom means to identify or describe a situation, problem, or cause with complete accuracy — like a hammer striking a nail squarely.",
    trick="Don't confuse it with idioms about mistakes or avoidance — this one is specifically about precision/accuracy, a positive meaning.",
    options=dict(a="Correct — it means to identify a cause or issue exactly and accurately.",
                 b="This is nearly the opposite meaning — the idiom is about precision, not carelessness.",
                 c="This describes avoidance, not what the idiom means.",
                 d="This describes irrational argument, unrelated to the idiom's meaning.")
),
8474: dict(
    short="'Neither of the two options' is singular and takes 'was', not 'were'.",
    long="'Neither' (like 'either') is grammatically singular, so it takes a singular verb ('was acceptable'), even when followed by a plural noun phrase like 'of the two options'.",
    trick="The plural noun 'options' right before the verb tempts a plural verb, but 'neither' — the actual subject — is always singular.",
    options=dict(a="This repeats the same 'options were' agreement error and also breaks 'option' to singular incorrectly.",
                 b="Correct — 'neither...was acceptable' fixes the subject-verb agreement (neither = singular).",
                 c="'Are' is plural and still disagrees with singular 'neither'.",
                 d="The original sentence does have an agreement error, so a correction is needed.")
),
8475: dict(
    short="The idiom is 'known for' — 'for' is the correct preposition here.",
    long="'Known for' is the standard fixed preposition used when describing what someone or something is recognized/famous for (a quality, skill, or reputation).",
    trick="Prepositions in fixed phrases like this must be memorized — 'known with/at/about' are not idiomatic in this sense.",
    options=dict(a="'Known with' is not idiomatic English.",
                 b="'Known at' is not the correct fixed preposition here.",
                 c="Correct — 'known for' is the standard idiomatic preposition.",
                 d="'Known about' changes the meaning (implies awareness of something) rather than reputation.")
),
8476: dict(
    short="Arithmetic series with a common difference of 7: 7,14,21,28,35.",
    long="Each term increases by 7 (a multiplication-table pattern: 7x1, 7x2, 7x3, 7x4). The next term is 7x5 = 35.",
    trick="Don't miscalculate the pattern as +7 from 28 giving something other than 35 — always verify by checking the constant difference across all given terms first.",
    options=dict(a="32 doesn't follow the constant +7 pattern (28+7=35, not 32).",
                 b="30 doesn't fit; 28+7=35, not 30.",
                 c="42 would be 7x6, skipping a step — the next term after 28 (7x4) is 7x5=35.",
                 d="Correct — 28+7=35, continuing the multiples-of-7 pattern.")
),
8477: dict(
    short="Perfect squares: 1,4,9,16,25 (1^2,2^2,3^2,4^2,5^2).",
    long="Each term is a perfect square: 1=1^2, 4=2^2, 9=3^2, 16=4^2. The next term is 5^2=25.",
    trick="Don't confuse this with an arithmetic series — the differences here (3,5,7,9) themselves increase, which is the signature of a squares series, not a constant-difference one.",
    options=dict(a="Correct — 5^2 = 25 continues the perfect-squares pattern.",
                 b="24 is not a perfect square and breaks the pattern.",
                 c="20 is not a perfect square.",
                 d="36 is 6^2, skipping ahead — the correct next square after 4^2 is 5^2=25.")
),
8478: dict(
    short="Analogy of tool-to-function: a Pen is used to Write; a Knife is used to Cut.",
    long="This is a tool-to-purpose analogy. A pen's primary function is writing; a knife's primary function is cutting — matching the same relationship.",
    trick="'Sharp' and 'Metal' describe properties of a knife, not its function, and 'Kitchen' is just a place it's often found — none match the Pen:Write function relationship.",
    options=dict(a="Metal describes a material property, not a function, unlike 'Write' for pen.",
                 b="Correct — Cut is Knife's function, matching Write as Pen's function.",
                 c="Kitchen is a location, not a function.",
                 d="Sharp is a property/adjective, not an action/function like 'Write'.")
),
8479: dict(
    short="Artist-to-medium analogy: a Painter works on Canvas; a Sculptor works on Marble.",
    long="This analogy pairs an artist with the material/medium they typically work with. A painter paints on canvas; a sculptor carves/shapes marble (or similar materials like stone).",
    trick="Gallery and Museum are places where finished art is displayed, not the material the artist works ON — don't confuse display venue with working medium.",
    options=dict(a="Brush is a painter's tool, not the sculptor's medium.",
                 b="Gallery is a display venue, not a working medium.",
                 c="Correct — Marble is a medium a sculptor works on, matching Canvas for a painter.",
                 d="Museum is also a display venue, not the sculptor's material.")
),
8480: dict(
    short="'His mother is the only sister of my father' means the man's mother is the woman's paternal aunt — making the man the woman's cousin.",
    long="The woman's father's only sister is the man's mother. So the man's mother is the woman's father's sister, i.e. the woman's paternal aunt. That makes the man the son of the woman's aunt — her cousin.",
    trick="Work through the relation step by step (father's sister = aunt; aunt's son = cousin) rather than guessing from a quick read — these puzzles are solved by tracing the chain precisely.",
    options=dict(a="Brother would require the same parents, which isn't established here.",
                 b="Nephew would apply if the man were the woman's sibling's son, not the case here.",
                 c="Uncle would apply if the man were of the parents' generation, but he's the aunt's son (same generation as the woman).",
                 d="Correct — the man is the son of the woman's paternal aunt, making him her cousin.")
),
8481: dict(
    short="Each letter is shifted forward by 1: DOG->EPH, so CAT->DBU.",
    long="D->E, O->P, G->H is a +1 shift per letter. Applying the same +1 shift to CAT: C->D, A->B, T->U, giving DBU.",
    trick="Verify the shift amount using ALL three letters of the example word, not just the first — a consistent +1 shift confirms the code rule before applying it to the new word.",
    options=dict(a="Correct — shifting C,A,T each forward by 1 gives D,B,U.",
                 b="DBV shifts the last letter by 2 instead of 1 (T should become U, not V).",
                 c="CBU keeps the first letter unshifted, breaking the consistent +1 rule.",
                 d="DBS shifts the last letter backward instead of forward.")
),
8482: dict(
    short="From 'All roses are flowers' and 'Some flowers fade quickly', nothing can be validly concluded specifically about roses fading.",
    long="The two statements only tell us roses are a subset of flowers, and that some (unspecified) flowers fade quickly — those fast-fading flowers might or might not include any roses. No valid syllogistic conclusion links roses specifically to fading.",
    trick="A very common trap is to assume 'some flowers fade quickly' extends to roses just because roses are flowers — but 'some' doesn't guarantee overlap with any particular subset.",
    options=dict(a="'All flowers are roses' reverses the given relationship and isn't stated or implied.",
                 b="Correct — no valid conclusion about roses fading follows from these two premises.",
                 c="'Some flowers are roses' is true from the premises but doesn't answer the question about fading.",
                 d="'All roses fade quickly' incorrectly generalizes from 'some flowers' to 'all roses'.")
),
8483: dict(
    short="Second differences increase by 1 each time: differences are 1,2,3,4, so the next difference is 5, giving 11+5=16.",
    long="1->2 (+1), 2->4 (+2), 4->7 (+3), 7->11 (+4). The differences themselves increase by 1 each step, so the next difference is +5, making the next term 11+5=16.",
    trick="Don't stop at spotting 'the differences increase' — actually track the specific difference sequence (1,2,3,4,...) to predict the next difference correctly.",
    options=dict(a="14 would only be +3 from 11, breaking the increasing-difference pattern.",
                 b="15 would only be +4 from 11, repeating the previous difference instead of increasing it.",
                 c="Correct — the next difference is +5, giving 11+5=16.",
                 d="18 would be +7 from 11, skipping ahead of the correct +5 difference.")
),
8484: dict(
    short="Perpendicular displacement forms a right triangle: distance = sqrt(8^2+15^2) = 17 km.",
    long="Walking 8 km west then 15 km south forms a right angle between the two legs. The straight-line distance from the start is the hypotenuse: sqrt(8^2 + 15^2) = sqrt(64+225) = sqrt(289) = 17 km — the classic 8-15-17 Pythagorean triple.",
    trick="Don't simply add 8+15=23 — that's the total distance walked, not the straight-line displacement from the starting point, which requires the Pythagorean theorem.",
    options=dict(a="23 km is just 8+15 added directly, ignoring that the two legs are perpendicular.",
                 b="120 km would be 8x15 (an area-like product), not a distance calculation.",
                 c="7 km would be 15-8, which has no correct geometric meaning here.",
                 d="Correct — sqrt(8^2+15^2)=17 km is the straight-line distance via the Pythagorean theorem.")
),
}

def main():
    root = Path(__file__).parent.parent
    out = []
    for qid, e in EXPL.items():
        out.append({
            "id": qid,
            "short": e["short"],
            "long": e["long"],
            "trick": e["trick"],
            "options": e["options"],
        })
    out_path = root / "scripts" / "mock20_explanations_eng_lr.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(out)} explanations to {out_path}")

if __name__ == "__main__":
    main()
