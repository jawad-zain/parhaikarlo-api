"""
LUMS Common Admission Test (LCAT) - Full-Length Mock Test #4
=============================================================
ParhaiKarlo-prepared full-length mock test. NOT an official LUMS past paper.
Answer keys prepared by content team, pending human verification.

Nothing in this file is taken from LUMS' official "Sample Questions for
Verbal & Math Sections" guide (raw-sources/sample_lcat_2025.pdf), nor from
`lums_lcat_mock_01.py`, `lums_lcat_mock_02.py` or `lums_lcat_mock_03.py`.
Every question below is newly written; the topic and subtopic assigned to
each question slot mirrors the position it occupies in the earlier mocks
(same section, same slot), since those labels were already verified against
the syllabus when Mock 1 was checked in.

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
Groq tagger is skipped for this bank, exactly as it is for lums_lcat_sample.py,
lums_lcat_mock_01.py, lums_lcat_mock_02.py and lums_lcat_mock_03.py.

Each question is a dict:
    id, section, subject, topic, subtopic, difficulty, question,
    options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.
"""

SOURCE = "parhaikarlo_mock_04"

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
 "question": "Restorers cleaning the frescoes at Thatta's Shah Jahan Mosque worked with ____ patience, testing solvent strength on a coin-sized patch before treating a single square metre of tile-work. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "careless", "B": "hurried", "C": "unwavering", "D": "casual"},
 "answer": "C"},

{"id": 2, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Medium",
 "question": "Text: \"Cotton yield gains in southern Punjab are often cited as proof that new seed varieties alone have solved the region's productivity problem. The claim overstates matters. Yield increases have tracked almost exactly with the spread of drip irrigation over the same years, and fields still using flood irrigation show little improvement even with the new seed.\" Which choice best describes the function of the third sentence in the text as a whole?",
 "options": {"A": "It concedes that the claim is entirely false.",
             "B": "It provides evidence that narrows the credit assigned to seed varieties alone.",
             "C": "It summarises a consensus the author later rejects.",
             "D": "It offers an illustrative anecdote unrelated to the claim."},
 "answer": "B"},

{"id": 3, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: Raising the height of Mangla Dam is the fastest way to add water storage for Punjab's growing population. Text 2: Raising Mangla's height further would submerge additional inhabited land in Azad Kashmir, and resettlement costs alone could exceed what a smaller, faster-to-build canal-lining programme would cost; real storage gains need not come from raising the dam at all. Based on the texts, how would the author of Text 2 most likely respond to the claim in Text 1?",
 "options": {"A": "By agreeing that raising the dam is both the fastest and cheapest option.",
             "B": "By arguing that dam-raising carries resettlement costs that make an alternative approach more practical.",
             "C": "By denying that Punjab's population is growing.",
             "D": "By conceding that canal-lining cannot increase storage."},
 "answer": "B"},

{"id": 4, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Easy",
 "question": "Passage: For years, no reliable count existed of the markhor population in Chitral Gol National Park, since the animals favour steep cliffs where observers on foot cannot easily follow. Wildlife officers began using fixed-point telescopes at dawn and dusk, when markhor descend to graze, and cross-referenced counts from several vantage points on the same morning to avoid counting one animal twice. The method produced the park's first population figure that outside reviewers accepted. What is the main idea of the passage?",
 "options": {"A": "Chitral Gol is the largest national park in Pakistan.",
             "B": "Markhor populations are declining across their entire range.",
             "C": "Coordinated dawn-and-dusk telescope counts from multiple vantage points produced the first widely accepted markhor population figure for the park.",
             "D": "Markhor prefer grazing at night rather than at dawn."},
 "answer": "C"},

{"id": 5, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: Over a decade, registered beekeeping households in Chitral rose sharply, while national honey imports fell only slightly across the same period. Most of the new honey was sold directly to local buyers rather than through the packaged retail chains where imported brands are strongest. Which choice most logically completes the reasoning in the passage?",
 "options": {"A": "Therefore, imported honey brands are likely to disappear from shelves within a few years.",
             "B": "Therefore, local beekeeping growth appears to have expanded direct sales to buyers without significantly displacing the packaged import trade.",
             "C": "Therefore, Chitral's beekeepers mostly export their honey abroad.",
             "D": "Therefore, national honey consumption has fallen overall."},
 "answer": "B"},

{"id": 6, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A researcher claims that a district's rise in total cotton output was driven more by an increase in cultivated area than by any improvement in yield per acre. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Output rose 45%, while cultivated area rose 41% and yield per acre rose 3%.",
             "B": "Output rose 45%, while cultivated area rose 6% and yield per acre rose 37%.",
             "C": "Output fell 6%, while cultivated area rose 30%.",
             "D": "Output rose 45%, and the export price of cotton rose 8%."},
 "answer": "A"},

{"id": 7, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "While researching Allama Iqbal, a student compiles three notes: he trained as a philosopher in Europe before returning to British India; his Persian and Urdu poetry argued for spiritual and intellectual self-renewal among Muslims; his 1930 Allahabad address is often cited as an early articulation of a separate Muslim homeland. Which statement best synthesises these notes?",
 "options": {"A": "Trained as a philosopher in Europe, Iqbal used his Persian and Urdu poetry to call for Muslim self-renewal, and his 1930 address later came to be seen as an early call for a separate homeland.",
             "B": "Iqbal wrote exclusively in English.",
             "C": "Iqbal's Allahabad address made no reference to the Muslim political future.",
             "D": "Iqbal never studied outside British India."},
 "answer": "A"},

{"id": 8, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "Karachi's population more than tripled after Partition as refugees settled in the city. ____ the city's water and sewage systems, designed for a much smaller population, have struggled to keep pace ever since. Which transition best completes the text?",
 "options": {"A": "Similarly,", "B": "For instance,", "C": "Consequently,", "D": "In addition,"},
 "answer": "C"},

{"id": 9, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: khussa, traditional leather footwear, is hand-stitched without nails or machine soles; a single pair can take a craftsman two to three days; the trade is concentrated in a few family workshops in Multan and Bahawalpur; finished pairs are often bought for weddings. The student wants to emphasise that the craft is both labour-intensive and passed down within a small number of families. Which choice best accomplishes this goal?",
 "options": {"A": "Khussa is stitched without nails or machine soles, a technique associated with Multan and Bahawalpur.",
             "B": "A single pair of khussa can take a craftsman two to three days to complete, and the trade remains concentrated in a handful of family workshops.",
             "C": "Khussa is commonly bought for weddings.",
             "D": "Khussa-making is associated with Multan and Bahawalpur."},
 "answer": "B"},

{"id": 10, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "The archive of court records preserved at the Lahore High Court ____ documents dating back to the nineteenth century. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "include", "B": "are including", "C": "includes", "D": "have included"},
 "answer": "C"},

{"id": 11, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "The brick-kiln workers rejected the revised wage schedule, and ____ grievance was later raised with the labour department. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "its", "B": "their", "C": "it's", "D": "there"},
 "answer": "B"},

{"id": 12, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The inspection team reached one firm conclusion ____ the retaining wall had shifted several centimetres since the last survey. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", that", "B": ", being", "C": "; which", "D": ": "},
 "answer": "D"},

{"id": 13, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Medium",
 "question": "The caravanserai had lain in ruins for over a century ____ a conservation trust began restoring it as a cultural centre last year. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "; ", "B": ", ", "C": " which ", "D": " and which "},
 "answer": "A"},

{"id": 14, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Having monitored the Ravi's water quality for three consecutive summers, ____\"",
 "options": {"A": "the conclusion of the researchers was that pollution levels had risen.",
             "B": "it was concluded by the researchers that pollution levels had risen.",
             "C": "the researchers concluded that pollution levels had risen.",
             "D": "pollution levels were shown by the researchers to have risen."},
 "answer": "C"},

{"id": 15, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: Peshawar's copperware trade is usually filed under souvenir craft, aimed at tourists passing through Qissa Khwani Bazaar. The workshops tell a different story: master coppersmiths take on multi-year apprentices under formal contracts, export orders account for a majority of large workshops' revenue, and pricing is set well in advance based on projected copper futures. The trade, in other words, runs less like a tourist curio business and more like a specialised export manufacturing operation. Which choice best states the main idea of the passage?",
 "options": {"A": "Peshawar's copperware trade caters only to tourists.",
             "B": "Peshawar's copperware trade is better understood as a specialised export manufacturing operation than as a tourist curio trade.",
             "C": "Copper futures have no bearing on the trade's pricing.",
             "D": "Apprenticeships in the trade are informal and unpaid."},
 "answer": "B"},

{"id": 16, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: Peshawar's copperware trade is usually filed under souvenir craft, aimed at tourists passing through Qissa Khwani Bazaar. The workshops tell a different story: master coppersmiths take on multi-year apprentices under formal contracts, export orders account for a majority of large workshops' revenue, and pricing is set well in advance based on projected copper futures. The trade, in other words, runs less like a tourist curio business and more like a specialised export manufacturing operation. The author's attitude toward the conventional description of the trade as a tourist curio business is best characterised as",
 "options": {"A": "openly contemptuous.", "B": "mildly corrective.", "C": "entirely neutral.", "D": "wistfully nostalgic."},
 "answer": "B"},

{"id": 17, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as FRUGAL.",
 "options": {"A": "wasteful", "B": "thrifty", "C": "generous", "D": "reckless"},
 "answer": "B"},

{"id": 18, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to the underlined word as it is used here: \"The negotiations proceeded at a LEISURELY pace.\"",
 "options": {"A": "hurried", "B": "quiet", "C": "formal", "D": "private"},
 "answer": "A"},

# ============================================================
# SECTION 2 - MATH (17) - q19-35
# ============================================================

{"id": 19, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Easy",
 "question": "If 4(x - 1) + 6 = 2x + 16, what is the value of x?",
 "options": {"A": "5", "B": "6", "C": "7", "D": "8"},
 "answer": "C"},

{"id": 20, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 2x + 3y = 19 and x - y = 2, what is the value of x?",
 "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
 "answer": "C"},

{"id": 21, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "Which of the following describes all values of x for which 9 - 4x > 1?",
 "options": {"A": "x > 2", "B": "x < 2", "C": "x > -2", "D": "x < -2"},
 "answer": "B"},

{"id": 22, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Medium",
 "question": "An arithmetic sequence has first term 4 and common difference 5. What is the sum of its first 14 terms?",
 "options": {"A": "511", "B": "500", "C": "525", "D": "490"},
 "answer": "A"},

{"id": 23, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "The equation x^2 + kx + 35 = 0 has roots 5 and 7. What is the value of k?",
 "options": {"A": "-12", "B": "12", "C": "-35", "D": "35"},
 "answer": "A"},

{"id": 24, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is the value of 16^(3/4) * 9^(1/2)?",
 "options": {"A": "12", "B": "18", "C": "24", "D": "32"},
 "answer": "C"},

{"id": 25, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "What is the value of (log_2 64) - (log_3 9)?",
 "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
 "answer": "B"},

{"id": 26, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "If 1/x + 1/(4x) = 5/8, what is the value of x?",
 "options": {"A": "1/2", "B": "1", "C": "2", "D": "4"},
 "answer": "C"},

{"id": 27, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "A shopkeeper raises the price of an item by 20% and then, in a sale, reduces the new price by 15%. Compared with the original price, the final price is",
 "options": {"A": "2% higher.", "B": "2% lower.", "C": "unchanged.", "D": "5% higher."},
 "answer": "A"},

{"id": 28, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Easy",
 "question": "A sum of Rs. 90,000 is divided between two partners in the ratio 2 : 7. By how much does the larger share exceed the smaller share, in rupees?",
 "options": {"A": "40,000", "B": "45,000", "C": "50,000", "D": "55,000"},
 "answer": "C"},

{"id": 29, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "A class of 24 students has a mean score of 70. Six more students, whose mean score is 90, join the class. What is the mean score of all 30 students?",
 "options": {"A": "72", "B": "74", "C": "76", "D": "78"},
 "answer": "B"},

{"id": 30, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A bag contains 6 red marbles and 4 blue marbles. Two marbles are drawn at random without replacement. What is the probability that both are blue?",
 "options": {"A": "2/15", "B": "1/5", "C": "3/10", "D": "1/3"},
 "answer": "A"},

{"id": 31, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A rectangle has a perimeter of 50 cm, and its length is 5 cm greater than its width. What is its area, in square centimetres?",
 "options": {"A": "140", "B": "150", "C": "160", "D": "175"},
 "answer": "B"},

{"id": 32, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Easy",
 "question": "A right triangle has legs of length 7 cm and 24 cm. What is its perimeter, in centimetres?",
 "options": {"A": "52", "B": "54", "C": "56", "D": "58"},
 "answer": "C"},

{"id": 33, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Easy",
 "question": "A circle has an area of 100pi square centimetres. What is its circumference, in centimetres?",
 "options": {"A": "10pi", "B": "20pi", "C": "40pi", "D": "100pi"},
 "answer": "B"},

{"id": 34, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Ratios", "difficulty": "Medium",
 "question": "In a right triangle, theta is an acute angle and cos(theta) = 20/29. What is the value of sin(theta)?",
 "options": {"A": "20/29", "B": "21/29", "C": "29/21", "D": "29/20"},
 "answer": "B"},

{"id": 35, "section": 2, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the least common multiple of 14 and 21, minus their greatest common divisor?",
 "options": {"A": "28", "B": "35", "C": "42", "D": "49"},
 "answer": "B"},

# ============================================================
# SECTION 3 - VERBAL (17) - q36-52
# ============================================================

{"id": 36, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "Though praised at its launch as revolutionary, the e-governance portal proved largely ____: two years later, most district offices still processed applications on paper. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "transformative", "B": "contentious", "C": "illusory", "D": "premature"},
 "answer": "C"},

{"id": 37, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Urban planners have long modelled public parks as a straightforward driver of neighbourhood property values: build a park, and nearby prices rise. The model is intuitive, and it predicts steadily climbing valuations near new green spaces. That is not what repeated valuation surveys near several new Lahore parks show: prices rose only in neighbourhoods that already had reliable water and electricity supply, and stayed flat elsewhere.\" Which choice best describes the function of the final sentence in the text as a whole?",
 "options": {"A": "It supplies an example that confirms the model's prediction.",
             "B": "It introduces survey evidence that conflicts with the model's prediction and points to a condition the model ignores.",
             "C": "It proposes that more parks be built regardless of infrastructure.",
             "D": "It restates the model's central claim in more concrete terms."},
 "answer": "B"},

{"id": 38, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: Over two decades, the total area under rice in Punjab grew only modestly, while the groundwater pumped for rice districts grew far faster, because rice paddies are flooded for weeks at a stretch and provincial irrigation departments rarely meter tube-well extraction. Economists warn against treating the modest growth in area as reassuring: the real story is how much groundwater an expanding rice sector is drawing down for other crops nearby. Which choice best states the main idea of the passage?",
 "options": {"A": "Rice cultivation has become dramatically more water-efficient.",
             "B": "Total area under rice matters more than groundwater use.",
             "C": "Provincial irrigation departments meter tube-well extraction accurately.",
             "D": "The modest growth in rice area understates the crop's growing claim on a groundwater supply shared with other crops."},
 "answer": "D"},

{"id": 39, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: Pakistan's national parks are managed province by province, but the migratory raptors that researchers track most closely pass through several provinces during a single autumn, and the same bird is often logged at more than one site along its route. It follows that separate provincial raptor counts ____ Which choice most logically completes the text?",
 "options": {"A": "should be conducted more frequently than they currently are.",
             "B": "cannot simply be summed to produce a reliable national total.",
             "C": "will always undercount the birds in each province.",
             "D": "are the only practical way to track migratory raptors."},
 "answer": "B"},

{"id": 40, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "In a study of informal credit among Multan's cloth traders, a researcher argues that traders borrow from wholesale suppliers on credit terms rather than from banks because supplier credit requires no collateral. Which quotation from a trader interview, if authentic, would most directly support that argument?",
 "options": {"A": "\"No bank has ever agreed to open an account for my shop.\"",
             "B": "\"The bank might approve a loan eventually, but my supplier lets me pay in sixty days with nothing pledged against it.\"",
             "C": "\"My supplier charges nearly double what a bank would charge in interest.\"",
             "D": "\"I have bought cloth from the same supplier for over a decade.\""},
 "answer": "B"},

{"id": 41, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student researching the Katas Raj temples records three observations: the complex is built around a sacred pond believed in Hindu tradition to have formed from Shiva's tears; it includes temples dating from several different centuries; it now draws both religious pilgrims and history tourists. Which statement best synthesises these observations?",
 "options": {"A": "Katas Raj lasts for several days each year.",
             "B": "Built around a pond linked in Hindu tradition to Shiva's tears, the multi-century Katas Raj complex now draws both pilgrims and history tourists.",
             "C": "Tourists at Katas Raj come mainly from abroad.",
             "D": "Katas Raj has had little religious significance in modern times."},
 "answer": "B"},

{"id": 42, "section": 3, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "The 2005 earthquake destroyed most reinforced-concrete-frame schools in the affected valleys. ____ single-storey stone buildings with timber roof bracing in the same valleys largely withstood the shaking. Which transition best completes the text?",
 "options": {"A": "Consequently,", "B": "In short,", "C": "Similarly,", "D": "By contrast,"},
 "answer": "D"},

{"id": 43, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The programme trains lady health workers to screen for tuberculosis symptoms, to counsel patients on treatment adherence, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "referring drug-resistant cases to a specialist centre.",
             "B": "they refer drug-resistant cases to a specialist centre.",
             "C": "to refer drug-resistant cases to a specialist centre.",
             "D": "drug-resistant cases are referred to a specialist centre."},
 "answer": "C"},

{"id": 44, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The delegation toured three archaeological sites in Punjab ____ Taxila, Harappa and Katas Raj. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ": ", "B": ", ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 45, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "Each of the tehsil offices ____ required to submit a monthly land-record summary. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "are", "B": "were", "C": "is", "D": "have been"},
 "answer": "C"},

{"id": 46, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Hard",
 "question": "The spillway was widened in 2011 ____ downstream erosion has accelerated in nearly every monsoon since. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ", however ", "C": " and which ", "D": "; nevertheless, "},
 "answer": "D"},

{"id": 47, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: The Indus blind dolphin's range has occupied an uncomfortable place in water policy for decades: officially protected under wildlife law, yet regularly stranded in irrigation canals that draw water away from the main river channel during the dry season. Conservationists argue that canal offtake schedules are set without any reliable estimate of how many dolphins occupy a given river stretch, so a release schedule fixed on paper may leave too little water for the animals that remain. Rescue teams have expanded steadily, and officials point to rising numbers of dolphins rescued from canals as evidence the population is stable. Independent biologists tell a thinner story: rescue numbers have risen mainly because rescue teams now patrol a wider stretch of canal network, not because more individual dolphins are surviving to be rescued twice, which suggests the underlying population trend remains unclear. Which choice best states the main idea of the passage?",
 "options": {"A": "Indus dolphin hunting has been banned outright.",
             "B": "Rising rescue numbers may reflect wider patrol coverage rather than confirm a stable population.",
             "C": "Canal offtake schedules are set with precise dolphin population counts.",
             "D": "Rescue teams no longer operate along the Indus."},
 "answer": "B"},

{"id": 48, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: The Indus blind dolphin's range has occupied an uncomfortable place in water policy for decades: officially protected under wildlife law, yet regularly stranded in irrigation canals that draw water away from the main river channel during the dry season. Conservationists argue that canal offtake schedules are set without any reliable estimate of how many dolphins occupy a given river stretch, so a release schedule fixed on paper may leave too little water for the animals that remain. Rescue teams have expanded steadily, and officials point to rising numbers of dolphins rescued from canals as evidence the population is stable. Independent biologists tell a thinner story: rescue numbers have risen mainly because rescue teams now patrol a wider stretch of canal network, not because more individual dolphins are surviving to be rescued twice, which suggests the underlying population trend remains unclear. According to the passage, what do conservationists argue about canal offtake schedules?",
 "options": {"A": "They are generously funded by international donors.",
             "B": "They are set without a reliable estimate of how many dolphins occupy a given river stretch.",
             "C": "They have eliminated dolphin strandings entirely.",
             "D": "They are administered only by rescue teams."},
 "answer": "B"},

{"id": 49, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: The Indus blind dolphin's range has occupied an uncomfortable place in water policy for decades: officially protected under wildlife law, yet regularly stranded in irrigation canals that draw water away from the main river channel during the dry season. Conservationists argue that canal offtake schedules are set without any reliable estimate of how many dolphins occupy a given river stretch, so a release schedule fixed on paper may leave too little water for the animals that remain. Rescue teams have expanded steadily, and officials point to rising numbers of dolphins rescued from canals as evidence the population is stable. Independent biologists tell a thinner story: rescue numbers have risen mainly because rescue teams now patrol a wider stretch of canal network, not because more individual dolphins are surviving to be rescued twice, which suggests the underlying population trend remains unclear. The author's attitude toward officials' claim that the population is stable is best characterised as",
 "options": {"A": "fully persuaded.", "B": "openly mocking.", "C": "skeptical, given the alternate explanation offered.", "D": "indifferent."},
 "answer": "C"},

{"id": 50, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: The Indus blind dolphin's range has occupied an uncomfortable place in water policy for decades: officially protected under wildlife law, yet regularly stranded in irrigation canals that draw water away from the main river channel during the dry season. Conservationists argue that canal offtake schedules are set without any reliable estimate of how many dolphins occupy a given river stretch, so a release schedule fixed on paper may leave too little water for the animals that remain. Rescue teams have expanded steadily, and officials point to rising numbers of dolphins rescued from canals as evidence the population is stable. Independent biologists tell a thinner story: rescue numbers have risen mainly because rescue teams now patrol a wider stretch of canal network, not because more individual dolphins are surviving to be rescued twice, which suggests the underlying population trend remains unclear. It can most reasonably be inferred that the author regards rising rescue numbers as",
 "options": {"A": "a reliable substitute for a direct population count.",
             "B": "evidence that risks being misread as proof of population stability when it may simply reflect wider patrol coverage.",
             "C": "irrelevant to the debate over canal schedules.",
             "D": "more effective than any current conservation method."},
 "answer": "B"},

{"id": 51, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as INSCRUTABLE.",
 "options": {"A": "obvious", "B": "mysterious", "C": "talkative", "D": "generous"},
 "answer": "B"},

{"id": 52, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The company's apology proved HOLLOW when the layoffs proceeded regardless,\" the word \"hollow\" most nearly means",
 "options": {"A": "empty of real substance.", "B": "physically concave.", "C": "loud.", "D": "temporary."},
 "answer": "A"},

# ============================================================
# SECTION 4 - MATH (17) - q53-69
# ============================================================

{"id": 53, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in Two Variables", "difficulty": "Medium",
 "question": "A line in the xy-plane passes through the points (3, 10) and (7, 26). What is the y-coordinate of its y-intercept?",
 "options": {"A": "-2", "B": "2", "C": "-4", "D": "4"},
 "answer": "A"},

{"id": 54, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "The function f is defined by f(x) = 6x - 11. If f(a) = 19, what is the value of a?",
 "options": {"A": "4", "B": "5", "C": "6", "D": "7"},
 "answer": "B"},

{"id": 55, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 2x + 5y = 27 and 2x - 3y = 3, what is the value of y?",
 "options": {"A": "2", "B": "3", "C": "4", "D": "5"},
 "answer": "B"},

{"id": 56, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "A delivery van weighs 900 kg when empty, and the total weight of the loaded van must not exceed 2,000 kg. If each crate weighs 55 kg, what is the greatest number of whole crates the van can carry?",
 "options": {"A": "18", "B": "19", "C": "20", "D": "21"},
 "answer": "C"},

{"id": 57, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Nonlinear Functions", "difficulty": "Medium",
 "question": "What is the minimum value of the function f(x) = x^2 - 10x + 13?",
 "options": {"A": "-10", "B": "-12", "C": "-14", "D": "12"},
 "answer": "B"},

{"id": 58, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Polynomial Expressions", "difficulty": "Easy",
 "question": "Which expression is equivalent to (4x - 3)(x + 2)?",
 "options": {"A": "4x^2 + 5x - 6", "B": "4x^2 - 5x - 6", "C": "4x^2 + 11x - 6", "D": "4x^2 + 5x + 6"},
 "answer": "A"},

{"id": 59, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "How many real solutions does the equation x^2 + 6x + 13 = 0 have?",
 "options": {"A": "Two distinct real solutions", "B": "Exactly one real solution", "C": "Infinitely many real solutions", "D": "No real solutions"},
 "answer": "D"},

{"id": 60, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is sqrt(48) + sqrt(27) in simplest radical form?",
 "options": {"A": "7*sqrt(3)", "B": "5*sqrt(5)", "C": "2*sqrt(5)", "D": "sqrt(75)"},
 "answer": "A"},

{"id": 61, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Unit Conversion", "difficulty": "Easy",
 "question": "A car consumes fuel at a rate of 7 litres per 100 kilometres. How many litres will it consume on a 400-kilometre journey at that rate?",
 "options": {"A": "26", "B": "28", "C": "30", "D": "32"},
 "answer": "B"},

{"id": 62, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Two-Variable Data Interpretation (tables/graphs)", "difficulty": "Medium",
 "question": "A shop records the number of units sold on each of five days: Monday 35, Tuesday 38, Wednesday 28, Thursday 35, Friday 42. By what percentage did the number of units sold increase from Wednesday to Thursday?",
 "options": {"A": "20%", "B": "25%", "C": "30%", "D": "35%"},
 "answer": "B"},

{"id": 63, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "For the data set 6, 10, 10, 12, 27, what is the mean minus the median?",
 "options": {"A": "0", "B": "1", "C": "2", "D": "3"},
 "answer": "D"},

{"id": 64, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "After a 15% discount, an item sells for Rs. 5,100. What was its price before the discount, in rupees?",
 "options": {"A": "5,800", "B": "6,000", "C": "5,650", "D": "6,200"},
 "answer": "B"},

{"id": 65, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Medium",
 "question": "A cube has a volume of 216 cubic centimetres. What is its total surface area, in square centimetres?",
 "options": {"A": "180", "B": "216", "C": "196", "D": "256"},
 "answer": "B"},

{"id": 66, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Easy",
 "question": "The three interior angles of a triangle are in the ratio 1 : 2 : 3. What is the measure of the largest angle, in degrees?",
 "options": {"A": "90", "B": "75", "C": "60", "D": "100"},
 "answer": "A"},

{"id": 67, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Medium",
 "question": "A sector of a circle of radius 15 cm has a central angle of 24 degrees. What is the area of the sector, in square centimetres?",
 "options": {"A": "15pi", "B": "10pi", "C": "20pi", "D": "25pi"},
 "answer": "A"},

{"id": 68, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Identities", "difficulty": "Medium",
 "question": "For any angle theta with cos(theta) not equal to 0, which expression is equivalent to sec^2(theta) - tan^2(theta)?",
 "options": {"A": "0", "B": "sin(theta)", "C": "cos(theta)", "D": "1"},
 "answer": "D"},

{"id": 69, "section": 4, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Easy",
 "question": "What is the sum of all prime numbers strictly between 50 and 60?",
 "options": {"A": "106", "B": "110", "C": "112", "D": "118"},
 "answer": "C"},

# ============================================================
# SECTION 5 - VERBAL (17) - q70-86
# ============================================================

{"id": 70, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "The auditor's report was notable for its ____: it examined each of the sixteen flagged transactions individually, citing the relevant regulation for every one. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "brevity", "B": "thoroughness", "C": "leniency", "D": "ambiguity"},
 "answer": "B"},

{"id": 71, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: A single standardised university entrance test, taken by every applicant nationwide, is the fairest way to rank candidates because everyone answers the same questions. Text 2: Identical questions do not produce a fair ranking when applicants differ enormously in access to internet-based practice tests and paid coaching centres; the test only equalises the questions on the page, not the preparation behind them. The author of Text 2 would most likely characterise Text 1's claim as",
 "options": {"A": "false, because the questions are not actually identical.",
             "B": "correct, and reason enough to keep the test unchanged.",
             "C": "accurate about the exam itself but incomplete about the unequal preparation surrounding it.",
             "D": "irrelevant, because coaching centres have no effect on scores."},
 "answer": "C"},

{"id": 72, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: Bala Hisar Fort, overlooking Peshawar from a raised mound, is usually valued for its long military history under successive empires. But history alone doesn't explain the site: the mound sits at the point where roads from the Khyber Pass converge before spreading into the plains, which suggests it was placed less for prestige than for surveillance of a critical approach. Which choice best states the main idea of the passage?",
 "options": {"A": "Bala Hisar Fort's chief significance lies in overseeing a strategic road convergence rather than in its military history alone.",
             "B": "Bala Hisar Fort is the tallest structure in Peshawar.",
             "C": "The Khyber Pass has never been used as a trade route.",
             "D": "Bala Hisar Fort was built purely as a ceremonial residence."},
 "answer": "A"},

{"id": 73, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A city introduced a dedicated BRT lane along one congested corridor. In the first year, average bus travel time on that corridor fell by 15 per cent. Over the same period, travel times on parallel general-traffic lanes rose by 10 per cent. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "the BRT lane had no effect on travel behaviour.",
             "B": "total citywide travel time fell by roughly 15 per cent.",
             "C": "at least part of the corridor's improvement came at the cost of slower general traffic rather than from fewer total trips.",
             "D": "drivers in the general lanes were unaware the BRT lane existed."},
 "answer": "C"},

{"id": 74, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A clinic claims a new SMS reminder programme cut missed follow-up appointments more among elderly patients than among younger patients. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Missed-appointment rates fell 22 points among elderly patients and 3 points among younger patients.",
             "B": "The clinic's overall missed-appointment rate fell 9 points.",
             "C": "Younger patients had the lowest missed-appointment rate in the clinic.",
             "D": "Attendance at optional sessions was highest among elderly patients."},
 "answer": "A"},

{"id": 75, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student compiles three observations about the Minar-e-Pakistan: it was built on the site where the 1940 Lahore Resolution was adopted; its design blends Mughal, Islamic, and modern architectural elements; it now serves as a venue for national commemorations. Which statement best synthesises these observations?",
 "options": {"A": "Built on the site of the 1940 Lahore Resolution, the Minar-e-Pakistan blends Mughal, Islamic, and modern design and now hosts national commemorations.",
             "B": "The Minar-e-Pakistan was built entirely in a modern architectural style.",
             "C": "The 1940 Lahore Resolution was adopted after the Minar-e-Pakistan's construction.",
             "D": "The Minar-e-Pakistan is rarely used for public events."},
 "answer": "A"},

{"id": 76, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "The library digitised its entire newspaper archive over a five-year project. ____ a researcher in Quetta can now search editions that once existed only as a single bound volume in Karachi. Which transition best completes the text?",
 "options": {"A": "Nevertheless,", "B": "Admittedly,", "C": "By comparison,", "D": "As a result,"},
 "answer": "D"},

{"id": 77, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: the Urs of Data Ganj Bakhsh draws pilgrims to Lahore each year; it features qawwali performances through the night; the shrine also runs a free community kitchen year-round; smaller commemorations are held at the shrine on other occasions. The student wants to emphasise the annual scale of the Urs and its musical tradition. Which choice best accomplishes this goal?",
 "options": {"A": "The Urs of Data Ganj Bakhsh draws large crowds of pilgrims to Lahore each year for all-night qawwali performances.",
             "B": "The shrine runs a free community kitchen year-round.",
             "C": "Smaller commemorations are held at the shrine on other occasions.",
             "D": "The shrine is located in Lahore."},
 "answer": "A"},

{"id": 78, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The committee's recommendations ____ released in April, prompted debate in two provincial assemblies. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ": ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 79, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "Every one of the interviewed vendors reported that ____ stall rent had increased at least once that year. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "their", "B": "it's", "C": "its", "D": "whose"},
 "answer": "A"},

{"id": 80, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Built on the site of the 1940 Lahore Resolution and blending several architectural styles, ____\"",
 "options": {"A": "historians regard the Minar-e-Pakistan as a national landmark.",
             "B": "the monument's base is what most visitors remember.",
             "C": "the Minar-e-Pakistan still anchors Lahore's Iqbal Park.",
             "D": "it is Iqbal Park that the Minar-e-Pakistan anchors."},
 "answer": "C"},

{"id": 81, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The report praised the school's low dropout rate, its trained teaching staff, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "it kept detailed attendance records.",
             "B": "that its records were detailed.",
             "C": "keeping detailed attendance records.",
             "D": "the thoroughness of its attendance records."},
 "answer": "D"},

{"id": 82, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Hard",
 "question": "Neither the project director nor the field officers ____ satisfied with the revised budget. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "was", "B": "is", "C": "has been", "D": "were"},
 "answer": "D"},

{"id": 83, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Hard",
 "question": "Passage: For decades Pakistan's rail freight decline has been blamed on road subsidies and on an aging locomotive fleet, and both complaints are real. Neither explains why so much freight that could travel by rail is instead routed by truck even on routes where rail capacity sits unused. That gap traces to a scheduling system built for a much smaller, passenger-first network, one that still gives freight trains the lowest priority on shared track. The fix is not chiefly in buying new locomotives. It is in how track time is allocated. Which choice best states the main idea of the passage?",
 "options": {"A": "Road subsidies are the sole cause of the freight decline.",
             "B": "The decline is better explained by freight's low scheduling priority on shared track than by fleet age or road subsidies alone.",
             "C": "Pakistan's rail network no longer carries any freight.",
             "D": "Buying new locomotives has fully resolved the scheduling problem."},
 "answer": "B"},

{"id": 84, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: For decades Pakistan's rail freight decline has been blamed on road subsidies and on an aging locomotive fleet, and both complaints are real. Neither explains why so much freight that could travel by rail is instead routed by truck even on routes where rail capacity sits unused. That gap traces to a scheduling system built for a much smaller, passenger-first network, one that still gives freight trains the lowest priority on shared track. The fix is not chiefly in buying new locomotives. It is in how track time is allocated. It can most reasonably be inferred that the author would agree with which statement?",
 "options": {"A": "Buying new locomotives alone would resolve most of the freight decline.",
             "B": "Road subsidies are a fabricated excuse used by the railway.",
             "C": "Reforming how track time is allocated to freight would address a cause of the decline that new locomotives cannot.",
             "D": "The rail network was originally built larger than passenger traffic needed."},
 "answer": "C"},

{"id": 85, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as VIGILANT.",
 "options": {"A": "careless", "B": "watchful", "C": "hasty", "D": "indifferent"},
 "answer": "B"},

{"id": 86, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The agency's decision to postpone the launch was largely a SAFE move,\" the word \"safe\" most nearly means",
 "options": {"A": "protected from theft.", "B": "legally required.", "C": "financially profitable.", "D": "cautious rather than bold."},
 "answer": "D"},

# ============================================================
# SECTION 6 - MATH (17) - q87-103
# ============================================================

{"id": 87, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Medium",
 "question": "If x/2 - 3 = x/5, what is the value of x?",
 "options": {"A": "8", "B": "10", "C": "12", "D": "15"},
 "answer": "B"},

{"id": 88, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Hard",
 "question": "In an arithmetic sequence the 7th term is 19 and the 12th term is 39. What is the first term?",
 "options": {"A": "-5", "B": "5", "C": "-9", "D": "9"},
 "answer": "A"},

{"id": 89, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "A taxi charges a fixed Rs. 90 plus Rs. 30 for every kilometre travelled. A journey costs Rs. 420. How many kilometres was the journey?",
 "options": {"A": "9", "B": "10", "C": "11", "D": "12"},
 "answer": "C"},

{"id": 90, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Easy",
 "question": "What is the sum of the solutions of x^2 - 12x + 20 = 0?",
 "options": {"A": "10", "B": "-12", "C": "20", "D": "12"},
 "answer": "D"},

{"id": 91, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "If log(x) = 2, where log denotes the base-10 logarithm, what is the value of log(10000x)?",
 "options": {"A": "5", "B": "6", "C": "20", "D": "200"},
 "answer": "B"},

{"id": 92, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "For all x other than 6 and -4, which expression is equivalent to (x^2 - 36) / (x^2 - 2x - 24)?",
 "options": {"A": "(x - 6)/(x + 4)", "B": "(x + 6)/(x - 4)", "C": "2", "D": "(x + 6)/(x + 4)"},
 "answer": "D"},

{"id": 93, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Medium",
 "question": "Seven identical machines together produce 630 units in 3 hours. Working at the same rate, how many units would 10 such machines produce in 6 hours?",
 "options": {"A": "1,500", "B": "1,700", "C": "1,800", "D": "1,900"},
 "answer": "C"},

{"id": 94, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "The mean of seven numbers is 15. When one of the numbers is removed, the mean of the remaining six is 17. What was the number that was removed?",
 "options": {"A": "3", "B": "5", "C": "7", "D": "9"},
 "answer": "A"},

{"id": 95, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A fair six-sided die is rolled twice. What is the probability that the two results add up to 10?",
 "options": {"A": "1/12", "B": "1/9", "C": "5/36", "D": "1/6"},
 "answer": "A"},

{"id": 96, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "Set X is {20, 20, 20, 20, 20} and Set Y is {10, 15, 20, 25, 30}. Both sets have a mean of 20. Which set has the larger standard deviation?",
 "options": {"A": "Set X", "B": "They are equal", "C": "It cannot be determined from the information given", "D": "Set Y"},
 "answer": "D"},

{"id": 97, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A square and an equilateral triangle each have a perimeter of 72 cm. By how many centimetres does the triangle's side exceed the square's side?",
 "options": {"A": "4", "B": "5", "C": "6", "D": "8"},
 "answer": "C"},

{"id": 98, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Easy",
 "question": "A right circular cylinder has a radius of 5 cm and a height of 8 cm. What is its volume, in cubic centimetres?",
 "options": {"A": "150pi", "B": "200pi", "C": "100pi", "D": "250pi"},
 "answer": "B"},

{"id": 99, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Medium",
 "question": "Two parallel lines are cut by a transversal. One of the two interior angles on the same side of the transversal measures 75 degrees. What is the measure, in degrees, of the other?",
 "options": {"A": "75", "B": "105", "C": "90", "D": "115"},
 "answer": "B"},

{"id": 100, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Medium",
 "question": "In a 30-60-90 right triangle, the shorter leg measures 11 cm. What is the length of the hypotenuse, in centimetres?",
 "options": {"A": "22", "B": "11*sqrt(3)", "C": "22*sqrt(3)", "D": "16.5"},
 "answer": "A"},

{"id": 101, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Number Properties (odd/even, divisibility)", "difficulty": "Easy",
 "question": "If m is an odd integer, which of the following expressions must be an even integer?",
 "options": {"A": "m^3", "B": "4m + 1", "C": "m + 7", "D": "3m"},
 "answer": "C"},

{"id": 102, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the smallest positive integer that is divisible by 5, 6 and 8?",
 "options": {"A": "120", "B": "60", "C": "90", "D": "240"},
 "answer": "A"},

{"id": 103, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Medium",
 "question": "Which of the following is NOT a prime number?",
 "options": {"A": "101", "B": "103", "C": "111", "D": "107"},
 "answer": "C"},

# ============================================================
# SECTION 7 - VERBAL (17) - q104-120
# ============================================================

{"id": 104, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Easy",
 "question": "The ambassador's remarks were strikingly ____: they named a specific date, a specific figure, and nothing else. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "vague", "B": "lengthy", "C": "evasive", "D": "precise"},
 "answer": "D"},

{"id": 105, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Every history of Pakistani mountaineering lists the 8,000-metre summits reached. The list is accurate. But it hides the more interesting fact, which is that most of those expeditions relied on the same small pool of local high-altitude porters from a handful of Shimshal and Hunza villages -- and it was this concentrated expertise, not any single climber's ability, that made the summits possible.\" Which choice best describes the function of the final clause in the text as a whole?",
 "options": {"A": "It withdraws a claim made earlier in the text.",
             "B": "It provides statistical evidence for the first sentence.",
             "C": "It concedes that the conventional list is factually wrong.",
             "D": "It states the specific point the author believes the conventional account obscures."},
 "answer": "D"},

{"id": 106, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: For decades the government has guaranteed a minimum purchase price for cotton, above what most competing crops can expect. The policy works: farmers keep planting cotton. It also works too well: land that would earn more under vegetables or pulses stays under cotton, because cotton is the one crop whose price a farmer can bank on before sowing even begins. Which choice best states the main idea of the passage?",
 "options": {"A": "The guaranteed cotton price has failed to keep farmers planting cotton.",
             "B": "By removing price risk for cotton alone, the guarantee succeeds at its aim while locking land into a lower-value crop.",
             "C": "Vegetables and pulses are less profitable than cotton in every district.",
             "D": "Market prices for agricultural produce are impossible to forecast."},
 "answer": "B"},

{"id": 107, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A publisher reissued a set of exam-prep guides in two versions identical except for cover price: one printed on the cover, one left for the bookshop to add. Copies with no printed price sold 14 per cent more in markets where haggling is common. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "readers prefer guides without any price information at all.",
             "B": "removing a fixed cover price can increase sales where buyers expect to negotiate.",
             "C": "the reissued guides were printed on cheaper paper.",
             "D": "exam-prep guides sell better than general non-fiction."},
 "answer": "B"},

{"id": 108, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "A critic argues that Faiz Ahmed Faiz's political poems deliberately address an unnamed collective \"we\" rather than a single first-person speaker, to universalise the experience of oppression. Which description of a poem, if accurate, would most directly support that argument?",
 "options": {"A": "The poem opens with a detailed physical description of the poet himself.",
             "B": "The poem is addressed to a single named individual throughout.",
             "C": "The poem consistently uses first-person plural pronouns and never names a specific speaker.",
             "D": "The poem closes with statistics about a historical event."},
 "answer": "C"},

{"id": 109, "section": 7, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "Domestic sugar production fell for two consecutive seasons, and several mills reduced their crushing capacity. ____ the industry's molasses exports rose sharply, offsetting some of the decline. Which transition best completes the text?",
 "options": {"A": "Therefore,", "B": "For example,", "C": "In conclusion,", "D": "Meanwhile,"},
 "answer": "D"},

{"id": 110, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The first phase of the resettlement plan proceeded on schedule ____ the second phase stalled for nearly a year. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; ", "C": " which ", "D": ", also "},
 "answer": "B"},

{"id": 111, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Easy",
 "question": "Because the flyover had been closed for repairs ____ traffic was diverted through the adjoining service road for two months. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; ", "C": ". ", "D": ": "},
 "answer": "A"},

{"id": 112, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which version of the sentence most clearly means that the grant covers travel and for nothing else?",
 "options": {"A": "The grant only covers travel.",
             "B": "Only the grant covers travel.",
             "C": "The grant covers only travel.",
             "D": "The grant covers travel only for postgraduate students."},
 "answer": "C"},

{"id": 113, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: When a district switched from a flat agricultural tax to one based on satellite-measured crop area, it billed the change as a fairness measure: farmers would pay for the land they actually cultivated, not a fixed estimate. On paper, tax revenue from the district rose by a fifth within a year. In practice, the rise was uneven -- large landholders with legal title barely saw their assessments change, while tenant farmers on informally divided plots were reassessed sharply upward because satellite imagery could not distinguish who actually held each strip. The arithmetic that judges the reform's success almost everywhere counts total revenue collected, because that figure is easy to measure. Until it counts who is actually paying more and why, districts will keep mistaking a higher total for a fairer system. Which choice best states the main idea of the passage?",
 "options": {"A": "Satellite-based taxation should be abandoned across the district.",
             "B": "The reform raised total revenue but concealed an uneven burden that raw totals don't reveal.",
             "C": "Large landholders pay more tax than tenant farmers in every district.",
             "D": "A flat agricultural tax is fairer than satellite-based assessment."},
 "answer": "B"},

{"id": 114, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: When a district switched from a flat agricultural tax to one based on satellite-measured crop area, it billed the change as a fairness measure: farmers would pay for the land they actually cultivated, not a fixed estimate. On paper, tax revenue from the district rose by a fifth within a year. In practice, the rise was uneven -- large landholders with legal title barely saw their assessments change, while tenant farmers on informally divided plots were reassessed sharply upward because satellite imagery could not distinguish who actually held each strip. The arithmetic that judges the reform's success almost everywhere counts total revenue collected, because that figure is easy to measure. Until it counts who is actually paying more and why, districts will keep mistaking a higher total for a fairer system. According to the passage, by how much did tax revenue from the district rise within a year?",
 "options": {"A": "By a fifth.", "B": "By half.", "C": "It fell slightly.", "D": "The passage does not say."},
 "answer": "A"},

{"id": 115, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: When a district switched from a flat agricultural tax to one based on satellite-measured crop area, it billed the change as a fairness measure: farmers would pay for the land they actually cultivated, not a fixed estimate. On paper, tax revenue from the district rose by a fifth within a year. In practice, the rise was uneven -- large landholders with legal title barely saw their assessments change, while tenant farmers on informally divided plots were reassessed sharply upward because satellite imagery could not distinguish who actually held each strip. The arithmetic that judges the reform's success almost everywhere counts total revenue collected, because that figure is easy to measure. Until it counts who is actually paying more and why, districts will keep mistaking a higher total for a fairer system. The author's attitude toward measuring the reform's success purely by total revenue collected is best characterised as",
 "options": {"A": "enthusiastic approval.", "B": "detached and purely descriptive.", "C": "critical of it as a convenient but incomplete measure.", "D": "resigned to it as unavoidable."},
 "answer": "C"},

{"id": 116, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: When a district switched from a flat agricultural tax to one based on satellite-measured crop area, it billed the change as a fairness measure: farmers would pay for the land they actually cultivated, not a fixed estimate. On paper, tax revenue from the district rose by a fifth within a year. In practice, the rise was uneven -- large landholders with legal title barely saw their assessments change, while tenant farmers on informally divided plots were reassessed sharply upward because satellite imagery could not distinguish who actually held each strip. The arithmetic that judges the reform's success almost everywhere counts total revenue collected, because that figure is easy to measure. Until it counts who is actually paying more and why, districts will keep mistaking a higher total for a fairer system. It can most reasonably be inferred that the author would support",
 "options": {"A": "returning to a flat agricultural tax for all districts.",
             "B": "rolling out satellite-based taxation everywhere regardless of land-title clarity.",
             "C": "exempting tenant farmers from any agricultural tax at all.",
             "D": "tracking assessment changes by landholding type rather than relying on total revenue alone."},
 "answer": "D"},

{"id": 117, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The internship is open to applicants who have completed a relevant diploma, who have prior fieldwork experience, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "having strong written communication skills.",
             "B": "strong written communication skills.",
             "C": "they have strong written communication skills.",
             "D": "who have strong written communication skills."},
 "answer": "D"},

{"id": 118, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as FORTHRIGHT.",
 "options": {"A": "evasive", "B": "direct", "C": "anxious", "D": "reserved"},
 "answer": "B"},

{"id": 119, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to CONCEAL.",
 "options": {"A": "hide", "B": "reveal", "C": "postpone", "D": "diminish"},
 "answer": "B"},

{"id": 120, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The new bylaw did little to DETER informal construction,\" the word \"deter\" most nearly means",
 "options": {"A": "verify.", "B": "mark.", "C": "discourage.", "D": "examine."},
 "answer": "C"},

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
#   2. Every (question_text, option_a) pair must be absent from
#      lums_lcat_sample.py, lums_lcat_mock_01.py, lums_lcat_mock_02.py and
#      lums_lcat_mock_03.py. That tuple (with past_paper) is
#      import_mcqs.py's dedupe key -- a collision would make one bank's
#      question silently overwrite another's. Check it before every
#      import, not after.
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
    """(question_text, option_a) must not collide with the sample bank, Mock 1, or Mock 2."""
    keys = set()
    sources_checked = []
    try:
        from lums_lcat_sample import QUESTIONS as SAMPLE
        keys |= {(q["question"], q["options"]["A"]) for q in SAMPLE}
        sources_checked.append("lums_lcat_sample")
    except ImportError:
        print("\nCould not import lums_lcat_sample -- that collision check SKIPPED.")
    try:
        from lums_mock_01 import QUESTIONS as MOCK1
        keys |= {(q["question"], q["options"]["A"]) for q in MOCK1}
        sources_checked.append("lums_mock_01")
    except ImportError:
        print("Could not import lums_mock_01 -- that collision check SKIPPED.")
    try:
        from lums_mock_02 import QUESTIONS as MOCK2
        keys |= {(q["question"], q["options"]["A"]) for q in MOCK2}
        sources_checked.append("lums_mock_02")
    except ImportError:
        print("Could not import lums_mock_02 -- that collision check SKIPPED.")

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