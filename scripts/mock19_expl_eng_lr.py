import json
from pathlib import Path

EXPL = {
8287: dict(
    short="'Candid' means frank/honest, matching 'Frank' most closely.",
    long="'Candid' describes speaking openly, honestly, and without reservation. 'Frank' is the closest synonym among the options, sharing this exact meaning of direct honesty.",
    trick="Don't be fooled by 'Secretive' or 'Deceptive' — these are near-opposite in meaning to candid, not synonyms.",
    options=dict(a="'Hostile' means aggressive/unfriendly, unrelated to honesty.",
                 b="Correct — 'Frank' means open and honest, the closest synonym to 'Candid.'",
                 c="'Secretive' is nearly opposite in meaning to candid (which implies openness).",
                 d="'Deceptive' is essentially opposite to candid (which implies truthfulness).")
),
8288: dict(
    short="'Abundant' (plentiful) is opposite in meaning to 'Scarce.'",
    long="'Abundant' means existing in large quantities; its antonym is 'Scarce,' meaning insufficient or rare in supply.",
    trick="'Plentiful' is actually a SYNONYM of abundant, not its opposite — watch for synonym distractors when asked for an antonym.",
    options=dict(a="'Generous' relates to giving freely, not really an antonym of abundant.",
                 b="'Wealthy' relates to having money/riches, not a direct antonym of abundant.",
                 c="'Plentiful' is a synonym of abundant, not its opposite.",
                 d="Correct — 'Scarce' (in short supply) is the direct opposite of 'Abundant.'")
),
8289: dict(
    short="Correct subject-verb agreement: 'She doesn't like coffee.'",
    long="With third-person singular subjects using the auxiliary 'does' (doesn't), the main verb should be in its base/plain form: 'doesn't like' (not 'doesn't likes' or 'don't like').",
    trick="'Doesn't' already carries the third-person singular '-s'; adding '-s' again to the main verb ('doesn't likes') is a double-marking error.",
    options=dict(a="'Not likes' is an incorrect negative construction, missing the auxiliary 'does.'",
                 b="'Doesn't likes' incorrectly double-marks the verb — the base form 'like' should follow 'doesn't.'",
                 c="'Don't' is used for I/you/we/they, not for the third-person singular 'she' — should be 'doesn't.'",
                 d="Correct — 'doesn't' (auxiliary) + base verb 'like' properly agrees with the singular subject 'she.'")
),
8290: dict(
    short="'Suggest that he go...' uses the subjunctive mood (base verb) correctly.",
    long="Verbs like 'suggest,' 'recommend,' and 'insist' trigger the subjunctive mood in the 'that' clause, which uses the base form of the verb regardless of subject — hence 'that he go,' not 'goes' or 'going.'",
    trick="This is a classic subjunctive-mood trap: even though 'he' is third-person singular (which would normally take 'goes'), suggestion/demand verbs require the plain base form in the subordinate clause.",
    options=dict(a="'He going' is not a complete/correct verb form for this clause.",
                 b="'He will go' avoids the required subjunctive construction after 'suggest that.'",
                 c="'He goes' incorrectly applies standard subject-verb agreement instead of the subjunctive base form required here.",
                 d="Correct — the subjunctive mood after 'suggest that' requires the base form 'go,' regardless of the third-person subject.")
),
8291: dict(
    short="'Each of the students HAS submitted...' — 'each' takes a singular verb.",
    long="'Each' is a singular indefinite pronoun, even when followed by a plural noun phrase like 'of the students' — the verb must agree with 'each' (singular), so 'has submitted' is correct, not 'have submitted.'",
    trick="Don't be misled by the plural noun ('students') sitting right before the verb — always identify the TRUE grammatical subject ('each'), which is singular here.",
    options=dict(a="'The student' is grammatically odd/incomplete here, and 'have' still mismatches the singular 'each.'",
                 b="'Were submitted' uses passive voice incorrectly and mismatches with 'each' (which needs a singular active verb).",
                 c="'Have submitted' incorrectly treats 'each' as plural — it should be singular ('has').",
                 d="Correct — 'each' is singular, so 'has submitted' is the grammatically correct agreement.")
),
8292: dict(
    short="'Resolute' fits the context of remaining firm despite criticism.",
    long="The sentence describes someone standing by their decision despite heavy criticism — 'resolute' (firm, determined, unwavering) precisely fits this meaning, contrasting with words implying doubt or change of mind.",
    trick="'Wavering' and 'Hesitant' describe indecision, which is the OPPOSITE of what the sentence describes (remaining firm despite criticism) — don't pick a word that contradicts the sentence's clear meaning.",
    options=dict(a="Correct — 'Resolute' (firm, unwavering) fits remaining firm 'despite criticism.'",
                 b="'Hesitant' implies indecision, contradicting the idea of remaining firm despite criticism.",
                 c="'Indifferent' implies not caring, which doesn't fit 'remained ___ in her decision' (implying steadfastness).",
                 d="'Wavering' implies changing one's mind, the opposite of remaining firm despite criticism.")
),
8293: dict(
    short="'Let the cat out of the bag' means to accidentally reveal a secret.",
    long="This common idiom means to accidentally disclose information that was meant to be kept secret, often unintentionally spoiling a surprise or confidential matter.",
    trick="Don't confuse this idiom (revealing a secret) with the opposite meaning (keeping a secret) — the imagery of the cat 'escaping the bag' evokes something getting out/exposed, not staying contained.",
    options=dict(a="Correct — the idiom means to accidentally reveal a secret.",
                 b="The idiom is not about anger; it's specifically about revealing hidden information.",
                 c="The idiom is not about ignoring a problem; it's about disclosure of a secret.",
                 d="This is essentially the OPPOSITE meaning — the idiom is about secrets getting OUT, not being kept.")
),
8294: dict(
    short="Correction: 'Each of the boys HAS finished HIS homework...'",
    long="'Each' is singular, so it requires a singular verb ('has,' not 'have') and, traditionally, a singular pronoun ('his,' not 'their') to maintain grammatical agreement throughout the sentence.",
    trick="Both the verb AND the pronoun need to agree with the singular 'each' — a sentence can look 'almost right' by fixing only one of the two agreement errors, so check both.",
    options=dict(a="'Each of the boy' is grammatically wrong; it should remain 'boys' (plural noun after 'each of the').",
                 b="'Have finished' still mismatches 'each' (should be singular 'has'), even though the pronoun 'his' was fixed.",
                 c="The original sentence does have an error ('have' should be 'has'), so 'no correction needed' is incorrect.",
                 d="Correct — 'has finished his homework' fixes BOTH the verb and pronoun to agree with singular 'each.'")
),
8295: dict(
    short="'Capable of' is the correct prepositional phrase.",
    long="'Capable' idiomatically pairs with the preposition 'of' (e.g., 'capable of doing something'), a fixed collocation in English.",
    trick="Preposition questions like this often can't be reasoned out logically — they depend on memorized fixed collocations ('capable of,' not 'capable for/in/at').",
    options=dict(a="'Capable for' is not the correct idiomatic preposition pairing.",
                 b="'Capable in' is not the correct idiomatic preposition pairing.",
                 c="Correct — 'capable of' is the standard fixed collocation.",
                 d="'Capable at' is not the correct idiomatic preposition pairing.")
),
8296: dict(
    short="Series 4,8,12,16 increases by 4 each time; next is 20.",
    long="The pattern adds 4 at each step (4, 8, 12, 16, 20...), a simple arithmetic sequence with common difference 4.",
    trick="Double-check by verifying the difference is CONSTANT (always +4) rather than assuming a different (e.g., multiplicative) pattern.",
    options=dict(a="22 doesn't fit the consistent +4 pattern (would require a +6 jump).",
                 b="24 doesn't fit the consistent +4 pattern (would require an +8 jump).",
                 c="18 doesn't fit the consistent +4 pattern (would only be a +2 jump).",
                 d="Correct — continuing the +4 pattern: 16+4=20.")
),
8297: dict(
    short="Series 3,6,11,18: differences are 3,5,7 -> next difference 9 -> 27.",
    long="The differences between consecutive terms are 3 (6-3), 5 (11-6), 7 (18-11) — an increasing odd-number pattern. The next difference should be 9, giving 18+9=27.",
    trick="This is a second-order (difference-of-differences) pattern, not a simple constant addition — always check if the FIRST differences themselves form a recognizable pattern when a simple arithmetic check fails.",
    options=dict(a="24 would only add 6, not matching the growing +3,+5,+7,+9 difference pattern.",
                 b="25 would only add 7 again, not continuing the growing difference pattern.",
                 c="Correct — following the +3,+5,+7,+9 difference pattern: 18+9=27.",
                 d="29 would add 11, overshooting the expected next difference of 9.")
),
8298: dict(
    short="Fish:Gills as Human:Lungs (both are respiratory organs for their organism).",
    long="This analogy compares respiratory organs: gills are how fish breathe (extract oxygen from water), and lungs are the corresponding organ by which humans breathe (extract oxygen from air).",
    trick="Focus on the FUNCTIONAL relationship (the respiratory organ), not just any random body part — skin, blood, and heart don't serve the same specific 'breathing organ' role that gills do for fish.",
    options=dict(a="Skin is a respiratory surface for some organisms (like amphibians) but not the primary human breathing organ analogous to fish gills.",
                 b="Blood carries oxygen but is not itself the breathing/gas-exchange organ (that's the lungs).",
                 c="The heart pumps blood; it is not the respiratory (gas-exchange) organ.",
                 d="Correct — lungs are the human respiratory organ, analogous to gills in fish.")
),
8299: dict(
    short="Author:Book as Composer:Symphony (creator to their created work).",
    long="This analogy compares a creator to their created artistic work: an author writes a book, and a composer writes/creates a symphony (a musical composition).",
    trick="'Instrument' or 'Orchestra' relate to music but aren't the composer's CREATED WORK the way a book is the author's — the analogy specifically needs the parallel 'creator makes THIS finished work.'",
    options=dict(a="An orchestra performs music but isn't itself the composer's created WORK (the composition), unlike a book being the author's created work.",
                 b="Correct — a symphony is the composer's created work, paralleling a book being the author's created work.",
                 c="An instrument is a tool used to play music, not the composer's created work itself.",
                 d="A concert is an event/performance, not the composer's created work (the composition) itself.")
),
8300: dict(
    short="The boy is the woman's own son (mother's only daughter = the woman herself).",
    long="'My mother's only daughter' refers to the woman herself (since she has no siblings, she is her mother's only daughter). So 'the son of my mother's only daughter' means 'my own son.'",
    trick="These blood-relation riddles hinge on carefully identifying who a phrase like 'my mother's only daughter' actually refers to — work it out step by step rather than guessing based on the surface wording.",
    options=dict(a="Cousin doesn't fit, since 'my mother's only daughter' is the woman herself, not an aunt's child.",
                 b="Brother would require the described person to be male and a sibling, but the phrase points to the woman's OWN child.",
                 c="Correct — since the woman has no siblings, she is her mother's only daughter, so the boy is her own son.",
                 d="Nephew would apply if the daughter referred to were someone else's mother's daughter (a sister), but here it's the woman herself.")
),
8301: dict(
    short="Coding pattern: each letter shifts forward by 1 (TABLE->UBCMF); CHAIR->DIBJS.",
    long="Comparing TABLE to UBCMF: T->U, A->B, B->C, L->M, E->F — each letter shifts forward by exactly one position in the alphabet. Applying the same shift to CHAIR: C->D, H->I, A->B, I->J, R->S, giving DIBJS.",
    trick="Verify the shift amount and direction using ALL letter pairs in the example word, not just the first one — a consistent 'shift by 1 forward' pattern should hold for every letter.",
    options=dict(a="CIBJS doesn't apply a consistent +1 shift to every letter (the first letter is wrong).",
                 b="DHBJS doesn't correctly shift every letter by +1 (the second letter is wrong).",
                 c="Correct — shifting every letter of CHAIR forward by 1 gives DIBJS.",
                 d="DIBJT applies the shift correctly to most letters but incorrectly to the last one (R should become S, not T).")
),
8302: dict(
    short="All scientists are logical; no logical people are superstitious -> no scientists are superstitious.",
    long="This is a valid syllogism: All S are L (scientists are logical), and No L are Sup (logical people aren't superstitious). By transitivity, no scientists can be superstitious (since all scientists fall within the 'logical' group, which is entirely excluded from 'superstitious').",
    trick="Watch for syllogism traps that try to reverse or invalidly combine the premises — here, the valid conclusion follows a clean 'All A are B, No B are C, therefore No A are C' chain.",
    options=dict(a="This reverses the logical direction incorrectly; it isn't a valid conclusion from the premises.",
                 b="This weakens the conclusion unnecessarily ('some') when the premises actually support the STRONGER universal conclusion ('no').",
                 c="Correct — since all scientists are logical, and no logical people are superstitious, no scientists can be superstitious.",
                 d="This directly contradicts the second premise (no logical people are superstitious, and all scientists are logical).")
),
8303: dict(
    short="Series 2,5,10,17,26: differences are 3,5,7,9 -> next difference 11 -> 37.",
    long="The differences between consecutive terms are 3 (5-2), 5 (10-5), 7 (17-10), 9 (26-17) — increasing by 2 each time (a quadratic pattern). The next difference should be 11, giving 26+11=37.",
    trick="This is the same 'growing odd-number difference' pattern type as other number-series questions — always compute the first differences and look for a recognizable secondary pattern.",
    options=dict(a="39 would require a difference of 13, overshooting the expected next difference of 11.",
                 b="Correct — continuing the +3,+5,+7,+9,+11 difference pattern: 26+11=37.",
                 c="33 would require a difference of only 7, repeating an earlier difference instead of continuing the growth.",
                 d="35 would require a difference of only 9, repeating the previous difference instead of the expected 11.")
),
8304: dict(
    short="Pythagorean theorem: distance = sqrt(9² + 12²) = sqrt(225) = 15 km.",
    long="The man's path forms a right angle (north then east), so his straight-line distance from the start is the hypotenuse of a right triangle with legs 9 km and 12 km: sqrt(9²+12²) = sqrt(81+144) = sqrt(225) = 15 km.",
    trick="Don't simply add the two distances (9+12=21) — since the turns are perpendicular, you need the Pythagorean theorem for the direct (straight-line) distance, not the total path length walked.",
    options=dict(a="3 km doesn't match the Pythagorean calculation for these leg lengths.",
                 b="108 km would result from squaring and forgetting to take the square root (or a similar large-scale error).",
                 c="21 km is simply the SUM of the two legs (total distance walked), not the direct straight-line distance.",
                 d="Correct — sqrt(9²+12²) = sqrt(225) = 15 km is the direct distance from the starting point.")
),
}

def main():
    root = Path(__file__).parent.parent
    out = []
    for qid, e in EXPL.items():
        out.append({"id": qid, "short": e["short"], "long": e["long"], "trick": e["trick"], "options": e["options"]})
    out_path = root / "scripts" / "mock19_explanations_eng_lr.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(out)} explanations to {out_path}")

if __name__ == "__main__":
    main()
