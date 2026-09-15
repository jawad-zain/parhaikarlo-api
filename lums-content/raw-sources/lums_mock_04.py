"""
LUMS Common Admission Test (LCAT) - Full-Length Mock Test #3
=============================================================
ParhaiKarlo-prepared full-length mock test. NOT an official LUMS past paper.
Answer keys prepared by content team, pending human verification.

Nothing in this file is taken from LUMS' official "Sample Questions for
Verbal & Math Sections" guide (raw-sources/sample_lcat_2025.pdf), nor from
`lums_lcat_mock_01.py` or `lums_lcat_mock_02.py`. Every question below is
newly written; the topic and subtopic assigned to each question slot mirrors
the position it occupies in Mocks 1 and 2 (same section, same slot), since
those labels were already verified against the syllabus when those mocks
were checked in.

Format (mirrors the real LCAT's ~3-hour, 7-module shape, ~25 min per section):

    Section 1  Verbal   18 Q   (q1-18)
    Section 2  Math     17 Q   (q19-35)
    Section 3  Verbal   17 Q   (q36-52)
    Section 4  Math     17 Q   (q53-69)
    Section 5  Verbal   17 Q   (q70-86)
    Section 6  Math     17 Q   (q87-103)
    Section 7  Verbal   17 Q   (q104-120)
                       ------
                        120 Q   (Verbal 69 / Math 51 -- 57.5% / 42.5%,
                                 matching the official sample's 14/10 split)

No calculator: the official guide states calculators are not allowed, so every
Math item below is solvable by hand in well under 90 seconds.

Reading-comprehension items are deliberately SELF-CONTAINED -- each one carries
its own passage inline, because `content.models.Question` has no `context`
field for a shared passage block (see lums-content/README.md, "Schema"). Where
several questions share a passage the passage text is repeated verbatim in each.

Topic / subtopic strings are the CANONICAL vocabulary from
lums-content/syllabus/lums_syllabus.json -- nothing invented. That means the
Groq tagger is skipped for this bank, exactly as it is for lums_lcat_sample.py
and the earlier mocks.

Each question is a dict:
    id, section, subject, topic, subtopic, difficulty, question,
    options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.
"""

SOURCE = "parhaikarlo_mock_03"

# Every question in this bank must land is_verified=False on import -- the
# answer keys below were derived by the content team, not by LUMS.
NEEDS_REVIEW = True

SECTIONS = [
    (1, "Verbal", 18),
    (2, "Math", 17),
    (3, "Verbal", 17),
    (4, "Math", 17),
    (5, "Verbal", 17),
    (6, "Math", 17),
    (7, "Verbal", 17),
]

QUESTIONS = [

# ============================================================
# SECTION 1 - VERBAL (18) - q1-18
# ============================================================

{"id": 1, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Easy",
 "question": "The Mughal engineers who designed Lahore's Shalimar Gardens built an unusually ____ terrace system: water fell from one level to the next by gravity alone, and not a single pump was needed anywhere along its course. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "careless", "B": "temporary", "C": "crude", "D": "ingenious"},
 "answer": "D"},

{"id": 2, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Medium",
 "question": "Text: \"Gwadar is routinely described as Pakistan's gateway to Central Asia. The description is not wrong on a map. It obscures a harder fact on the ground: the road and rail links that would actually carry freight from Gwadar into Central Asia remain, for the most part, unbuilt.\" Which choice best describes the function of the second and third sentences in the text as a whole?",
 "options": {"A": "They concede that the map-based description is entirely false.",
             "B": "They offer an example confirming the first sentence.",
             "C": "They qualify the map-based description by pointing out infrastructure it assumes that does not yet exist.",
             "D": "They summarise a scholarly consensus the author endorses."},
 "answer": "C"},

{"id": 3, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: Community-managed trophy hunting of markhor lets villages earn revenue directly from a permitted, limited hunt, which gives them a direct incentive to protect the herd from poachers. Text 2: Revenue from a handful of permits, however large, is a fragile incentive: it depends on a foreign hunter's willingness to pay, and any disruption to that market removes the villagers' reason to protect the herd overnight. Based on the texts, how would the author of Text 2 most likely respond to Text 1's claim about a direct incentive?",
 "options": {"A": "By agreeing fully and proposing no changes to the programme.",
             "B": "By arguing that the incentive Text 1 describes is real but dependent on an external market that could collapse.",
             "C": "By denying that any revenue reaches villagers at all.",
             "D": "By conceding that poaching has stopped entirely because of the programme."},
 "answer": "B"},

{"id": 4, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Easy",
 "question": "Passage: Herders in the Cholistan desert have long followed a seasonal pattern known locally as Rohi: families move their cattle and camels toward the toba wells scattered across the dunes as surface water dries up, then move again once those wells run low, tracing a route their grandparents followed before them. Aid agencies once tried to settle these families permanently near a handful of new tube wells, assuming a fixed water source would improve their lives. Herd sizes fell instead, because a single well cannot support grazing pressure the way a moving herd, spread across dozens of wells in rotation, can. What is the main idea of the passage?",
 "options": {"A": "Fixed tube wells have made pastoral life easier for Cholistani herders.",
             "B": "Camels are better suited to desert conditions than cattle.",
             "C": "Cholistani herders no longer follow the traditional Rohi migration pattern.",
             "D": "Settling herders near a single well undermined the rotational grazing that seasonal migration between many wells had long supported."},
 "answer": "D"},

{"id": 5, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: Over a decade, the number of registered mango exporters in Sindh roughly doubled, while the share of the crop rejected at the port for spoilage barely changed. Most of the new exporters entered the trade without investing in pre-cooling facilities, relying instead on the same open-air loading practices smaller traders had always used. Which choice most logically completes the reasoning in the passage?",
 "options": {"A": "Therefore, mango spoilage rates are likely to fall sharply in coming years.",
             "B": "Therefore, the growth in exporters appears to have expanded the trade without addressing the cold-chain gap that drives spoilage.",
             "C": "Therefore, Sindh's mango exporters primarily sell within the domestic market.",
             "D": "Therefore, pre-cooling facilities have become standard practice across the industry."},
 "answer": "B"},

{"id": 6, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A researcher claims that a district's rise in total wheat output was driven more by an increase in cultivated area than by any rise in yield per hectare. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Output rose 32%, and the government support price for wheat rose 15%.",
             "B": "Output rose 32%, while cultivated area rose 4% and yield per hectare rose 27%.",
             "C": "Output fell 6%, while cultivated area rose 29%.",
             "D": "Output rose 32%, while cultivated area rose 29% and yield per hectare rose 2%."},
 "answer": "D"},

{"id": 7, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "While researching the poet Shah Abdul Latif Bhittai, a student compiles three notes: he composed verse in the Sindhi language rather than Persian, the court language of his time; his poetry drew on the everyday lives of fisherfolk, herders and desert travellers; and his shrine at Bhit Shah still hosts all-night sung recitations of his verse. Which statement best synthesises these notes?",
 "options": {"A": "Bhittai wrote in Sindhi rather than the era's court language, drew his imagery from ordinary rural life, and his verse is still sung at all-night gatherings at his shrine.",
             "B": "Bhittai's poetry was written primarily for the Mughal court.",
             "C": "The shrine at Bhit Shah was built long after Bhittai's death and has no connection to his poetry.",
             "D": "Bhittai's verse is rarely performed today."},
 "answer": "A"},

{"id": 8, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "Faisalabad's power-loom sheds multiplied rapidly once cheap imported machinery became available in the 1990s. ____ most of those sheds still run on unmetered or informally metered electricity connections, and the city's transmission losses remain among the highest in the province. Which transition best completes the text?",
 "options": {"A": "Similarly,", "B": "For example,", "C": "Consequently,", "D": "In addition,"},
 "answer": "C"},

{"id": 9, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: phulkari embroidery is worked in darning stitches from the reverse side of the cloth; a single large phulkari shawl can take months to complete; the craft was traditionally made by a bride's female relatives as part of her dowry; commercial workshops now produce faster machine-embroidered versions. The student wants to emphasise the contrast between the traditional practice and today's commercial versions. Which choice best accomplishes this goal?",
 "options": {"A": "Phulkari is worked in darning stitches from the reverse side of the cloth.",
             "B": "Commercial workshops produce machine-embroidered phulkari today.",
             "C": "Phulkari shawls were traditionally part of a bride's dowry.",
             "D": "A phulkari shawl traditionally took a bride's female relatives months to complete by hand, a pace commercial workshops now bypass with machine embroidery."},
 "answer": "D"},

{"id": 10, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "The collection of handwritten Sufi manuscripts held at the shrine library ____ more than two hundred separate volumes. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "include", "B": "are including", "C": "includes", "D": "have include"},
 "answer": "C"},

{"id": 11, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "The fishing communities along the Balochistan coast opposed the new trawling licences, and ____ objections were later raised in the provincial assembly. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "its", "B": "their", "C": "it's", "D": "there"},
 "answer": "B"},

{"id": 12, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The inspection team reached one firm conclusion ____ the embankment had been built well below the specified height. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", that", "B": ", being", "C": "; which", "D": ": "},
 "answer": "D"},

{"id": 13, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Medium",
 "question": "The canal had run dry for three straight months ____ farmers in the tail-end villages abandoned their cotton crop altogether. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "; ", "B": ", ", "C": " which ", "D": " and which "},
 "answer": "A"},

{"id": 14, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Having examined the tomb inscriptions at Makli for over a decade, ____\"",
 "options": {"A": "the conclusion of the archaeologists was that several dynasties were represented.",
             "B": "it was concluded by the archaeologists that several dynasties were represented.",
             "C": "the archaeologists concluded that several dynasties were represented.",
             "D": "several dynasties were shown by the archaeologists to be represented."},
 "answer": "C"},

{"id": 15, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: Empress Market is usually described as a Karachi landmark, a phrase that flattens what the building actually does. Its clock tower draws photographs, but the real activity is underneath it: a produce and livestock market that has operated on the same site, under the same vaulted arcades, for well over a century, feeding a rotating cast of neighbourhoods that has otherwise been rebuilt many times over. Read that way, the market is less a monument than a piece of continuously working infrastructure that happens to have a clock tower attached. Which choice best states the main idea of the passage?",
 "options": {"A": "Empress Market's clock tower is its most historically significant feature.",
             "B": "Empress Market functions less as a monument and more as continuously operating market infrastructure.",
             "C": "The neighbourhoods around Empress Market have never been rebuilt.",
             "D": "Empress Market has operated only intermittently over the past century."},
 "answer": "B"},

{"id": 16, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: Empress Market is usually described as a Karachi landmark, a phrase that flattens what the building actually does. Its clock tower draws photographs, but the real activity is underneath it: a produce and livestock market that has operated on the same site, under the same vaulted arcades, for well over a century, feeding a rotating cast of neighbourhoods that has otherwise been rebuilt many times over. Read that way, the market is less a monument than a piece of continuously working infrastructure that happens to have a clock tower attached. The author's attitude toward describing Empress Market simply as a \"landmark\" is best characterised as",
 "options": {"A": "openly contemptuous.", "B": "mildly corrective.", "C": "entirely neutral.", "D": "wistfully nostalgic."},
 "answer": "B"},

{"id": 17, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as RESILIENT.",
 "options": {"A": "fragile", "B": "indifferent", "C": "cautious", "D": "hardy"},
 "answer": "D"},

{"id": 18, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to the underlined word as it is used here: \"The committee's report was praised for its IMPARTIAL account of the dispute.\"",
 "options": {"A": "biased", "B": "lengthy", "C": "informal", "D": "confidential"},
 "answer": "A"},

# ============================================================
# SECTION 2 - MATH (17) - q19-35
# ============================================================

{"id": 19, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Easy",
 "question": "If 6(x - 1) + 4 = 2x + 18, what is the value of x?",
 "options": {"A": "4", "B": "5", "C": "6", "D": "7"},
 "answer": "B"},

{"id": 20, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 4x + y = 22 and x - y = 3, what is the value of x?",
 "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
 "answer": "C"},

{"id": 21, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "Which of the following describes all values of x for which 7 - 2x > 15?",
 "options": {"A": "x > -4", "B": "x < 4", "C": "x > 4", "D": "x < -4"},
 "answer": "D"},

{"id": 22, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Medium",
 "question": "An arithmetic sequence has first term 9 and common difference 5. What is the sum of its first 12 terms?",
 "options": {"A": "438", "B": "420", "C": "450", "D": "408"},
 "answer": "A"},

{"id": 23, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "The equation x^2 + kx + 20 = 0 has roots 4 and 5. What is the value of k?",
 "options": {"A": "-9", "B": "9", "C": "-20", "D": "20"},
 "answer": "A"},

{"id": 24, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is the value of 16^(3/4) * 9^(1/2)?",
 "options": {"A": "18", "B": "24", "C": "32", "D": "12"},
 "answer": "B"},

{"id": 25, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "What is the value of (log_4 64) - (log_3 9)?",
 "options": {"A": "1", "B": "2", "C": "5", "D": "0"},
 "answer": "A"},

{"id": 26, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "If 1/x + 1/(3x) = 4/9, what is the value of x?",
 "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
 "answer": "C"},

{"id": 27, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "A shopkeeper raises the price of an item by 20% and then, in a sale, reduces the new price by 25%. Compared with the original price, the final price is",
 "options": {"A": "10% higher.", "B": "10% lower.", "C": "unchanged.", "D": "5% lower."},
 "answer": "B"},

{"id": 28, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Easy",
 "question": "A sum of Rs. 135,000 is divided between two partners in the ratio 5 : 4. By how much does the larger share exceed the smaller share, in rupees?",
 "options": {"A": "10,000", "B": "25,000", "C": "20,000", "D": "15,000"},
 "answer": "D"},

{"id": 29, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "A class of 15 students has a mean score of 60. Five more students, whose mean score is 84, join the class. What is the mean score of all 20 students?",
 "options": {"A": "64", "B": "66", "C": "68", "D": "70"},
 "answer": "B"},

{"id": 30, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A bag contains 6 red marbles and 8 blue marbles. Two marbles are drawn at random without replacement. What is the probability that both are red?",
 "options": {"A": "15/91", "B": "3/14", "C": "6/49", "D": "5/26"},
 "answer": "A"},

{"id": 31, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A rectangle has a perimeter of 46 cm, and its length is 5 cm greater than its width. What is its area, in square centimetres?",
 "options": {"A": "117", "B": "126", "C": "130", "D": "112"},
 "answer": "B"},

{"id": 32, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Easy",
 "question": "A right triangle has legs of length 10 cm and 24 cm. What is its perimeter, in centimetres?",
 "options": {"A": "54", "B": "58", "C": "60", "D": "64"},
 "answer": "C"},

{"id": 33, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Easy",
 "question": "A circle has an area of 64pi square centimetres. What is its circumference, in centimetres?",
 "options": {"A": "8pi", "B": "64pi", "C": "32pi", "D": "16pi"},
 "answer": "D"},

{"id": 34, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Ratios", "difficulty": "Medium",
 "question": "In a right triangle, theta is an acute angle and sin(theta) = 8/17. What is the value of cos(theta)?",
 "options": {"A": "15/17", "B": "8/15", "C": "17/15", "D": "8/17"},
 "answer": "A"},

{"id": 35, "section": 2, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the least common multiple of 8 and 12, minus their greatest common divisor?",
 "options": {"A": "16", "B": "18", "C": "20", "D": "22"},
 "answer": "C"},

# ============================================================
# SECTION 3 - VERBAL (17) - q36-52
# ============================================================

{"id": 36, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "Though celebrated at its opening as revolutionary, the new market-price app for farmers proved largely ____: adoption stalled at a few hundred users, most of whom stopped checking it within a month. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "transformative", "B": "contentious", "C": "negligible", "D": "premature"},
 "answer": "C"},

{"id": 37, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Urban planners have long modelled bus rapid transit as a simple substitution: replace private cars with buses, and congestion falls in proportion to the cars removed. The model is tidy, and it predicts a straightforward drop in road traffic. That is not what ridership surveys along Lahore's Metrobus corridor show: a large share of new riders previously walked, cycled or used a rickshaw, not a private car.\" Which choice best describes the function of the final sentence in the text as a whole?",
 "options": {"A": "It supplies an example confirming the model's prediction.",
             "B": "It introduces survey evidence that conflicts with the model's prediction.",
             "C": "It proposes a refinement to make the model easier to apply.",
             "D": "It restates the model's claim in more concrete terms."},
 "answer": "B"},

{"id": 38, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: Over three decades, the total tonnage of wheat stored in government warehouses grew steadily, while post-harvest losses to rodents and damp reported by the same warehouses barely fell. Agricultural auditors caution against reading steady storage growth as evidence of better preservation: much of the growth simply reflects more warehouses built to the same ageing design, not any improvement in how grain is protected once it arrives. Which choice best states the main idea of the passage?",
 "options": {"A": "Government wheat storage has become substantially more efficient over three decades.",
             "B": "Total storage tonnage is a more useful statistic than loss rates.",
             "C": "Rodent damage has been eliminated from government warehouses.",
             "D": "Growth in stored tonnage reflects more warehouses of an unchanged design rather than any real gain in preservation."},
 "answer": "D"},

{"id": 39, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: Pakistan's marine fisheries are licensed province by province, but the trawlers that draw the most complaints from small fishing communities routinely cross provincial waters in a single trip, and the same vessel is often registered in one province while fishing mainly off the coast of another. It follows that separate provincial catch records ____ Which choice most logically completes the text?",
 "options": {"A": "should be compiled more frequently than they currently are.",
             "B": "cannot simply be added together to produce a reliable national catch total.",
             "C": "will always overstate the true catch in each province.",
             "D": "are the only practical method of monitoring trawlers."},
 "answer": "B"},

{"id": 40, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "In a study of Data Darbar's shrine economy in Lahore, a researcher argues that most visitors come less for formal religious instruction than for a sense of communal belonging the shrine's courtyard provides. Which quotation from a visitor interview, if authentic, would most directly support that argument?",
 "options": {"A": "\"I come here mainly to attend the scheduled lectures on scripture.\"",
             "B": "\"I don't come for a sermon -- I come to sit in the courtyard where everyone, whoever they are, is welcome at the same table.\"",
             "C": "\"The shrine's annual festival draws visitors from across the province.\"",
             "D": "\"Donations at the shrine fund a free kitchen for the poor.\""},
 "answer": "B"},

{"id": 41, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student researching Chitral's traditional freestyle polo records three observations: it is played on a narrower, unfenced ground than modern polo; matches historically had no fixed limit on the number of players per side; and the sport predates the codified rules introduced under British colonial administration. Which statement best synthesises these observations?",
 "options": {"A": "Chitral's traditional polo is played on a narrower ground with no fixed team size, and it predates the codified rules British administrators later introduced.",
             "B": "Chitral's polo ground is fenced on all sides.",
             "C": "Modern codified polo rules originated in Chitral.",
             "D": "Chitral's polo matches always feature exactly six players per side."},
 "answer": "A"},

{"id": 42, "section": 3, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "Karachi's Empress Market survived British colonial rule, Partition, and decades of unregulated encroachment largely unchanged. ____ a 2018 anti-encroachment drive removed hundreds of surrounding stalls in a matter of days, altering the market's footprint more than any single event in over a century. Which transition best completes the text?",
 "options": {"A": "Consequently,", "B": "In short,", "C": "Similarly,", "D": "By contrast,"},
 "answer": "D"},

{"id": 43, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The programme trains community wardens to monitor water levels, to report embankment damage, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "coordinating evacuation drills each monsoon season.",
             "B": "they coordinate evacuation drills each monsoon season.",
             "C": "to coordinate evacuation drills each monsoon season.",
             "D": "evacuation drills are coordinated each monsoon season."},
 "answer": "C"},

{"id": 44, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The tour covered three sites along the Indus ____ Attock Fort, Kalabagh and the Chashma barrage. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ": ", "B": ", ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 45, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "Each of the fourteen union councils ____ required to appoint a flood warden. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "are", "B": "were", "C": "is", "D": "have been"},
 "answer": "C"},

{"id": 46, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Hard",
 "question": "The embankment was raised in 2014 ____ breaches along the same stretch have grown more frequent every monsoon since. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ", however ", "C": " and which ", "D": "; nevertheless, "},
 "answer": "D"},

{"id": 47, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: The shrine pool at Manghopir on Karachi's outskirts has sheltered a colony of marsh crocodiles for centuries, and for most of that time the arrangement worked in the crocodiles' favour: pilgrims fed them, and killing one was considered deeply inauspicious. Urban expansion has complicated that old bargain. The stream that once fed the pool now runs low for much of the year, cut off by upstream construction, and the colony survives increasingly on water trucked in rather than water that arrives on its own. Conservationists note that the crocodiles are in no immediate danger of extinction -- the species survives elsewhere in Sindh's wetlands -- but they warn that a population once sustained by a living river is now sustained mainly by intervention, and that the distinction matters for how the site should be managed going forward. Which choice best states the main idea of the passage?",
 "options": {"A": "The marsh crocodiles at Manghopir face imminent extinction.",
             "B": "Urban expansion has shifted the Manghopir crocodile colony from a self-sustaining river-fed population to one that depends on active human intervention.",
             "C": "Pilgrims have stopped visiting the shrine pool at Manghopir.",
             "D": "The marsh crocodile no longer survives anywhere else in Sindh."},
 "answer": "B"},

{"id": 48, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: The shrine pool at Manghopir on Karachi's outskirts has sheltered a colony of marsh crocodiles for centuries, and for most of that time the arrangement worked in the crocodiles' favour: pilgrims fed them, and killing one was considered deeply inauspicious. Urban expansion has complicated that old bargain. The stream that once fed the pool now runs low for much of the year, cut off by upstream construction, and the colony survives increasingly on water trucked in rather than water that arrives on its own. Conservationists note that the crocodiles are in no immediate danger of extinction -- the species survives elsewhere in Sindh's wetlands -- but they warn that a population once sustained by a living river is now sustained mainly by intervention, and that the distinction matters for how the site should be managed going forward. According to the passage, how is the Manghopir crocodile pool's water supply now largely maintained?",
 "options": {"A": "By a natural stream that still flows freely year-round.",
             "B": "By water trucked in, since the stream that once fed it runs low much of the year.",
             "C": "By seasonal monsoon rainfall alone.",
             "D": "By a new canal built specifically for the shrine."},
 "answer": "B"},

{"id": 49, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: The shrine pool at Manghopir on Karachi's outskirts has sheltered a colony of marsh crocodiles for centuries, and for most of that time the arrangement worked in the crocodiles' favour: pilgrims fed them, and killing one was considered deeply inauspicious. Urban expansion has complicated that old bargain. The stream that once fed the pool now runs low for much of the year, cut off by upstream construction, and the colony survives increasingly on water trucked in rather than water that arrives on its own. Conservationists note that the crocodiles are in no immediate danger of extinction -- the species survives elsewhere in Sindh's wetlands -- but they warn that a population once sustained by a living river is now sustained mainly by intervention, and that the distinction matters for how the site should be managed going forward. The author's attitude toward conservationists' distinction between a self-sustaining and an intervention-sustained population is best characterised as",
 "options": {"A": "dismissive.", "B": "uncritically celebratory.", "C": "treating the distinction as a meaningful basis for management decisions.", "D": "indifferent to the outcome."},
 "answer": "C"},

{"id": 50, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: The shrine pool at Manghopir on Karachi's outskirts has sheltered a colony of marsh crocodiles for centuries, and for most of that time the arrangement worked in the crocodiles' favour: pilgrims fed them, and killing one was considered deeply inauspicious. Urban expansion has complicated that old bargain. The stream that once fed the pool now runs low for much of the year, cut off by upstream construction, and the colony survives increasingly on water trucked in rather than water that arrives on its own. Conservationists note that the crocodiles are in no immediate danger of extinction -- the species survives elsewhere in Sindh's wetlands -- but they warn that a population once sustained by a living river is now sustained mainly by intervention, and that the distinction matters for how the site should be managed going forward. It can most reasonably be inferred that the author regards the crocodile colony's current stability as",
 "options": {"A": "proof that urban expansion has had no real effect on the site.",
             "B": "secure for the same reasons it always was.",
             "C": "dependent on continued human intervention rather than on the natural conditions that originally sustained it.",
             "D": "irrelevant to how the site should be managed."},
 "answer": "C"},

{"id": 51, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as INSCRUTABLE.",
 "options": {"A": "transparent", "B": "predictable", "C": "talkative", "D": "unfathomable"},
 "answer": "D"},

{"id": 52, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The new tariff structure will TELL heavily on small importers within a year,\" the word \"tell\" most nearly means",
 "options": {"A": "narrate.", "B": "have a noticeable effect.", "C": "distinguish.", "D": "count aloud."},
 "answer": "B"},

# ============================================================
# SECTION 4 - MATH (17) - q53-69
# ============================================================

{"id": 53, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in Two Variables", "difficulty": "Medium",
 "question": "A line in the xy-plane passes through the points (2, 7) and (5, 19). What is the y-coordinate of its y-intercept?",
 "options": {"A": "-1", "B": "1", "C": "2", "D": "-2"},
 "answer": "A"},

{"id": 54, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "The function f is defined by f(x) = 5x - 6. If f(a) = 19, what is the value of a?",
 "options": {"A": "4", "B": "7", "C": "6", "D": "5"},
 "answer": "D"},

{"id": 55, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 5x + 2y = 28 and 3x - 2y = 4, what is the value of y?",
 "options": {"A": "2", "B": "3", "C": "4", "D": "5"},
 "answer": "C"},

{"id": 56, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "A delivery van weighs 1,100 kg when empty, and the total weight of the loaded van must not exceed 2,000 kg. If each crate weighs 50 kg, what is the greatest number of whole crates the van can carry?",
 "options": {"A": "16", "B": "17", "C": "18", "D": "19"},
 "answer": "C"},

{"id": 57, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Nonlinear Functions", "difficulty": "Medium",
 "question": "What is the minimum value of the function f(x) = x^2 - 8x + 5?",
 "options": {"A": "-9", "B": "11", "C": "-13", "D": "-11"},
 "answer": "D"},

{"id": 58, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Polynomial Expressions", "difficulty": "Easy",
 "question": "Which expression is equivalent to (3x + 2)(x - 4)?",
 "options": {"A": "3x^2 - 10x - 8", "B": "3x^2 - 14x - 8", "C": "3x^2 + 10x - 8", "D": "3x^2 - 10x + 8"},
 "answer": "A"},

{"id": 59, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "How many real solutions does the equation x^2 + 3x + 9 = 0 have?",
 "options": {"A": "Two distinct real solutions", "B": "Exactly one real solution", "C": "Infinitely many real solutions", "D": "No real solutions"},
 "answer": "D"},

{"id": 60, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is sqrt(45) + sqrt(20) in simplest radical form?",
 "options": {"A": "5*sqrt(5)", "B": "3*sqrt(13)", "C": "2*sqrt(13)", "D": "sqrt(65)"},
 "answer": "A"},

{"id": 61, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Unit Conversion", "difficulty": "Easy",
 "question": "A car consumes fuel at a rate of 7 litres per 100 kilometres. How many litres will it consume on a 250-kilometre journey at that rate?",
 "options": {"A": "15", "B": "20", "C": "17.5", "D": "12.5"},
 "answer": "C"},

{"id": 62, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Two-Variable Data Interpretation (tables/graphs)", "difficulty": "Medium",
 "question": "A shop records the number of units sold on each of five days: Monday 40, Tuesday 48, Wednesday 36, Thursday 45, Friday 50. By what percentage did the number of units sold increase from Wednesday to Thursday?",
 "options": {"A": "20%", "B": "30%", "C": "15%", "D": "25%"},
 "answer": "D"},

{"id": 63, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "For the data set 2, 5, 5, 7, 11, what is the mean minus the median?",
 "options": {"A": "0", "B": "1", "C": "2", "D": "3"},
 "answer": "B"},

{"id": 64, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "After a 15% discount, an item sells for Rs. 4,250. What was its price before the discount, in rupees?",
 "options": {"A": "5,000", "B": "4,887.5", "C": "4,750", "D": "4,600"},
 "answer": "A"},

{"id": 65, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Medium",
 "question": "A cube has a volume of 512 cubic centimetres. What is its total surface area, in square centimetres?",
 "options": {"A": "384", "B": "256", "C": "320", "D": "512"},
 "answer": "A"},

{"id": 66, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Easy",
 "question": "The three interior angles of a triangle are in the ratio 4 : 5 : 6. What is the measure of the largest angle, in degrees?",
 "options": {"A": "90", "B": "60", "C": "80", "D": "72"},
 "answer": "D"},

{"id": 67, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Medium",
 "question": "A sector of a circle of radius 10 cm has a central angle of 45 degrees. What is the area of the sector, in square centimetres?",
 "options": {"A": "12.5pi", "B": "10pi", "C": "25pi", "D": "20pi"},
 "answer": "A"},

{"id": 68, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Identities", "difficulty": "Medium",
 "question": "For any angle theta with cos(theta) not equal to 0, which expression is equivalent to tan(theta) * cos(theta)?",
 "options": {"A": "sin(theta)", "B": "cos(theta)", "C": "1", "D": "cot(theta)"},
 "answer": "A"},

{"id": 69, "section": 4, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Easy",
 "question": "What is the sum of all prime numbers strictly between 40 and 50?",
 "options": {"A": "121", "B": "125", "C": "131", "D": "137"},
 "answer": "C"},

# ============================================================
# SECTION 5 - VERBAL (17) - q70-86
# ============================================================

{"id": 70, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "The arbitrator's decision was notable for its ____: it addressed each of the nine contested clauses individually, with a separate finding and citation for each. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "brevity", "B": "ambiguity", "C": "leniency", "D": "thoroughness"},
 "answer": "D"},

{"id": 71, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: A single national curriculum, taught identically in every school, is the fairest way to guarantee that every student receives the same education. Text 2: An identical curriculum guarantees identical content, not an identical education, when schools differ wildly in trained teachers, working labs, and functioning libraries; the curriculum only standardises what is supposed to be taught, not what is actually learned. Based on the texts, the author of Text 2 would most likely characterise Text 1's claim about guaranteeing sameness as",
 "options": {"A": "false, because the curriculum itself varies between schools.",
             "B": "correct, and sufficient on its own to ensure equal outcomes.",
             "C": "accurate about what is prescribed but incomplete about what schools can actually deliver.",
             "D": "irrelevant, because teacher training has no measurable effect on outcomes."},
 "answer": "C"},

{"id": 72, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: Attock Fort sits at the point where the Kabul river meets the Indus, and it is usually described for its walls, which rise directly from the water on three sides. The more consequential fact is its placement: for centuries, any army or caravan crossing between the Punjab plains and the routes into Afghanistan had to pass beneath those walls, which made the fort less a fortress in the ordinary sense than a toll gate that happened to be heavily armed. Which choice best states the main idea of the passage?",
 "options": {"A": "Attock Fort's chief significance lies in controlling a key river crossing rather than in the height of its walls.",
             "B": "Attock Fort's walls rise from the water on all four sides.",
             "C": "The Kabul river no longer meets the Indus at Attock.",
             "D": "Attock Fort was built mainly as a ceremonial residence."},
 "answer": "A"},

{"id": 73, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A city introduced free morning bus service along a single corridor to reduce car use. In the first year, average car traffic on that corridor fell by 12 per cent. Over the same period, ridership on the free buses rose far more than the number of cars that disappeared could account for. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "the free buses had no effect on ridership.",
             "B": "most of the new bus riders were previously driving cars on that corridor.",
             "C": "at least some of the new riders switched from walking, cycling or paid transport rather than from driving.",
             "D": "car traffic fell because of factors entirely unrelated to the bus service."},
 "answer": "C"},

{"id": 74, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A hospital claims its new triage system reduced waiting times more for emergency cases than for routine ones. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Average waiting time for emergency cases fell by 22 minutes, while waiting time for routine cases fell by 3 minutes.",
             "B": "The hospital's overall average waiting time fell by 12 minutes.",
             "C": "Routine cases had the shortest waiting times in the hospital both before and after the change.",
             "D": "Staffing levels increased across all departments during the study period."},
 "answer": "A"},

{"id": 75, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student compiles three observations about Rawalpindi's Liaquat Bagh: it was originally laid out as a public park under British administration; it was renamed after the country's first prime minister; and it was the site of his assassination in 1951, and it still hosts major political rallies today. Which statement best synthesises these observations?",
 "options": {"A": "Liaquat Bagh, originally a colonial-era public park later renamed for the country's first prime minister and the site of his 1951 assassination, remains a venue for major political rallies.",
             "B": "Liaquat Bagh was built specifically as a memorial to the prime minister's assassination.",
             "C": "The park has been closed to the public since 1951.",
             "D": "Liaquat Bagh predates British administration in the region."},
 "answer": "A"},

{"id": 76, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "The archive digitised its collection of colonial-era land records over a four-year project. ____ a researcher in Multan can now search deeds that once required a personal visit to a single office in Lahore. Which transition best completes the text?",
 "options": {"A": "Nevertheless,", "B": "Admittedly,", "C": "By comparison,", "D": "As a result,"},
 "answer": "D"},

{"id": 77, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: the National Horse and Cattle Show in Lahore began as a small agricultural exhibition; it now features livestock competitions, military band displays and folk dance performances over several days; attendance draws visitors from across the province; the event has run almost every year since the 1950s. The student wants to emphasise the show's growth from a narrow purpose into a broad public event. Which choice best accomplishes this goal?",
 "options": {"A": "The National Horse and Cattle Show has run almost every year since the 1950s.",
             "B": "What began as a small agricultural exhibition has grown into a multi-day event combining livestock competitions, military displays and folk performances.",
             "C": "The event draws visitors from across the province each year.",
             "D": "The show features livestock competitions among its many attractions."},
 "answer": "B"},

{"id": 78, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The tribunal's findings ____ released in September, drew immediate criticism from both parties. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ": ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 79, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "Every one of the surveyed shopkeepers reported that ____ electricity bill had roughly doubled that year. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "their", "B": "it's", "C": "its", "D": "whose"},
 "answer": "A"},

{"id": 80, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Built where the Kabul river meets the Indus and armed on three sides, ____\"",
 "options": {"A": "historians regard Attock Fort as a strategic landmark.",
             "B": "the fort's walls are what most visitors remember.",
             "C": "Attock Fort still commands the crossing between Punjab and the routes to Afghanistan.",
             "D": "it is the river crossing that Attock Fort commands."},
 "answer": "C"},

{"id": 81, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The report praised the cooperative's transparent accounting, its trained staff, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "it paid members promptly.",
             "B": "that its payments were prompt.",
             "C": "paying members promptly.",
             "D": "the promptness of its payments to members."},
 "answer": "D"},

{"id": 82, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Hard",
 "question": "Neither the site engineer nor the two contractors ____ willing to accept responsibility for the delay. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "was", "B": "is", "C": "has been", "D": "were"},
 "answer": "D"},

{"id": 83, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Hard",
 "question": "Passage: For decades Balochistan's coastal fishing communities have blamed their declining catch on foreign trawlers working just outside the legal boundary, and the complaint is not baseless. It does not fully explain why catch per boat has fallen even in seasons when trawler activity was reported as light. Marine biologists point instead to a slower, less visible cause: juvenile fish are being taken in far greater numbers by small local boats using fine-mesh nets, a practice that predates large-scale trawling and has simply expanded alongside it. The fix, on this reading, is not solely a matter of policing the boundary. It is also a matter of what mesh size local boats are permitted to use. Which choice best states the main idea of the passage?",
 "options": {"A": "Foreign trawlers are the sole cause of the decline in Balochistan's coastal catch.",
             "B": "The decline in catch is better explained by fine-mesh local fishing practices than by trawlers alone.",
             "C": "Catch per boat has risen in seasons with light trawler activity.",
             "D": "Local boats should be banned from fishing entirely."},
 "answer": "B"},

{"id": 84, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: For decades Balochistan's coastal fishing communities have blamed their declining catch on foreign trawlers working just outside the legal boundary, and the complaint is not baseless. It does not fully explain why catch per boat has fallen even in seasons when trawler activity was reported as light. Marine biologists point instead to a slower, less visible cause: juvenile fish are being taken in far greater numbers by small local boats using fine-mesh nets, a practice that predates large-scale trawling and has simply expanded alongside it. The fix, on this reading, is not solely a matter of policing the boundary. It is also a matter of what mesh size local boats are permitted to use. It can most reasonably be inferred that the author would agree with which statement?",
 "options": {"A": "Policing the trawler boundary alone would resolve the decline in catch.",
             "B": "Local fine-mesh fishing has had no measurable effect on fish stocks.",
             "C": "Regulating local mesh size would address a cause of the decline that boundary enforcement cannot.",
             "D": "Trawler activity has increased steadily every season for decades."},
 "answer": "C"},

{"id": 85, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as FRUGAL.",
 "options": {"A": "lavish", "B": "thrifty", "C": "generous", "D": "reckless"},
 "answer": "B"},

{"id": 86, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The board's decision to delay the merger was largely a GUARDED move,\" the word \"guarded\" most nearly means",
 "options": {"A": "protected by security.", "B": "cautious rather than open.", "C": "financially risky.", "D": "legally mandated."},
 "answer": "B"},

# ============================================================
# SECTION 6 - MATH (17) - q87-103
# ============================================================

{"id": 87, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Medium",
 "question": "If x/4 - 5 = x/9, what is the value of x?",
 "options": {"A": "30", "B": "33", "C": "36", "D": "40"},
 "answer": "C"},

{"id": 88, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Hard",
 "question": "In an arithmetic sequence the 6th term is 17 and the 11th term is 42. What is the first term?",
 "options": {"A": "-8", "B": "-3", "C": "3", "D": "8"},
 "answer": "A"},

{"id": 89, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "A taxi charges a fixed Rs. 100 plus Rs. 35 for every kilometre travelled. A journey costs Rs. 485. How many kilometres was the journey?",
 "options": {"A": "11", "B": "12", "C": "13", "D": "10"},
 "answer": "A"},

{"id": 90, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Easy",
 "question": "What is the sum of the solutions of x^2 - 10x + 16 = 0?",
 "options": {"A": "16", "B": "-10", "C": "-16", "D": "10"},
 "answer": "D"},

{"id": 91, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "If log(x) = 5, where log denotes the base-10 logarithm, what is the value of log(10000x)?",
 "options": {"A": "9", "B": "20", "C": "50000", "D": "10"},
 "answer": "A"},

{"id": 92, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "For all x other than 5 and -2, which expression is equivalent to (x^2 - 25) / (x^2 - 3x - 10)?",
 "options": {"A": "(x - 5)/(x + 2)", "B": "(x + 5)/(x - 2)", "C": "5/2", "D": "(x + 5)/(x + 2)"},
 "answer": "D"},

{"id": 93, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Medium",
 "question": "Five identical machines together produce 750 units in 6 hours. Working at the same rate, how many units would 8 such machines produce in 3 hours?",
 "options": {"A": "500", "B": "600", "C": "700", "D": "800"},
 "answer": "B"},

{"id": 94, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "The mean of seven numbers is 24. When one of the numbers is removed, the mean of the remaining six is 26. What was the number that was removed?",
 "options": {"A": "8", "B": "10", "C": "12", "D": "14"},
 "answer": "C"},

{"id": 95, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A fair six-sided die is rolled twice. What is the probability that the two results add up to 10?",
 "options": {"A": "1/9", "B": "1/6", "C": "1/12", "D": "5/36"},
 "answer": "C"},

{"id": 96, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "Set P is {15, 15, 15, 15, 15} and Set Q is {5, 10, 15, 20, 25}. Both sets have a mean of 15. Which set has the larger standard deviation?",
 "options": {"A": "Set P", "B": "They are equal", "C": "It cannot be determined from the information given", "D": "Set Q"},
 "answer": "D"},

{"id": 97, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A square and an equilateral triangle each have a perimeter of 60 cm. By how many centimetres does the triangle's side exceed the square's side?",
 "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
 "answer": "C"},

{"id": 98, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Easy",
 "question": "A right circular cylinder has a radius of 5 cm and a height of 8 cm. What is its volume, in cubic centimetres?",
 "options": {"A": "200pi", "B": "160pi", "C": "100pi", "D": "40pi"},
 "answer": "A"},

{"id": 99, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Medium",
 "question": "Two parallel lines are cut by a transversal. One of the two interior angles on the same side of the transversal measures 55 degrees. What is the measure, in degrees, of the other?",
 "options": {"A": "55", "B": "125", "C": "90", "D": "145"},
 "answer": "B"},

{"id": 100, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Medium",
 "question": "In a 30-60-90 right triangle, the shorter leg measures 13 cm. What is the length of the hypotenuse, in centimetres?",
 "options": {"A": "26", "B": "13*sqrt(3)", "C": "26*sqrt(3)", "D": "19.5"},
 "answer": "A"},

{"id": 101, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Number Properties (odd/even, divisibility)", "difficulty": "Easy",
 "question": "If p is an odd integer, which of the following expressions must be an even integer?",
 "options": {"A": "p^2", "B": "5p", "C": "p + 9", "D": "p^3"},
 "answer": "C"},

{"id": 102, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the smallest positive integer that is divisible by 9, 12 and 15?",
 "options": {"A": "180", "B": "90", "C": "120", "D": "360"},
 "answer": "A"},

{"id": 103, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Medium",
 "question": "Which of the following is NOT a prime number?",
 "options": {"A": "71", "B": "77", "C": "83", "D": "89"},
 "answer": "B"},

# ============================================================
# SECTION 7 - VERBAL (17) - q104-120
# ============================================================

{"id": 104, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Easy",
 "question": "The chairman's opening remarks were unusually ____: he stated the budget figure, the deadline, and sat down. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "verbose", "B": "flattering", "C": "evasive", "D": "succinct"},
 "answer": "D"},

{"id": 105, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Every retrospective on Pakistani hockey lists the Olympic golds. The list is accurate. But it hides a more interesting fact, which is that the team's dominant era coincided almost exactly with a single coaching lineage passed from one captain to the next -- and that it was this continuity, not any one generation of players, that explains the run.\" Which choice best describes the function of the final clause in the text as a whole?",
 "options": {"A": "It withdraws a claim made earlier in the text.",
             "B": "It supplies statistical evidence for the first sentence.",
             "C": "It concedes that the conventional list is factually wrong.",
             "D": "It states the specific point the author believes the conventional account obscures."},
 "answer": "D"},

{"id": 106, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: For decades the government has guaranteed a floor price for cotton, above what most competing crops can expect in a normal year. The policy works: farmers keep planting cotton even when yields are poor. It also works too well: land that would earn more under fruit orchards or vegetables stays under cotton, because cotton is the one crop whose minimum price a farmer can count on before the season even begins. Which choice best states the main idea of the passage?",
 "options": {"A": "The guaranteed cotton price has failed to keep farmers planting cotton.",
             "B": "By removing price risk for cotton alone, the guarantee succeeds at its aim while locking land into a lower-value crop.",
             "C": "Fruit orchards are less profitable than cotton in every district.",
             "D": "Market prices for agricultural produce cannot be forecast at all."},
 "answer": "B"},

{"id": 107, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A publisher reissued a set of children's storybooks in two versions identical except for the illustrator's name: printed prominently on some covers, omitted from others. Copies naming the illustrator sold 20 per cent more in markets where that illustrator was already well known locally. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "children prefer books with no illustrations at all.",
             "B": "how prominently a known illustrator is credited can affect how many copies are bought.",
             "C": "the illustrator's name made the storybooks more accurately printed.",
             "D": "storybooks sell better than novels in general."},
 "answer": "B"},

{"id": 108, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "A critic argues that the poet Parveen Shakir's verse deliberately withholds a fixed resolution to the emotional conflicts it raises. Which description of a poem's closing lines, if accurate, would most directly support that argument?",
 "options": {"A": "The final couplet explicitly states which choice the speaker has made.",
             "B": "A narrator summarises the moral the reader should draw.",
             "C": "The poem ends on an open question addressed to the beloved, with no further lines to answer it.",
             "D": "The poem closes with a description of a garden with no emotional content."},
 "answer": "C"},

{"id": 109, "section": 7, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "Domestic leather exports fell for five consecutive quarters, and two tanneries closed altogether. ____ the industry's finished-goods exports, such as jackets and footwear, rose sharply, offsetting some of the decline. Which transition best completes the text?",
 "options": {"A": "Therefore,", "B": "For example,", "C": "In conclusion,", "D": "Meanwhile,"},
 "answer": "D"},

{"id": 110, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The first phase of the canal lining project finished on budget ____ the second phase ran nearly forty per cent over. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; ", "C": " which ", "D": ", also "},
 "answer": "B"},

{"id": 111, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Easy",
 "question": "Because the pass had been closed by early snowfall ____ supplies were flown in for six weeks instead. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; ", "C": ". ", "D": ": "},
 "answer": "A"},

{"id": 112, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which version of the sentence most clearly means that the stipend covers travel and nothing else?",
 "options": {"A": "The stipend only covers travel.",
             "B": "Only the stipend covers travel.",
             "C": "The stipend covers only travel.",
             "D": "The stipend covers travel only for conference attendees."},
 "answer": "C"},

{"id": 113, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: When conflict disrupted Swat's tourism industry, hotel occupancy in the valley's main towns fell by more than three-quarters within two seasons, and most of the larger hotels closed. Recovery since has been billed, in the official telling, as a straightforward return to normal: occupancy figures have climbed back to pre-conflict levels within the past several years. The figures understate how uneven the return has been. Domestic tourists, drawn by day trips and short weekend stays, account for most of the recovery; the foreign visitors who once stayed for weeks and spent accordingly have not returned in comparable numbers, and several of the valley's mid-range guesthouses that depended on that longer, higher-spending stay have not reopened at all. An occupancy figure that looks fully recovered can still describe an industry that has not recovered the kind of visit it used to depend on. Which choice best states the main idea of the passage?",
 "options": {"A": "Swat's tourism industry has fully recovered in every respect since the conflict ended.",
             "B": "Recovered occupancy figures conceal a shift toward shorter domestic visits and the loss of the longer-stay foreign tourism the industry once relied on.",
             "C": "Foreign tourists now outnumber domestic tourists in Swat.",
             "D": "Most of Swat's larger hotels reopened within two seasons of the conflict ending."},
 "answer": "B"},

{"id": 114, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: When conflict disrupted Swat's tourism industry, hotel occupancy in the valley's main towns fell by more than three-quarters within two seasons, and most of the larger hotels closed. Recovery since has been billed, in the official telling, as a straightforward return to normal: occupancy figures have climbed back to pre-conflict levels within the past several years. The figures understate how uneven the return has been. Domestic tourists, drawn by day trips and short weekend stays, account for most of the recovery; the foreign visitors who once stayed for weeks and spent accordingly have not returned in comparable numbers, and several of the valley's mid-range guesthouses that depended on that longer, higher-spending stay have not reopened at all. An occupancy figure that looks fully recovered can still describe an industry that has not recovered the kind of visit it used to depend on. According to the passage, what happened to hotel occupancy in Swat's main towns within two seasons of the conflict's disruption?",
 "options": {"A": "It fell by more than three-quarters.", "B": "It rose sharply.", "C": "It remained roughly unchanged.", "D": "The passage does not say."},
 "answer": "A"},

{"id": 115, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: When conflict disrupted Swat's tourism industry, hotel occupancy in the valley's main towns fell by more than three-quarters within two seasons, and most of the larger hotels closed. Recovery since has been billed, in the official telling, as a straightforward return to normal: occupancy figures have climbed back to pre-conflict levels within the past several years. The figures understate how uneven the return has been. Domestic tourists, drawn by day trips and short weekend stays, account for most of the recovery; the foreign visitors who once stayed for weeks and spent accordingly have not returned in comparable numbers, and several of the valley's mid-range guesthouses that depended on that longer, higher-spending stay have not reopened at all. An occupancy figure that looks fully recovered can still describe an industry that has not recovered the kind of visit it used to depend on. The author's attitude toward the official description of the recovery as a \"straightforward return to normal\" is best characterised as",
 "options": {"A": "fully in agreement.", "B": "detached and purely descriptive.", "C": "skeptical of what the headline figure leaves out.", "D": "enthusiastically supportive."},
 "answer": "C"},

{"id": 116, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: When conflict disrupted Swat's tourism industry, hotel occupancy in the valley's main towns fell by more than three-quarters within two seasons, and most of the larger hotels closed. Recovery since has been billed, in the official telling, as a straightforward return to normal: occupancy figures have climbed back to pre-conflict levels within the past several years. The figures understate how uneven the return has been. Domestic tourists, drawn by day trips and short weekend stays, account for most of the recovery; the foreign visitors who once stayed for weeks and spent accordingly have not returned in comparable numbers, and several of the valley's mid-range guesthouses that depended on that longer, higher-spending stay have not reopened at all. An occupancy figure that looks fully recovered can still describe an industry that has not recovered the kind of visit it used to depend on. It can most reasonably be inferred that the author would support",
 "options": {"A": "reporting only the overall occupancy figure, since it already tells the full story.",
             "B": "discouraging domestic tourism in favour of foreign visitors.",
             "C": "closing the mid-range guesthouses that have not reopened.",
             "D": "tracking the mix of visitor types and length of stay rather than relying on the aggregate occupancy figure alone."},
 "answer": "D"},

{"id": 117, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The fellowship is open to applicants who have completed a relevant degree, who have field experience, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "having published at least one paper.",
             "B": "at least one published paper.",
             "C": "they have published at least one paper.",
             "D": "who have published at least one paper."},
 "answer": "D"},

{"id": 118, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as CANDOUR.",
 "options": {"A": "deception", "B": "frankness", "C": "hesitation", "D": "formality"},
 "answer": "B"},

{"id": 119, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to SCARCITY.",
 "options": {"A": "abundance", "B": "shortage", "C": "delay", "D": "demand"},
 "answer": "A"},

{"id": 120, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The new policy did little to CURB informal money-lending,\" the word \"curb\" most nearly means",
 "options": {"A": "verify.", "B": "restrain.", "C": "mark.", "D": "examine."},
 "answer": "B"},

]


# ------------------------------------------------------------
# Sanity-check / summary utility
# ------------------------------------------------------------
# Deliberately stricter than lums_lcat_sample.py's version, because this bank
# is authored rather than transcribed. On top of the usual duplicate/option
# checks it enforces two things that have bitten this repo before:
#
#   1. Topic AND subtopic must be canonical strings from
#      lums-content/syllabus/lums_syllabus.json, under the right subject.
#      A typo here silently creates a junk Topic/Subtopic row on import,
#      because import_mcqs.py uses get_or_create.
#
#   2. Every (question_text, option_a) pair must be absent from the sample
#      bank and from Mocks 1 and 2. That tuple (with past_paper) is
#      import_mcqs.py's dedupe key -- a collision would make one bank's
#      question silently overwrite another's. Check it before every import,
#      not after.
import json
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_SYLLABUS = _HERE.parent / "syllabus" / "lums_syllabus.json"


def _load_syllabus():
    # utf-8-sig: the syllabus file ships with a BOM, matching PMDC's.
    with open(_SYLLABUS, encoding="utf-8-sig") as fh:
        return json.load(fh)["subjects"]


def check_canonical_labels(questions):
    subjects = _load_syllabus()
    bad = []
    for q in questions:
        topics = subjects.get(q["subject"])
        if topics is None:
            bad.append((q["id"], f"unknown subject {q['subject']!r}"))
            continue
        subs = topics.get(q["topic"])
        if subs is None:
            bad.append((q["id"], f"topic {q['topic']!r} not under {q['subject']}"))
            continue
        if q["subtopic"] not in subs:
            bad.append((q["id"], f"subtopic {q['subtopic']!r} not under {q['topic']!r}"))
    if bad:
        print("\nNON-CANONICAL LABELS:")
        for qid, msg in bad:
            print(f"  Q{qid}: {msg}")
    else:
        print("\nEvery topic/subtopic is a canonical string from lums_syllabus.json. OK.")
    return bad


def check_other_bank_collisions(questions):
    """(question_text, option_a) must not collide with the sample bank or earlier mocks."""
    keys = set()
    sources_checked = []
    try:
        from lums_lcat_sample import QUESTIONS as SAMPLE
        keys |= {(q["question"], q["options"]["A"]) for q in SAMPLE}
        sources_checked.append("lums_lcat_sample")
    except ImportError:
        print("\nCould not import lums_lcat_sample -- that collision check SKIPPED.")
    for modname in ("lums_mock_01", "lums_mock_02", "lums_mock_03"):
        try:
            mod = __import__(modname, fromlist=["QUESTIONS"])
            keys |= {(q["question"], q["options"]["A"]) for q in mod.QUESTIONS}
            sources_checked.append(modname)
        except ImportError:
            print(f"Could not import {modname} -- that collision check SKIPPED.")

    if not sources_checked:
        return []

    clashes = [q["id"] for q in questions if (q["question"], q["options"]["A"]) in keys]
    if clashes:
        print(f"\nCOLLISION with {', '.join(sources_checked)} on ids: {clashes}")
    else:
        print(f"Zero (question_text, option_a) overlap with {', '.join(sources_checked)}. OK.")
    return clashes


def summarize(questions):
    subj = Counter(q["subject"] for q in questions)
    topic = Counter((q["subject"], q["topic"]) for q in questions)
    sub = Counter((q["topic"], q["subtopic"]) for q in questions)
    diff = Counter(q["difficulty"] for q in questions)
    ans = Counter(q["answer"] for q in questions)
    sec = Counter(q["section"] for q in questions)
    ids = [q["id"] for q in questions]
    dup_ids = sorted(i for i in set(ids) if ids.count(i) > 1)
    texts = [q["question"] for q in questions]
    dup_text = [t for t in set(texts) if texts.count(t) > 1]

    print(f"Total questions: {len(questions)}")

    print("\nBy section:")
    for num, name, expected in SECTIONS:
        got = sec[num]
        flag = "" if got == expected else f"  <-- EXPECTED {expected}"
        print(f"  Section {num} ({name}): {got}{flag}")

    print("\nBy subject:")
    for s, c in subj.items():
        print(f"  {s}: {c}  ({c / len(questions):.1%})")

    print("\nBy topic:")
    for (s, t), c in sorted(topic.items()):
        print(f"  {s} / {t}: {c}")

    print("\nBy subtopic:")
    for (t, st), c in sorted(sub.items()):
        print(f"  {t} / {st}: {c}")

    print("\nBy difficulty:")
    for d in ("Easy", "Medium", "Hard"):
        print(f"  {d}: {diff[d]}")

    print("\nBy correct-answer letter:")
    for L in ("A", "B", "C", "D"):
        print(f"  {L}: {ans[L]}")

    print(f"\nDuplicate IDs: {dup_ids if dup_ids else 'None'}")
    print(f"Duplicate question text: {dup_text if dup_text else 'None'}")

    for q in questions:
        assert set(q["options"].keys()) == {"A", "B", "C", "D"}, f"Q{q['id']} missing an option"
        assert q["answer"] in q["options"], f"Q{q['id']} answer key invalid"
        assert len(set(q["options"].values())) == 4, f"Q{q['id']} has duplicate option text"
        assert q["difficulty"] in {"Easy", "Medium", "Hard"}, f"Q{q['id']} bad difficulty"
    print("\nAll questions have 4 distinct options (A-D) and a valid answer key. OK.")

    check_canonical_labels(questions)
    check_other_bank_collisions(questions)


def print_answer_key(questions):
    print("\nANSWER KEY (UNVERIFIED -- content-team derived, not LUMS')")
    print("-" * 60)
    for q in questions:
        print(f"{q['id']:>3}. {q['answer']}", end="   ")
        if q["id"] % 10 == 0:
            print()
    print()


if __name__ == "__main__":
    summarize(QUESTIONS)
    print_answer_key(QUESTIONS)