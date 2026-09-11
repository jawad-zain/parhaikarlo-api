"""
LUMS Common Admission Test (LCAT) - Full-Length Mock Test #2
=============================================================
ParhaiKarlo-prepared full-length mock test. NOT an official LUMS past paper.
Answer keys prepared by content team, pending human verification.

Nothing in this file is taken from LUMS' official "Sample Questions for
Verbal & Math Sections" guide (raw-sources/sample_lcat_2025.pdf), nor from
`lums_lcat_mock_01.py`. Every question below is newly written; the topic and
subtopic assigned to each question slot mirrors the position it occupies in
Mock 1 (same section, same slot), since those labels were already verified
against the syllabus when Mock 1 was checked in.

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
and lums_lcat_mock_01.py.

Each question is a dict:
    id, section, subject, topic, subtopic, difficulty, question,
    options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.
"""

SOURCE = "parhaikarlo_mock_02"

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
 "question": "The conservators restoring Karachi's Mohatta Palace worked with ____ care, testing each patch of lime plaster on a hidden corner before applying it to the facade. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "careless", "B": "hurried", "C": "indifferent", "D": "painstaking"},
 "answer": "D"},

{"id": 2, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Medium",
 "question": "Text: \"Karakoram glaciers have long been cited as an anomaly, gaining mass while most of the world's glaciers shrink. The claim is broadly accurate. It has also encouraged a complacency the data do not support: gains in the eastern Karakoram have been offset by losses further west, and the range as a whole has been roughly stable, not growing.\" Which choice best describes the function of the third sentence in the text as a whole?",
 "options": {"A": "It concedes an error in the claim just presented.",
             "B": "It qualifies an accurate claim by showing the complacency it has invited is unwarranted.",
             "C": "It provides a specific example that illustrates the first sentence.",
             "D": "It summarises a scholarly consensus the author goes on to endorse."},
 "answer": "B"},

{"id": 3, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: Karachi Port has handled the bulk of Pakistan's seaborne trade for over a century, and expanding it further is the fastest way to raise national trade capacity. Text 2: Karachi Port's channel cannot be dredged much deeper without threatening the mangrove creeks around it; real capacity growth has to come from a second deep-water port, not from expanding this one. Based on the texts, how would the author of Text 2 most likely respond to the claim in Text 1 that expanding the port is the fastest way to grow capacity?",
 "options": {"A": "By agreeing, but insisting the dredging proceed more slowly.",
             "B": "By conceding that mangrove creeks are not significantly affected by dredging.",
             "C": "By questioning whether Karachi Port has in fact handled most of Pakistan's trade historically.",
             "D": "By arguing that expanding this port runs into a physical and ecological limit that makes a second port necessary instead."},
 "answer": "D"},

{"id": 4, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Easy",
 "question": "Passage: The Deosai plains hold one of the largest surviving populations of Himalayan brown bear in South Asia, but for years nobody knew how large. The bears range across a plateau the size of a small country, and a bear seen once might be seen again fifty kilometres away the following week. Researchers now snag tufts of hair on barbed-wire loops set around scent stations; because each tuft carries a distinct genetic signature, individual bears can be told apart without ever being captured, and a defensible population count has finally emerged. What is the main idea of the passage?",
 "options": {"A": "The Deosai plains are the largest plateau in South Asia.",
             "B": "Genetic sampling from snagged hair has allowed researchers to count individual bears that were previously impossible to census reliably.",
             "C": "Himalayan brown bears are more numerous than snow leopards.",
             "D": "Barbed-wire traps have proven harmful to the bear population."},
 "answer": "B"},

{"id": 5, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: Over a fifteen-year period, the number of registered beekeeping households in Swat rose sharply, while honey imports into the country fell only slightly. Most of the new honey entered informal local markets rather than the packaged retail chains that import brands dominate. Which choice most logically completes the reasoning in the passage?",
 "options": {"A": "Therefore, imported honey brands are likely to disappear from retail shelves soon.",
             "B": "Therefore, honey consumption in Pakistan has fallen overall.",
             "C": "Therefore, Swat's beekeepers export most of their honey abroad.",
             "D": "Therefore, the growth in local beekeeping appears to have expanded the market for unpackaged honey without displacing the packaged import trade."},
 "answer": "D"},

{"id": 6, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A researcher claims that a province's rise in total rice exports was driven more by an increase in cultivated area than by any improvement in yield per hectare. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Exports rose 40%, while cultivated area rose 36% and yield per hectare rose 3%.",
             "B": "Exports rose 40%, while cultivated area rose 5% and yield per hectare rose 33%.",
             "C": "Exports fell 5%, while cultivated area rose 36%.",
             "D": "Exports rose 40%, and the international price of rice fell 10%."},
 "answer": "A"},

{"id": 7, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "While researching Abdul Sattar Edhi, a student compiles three notes: his ambulance service began with a single van; he refused government funding for decades to preserve the service's independence; and the network eventually became one of the largest volunteer ambulance fleets in the world. Which statement best synthesises these notes?",
 "options": {"A": "Edhi's ambulance service began small and, by insisting on financial independence from government, grew into one of the largest volunteer fleets in the world.",
             "B": "Edhi was primarily interested in expanding government social services.",
             "C": "Edhi's ambulance service received extensive corporate sponsorship.",
             "D": "Edhi's fleet remained roughly the same size for most of its history."},
 "answer": "A"},

{"id": 8, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "Punjab's tube-well irrigation expanded rapidly after diesel pumps became affordable in the 1980s. ____ groundwater levels in several districts have fallen by more than a metre a year since, and some wells now run dry before the rabi season ends. Which transition best completes the text?",
 "options": {"A": "Similarly,", "B": "For example,", "C": "Consequently,", "D": "In addition,"},
 "answer": "C"},

{"id": 9, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: ajrak block-printing uses natural indigo and madder dyes; a single large ajrak can take up to two weeks to finish; artisans in Sindh have passed the technique down for generations; finished pieces are worn at weddings and given as gifts. The student wants to emphasise that the craft is both labour-intensive and central to social life. Which choice best accomplishes this goal?",
 "options": {"A": "Ajrak is printed using natural indigo and madder dyes passed down through generations of Sindhi artisans.",
             "B": "Ajrak block-printing has been practised in Sindh for generations.",
             "C": "A single large ajrak can take up to two weeks to complete, and finished pieces are worn at weddings and exchanged as gifts.",
             "D": "Finished ajrak pieces are commonly given as wedding gifts."},
 "answer": "C"},

{"id": 10, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "The archive of oral histories collected from Partition survivors ____ more than four hundred recorded interviews. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "contain", "B": "contains", "C": "are containing", "D": "have contained"},
 "answer": "B"},

{"id": 11, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "The fishing cooperatives rejected the new licensing fee, and ____ complaint was later taken up by the provincial assembly. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "its", "B": "there", "C": "it's", "D": "their"},
 "answer": "D"},

{"id": 12, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The survey team reached one firm conclusion ____ the aquifer beneath the district was being drawn down faster than rainfall could replenish it. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", that", "B": ": ", "C": "; which", "D": ", being"},
 "answer": "B"},

{"id": 13, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Medium",
 "question": "The bridge had stood for nearly a century ____ engineers closed it to heavy vehicles after the latest inspection. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "; ", "B": ", ", "C": " which ", "D": " and which "},
 "answer": "A"},

{"id": 14, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Having surveyed the coral reefs off the Sindh coast for three seasons, ____\"",
 "options": {"A": "the conclusion of the divers was that bleaching had worsened.",
             "B": "it was concluded by the divers that bleaching had worsened.",
             "C": "the divers concluded that bleaching had worsened.",
             "D": "bleaching was shown by the divers to have worsened."},
 "answer": "C"},

{"id": 15, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: Multan's blue pottery is usually filed under handicraft, a word that suggests something made for its own sake. The kilns tell a different story: firing schedules are set around wedding-season and export orders, glaze recipes are guarded the way a factory guards a patent, and a workshop's output is costed per piece before a single pot is thrown. The craft, in other words, runs on the same logic as any small manufacturing business. Which choice best states the main idea of the passage?",
 "options": {"A": "Multan's blue pottery is more decorative than functional.",
             "B": "Glaze recipes in Multan have remained unchanged for centuries.",
             "C": "Export orders account for most of Multan's pottery output.",
             "D": "Blue pottery is better understood as a costed manufacturing operation than as craft made for its own sake."},
 "answer": "D"},

{"id": 16, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: Multan's blue pottery is usually filed under handicraft, a word that suggests something made for its own sake. The kilns tell a different story: firing schedules are set around wedding-season and export orders, glaze recipes are guarded the way a factory guards a patent, and a workshop's output is costed per piece before a single pot is thrown. The craft, in other words, runs on the same logic as any small manufacturing business. The author's attitude toward the conventional description of blue pottery as mere handicraft is best characterised as",
 "options": {"A": "openly contemptuous.",
             "B": "mildly corrective.",
             "C": "entirely neutral.",
             "D": "wistfully nostalgic."},
 "answer": "B"},

{"id": 17, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as PRAGMATIC.",
 "options": {"A": "idealistic", "B": "reckless", "C": "stubborn", "D": "practical"},
 "answer": "D"},

{"id": 18, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to the underlined word as it is used here: \"The negotiators reached a TENTATIVE agreement.\"",
 "options": {"A": "firm", "B": "brief", "C": "informal", "D": "private"},
 "answer": "A"},

# ============================================================
# SECTION 2 - MATH (17) - q19-35
# ============================================================

{"id": 19, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Easy",
 "question": "If 4(x - 2) + 3 = 2x + 9, what is the value of x?",
 "options": {"A": "5", "B": "6", "C": "7", "D": "8"},
 "answer": "C"},

{"id": 20, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 3x + y = 17 and x - y = 3, what is the value of x?",
 "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
 "answer": "C"},

{"id": 21, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "Which of the following describes all values of x for which 5 - 3x > 14?",
 "options": {"A": "x > -3", "B": "x < 3", "C": "x > 3", "D": "x < -3"},
 "answer": "D"},

{"id": 22, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Medium",
 "question": "An arithmetic sequence has first term 7 and common difference 4. What is the sum of its first 15 terms?",
 "options": {"A": "525", "B": "500", "C": "550", "D": "480"},
 "answer": "A"},

{"id": 23, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "The equation x^2 + kx + 18 = 0 has roots 2 and 9. What is the value of k?",
 "options": {"A": "-11", "B": "11", "C": "-18", "D": "18"},
 "answer": "A"},

{"id": 24, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is the value of 27^(2/3) * 4^(1/2)?",
 "options": {"A": "9", "B": "12", "C": "18", "D": "24"},
 "answer": "C"},

{"id": 25, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "What is the value of (log_2 32) - (log_5 25)?",
 "options": {"A": "3", "B": "2", "C": "7", "D": "1"},
 "answer": "A"},

{"id": 26, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "If 1/x + 1/(3x) = 2/3, what is the value of x?",
 "options": {"A": "1/2", "B": "1", "C": "2", "D": "3"},
 "answer": "C"},

{"id": 27, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "A shopkeeper raises the price of an item by 30% and then, in a sale, reduces the new price by 20%. Compared with the original price, the final price is",
 "options": {"A": "4% higher.", "B": "4% lower.", "C": "unchanged.", "D": "10% higher."},
 "answer": "A"},

{"id": 28, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Easy",
 "question": "A sum of Rs. 110,000 is divided between two partners in the ratio 4 : 7. By how much does the larger share exceed the smaller share, in rupees?",
 "options": {"A": "20,000", "B": "30,000", "C": "40,000", "D": "25,000"},
 "answer": "B"},

{"id": 29, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "A class of 20 students has a mean score of 75. Five more students, whose mean score is 90, join the class. What is the mean score of all 25 students?",
 "options": {"A": "80", "B": "79", "C": "78", "D": "77"},
 "answer": "C"},

{"id": 30, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A bag contains 5 red marbles and 7 blue marbles. Two marbles are drawn at random without replacement. What is the probability that both are red?",
 "options": {"A": "5/33", "B": "1/6", "C": "2/11", "D": "5/22"},
 "answer": "A"},

{"id": 31, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A rectangle has a perimeter of 40 cm, and its length is 6 cm greater than its width. What is its area, in square centimetres?",
 "options": {"A": "84", "B": "77", "C": "98", "D": "91"},
 "answer": "D"},

{"id": 32, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Easy",
 "question": "A right triangle has legs of length 8 cm and 15 cm. What is its perimeter, in centimetres?",
 "options": {"A": "36", "B": "38", "C": "40", "D": "42"},
 "answer": "C"},

{"id": 33, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Easy",
 "question": "A circle has an area of 49pi square centimetres. What is its circumference, in centimetres?",
 "options": {"A": "7pi", "B": "14pi", "C": "49pi", "D": "28pi"},
 "answer": "B"},

{"id": 34, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Ratios", "difficulty": "Medium",
 "question": "In a right triangle, theta is an acute angle and sin(theta) = 7/25. What is the value of cos(theta)?",
 "options": {"A": "24/25", "B": "7/24", "C": "25/24", "D": "7/25"},
 "answer": "A"},

{"id": 35, "section": 2, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the least common multiple of 15 and 20, minus their greatest common divisor?",
 "options": {"A": "45", "B": "50", "C": "55", "D": "60"},
 "answer": "C"},

# ============================================================
# SECTION 3 - VERBAL (17) - q36-52
# ============================================================

{"id": 36, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "Though hailed at its launch as a breakthrough, the irrigation scheme turned out to be largely ____: five years on, less than a tenth of the promised canal network had actually been dug. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "transformative", "B": "premature", "C": "contentious", "D": "illusory"},
 "answer": "D"},

{"id": 37, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Development economists have long modelled microfinance as a straightforward ladder out of poverty: lend to a household, and it invests, earns, and climbs. The model is elegant, and it predicts steadily rising incomes among borrowers. That is not what repeated household surveys in rural Sindh show: many borrowing households simply use the loan to smooth an existing income, not to grow one.\" Which choice best describes the function of the final sentence in the text as a whole?",
 "options": {"A": "It supplies an example that confirms the model's prediction.",
             "B": "It introduces survey evidence that conflicts with the model's prediction.",
             "C": "It proposes a refinement that would make the model more accurate.",
             "D": "It restates the model's central claim in more concrete terms."},
 "answer": "B"},

{"id": 38, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: Over two decades, the total area under sugarcane in Pakistan grew only modestly, while the water allocated to sugarcane districts grew far faster, because cane is a notoriously thirsty crop and provincial water boards rarely meter what reaches an individual field. Agricultural economists warn against treating the modest growth in area as reassuring: the real story is how much water an expanding cane sector is pulling away from other crops nearby. Which choice best states the main idea of the passage?",
 "options": {"A": "Sugarcane cultivation in Pakistan has become significantly more water-efficient.",
             "B": "Provincial water boards meter water use accurately.",
             "C": "The modest growth in sugarcane area understates the crop's growing claim on regional water supplies.",
             "D": "Total area under sugarcane is a more important statistic than water use."},
 "answer": "C"},

{"id": 39, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: Pakistan's wetlands are managed province by province, but the migratory waterfowl that draw the most attention -- bar-headed geese, common cranes -- pass through several provinces in a single season, and the same flock is often counted at more than one site along its route. It follows that separate provincial waterfowl counts ____ Which choice most logically completes the text?",
 "options": {"A": "should be conducted more often than they currently are.",
             "B": "are the only practical way to track migratory birds.",
             "C": "will always undercount the birds in each province.",
             "D": "cannot simply be summed to produce a reliable national total."},
 "answer": "D"},

{"id": 40, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "In a study of informal credit among Lahore's small traders, a researcher argues that traders borrow from commission agents not because banks refuse them credit but because the agent's loan arrives without paperwork or delay. Which quotation from a trader interview, if authentic, would most directly support that argument?",
 "options": {"A": "\"No bank has ever agreed to open an account for my shop.\"",
             "B": "\"The bank could probably lend to me, but the agent hands over the cash the same afternoon, no forms at all.\"",
             "C": "\"The agent charges nearly twice what a bank would charge in interest.\"",
             "D": "\"I have known my commission agent for over twenty years.\""},
 "answer": "B"},

{"id": 41, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student researching the Kalash valley spring festival Joshi records three observations: it marks the start of the pastoral year; it involves days of communal singing and dancing; and it now draws visitors from across the country and abroad. Which statement best synthesises these observations?",
 "options": {"A": "Joshi lasts for several days and includes singing and dancing.",
             "B": "The Kalash valley has had little contact with the wider subcontinent in modern times.",
             "C": "Visitors to Kalash mainly come from abroad rather than from within the country.",
             "D": "Joshi marks the start of the pastoral year with days of communal singing and dancing, and now also draws visitors from across the country and abroad."},
 "answer": "D"},

{"id": 42, "section": 3, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "The 2005 Kashmir earthquake destroyed most masonry buildings in the affected districts. ____ timber-and-stone structures built in the traditional dhajji-dewari style, with their flexible frames, survived the same shaking largely intact. Which transition best completes the text?",
 "options": {"A": "Consequently,", "B": "By contrast,", "C": "Similarly,", "D": "In short,"},
 "answer": "B"},

{"id": 43, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The programme trains health workers to screen for anaemia, to counsel new mothers, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "referring severe cases to the district hospital.",
             "B": "they refer severe cases to the district hospital.",
             "C": "to refer severe cases to the district hospital.",
             "D": "severe cases are referred to the district hospital."},
 "answer": "C"},

{"id": 44, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The delegation toured three heritage sites in Sindh ____ Mohenjo-daro, Ranikot Fort and the Makli necropolis. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ": ", "B": ", ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 45, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "Each of the district hospitals ____ required to submit a quarterly inventory. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "are", "B": "were", "C": "is", "D": "have been"},
 "answer": "C"},

{"id": 46, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Hard",
 "question": "The dam was completed in 2009 ____ sedimentation behind it has reduced its storage capacity every year since. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; nevertheless, ", "C": " and which ", "D": ", however "},
 "answer": "B"},

{"id": 47, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: The houbara bustard migrates each winter from Central Asia into Pakistan's deserts, and for decades it has occupied an uncomfortable place in national policy: officially protected, yet legally hunted under a permit system reserved for foreign dignitaries. Conservationists argue the permits are set without any reliable count of how many birds actually arrive in a given year, so a quota fixed on paper may bear no relation to what the population can sustain. Captive-breeding programmes release thousands of birds annually, and officials point to the releases as evidence the population is secure. Independent surveys tell a thinner story: wild sightings along traditional wintering routes have grown sparser even as release numbers have grown larger, which suggests that captive-bred birds are not simply topping up a healthy wild population but substituting for one that is shrinking. Which choice best states the main idea of the passage?",
 "options": {"A": "Houbara bustard hunting has been banned outright in Pakistan.",
             "B": "The houbara bustard migrates from Pakistan into Central Asia each winter.",
             "C": "Rising numbers of captive-bred releases may be masking a decline in the wild houbara population rather than confirming its health.",
             "D": "Foreign dignitaries no longer receive hunting permits for houbara bustards."},
 "answer": "C"},

{"id": 48, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: The houbara bustard migrates each winter from Central Asia into Pakistan's deserts, and for decades it has occupied an uncomfortable place in national policy: officially protected, yet legally hunted under a permit system reserved for foreign dignitaries. Conservationists argue the permits are set without any reliable count of how many birds actually arrive in a given year, so a quota fixed on paper may bear no relation to what the population can sustain. Captive-breeding programmes release thousands of birds annually, and officials point to the releases as evidence the population is secure. Independent surveys tell a thinner story: wild sightings along traditional wintering routes have grown sparser even as release numbers have grown larger, which suggests that captive-bred birds are not simply topping up a healthy wild population but substituting for one that is shrinking. According to the passage, how are hunting permits for the houbara bustard currently allocated?",
 "options": {"A": "Through an open lottery available to any applicant.",
             "B": "Only to licensed conservation researchers.",
             "C": "Under a permit system reserved for foreign dignitaries.",
             "D": "By provincial wildlife departments to local hunters."},
 "answer": "C"},

{"id": 49, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: The houbara bustard migrates each winter from Central Asia into Pakistan's deserts, and for decades it has occupied an uncomfortable place in national policy: officially protected, yet legally hunted under a permit system reserved for foreign dignitaries. Conservationists argue the permits are set without any reliable count of how many birds actually arrive in a given year, so a quota fixed on paper may bear no relation to what the population can sustain. Captive-breeding programmes release thousands of birds annually, and officials point to the releases as evidence the population is secure. Independent surveys tell a thinner story: wild sightings along traditional wintering routes have grown sparser even as release numbers have grown larger, which suggests that captive-bred birds are not simply topping up a healthy wild population but substituting for one that is shrinking. The author's attitude toward officials' claim that the population is secure is best characterised as",
 "options": {"A": "fully persuaded.",
             "B": "openly mocking.",
             "C": "skeptical, given the surveys cited.",
             "D": "indifferent."},
 "answer": "C"},

{"id": 50, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: The houbara bustard migrates each winter from Central Asia into Pakistan's deserts, and for decades it has occupied an uncomfortable place in national policy: officially protected, yet legally hunted under a permit system reserved for foreign dignitaries. Conservationists argue the permits are set without any reliable count of how many birds actually arrive in a given year, so a quota fixed on paper may bear no relation to what the population can sustain. Captive-breeding programmes release thousands of birds annually, and officials point to the releases as evidence the population is secure. Independent surveys tell a thinner story: wild sightings along traditional wintering routes have grown sparser even as release numbers have grown larger, which suggests that captive-bred birds are not simply topping up a healthy wild population but substituting for one that is shrinking. It can most reasonably be inferred that the author regards captive-breeding releases as",
 "options": {"A": "a reliable substitute for counting the wild population directly.",
             "B": "evidence that risks being misread as proof of a healthy wild population when independent surveys suggest otherwise.",
             "C": "irrelevant to the debate over hunting permits.",
             "D": "more effective than any current conservation method."},
 "answer": "B"},

{"id": 51, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as OBSTINATE.",
 "options": {"A": "flexible", "B": "cautious", "C": "stubborn", "D": "generous"},
 "answer": "C"},

{"id": 52, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The minister's promise to reform the tax code proved HOLLOW,\" the word \"hollow\" most nearly means",
 "options": {"A": "empty of real substance.",
             "B": "physically concave.",
             "C": "loud.",
             "D": "temporary."},
 "answer": "A"},

# ============================================================
# SECTION 4 - MATH (17) - q53-69
# ============================================================

{"id": 53, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in Two Variables", "difficulty": "Medium",
 "question": "A line in the xy-plane passes through the points (1, 4) and (5, 16). What is the y-coordinate of its y-intercept?",
 "options": {"A": "1", "B": "2", "C": "3", "D": "-1"},
 "answer": "A"},

{"id": 54, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "The function f is defined by f(x) = 4x - 9. If f(a) = 15, what is the value of a?",
 "options": {"A": "5", "B": "6", "C": "7", "D": "8"},
 "answer": "B"},

{"id": 55, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 4x + 3y = 25 and 2x - 3y = -1, what is the value of y?",
 "options": {"A": "2", "B": "3", "C": "4", "D": "5"},
 "answer": "B"},

{"id": 56, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "A delivery van weighs 1,000 kg when empty, and the total weight of the loaded van must not exceed 1,900 kg. If each crate weighs 60 kg, what is the greatest number of whole crates the van can carry?",
 "options": {"A": "14", "B": "15", "C": "16", "D": "13"},
 "answer": "B"},

{"id": 57, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Nonlinear Functions", "difficulty": "Medium",
 "question": "What is the minimum value of the function f(x) = x^2 - 6x + 2?",
 "options": {"A": "-5", "B": "-9", "C": "-7", "D": "7"},
 "answer": "C"},

{"id": 58, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Polynomial Expressions", "difficulty": "Easy",
 "question": "Which expression is equivalent to (3x - 2)(x + 4)?",
 "options": {"A": "3x^2 + 10x - 8",
             "B": "3x^2 - 10x - 8",
             "C": "3x^2 + 14x - 8",
             "D": "3x^2 + 10x + 8"},
 "answer": "A"},

{"id": 59, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "How many real solutions does the equation x^2 + 2x + 5 = 0 have?",
 "options": {"A": "Two distinct real solutions",
             "B": "Exactly one real solution",
             "C": "Infinitely many real solutions",
             "D": "No real solutions"},
 "answer": "D"},

{"id": 60, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is sqrt(32) + sqrt(8) in simplest radical form?",
 "options": {"A": "6*sqrt(2)", "B": "4*sqrt(10)", "C": "2*sqrt(10)", "D": "sqrt(40)"},
 "answer": "A"},

{"id": 61, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Unit Conversion", "difficulty": "Easy",
 "question": "A car consumes fuel at a rate of 6 litres per 100 kilometres. How many litres will it consume on a 450-kilometre journey at that rate?",
 "options": {"A": "25", "B": "27", "C": "29", "D": "24"},
 "answer": "B"},

{"id": 62, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Two-Variable Data Interpretation (tables/graphs)", "difficulty": "Medium",
 "question": "A shop records the number of units sold on each of five days: Monday 38, Tuesday 45, Wednesday 35, Thursday 49, Friday 52. By what percentage did the number of units sold increase from Wednesday to Thursday?",
 "options": {"A": "35%", "B": "20%", "C": "40%", "D": "45%"},
 "answer": "C"},

{"id": 63, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "For the data set 3, 6, 6, 8, 12, what is the mean minus the median?",
 "options": {"A": "0", "B": "1", "C": "2", "D": "3"},
 "answer": "B"},

{"id": 64, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "After a 25% discount, an item sells for Rs. 3,750. What was its price before the discount, in rupees?",
 "options": {"A": "5,000", "B": "4,800", "C": "4,500", "D": "4,687.5"},
 "answer": "A"},

{"id": 65, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Medium",
 "question": "A cube has a volume of 343 cubic centimetres. What is its total surface area, in square centimetres?",
 "options": {"A": "294", "B": "196", "C": "245", "D": "343"},
 "answer": "A"},

{"id": 66, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Easy",
 "question": "The three interior angles of a triangle are in the ratio 3 : 4 : 5. What is the measure of the largest angle, in degrees?",
 "options": {"A": "90", "B": "75", "C": "80", "D": "60"},
 "answer": "B"},

{"id": 67, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Medium",
 "question": "A sector of a circle of radius 12 cm has a central angle of 30 degrees. What is the area of the sector, in square centimetres?",
 "options": {"A": "12pi", "B": "6pi", "C": "24pi", "D": "36pi"},
 "answer": "A"},

{"id": 68, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Identities", "difficulty": "Medium",
 "question": "For any angle theta with cos(theta) not equal to 0, which expression is equivalent to (1 - sin^2(theta)) / cos(theta)?",
 "options": {"A": "sin(theta)", "B": "1", "C": "tan(theta)", "D": "cos(theta)"},
 "answer": "D"},

{"id": 69, "section": 4, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Easy",
 "question": "What is the sum of all prime numbers strictly between 30 and 40?",
 "options": {"A": "62", "B": "68", "C": "70", "D": "74"},
 "answer": "B"},

# ============================================================
# SECTION 5 - VERBAL (17) - q70-86
# ============================================================

{"id": 70, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "The tribunal's ruling was notable for its ____: it addressed each of the eleven disputed clauses in turn, citing the relevant precedent for every one. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "brevity", "B": "ambiguity", "C": "leniency", "D": "thoroughness"},
 "answer": "D"},

{"id": 71, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: A national entrance exam, administered on paper in a single sitting, is the fairest way to rank applicants because every candidate faces the identical set of questions under identical conditions. Text 2: Identical questions do not guarantee a fair ranking when candidates arrive with wildly unequal access to past papers, tutoring, and quiet places to study; the exam only equalises what happens inside the room, not what happens before it. The author of Text 2 would most likely characterise Text 1's claim about fairness as",
 "options": {"A": "false, because the questions are not actually identical for every candidate.",
             "B": "correct, and sufficient reason to keep the exam unchanged.",
             "C": "accurate about conditions in the exam room but incomplete about the preparation that precedes it.",
             "D": "irrelevant, because tutoring has no measurable effect on scores."},
 "answer": "C"},

{"id": 72, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: Ranikot Fort, sometimes called the Great Wall of Sindh, is usually valued for its scale -- its outer wall runs for roughly thirty kilometres, longer than many national capitals' city limits. But scale alone doesn't explain why it was built where it was: the fort's placement corresponds almost exactly with a set of low passes that any force moving between the Indus plain and the Kirthar hills would have had to use, which suggests it was raised less as a monument than as a chokepoint. Which choice best states the main idea of the passage?",
 "options": {"A": "Ranikot Fort's chief significance lies in guarding key mountain passes rather than in its sheer scale.",
             "B": "Ranikot Fort is longer than the city limits of most national capitals.",
             "C": "The Kirthar hills have never been used as a trade route.",
             "D": "Ranikot Fort was built primarily as a ceremonial monument."},
 "answer": "A"},

{"id": 73, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A city introduced dedicated bus lanes along a single congested corridor. In the first year, average travel time on that corridor fell by 22 per cent. Over the same period, travel times on the parallel general-traffic lanes rose by 15 per cent. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "the bus lanes had no effect on travel behaviour.",
             "B": "total citywide travel time fell by roughly 22 per cent.",
             "C": "at least part of the improvement on the corridor came at the cost of slower general traffic rather than from fewer total trips.",
             "D": "drivers in the general lanes were unaware the bus lanes existed."},
 "answer": "C"},

{"id": 74, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A clinic claims its new outreach programme reduced missed vaccination appointments more among first-time mothers than among mothers who had already had a child. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Missed-appointment rates among first-time mothers fell by 18 points, while rates among mothers with a prior child fell by 3 points.",
             "B": "The clinic's overall missed-appointment rate fell by 10 points.",
             "C": "Mothers with a prior child had the lowest missed-appointment rate in the clinic.",
             "D": "Attendance at the programme's optional sessions was highest among first-time mothers."},
 "answer": "A"},

{"id": 75, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student compiles three observations about the Badshahi Mosque: it was commissioned in 1673 on the orders of Aurangzeb; its courtyard can hold tens of thousands of worshippers; and it remained the largest mosque in the world for nearly three centuries. Which statement best synthesises these observations?",
 "options": {"A": "Badshahi Mosque was commissioned by Aurangzeb in 1673, and its vast courtyard let it stand as the world's largest mosque for close to three hundred years.",
             "B": "Aurangzeb commissioned several mosques across the Mughal empire.",
             "C": "The mosque's courtyard is smaller than that of most modern mosques.",
             "D": "Badshahi Mosque was built primarily for administrative use."},
 "answer": "A"},

{"id": 76, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "The museum digitised its entire photographic archive over a three-year project. ____ a researcher in Multan can now view prints that once existed only in a single physical folder in Lahore. Which transition best completes the text?",
 "options": {"A": "Nevertheless,", "B": "As a result,", "C": "By comparison,", "D": "Admittedly,"},
 "answer": "B"},

{"id": 77, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: the Basant kite festival traditionally marked the start of spring in Punjab; kite string is sometimes coated with ground glass; the festival was banned in several districts after string-related injuries and deaths; smaller, informal celebrations continue in private spaces. The student wants to emphasise that the festival's history and its ban are directly connected. Which choice best accomplishes this goal?",
 "options": {"A": "Basant traditionally marked the start of spring in Punjab.",
             "B": "Smaller celebrations of Basant continue in private spaces.",
             "C": "Kite string is sometimes coated with ground glass.",
             "D": "After string-related injuries and deaths, the once-public Basant festival was banned in several districts, though smaller private celebrations continue."},
 "answer": "D"},

{"id": 78, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The audit's findings ____ released in June, prompted an immediate response from two ministries. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ": ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 79, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "Every one of the surveyed shops reported that ____ monthly rent had increased at least once that year. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "their", "B": "its", "C": "it's", "D": "whose"},
 "answer": "B"},

{"id": 80, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Built on the orders of Aurangzeb and unrivalled in size for centuries, ____\"",
 "options": {"A": "historians regard the Badshahi Mosque as an architectural landmark.",
             "B": "the mosque's courtyard is what most visitors remember.",
             "C": "the Badshahi Mosque still dominates Lahore's skyline near the fort.",
             "D": "it is Lahore's skyline that the Badshahi Mosque dominates."},
 "answer": "C"},

{"id": 81, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The report praised the clinic's low wait times, its trained staff, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "it kept detailed patient records.",
             "B": "that its records were detailed.",
             "C": "keeping detailed patient records.",
             "D": "the thoroughness of its patient records."},
 "answer": "D"},

{"id": 82, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Hard",
 "question": "Neither the project manager nor the site engineers ____ satisfied with the revised timeline. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "was", "B": "is", "C": "has been", "D": "were"},
 "answer": "D"},

{"id": 83, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Hard",
 "question": "Passage: For decades Pakistan's power sector has blamed its losses on theft and on unpaid bills, and both complaints are real. Neither explains why so much of the electricity that is properly billed and properly paid for still never reaches a customer's meter. That loss happens earlier, in transmission lines strung decades ago for a smaller, more concentrated grid, and in transformers run well past the load they were built to carry. The fix is not chiefly in the billing department. It is in the wires themselves. Which choice best states the main idea of the passage?",
 "options": {"A": "Theft and unpaid bills are the chief cause of Pakistan's power-sector losses.",
             "B": "The sector's losses are better explained by outdated transmission infrastructure than by billing failures alone.",
             "C": "Pakistan's transformers were built to carry more load than the grid currently requires.",
             "D": "The power sector should stop billing customers for electricity."},
 "answer": "B"},

{"id": 84, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: For decades Pakistan's power sector has blamed its losses on theft and on unpaid bills, and both complaints are real. Neither explains why so much of the electricity that is properly billed and properly paid for still never reaches a customer's meter. That loss happens earlier, in transmission lines strung decades ago for a smaller, more concentrated grid, and in transformers run well past the load they were built to carry. The fix is not chiefly in the billing department. It is in the wires themselves. It can most reasonably be inferred that the author would agree with which statement?",
 "options": {"A": "Improving bill collection alone would resolve most of the sector's losses.",
             "B": "Theft is a fabricated excuse used by utilities.",
             "C": "Upgrading ageing transmission infrastructure would address a cause of losses that billing reforms cannot.",
             "D": "The grid was originally built larger than it needed to be."},
 "answer": "C"},

{"id": 85, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as METICULOUS.",
 "options": {"A": "careless", "B": "indifferent", "C": "hasty", "D": "thorough"},
 "answer": "D"},

{"id": 86, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The board's decision to postpone the merger was largely a SAFE move,\" the word \"safe\" most nearly means",
 "options": {"A": "protected from theft.",
             "B": "financially profitable.",
             "C": "cautious rather than bold.",
             "D": "legally required."},
 "answer": "C"},

# ============================================================
# SECTION 6 - MATH (17) - q87-103
# ============================================================

{"id": 87, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Medium",
 "question": "If x/4 - 3 = x/6, what is the value of x?",
 "options": {"A": "30", "B": "33", "C": "36", "D": "40"},
 "answer": "C"},

{"id": 88, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Hard",
 "question": "In an arithmetic sequence the 8th term is 29 and the 13th term is 54. What is the first term?",
 "options": {"A": "-6", "B": "-1", "C": "1", "D": "6"},
 "answer": "A"},

{"id": 89, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "A taxi charges a fixed Rs. 120 plus Rs. 40 for every kilometre travelled. A journey costs Rs. 520. How many kilometres was the journey?",
 "options": {"A": "12", "B": "11", "C": "10", "D": "9"},
 "answer": "C"},

{"id": 90, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Easy",
 "question": "What is the sum of the solutions of x^2 - 8x + 7 = 0?",
 "options": {"A": "7", "B": "-8", "C": "-7", "D": "8"},
 "answer": "D"},

{"id": 91, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "If log(x) = 4, where log denotes the base-10 logarithm, what is the value of log(1000x)?",
 "options": {"A": "7", "B": "6", "C": "40", "D": "4000"},
 "answer": "A"},

{"id": 92, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "For all x other than 4 and -2, which expression is equivalent to (x^2 - 16) / (x^2 - 2x - 8)?",
 "options": {"A": "(x - 4)/(x + 2)", "B": "(x + 4)/(x + 2)", "C": "2", "D": "(x + 4)/(x - 2)"},
 "answer": "B"},

{"id": 93, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Medium",
 "question": "Eight identical machines together produce 960 units in 4 hours. Working at the same rate, how many units would 10 such machines produce in 5 hours?",
 "options": {"A": "1,200", "B": "1,350", "C": "1,500", "D": "1,600"},
 "answer": "C"},

{"id": 94, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "The mean of six numbers is 20. When one of the numbers is removed, the mean of the remaining five is 22. What was the number that was removed?",
 "options": {"A": "8", "B": "10", "C": "12", "D": "14"},
 "answer": "B"},

{"id": 95, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A fair six-sided die is rolled twice. What is the probability that the two results add up to 8?",
 "options": {"A": "1/9", "B": "1/12", "C": "1/6", "D": "5/36"},
 "answer": "D"},

{"id": 96, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "Set P is {12, 12, 12, 12, 12} and Set Q is {4, 8, 12, 16, 20}. Both sets have a mean of 12. Which set has the larger standard deviation?",
 "options": {"A": "Set P",
             "B": "They are equal",
             "C": "It cannot be determined from the information given",
             "D": "Set Q"},
 "answer": "D"},

{"id": 97, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A square and an equilateral triangle each have a perimeter of 48 cm. By how many centimetres does the triangle's side exceed the square's side?",
 "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
 "answer": "B"},

{"id": 98, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Easy",
 "question": "A right circular cylinder has a radius of 4 cm and a height of 9 cm. What is its volume, in cubic centimetres?",
 "options": {"A": "144pi", "B": "72pi", "C": "108pi", "D": "36pi"},
 "answer": "A"},

{"id": 99, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Medium",
 "question": "Two parallel lines are cut by a transversal. One of the two interior angles on the same side of the transversal measures 70 degrees. What is the measure, in degrees, of the other?",
 "options": {"A": "70", "B": "110", "C": "90", "D": "140"},
 "answer": "B"},

{"id": 100, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Medium",
 "question": "In a 30-60-90 right triangle, the shorter leg measures 9 cm. What is the length of the hypotenuse, in centimetres?",
 "options": {"A": "18", "B": "9*sqrt(3)", "C": "18*sqrt(3)", "D": "13.5"},
 "answer": "A"},

{"id": 101, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Number Properties (odd/even, divisibility)", "difficulty": "Easy",
 "question": "If n is an even integer, which of the following expressions must be an odd integer?",
 "options": {"A": "n^2", "B": "2n", "C": "n + 3", "D": "4n"},
 "answer": "C"},

{"id": 102, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the smallest positive integer that is divisible by 6, 8 and 10?",
 "options": {"A": "120", "B": "80", "C": "60", "D": "240"},
 "answer": "A"},

{"id": 103, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Medium",
 "question": "Which of the following is NOT a prime number?",
 "options": {"A": "67", "B": "69", "C": "73", "D": "79"},
 "answer": "B"},

# ============================================================
# SECTION 7 - VERBAL (17) - q104-120
# ============================================================

{"id": 104, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Easy",
 "question": "The spokesperson's statement was strikingly ____: it committed the ministry to a specific date, a specific budget, and nothing else. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "vague", "B": "lengthy", "C": "evasive", "D": "precise"},
 "answer": "D"},

{"id": 105, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Every account of Pakistani squash lists the champions. The list is accurate. But it hides the more interesting fact, which is that the country produced them from a handful of interconnected families -- and that it was this concentrated coaching lineage, not any single prodigy, that explains the run of titles.\" Which choice best describes the function of the final clause in the text as a whole?",
 "options": {"A": "It withdraws a claim made earlier in the text.",
             "B": "It provides statistical evidence for the first sentence.",
             "C": "It concedes that the conventional list is factually wrong.",
             "D": "It states the specific point the author believes the conventional account obscures."},
 "answer": "D"},

{"id": 106, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: For decades the government has guaranteed a minimum purchase price for sugarcane, above what most other crops can expect. The policy works: farmers keep planting cane. It also works too well: land that would earn more under vegetables or pulses stays under cane, because cane is the one crop whose price a farmer can bank on before the growing season even starts. Which choice best states the main idea of the passage?",
 "options": {"A": "The guaranteed cane price has failed to keep farmers planting sugarcane.",
             "B": "By removing price risk for cane alone, the guarantee succeeds at its aim while locking land into a lower-value crop.",
             "C": "Vegetables and pulses are less profitable than sugarcane in every district.",
             "D": "Market prices for agricultural produce are impossible to forecast."},
 "answer": "B"},

{"id": 107, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A publisher reissued a set of academic textbooks in two versions identical except for cover price: one printed on the cover, and one left for the bookshop to add. Copies with no price printed on the cover sold 15 per cent more in markets where prices are commonly negotiated. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "readers prefer textbooks without any price information at all.",
             "B": "academic textbooks sell better than general non-fiction.",
             "C": "the reissued textbooks were of lower printing quality.",
             "D": "removing a fixed cover price can increase sales where buyers expect to negotiate."},
 "answer": "D"},

{"id": 108, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "A critic argues that Ismat Chughtai's short stories deliberately give her female characters the last word rather than letting a male narrator close the story. Which description of a story's ending, if accurate, would most directly support that argument?",
 "options": {"A": "The male narrator summarises the moral of the story in the closing lines.",
             "B": "The story closes with a description of the weather with no character present.",
             "C": "A male elder is quoted approvingly in the story's final paragraph.",
             "D": "The story ends with the female protagonist's own unanswered question, and no further narration follows."},
 "answer": "D"},

{"id": 109, "section": 7, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "Domestic steel demand fell for four consecutive quarters, and one mill suspended operations altogether. ____ the industry's scrap-recycling exports rose sharply, offsetting some of the decline. Which transition best completes the text?",
 "options": {"A": "Therefore,", "B": "For example,", "C": "In conclusion,", "D": "Meanwhile,"},
 "answer": "D"},

{"id": 110, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The first phase of the survey was completed on schedule ____ the second phase ran nearly a year behind. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; ", "C": " which ", "D": ", also "},
 "answer": "B"},

{"id": 111, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Easy",
 "question": "Because the tunnel had been shut for maintenance ____ traffic was diverted through the old hill road for two months. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; ", "C": ". ", "D": ": "},
 "answer": "A"},

{"id": 112, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which version of the sentence most clearly means that the scholarship pays for housing and for nothing else?",
 "options": {"A": "The scholarship only covers housing.",
             "B": "Only the scholarship covers housing.",
             "C": "The scholarship covers only housing.",
             "D": "The scholarship covers housing only for graduate students."},
 "answer": "C"},

{"id": 113, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: When the city replaced its flat monthly water charge with individual meters in one district, it billed the change as a fairness measure: households would pay for what they used, not an average guess. On paper, consumption in the metered district fell by a third within a year. In practice, the fall was uneven -- large households with several income earners barely changed their usage at all, while single-income households cut back sharply, some skipping laundry loads to stay under budget. The arithmetic that judges the programme's success almost everywhere counts aggregate consumption, because aggregate consumption is easy to measure. Until it counts who is cutting back and why, cities will keep mistaking an average for a fair outcome. Which choice best states the main idea of the passage?",
 "options": {"A": "Individual water metering should be abandoned across the city.",
             "B": "Flat monthly water charges are fairer than metered billing.",
             "C": "Large households consume more water than single-income households in every district.",
             "D": "Metering succeeded in cutting overall consumption but concealed an uneven burden that raw averages don't reveal."},
 "answer": "D"},

{"id": 114, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: When the city replaced its flat monthly water charge with individual meters in one district, it billed the change as a fairness measure: households would pay for what they used, not an average guess. On paper, consumption in the metered district fell by a third within a year. In practice, the fall was uneven -- large households with several income earners barely changed their usage at all, while single-income households cut back sharply, some skipping laundry loads to stay under budget. The arithmetic that judges the programme's success almost everywhere counts aggregate consumption, because aggregate consumption is easy to measure. Until it counts who is cutting back and why, cities will keep mistaking an average for a fair outcome. According to the passage, by how much did consumption in the metered district fall within a year?",
 "options": {"A": "By a third.",
             "B": "By half.",
             "C": "It rose slightly.",
             "D": "The passage does not say."},
 "answer": "A"},

{"id": 115, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: When the city replaced its flat monthly water charge with individual meters in one district, it billed the change as a fairness measure: households would pay for what they used, not an average guess. On paper, consumption in the metered district fell by a third within a year. In practice, the fall was uneven -- large households with several income earners barely changed their usage at all, while single-income households cut back sharply, some skipping laundry loads to stay under budget. The arithmetic that judges the programme's success almost everywhere counts aggregate consumption, because aggregate consumption is easy to measure. Until it counts who is cutting back and why, cities will keep mistaking an average for a fair outcome. The author's attitude toward measuring the programme's success purely by aggregate consumption is best characterised as",
 "options": {"A": "enthusiastic approval.",
             "B": "detached and purely descriptive.",
             "C": "critical of it as a convenient but incomplete measure.",
             "D": "resigned to it as unavoidable."},
 "answer": "C"},

{"id": 116, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: When the city replaced its flat monthly water charge with individual meters in one district, it billed the change as a fairness measure: households would pay for what they used, not an average guess. On paper, consumption in the metered district fell by a third within a year. In practice, the fall was uneven -- large households with several income earners barely changed their usage at all, while single-income households cut back sharply, some skipping laundry loads to stay under budget. The arithmetic that judges the programme's success almost everywhere counts aggregate consumption, because aggregate consumption is easy to measure. Until it counts who is cutting back and why, cities will keep mistaking an average for a fair outcome. It can most reasonably be inferred that the author would support",
 "options": {"A": "returning to a flat monthly charge for all households.",
             "B": "metering water use in every district as quickly as possible regardless of impact.",
             "C": "exempting single-income households from any billing at all.",
             "D": "tracking consumption changes by household type rather than relying on the district-wide average alone."},
 "answer": "D"},

{"id": 117, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The scholarship is open to applicants who have completed an undergraduate degree, who have relevant work experience, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "having a strong academic record.",
             "B": "a strong academic record.",
             "C": "they have a strong academic record.",
             "D": "who have a strong academic record."},
 "answer": "D"},

{"id": 118, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as TACITURN.",
 "options": {"A": "talkative", "B": "reserved", "C": "anxious", "D": "cheerful"},
 "answer": "B"},

{"id": 119, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to DIMINISH.",
 "options": {"A": "augment", "B": "reduce", "C": "conceal", "D": "postpone"},
 "answer": "A"},

{"id": 120, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The new regulation did little to CHECK the rise in informal lending,\" the word \"check\" most nearly means",
 "options": {"A": "verify.", "B": "examine.", "C": "mark.", "D": "restrain."},
 "answer": "D"},

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
#   2. Every (question_text, option_a) pair must be absent from both
#      lums_lcat_sample.py and lums_lcat_mock_01.py. That tuple (with
#      past_paper) is import_mcqs.py's dedupe key -- a collision would make
#      one bank's question silently overwrite another's. Check it before
#      every import, not after.
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
    """(question_text, option_a) must not collide with the sample bank or Mock 1."""
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