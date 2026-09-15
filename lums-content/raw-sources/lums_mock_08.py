"""
LUMS Common Admission Test (LCAT) - Full-Length Mock Test #8
=============================================================
ParhaiKarlo-prepared full-length mock test. NOT an official LUMS past paper.
Answer keys prepared by content team, pending human verification.

Nothing in this file is taken from LUMS' official "Sample Questions for
Verbal & Math Sections" guide (raw-sources/sample_lcat_2025.pdf), nor from
`lums_lcat_mock_01.py`, `lums_lcat_mock_02.py`, `lums_lcat_mock_03.py` or
`lums_lcat_mock_04.py`. Every question below is newly written; the topic and
subtopic assigned to each question slot mirrors the position it occupies in
the earlier mocks (same section, same slot), since those labels were already
verified against the syllabus when Mock 1 was checked in.

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
lums_lcat_mock_01.py, lums_lcat_mock_02.py, lums_lcat_mock_03.py and
lums_lcat_mock_04.py.

Each question is a dict:
    id, section, subject, topic, subtopic, difficulty, question,
    options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.

NOTE: a few of the recurring "quick arithmetic" slots (e.g. Number Properties,
Prime Numbers, Factors and Multiples) have a limited number of natural
phrasings, so the numbers and wording in this bank were deliberately chosen to
differ from the exact strings used in Mocks 2-4 -- run
check_other_bank_collisions() before import to confirm no accidental overlap.
"""

SOURCE = "parhaikarlo_mock_08"

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
 "question": "Archivists cataloguing the Quaid-e-Azam's personal papers at his Karachi residence worked with ____ attention, cross-checking every date against three separate calendars before filing a single letter. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "careless", "B": "hurried", "C": "scrupulous", "D": "casual"},
 "answer": "C"},

{"id": 2, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Medium",
 "question": "Text: \"Mango export growth from Sindh is often credited entirely to new cold-storage facilities built near the port. The credit is only partly deserved. Export volumes rose fastest in the two years before most of the new facilities were even operational, tracking instead with a shift to earlier harvest scheduling that avoided the worst of the pre-monsoon heat.\" Which choice best describes the function of the third sentence in the text as a whole?",
 "options": {"A": "It concedes that the claim is entirely false.",
             "B": "It provides evidence that shifts credit away from cold storage toward an earlier, unrelated cause.",
             "C": "It summarises a consensus the author later accepts.",
             "D": "It offers an anecdote unrelated to the claim."},
 "answer": "B"},

{"id": 3, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: Building a new bypass around Multan's old city is the fastest way to relieve the congestion choking its historic core. Text 2: A bypass would only relieve congestion if through-traffic, not local traffic generated within the old city itself, were the main source of the jam; traffic counts show most vehicles in the core are making short local trips, so a bypass would leave the core just as congested. Based on the texts, how would the author of Text 2 most likely respond to the claim in Text 1?",
 "options": {"A": "By agreeing that the bypass is the fastest solution.",
             "B": "By arguing that the bypass targets the wrong source of congestion, since most trips are local rather than through-traffic.",
             "C": "By denying that Multan's old city is congested.",
             "D": "By conceding that local trips do not contribute to congestion."},
 "answer": "B"},

{"id": 4, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Easy",
 "question": "Passage: For years, no one had a reliable estimate of how many Marco Polo sheep crossed into Pakistan's Pamir borderlands each winter, since the animals cross at scattered, hard-to-reach passes. Rangers began installing motion-triggered cameras at the handful of passes low enough for the sheep to use, then matched horn patterns visible in photos across seasons to avoid counting the same animal twice. The method finally produced a border-crossing estimate that regional wildlife bodies accepted. What is the main idea of the passage?",
 "options": {"A": "The Pamir borderlands are the highest mountains in Pakistan.",
             "B": "Motion-triggered cameras and horn-pattern matching produced the first accepted estimate of Marco Polo sheep crossing into Pakistan.",
             "C": "Marco Polo sheep no longer cross into Pakistan.",
             "D": "Rangers primarily count sheep in summer."},
 "answer": "B"},

{"id": 5, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: Over a decade, the number of small-scale trout farms in upper Swat rose sharply, while imports of frozen fish into the country fell only slightly across the same years. Most of the new trout was sold fresh to hotels and restaurants in the same valley rather than distributed through the national cold-chain that frozen imports rely on. Which choice most logically completes the reasoning in the passage?",
 "options": {"A": "Therefore, frozen fish imports are likely to disappear from the market soon.",
             "B": "Therefore, the growth in local trout farming appears to have created a fresh, local market without significantly displacing the frozen import trade.",
             "C": "Therefore, Swat's trout farmers mostly export their fish abroad.",
             "D": "Therefore, national fish consumption has fallen overall."},
 "answer": "B"},

{"id": 6, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A researcher claims that a district's rise in total maize output was driven more by an increase in cultivated area than by any improvement in yield per acre. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Output rose 38%, while cultivated area rose 34% and yield per acre rose 3%.",
             "B": "Output rose 38%, while cultivated area rose 5% and yield per acre rose 31%.",
             "C": "Output fell 4%, while cultivated area rose 28%.",
             "D": "Output rose 38%, and the market price of maize rose 9%."},
 "answer": "A"},

{"id": 7, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "While researching Nusrat Fateh Ali Khan, a student compiles three notes: he trained for years in the classical qawwali tradition of his family's shrine performances; he later collaborated with Western musicians on film scores and world-music albums; his recordings introduced qawwali to international audiences who had never heard the form before. Which statement best synthesises these notes?",
 "options": {"A": "Trained in his family's classical qawwali tradition, Nusrat Fateh Ali Khan went on to collaborate with Western musicians and introduce qawwali to audiences worldwide.",
             "B": "Nusrat Fateh Ali Khan mainly performed Western classical music.",
             "C": "His international collaborations preceded his training in qawwali.",
             "D": "His recordings had no influence outside Pakistan."},
 "answer": "A"},

{"id": 8, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "Quetta's population grew rapidly as displaced families settled there following unrest in neighbouring regions. ____ the city's limited groundwater supply has come under mounting strain, with several older wells running dry in recent summers. Which transition best completes the text?",
 "options": {"A": "Similarly,", "B": "For instance,", "C": "Consequently,", "D": "In addition,"},
 "answer": "C"},

{"id": 9, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: rilli quilting in Sindh uses small hand-cut fabric patches arranged in geometric patterns; a large rilli can take a group of women several weeks working together to finish; the craft is traditionally passed between mothers and daughters; finished quilts are given as part of a bride's dowry. The student wants to emphasise the communal effort involved and the craft's transmission across generations. Which choice best accomplishes this goal?",
 "options": {"A": "Rilli quilting uses small hand-cut fabric patches arranged in geometric patterns.",
             "B": "A large rilli can take a group of women several weeks to finish together, and the craft passes from mothers to daughters across generations.",
             "C": "Finished rilli quilts are given as part of a bride's dowry.",
             "D": "Rilli quilting is traditionally practised in Sindh."},
 "answer": "B"},

{"id": 10, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "The collection of miniature paintings held at the Lahore Museum ____ works from several Mughal-era schools. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "include", "B": "are including", "C": "includes", "D": "have included"},
 "answer": "C"},

{"id": 11, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "The dockworkers' union rejected the revised shift schedule, and ____ objection was later discussed at a provincial labour hearing. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "its", "B": "their", "C": "it's", "D": "there"},
 "answer": "A"},

{"id": 12, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The geological survey reached one firm conclusion ____ the fault line beneath the valley had shifted more in the past decade than in the previous century. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", that", "B": ", being", "C": "; which", "D": ": "},
 "answer": "D"},

{"id": 13, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Medium",
 "question": "The watchtower had stood abandoned for over sixty years ____ a local council converted it into a small museum last spring. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "; ", "B": ", ", "C": " which ", "D": " and which "},
 "answer": "A"},

{"id": 14, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Having tracked snow-leopard scat samples across three field seasons, ____\"",
 "options": {"A": "the conclusion of the biologists was that the local population had grown.",
             "B": "it was concluded by the biologists that the local population had grown.",
             "C": "the biologists concluded that the local population had grown.",
             "D": "the local population was shown by the biologists to have grown."},
 "answer": "C"},

{"id": 15, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: Bahawalpur's camel-hair shawl trade is usually filed under desert handicraft, something spun for local use between harvests. The workshops tell a different story: weavers now source hair through standing supply contracts with herding cooperatives, dye lots are tested against colour-fastness standards set by export buyers, and production runs are scheduled around specific overseas trade-fair dates months in advance. The trade, in other words, runs less like a seasonal sideline and more like an export-oriented manufacturing operation. Which choice best states the main idea of the passage?",
 "options": {"A": "Bahawalpur's shawl trade caters only to local buyers.",
             "B": "Bahawalpur's shawl trade is better understood as an export-oriented manufacturing operation than as a seasonal sideline craft.",
             "C": "Colour-fastness testing plays no role in the trade.",
             "D": "Herding cooperatives no longer supply camel hair."},
 "answer": "B"},

{"id": 16, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: Bahawalpur's camel-hair shawl trade is usually filed under desert handicraft, something spun for local use between harvests. The workshops tell a different story: weavers now source hair through standing supply contracts with herding cooperatives, dye lots are tested against colour-fastness standards set by export buyers, and production runs are scheduled around specific overseas trade-fair dates months in advance. The trade, in other words, runs less like a seasonal sideline and more like an export-oriented manufacturing operation. The author's attitude toward the conventional description of the trade as a seasonal sideline is best characterised as",
 "options": {"A": "openly contemptuous.", "B": "mildly corrective.", "C": "entirely neutral.", "D": "wistfully nostalgic."},
 "answer": "B"},

{"id": 17, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as AMIABLE.",
 "options": {"A": "hostile", "B": "friendly", "C": "indifferent", "D": "arrogant"},
 "answer": "B"},

{"id": 18, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to the underlined word as it is used here: \"The manager's tone throughout the meeting was notably CONCILIATORY.\"",
 "options": {"A": "hostile", "B": "formal", "C": "brief", "D": "private"},
 "answer": "A"},

# ============================================================
# SECTION 2 - MATH (17) - q19-35
# ============================================================

{"id": 19, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Easy",
 "question": "If 5(x - 2) + 4 = 3x + 12, what is the value of x?",
 "options": {"A": "7", "B": "8", "C": "9", "D": "10"},
 "answer": "C"},

{"id": 20, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 3x + 2y = 21 and x - y = 2, what is the value of x?",
 "options": {"A": "4", "B": "5", "C": "6", "D": "7"},
 "answer": "B"},

{"id": 21, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "Which of the following describes all values of x for which 11 - 3x > 2?",
 "options": {"A": "x > 3", "B": "x < 3", "C": "x > -3", "D": "x < -3"},
 "answer": "B"},

{"id": 22, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Medium",
 "question": "An arithmetic sequence has first term 6 and common difference 7. What is the sum of its first 10 terms?",
 "options": {"A": "375", "B": "360", "C": "390", "D": "350"},
 "answer": "A"},

{"id": 23, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "The equation x^2 + kx + 40 = 0 has roots 4 and 10. What is the value of k?",
 "options": {"A": "-14", "B": "14", "C": "-40", "D": "40"},
 "answer": "A"},

{"id": 24, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is the value of 25^(3/2) * 4^(1/2)?",
 "options": {"A": "200", "B": "225", "C": "250", "D": "275"},
 "answer": "C"},

{"id": 25, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "What is the value of (log_5 125) - (log_2 8)?",
 "options": {"A": "0", "B": "1", "C": "2", "D": "3"},
 "answer": "A"},

{"id": 26, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "If 1/x + 1/(5x) = 6/10, what is the value of x?",
 "options": {"A": "1", "B": "2", "C": "3", "D": "5"},
 "answer": "B"},

{"id": 27, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "A shopkeeper raises the price of an item by 35% and then, in a sale, reduces the new price by 20%. Compared with the original price, the final price is",
 "options": {"A": "8% higher.", "B": "8% lower.", "C": "unchanged.", "D": "15% higher."},
 "answer": "A"},

{"id": 28, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Easy",
 "question": "A sum of Rs. 117,000 is divided between two partners in the ratio 4 : 9. By how much does the larger share exceed the smaller share, in rupees?",
 "options": {"A": "36,000", "B": "40,000", "C": "45,000", "D": "50,000"},
 "answer": "C"},

{"id": 29, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "A class of 18 students has a mean score of 65. Six more students, whose mean score is 85, join the class. What is the mean score of all 24 students?",
 "options": {"A": "68", "B": "70", "C": "72", "D": "74"},
 "answer": "B"},

{"id": 30, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A bag contains 3 red marbles and 9 blue marbles. Two marbles are drawn at random without replacement. What is the probability that both are blue?",
 "options": {"A": "6/11", "B": "3/4", "C": "2/3", "D": "9/22"},
 "answer": "A"},

{"id": 31, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A rectangle has a perimeter of 46 cm, and its length is 3 cm greater than its width. What is its area, in square centimetres?",
 "options": {"A": "120", "B": "126", "C": "130", "D": "140"},
 "answer": "C"},

{"id": 32, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Easy",
 "question": "A right triangle has legs of length 5 cm and 12 cm. What is its perimeter, in centimetres?",
 "options": {"A": "28", "B": "30", "C": "32", "D": "34"},
 "answer": "B"},

{"id": 33, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Easy",
 "question": "A circle has an area of 169pi square centimetres. What is its circumference, in centimetres?",
 "options": {"A": "13pi", "B": "26pi", "C": "52pi", "D": "169pi"},
 "answer": "B"},

{"id": 34, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Ratios", "difficulty": "Medium",
 "question": "In a right triangle, theta is an acute angle and sin(theta) = 15/17. What is the value of cos(theta)?",
 "options": {"A": "8/17", "B": "15/17", "C": "17/8", "D": "17/15"},
 "answer": "A"},

{"id": 35, "section": 2, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the least common multiple of 16 and 24, minus their greatest common divisor?",
 "options": {"A": "32", "B": "36", "C": "40", "D": "44"},
 "answer": "C"},

# ============================================================
# SECTION 3 - VERBAL (17) - q36-52
# ============================================================

{"id": 36, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "Though marketed at launch as a game-changer, the microloan app proved largely ____: a year later, fewer than one in twenty registered users had completed a single transaction. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "transformative", "B": "contentious", "C": "illusory", "D": "premature"},
 "answer": "C"},

{"id": 37, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Economists have long modelled export processing zones as a straightforward engine of local job creation: designate a zone, and factories fill it, hiring from the surrounding district. The model is intuitive, and it predicts steadily falling unemployment near new zones. That is not what employment surveys near several new Sindh zones show: many factories bussed in workers from other provinces because local training programmes hadn't kept pace with the skills the new factories needed.\" Which choice best describes the function of the final sentence in the text as a whole?",
 "options": {"A": "It supplies an example that confirms the model's prediction.",
             "B": "It introduces survey evidence that conflicts with the model's prediction, and explains the gap the model ignores.",
             "C": "It proposes closing the export processing zones.",
             "D": "It restates the model's central claim in more concrete terms."},
 "answer": "B"},

{"id": 38, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: Over two decades, the total area under basmati rice in Punjab grew only modestly, while the fertiliser and pesticide use in basmati districts grew far faster, because basmati is more disease-prone than coarser varieties and export buyers pay a premium for cosmetically flawless grain. Agricultural economists warn against treating the modest growth in area as reassuring: the real story is how much chemical input an expanding basmati sector is drawing away from other crops nearby. Which choice best states the main idea of the passage?",
 "options": {"A": "Basmati cultivation has become dramatically less input-intensive.",
             "B": "Total area under basmati matters more than chemical input use.",
             "C": "Export buyers no longer pay a premium for basmati.",
             "D": "The modest growth in basmati area understates the crop's growing claim on chemical inputs shared with other crops."},
 "answer": "D"},

{"id": 39, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: Pakistan's coastal fisheries are managed province by province, but the migratory tuna stocks that fishing fleets pursue most heavily move through several provinces' waters within a single season, and the same school is often logged by more than one fleet along its route. It follows that separate provincial catch reports ____ Which choice most logically completes the text?",
 "options": {"A": "should be filed more frequently than they currently are.",
             "B": "cannot simply be summed to produce a reliable estimate of the total catch.",
             "C": "will always undercount the fish in each province's waters.",
             "D": "are the only practical way to track migratory tuna."},
 "answer": "B"},

{"id": 40, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "In a study of informal credit among Karachi's fruit vendors, a researcher argues that vendors borrow from wholesale-market commission agents rather than banks because the agent's advance is repaid automatically out of daily sales rather than a fixed monthly instalment. Which quotation from a vendor interview, if authentic, would most directly support that argument?",
 "options": {"A": "\"No bank has ever agreed to open an account for my stall.\"",
             "B": "\"The bank wants a fixed payment every month, but the agent just deducts what I owe from each day's sales as it comes in.\"",
             "C": "\"The agent charges nearly double what a bank would charge in interest.\"",
             "D": "\"I have bought fruit from the same agent for over a decade.\""},
 "answer": "B"},

{"id": 41, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student researching Uch Sharif's shrine complex records three observations: it houses the tombs of several Sufi saints dating from different centuries; its brickwork uses a distinctive blue-glazed tile technique found in few other sites; it draws pilgrims from across South Asia during annual Urs gatherings. Which statement best synthesises these observations?",
 "options": {"A": "Uch Sharif lasts for several days each year.",
             "B": "Housing centuries-old Sufi tombs known for distinctive blue-glazed brickwork, Uch Sharif draws pilgrims from across South Asia during its annual Urs.",
             "C": "Pilgrims at Uch Sharif come mainly from outside South Asia.",
             "D": "Uch Sharif's brickwork technique is common across the region."},
 "answer": "B"},

{"id": 42, "section": 3, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "The 2010 floods destroyed most single-storey mud-brick homes in low-lying Sindh villages. ____ homes raised on stone plinths in the same villages emerged with only minor damage. Which transition best completes the text?",
 "options": {"A": "Consequently,", "B": "In short,", "C": "Similarly,", "D": "By contrast,"},
 "answer": "D"},

{"id": 43, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The programme trains extension officers to test soil samples, to advise farmers on fertiliser dosage, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "referring persistent pest problems to a research station.",
             "B": "they refer persistent pest problems to a research station.",
             "C": "to refer persistent pest problems to a research station.",
             "D": "persistent pest problems are referred to a research station."},
 "answer": "C"},

{"id": 44, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The tour covered three Sufi shrine complexes in southern Punjab ____ Uch Sharif, Multan's Bahauddin Zakariya shrine, and Pakpattan. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ": ", "B": ", ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 45, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "Each of the union councils ____ required to submit an annual development report. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "are", "B": "were", "C": "is", "D": "have been"},
 "answer": "C"},

{"id": 46, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Hard",
 "question": "The embankment was raised in 2015 ____ breaches have still occurred along the same stretch in two subsequent flood seasons. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ", however ", "C": " and which ", "D": "; nevertheless, "},
 "answer": "D"},

{"id": 47, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: The Hingol National Park's habitat for the Sindh ibex has occupied an uncomfortable place in conservation policy for years: officially a protected area, yet crossed by an unregulated network of unpaved tracks used by off-road tourists heading to the park's mud volcanoes. Conservationists argue that visitor caps are set without any reliable estimate of how much disturbance the ibex population can tolerate, so a limit fixed on paper may allow more traffic than the herds can absorb. Tourism authorities point to steadily rising ibex sighting reports from park rangers as evidence the population is thriving under current management. Independent surveys tell a thinner story: sighting reports have risen mainly because ranger patrols now cover a wider area of the park than before, not because more individual ibex are being spotted repeatedly, which suggests the underlying population trend remains unclear. Which choice best states the main idea of the passage?",
 "options": {"A": "Off-road tourism has been banned outright in Hingol National Park.",
             "B": "Rising ibex sighting reports may reflect wider ranger coverage rather than confirm a thriving population.",
             "C": "Visitor caps are set with a precise estimate of ibex tolerance for disturbance.",
             "D": "Ranger patrols no longer operate in the park."},
 "answer": "B"},

{"id": 48, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: The Hingol National Park's habitat for the Sindh ibex has occupied an uncomfortable place in conservation policy for years: officially a protected area, yet crossed by an unregulated network of unpaved tracks used by off-road tourists heading to the park's mud volcanoes. Conservationists argue that visitor caps are set without any reliable estimate of how much disturbance the ibex population can tolerate, so a limit fixed on paper may allow more traffic than the herds can absorb. Tourism authorities point to steadily rising ibex sighting reports from park rangers as evidence the population is thriving under current management. Independent surveys tell a thinner story: sighting reports have risen mainly because ranger patrols now cover a wider area of the park than before, not because more individual ibex are being spotted repeatedly, which suggests the underlying population trend remains unclear. According to the passage, what do conservationists argue about the visitor caps?",
 "options": {"A": "They are generously funded by international donors.",
             "B": "They are set without a reliable estimate of how much disturbance the ibex population can tolerate.",
             "C": "They have eliminated off-road tourism entirely.",
             "D": "They are administered only by tourism authorities."},
 "answer": "B"},

{"id": 49, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: The Hingol National Park's habitat for the Sindh ibex has occupied an uncomfortable place in conservation policy for years: officially a protected area, yet crossed by an unregulated network of unpaved tracks used by off-road tourists heading to the park's mud volcanoes. Conservationists argue that visitor caps are set without any reliable estimate of how much disturbance the ibex population can tolerate, so a limit fixed on paper may allow more traffic than the herds can absorb. Tourism authorities point to steadily rising ibex sighting reports from park rangers as evidence the population is thriving under current management. Independent surveys tell a thinner story: sighting reports have risen mainly because ranger patrols now cover a wider area of the park than before, not because more individual ibex are being spotted repeatedly, which suggests the underlying population trend remains unclear. The author's attitude toward tourism authorities' claim that the population is thriving is best characterised as",
 "options": {"A": "fully persuaded.", "B": "openly mocking.", "C": "skeptical, given the alternate explanation offered.", "D": "indifferent."},
 "answer": "C"},

{"id": 50, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: The Hingol National Park's habitat for the Sindh ibex has occupied an uncomfortable place in conservation policy for years: officially a protected area, yet crossed by an unregulated network of unpaved tracks used by off-road tourists heading to the park's mud volcanoes. Conservationists argue that visitor caps are set without any reliable estimate of how much disturbance the ibex population can tolerate, so a limit fixed on paper may allow more traffic than the herds can absorb. Tourism authorities point to steadily rising ibex sighting reports from park rangers as evidence the population is thriving under current management. Independent surveys tell a thinner story: sighting reports have risen mainly because ranger patrols now cover a wider area of the park than before, not because more individual ibex are being spotted repeatedly, which suggests the underlying population trend remains unclear. It can most reasonably be inferred that the author regards rising sighting reports as",
 "options": {"A": "a reliable substitute for a direct population count.",
             "B": "evidence that risks being misread as proof of a thriving population when it may simply reflect wider patrol coverage.",
             "C": "irrelevant to the debate over visitor caps.",
             "D": "more effective than any current conservation method."},
 "answer": "B"},

{"id": 51, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as PAINSTAKING.",
 "options": {"A": "careless", "B": "careful", "C": "quick", "D": "indifferent"},
 "answer": "B"},

{"id": 52, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The minister's reassurance proved HOLLOW once the budget cuts were announced anyway,\" the word \"hollow\" most nearly means",
 "options": {"A": "empty of real substance.", "B": "physically concave.", "C": "loud.", "D": "temporary."},
 "answer": "A"},

# ============================================================
# SECTION 4 - MATH (17) - q53-69
# ============================================================

{"id": 53, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in Two Variables", "difficulty": "Medium",
 "question": "A line in the xy-plane passes through the points (2, 9) and (5, 21). What is the y-coordinate of its y-intercept?",
 "options": {"A": "1", "B": "2", "C": "3", "D": "-1"},
 "answer": "A"},

{"id": 54, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "The function f is defined by f(x) = 7x - 13. If f(a) = 22, what is the value of a?",
 "options": {"A": "4", "B": "5", "C": "6", "D": "7"},
 "answer": "B"},

{"id": 55, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 3x + 4y = 29 and 3x - 2y = 5, what is the value of y?",
 "options": {"A": "2", "B": "3", "C": "4", "D": "5"},
 "answer": "C"},

{"id": 56, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "A delivery van weighs 700 kg when empty, and the total weight of the loaded van must not exceed 1,600 kg. If each crate weighs 45 kg, what is the greatest number of whole crates the van can carry?",
 "options": {"A": "18", "B": "19", "C": "20", "D": "21"},
 "answer": "C"},

{"id": 57, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Nonlinear Functions", "difficulty": "Medium",
 "question": "What is the minimum value of the function f(x) = x^2 - 12x + 15?",
 "options": {"A": "-18", "B": "-21", "C": "-24", "D": "18"},
 "answer": "B"},

{"id": 58, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Polynomial Expressions", "difficulty": "Easy",
 "question": "Which expression is equivalent to (6x - 5)(x + 4)?",
 "options": {"A": "6x^2 + 19x - 20", "B": "6x^2 - 19x - 20", "C": "6x^2 + 29x - 20", "D": "6x^2 + 19x + 20"},
 "answer": "A"},

{"id": 59, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "How many real solutions does the equation x^2 + 8x + 20 = 0 have?",
 "options": {"A": "Two distinct real solutions", "B": "Exactly one real solution", "C": "Infinitely many real solutions", "D": "No real solutions"},
 "answer": "D"},

{"id": 60, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is sqrt(72) + sqrt(50) in simplest radical form?",
 "options": {"A": "11*sqrt(2)", "B": "13*sqrt(2)", "C": "sqrt(122)", "D": "6*sqrt(2)"},
 "answer": "A"},

{"id": 61, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Unit Conversion", "difficulty": "Easy",
 "question": "A car consumes fuel at a rate of 9 litres per 100 kilometres. How many litres will it consume on a 200-kilometre journey at that rate?",
 "options": {"A": "16", "B": "18", "C": "20", "D": "22"},
 "answer": "B"},

{"id": 62, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Two-Variable Data Interpretation (tables/graphs)", "difficulty": "Medium",
 "question": "A shop records the number of units sold on each of five days: Monday 50, Tuesday 55, Wednesday 40, Thursday 52, Friday 60. By what percentage did the number of units sold increase from Wednesday to Thursday?",
 "options": {"A": "20%", "B": "25%", "C": "30%", "D": "35%"},
 "answer": "C"},

{"id": 63, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "For the data set 5, 8, 8, 10, 14, what is the mean minus the median?",
 "options": {"A": "0", "B": "1", "C": "2", "D": "3"},
 "answer": "B"},

{"id": 64, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "After a 30% discount, an item sells for Rs. 2,800. What was its price before the discount, in rupees?",
 "options": {"A": "3,800", "B": "4,000", "C": "3,640", "D": "4,200"},
 "answer": "B"},

{"id": 65, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Medium",
 "question": "A cube has a volume of 2,744 cubic centimetres. What is its total surface area, in square centimetres?",
 "options": {"A": "1,176", "B": "980", "C": "784", "D": "1,372"},
 "answer": "A"},

{"id": 66, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Easy",
 "question": "The three interior angles of a triangle are in the ratio 4 : 5 : 6. What is the measure of the largest angle, in degrees?",
 "options": {"A": "72", "B": "80", "C": "60", "D": "90"},
 "answer": "A"},

{"id": 67, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Medium",
 "question": "A sector of a circle of radius 20 cm has a central angle of 18 degrees. What is the area of the sector, in square centimetres?",
 "options": {"A": "20pi", "B": "15pi", "C": "25pi", "D": "30pi"},
 "answer": "A"},

{"id": 68, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Identities", "difficulty": "Medium",
 "question": "For any angle theta with sin(theta) not equal to 0, which expression is equivalent to (1 - cos^2(theta)) / sin(theta)?",
 "options": {"A": "sin(theta)", "B": "cos(theta)", "C": "tan(theta)", "D": "1"},
 "answer": "A"},

{"id": 69, "section": 4, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Easy",
 "question": "What is the sum of all prime numbers strictly between 60 and 70?",
 "options": {"A": "122", "B": "124", "C": "128", "D": "130"},
 "answer": "C"},

# ============================================================
# SECTION 5 - VERBAL (17) - q70-86
# ============================================================

{"id": 70, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "The panel's decision was notable for its ____: it addressed each of the twelve appeal grounds separately, citing the relevant precedent for every one. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "brevity", "B": "thoroughness", "C": "leniency", "D": "ambiguity"},
 "answer": "B"},

{"id": 71, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: A single nationwide medical-college admission test is the fairest way to rank applicants because every candidate answers the same set of questions. Text 2: Identical questions do not guarantee a fair ranking when applicants differ enormously in access to well-equipped school laboratories and paid test-prep academies; the test only equalises what's on the page, not what students bring to it. The author of Text 2 would most likely characterise Text 1's claim as",
 "options": {"A": "false, because the questions are not actually identical.",
             "B": "correct, and reason enough to keep the test unchanged.",
             "C": "accurate about the exam itself but incomplete about the unequal preparation surrounding it.",
             "D": "irrelevant, because laboratory access has no effect on scores."},
 "answer": "C"},

{"id": 72, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: Noor Mahal in Bahawalpur is usually valued for its ornate colonial-era facade, often photographed as the city's architectural centrepiece. But the facade alone doesn't explain the building's placement: it sits on one of the few elevated points in the surrounding floodplain, which suggests the site was chosen less for scenic display than for protection from the seasonal flooding that regularly submerged lower ground nearby. Which choice best states the main idea of the passage?",
 "options": {"A": "Noor Mahal's chief significance lies in its flood-safe elevated site rather than in its facade alone.",
             "B": "Noor Mahal is the largest palace built during the colonial era.",
             "C": "The surrounding floodplain has never flooded in recorded history.",
             "D": "Noor Mahal was built purely as a defensive fortress."},
 "answer": "A"},

{"id": 73, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A city introduced a congestion charge for private cars entering its old commercial core during business hours. In the first year, average car travel time within the charged zone fell by 18 per cent. Over the same period, travel times on roads just outside the zone's boundary rose by 14 per cent. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "the congestion charge had no effect on travel behaviour.",
             "B": "total citywide travel time fell by roughly 18 per cent.",
             "C": "at least part of the improvement inside the zone came at the cost of slower traffic just outside it rather than from fewer total trips.",
             "D": "drivers outside the zone were unaware the charge existed."},
 "answer": "C"},

{"id": 74, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A clinic claims a new text-reminder programme reduced missed diabetes-checkup appointments more among patients over 60 than among younger patients. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Missed-appointment rates fell 24 points among patients over 60 and 5 points among younger patients.",
             "B": "The clinic's overall missed-appointment rate fell 11 points.",
             "C": "Younger patients had the lowest missed-appointment rate in the clinic.",
             "D": "Attendance at optional education sessions was highest among patients over 60."},
 "answer": "A"},

{"id": 75, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student compiles three observations about Rohtas Fort near Jhelum: it was built in the 16th century to guard a strategic route into Punjab; its walls stretch for several kilometres and include multiple gates; it is now recognised as a UNESCO World Heritage Site. Which statement best synthesises these observations?",
 "options": {"A": "Built in the 16th century to guard a strategic route into Punjab, Rohtas Fort's multi-gated, kilometres-long walls have since earned it UNESCO World Heritage status.",
             "B": "Rohtas Fort was built primarily as a ceremonial palace.",
             "C": "UNESCO recognition came before the fort's construction.",
             "D": "Rohtas Fort has only a single gate."},
 "answer": "A"},

{"id": 76, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "The archive digitised its entire film-reel collection over a six-year project. ____ a researcher in Hyderabad can now view footage that once existed only as a single deteriorating reel in Lahore. Which transition best completes the text?",
 "options": {"A": "Nevertheless,", "B": "Admittedly,", "C": "By comparison,", "D": "As a result,"},
 "answer": "D"},

{"id": 77, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: the Cholistan Jeep Rally is held annually in the desert near Bahawalpur; it attracts competitors from across Pakistan and abroad; it coincides with the desert's brief post-monsoon bloom of wildflowers; smaller local races are held at other times of year. The student wants to emphasise the rally's annual scale and its connection to the desert's seasonal bloom. Which choice best accomplishes this goal?",
 "options": {"A": "The Cholistan Jeep Rally is held annually near Bahawalpur and draws competitors from across Pakistan and abroad, timed to coincide with the desert's brief wildflower bloom.",
             "B": "Smaller local races are held in Cholistan at other times of year.",
             "C": "The Cholistan desert experiences a wildflower bloom after the monsoon.",
             "D": "The rally is held near Bahawalpur."},
 "answer": "A"},

{"id": 78, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The tribunal's findings ____ released in August, prompted an appeal from both parties. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ": ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 79, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "Every one of the surveyed shopkeepers reported that ____ electricity bill had increased sharply that quarter. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "their", "B": "it's", "C": "its", "D": "whose"},
 "answer": "A"},

{"id": 80, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Built in the 16th century to guard a strategic route and stretching for several kilometres, ____\"",
 "options": {"A": "historians regard Rohtas Fort as a defensive landmark.",
             "B": "the fort's main gate is what most visitors remember.",
             "C": "Rohtas Fort still overlooks the road connecting Jhelum to the Potohar plateau.",
             "D": "it is the Potohar plateau that Rohtas Fort overlooks."},
 "answer": "C"},

{"id": 81, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The report praised the cooperative's low default rate, its trained loan officers, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "it kept detailed repayment records.",
             "B": "that its records were detailed.",
             "C": "keeping detailed repayment records.",
             "D": "the thoroughness of its repayment records."},
 "answer": "D"},

{"id": 82, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Hard",
 "question": "Neither the branch manager nor the loan officers ____ satisfied with the revised lending criteria. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "was", "B": "is", "C": "has been", "D": "were"},
 "answer": "D"},

{"id": 83, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Hard",
 "question": "Passage: For decades Pakistan's textile export slowdown has been blamed on energy shortages and on high labour costs relative to regional competitors, and both complaints are real. Neither explains why so many mills that do have reliable power and competitive wages still struggle to win large repeat orders from international buyers. That gap traces to a compliance-certification backlog: buyers increasingly require independent audits of labour and environmental standards, and Pakistan has too few accredited auditors to clear mills quickly. The fix is not chiefly in cutting energy tariffs further. It is in expanding certification capacity. Which choice best states the main idea of the passage?",
 "options": {"A": "Energy shortages are the sole cause of the textile export slowdown.",
             "B": "The slowdown is better explained by a compliance-certification bottleneck than by energy costs or wages alone.",
             "C": "Pakistan's textile mills no longer export internationally.",
             "D": "Cutting energy tariffs has fully resolved the certification backlog."},
 "answer": "B"},

{"id": 84, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: For decades Pakistan's textile export slowdown has been blamed on energy shortages and on high labour costs relative to regional competitors, and both complaints are real. Neither explains why so many mills that do have reliable power and competitive wages still struggle to win large repeat orders from international buyers. That gap traces to a compliance-certification backlog: buyers increasingly require independent audits of labour and environmental standards, and Pakistan has too few accredited auditors to clear mills quickly. The fix is not chiefly in cutting energy tariffs further. It is in expanding certification capacity. It can most reasonably be inferred that the author would agree with which statement?",
 "options": {"A": "Cutting energy tariffs alone would resolve most of the export slowdown.",
             "B": "High labour costs are a fabricated excuse used by mill owners.",
             "C": "Expanding accredited-auditor capacity would address a cause of the slowdown that tariff cuts cannot.",
             "D": "Pakistan currently has more accredited auditors than it needs."},
 "answer": "C"},

{"id": 85, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as CORDIAL.",
 "options": {"A": "hostile", "B": "friendly", "C": "formal", "D": "indifferent"},
 "answer": "B"},

{"id": 86, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The board's decision to delay the merger was largely a SAFE move,\" the word \"safe\" most nearly means",
 "options": {"A": "protected from theft.", "B": "legally required.", "C": "financially profitable.", "D": "cautious rather than bold."},
 "answer": "D"},

# ============================================================
# SECTION 6 - MATH (17) - q87-103
# ============================================================

{"id": 87, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Medium",
 "question": "If x/3 - 4 = x/9, what is the value of x?",
 "options": {"A": "12", "B": "15", "C": "18", "D": "21"},
 "answer": "C"},

{"id": 88, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Hard",
 "question": "In an arithmetic sequence the 5th term is 17 and the 10th term is 42. What is the first term?",
 "options": {"A": "-3", "B": "3", "C": "-7", "D": "7"},
 "answer": "A"},

{"id": 89, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "A taxi charges a fixed Rs. 80 plus Rs. 25 for every kilometre travelled. A journey costs Rs. 330. How many kilometres was the journey?",
 "options": {"A": "8", "B": "9", "C": "10", "D": "11"},
 "answer": "C"},

{"id": 90, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Easy",
 "question": "What is the sum of the solutions of x^2 - 14x + 24 = 0?",
 "options": {"A": "12", "B": "-14", "C": "24", "D": "14"},
 "answer": "D"},

{"id": 91, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "If log(x) = 5, where log denotes the base-10 logarithm, what is the value of log(10x)?",
 "options": {"A": "5", "B": "6", "C": "50", "D": "500"},
 "answer": "B"},

{"id": 92, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "For all x other than 7 and -5, which expression is equivalent to (x^2 - 49) / (x^2 - 2x - 35)?",
 "options": {"A": "(x - 7)/(x + 5)", "B": "(x + 7)/(x - 5)", "C": "2", "D": "(x + 7)/(x + 5)"},
 "answer": "D"},

{"id": 93, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Medium",
 "question": "Five identical machines together produce 450 units in 3 hours. Working at the same rate, how many units would 8 such machines produce in 6 hours?",
 "options": {"A": "1,200", "B": "1,350", "C": "1,440", "D": "1,500"},
 "answer": "C"},

{"id": 94, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "The mean of ten numbers is 30. When one of the numbers is removed, the mean of the remaining nine is 33. What was the number that was removed?",
 "options": {"A": "1", "B": "3", "C": "5", "D": "7"},
 "answer": "B"},

{"id": 95, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A fair six-sided die is rolled twice. What is the probability that the two results add up to 7?",
 "options": {"A": "1/6", "B": "1/9", "C": "5/36", "D": "1/12"},
 "answer": "A"},

{"id": 96, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "Set A is {18, 18, 18, 18, 18} and Set B is {8, 13, 18, 23, 28}. Both sets have a mean of 18. Which set has the larger standard deviation?",
 "options": {"A": "Set A", "B": "They are equal", "C": "It cannot be determined from the information given", "D": "Set B"},
 "answer": "D"},

{"id": 97, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A square and an equilateral triangle each have a perimeter of 108 cm. By how many centimetres does the triangle's side exceed the square's side?",
 "options": {"A": "7", "B": "8", "C": "9", "D": "10"},
 "answer": "C"},

{"id": 98, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Easy",
 "question": "A right circular cylinder has a radius of 6 cm and a height of 7 cm. What is its volume, in cubic centimetres?",
 "options": {"A": "210pi", "B": "252pi", "C": "294pi", "D": "168pi"},
 "answer": "B"},

{"id": 99, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Medium",
 "question": "Two parallel lines are cut by a transversal. One of the two interior angles on the same side of the transversal measures 62 degrees. What is the measure, in degrees, of the other?",
 "options": {"A": "62", "B": "118", "C": "90", "D": "152"},
 "answer": "B"},

{"id": 100, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Medium",
 "question": "In a 30-60-90 right triangle, the shorter leg measures 17 cm. What is the length of the hypotenuse, in centimetres?",
 "options": {"A": "34", "B": "17*sqrt(3)", "C": "34*sqrt(3)", "D": "25.5"},
 "answer": "A"},

{"id": 101, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Number Properties (odd/even, divisibility)", "difficulty": "Easy",
 "question": "If p is an even integer, which of the following expressions must be an odd integer?",
 "options": {"A": "p^2", "B": "p + 9", "C": "6p", "D": "p/2"},
 "answer": "B"},

{"id": 102, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the smallest positive integer that is divisible by 8, 10 and 12?",
 "options": {"A": "120", "B": "60", "C": "90", "D": "240"},
 "answer": "A"},

{"id": 103, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Medium",
 "question": "Which of the following is NOT a prime number?",
 "options": {"A": "109", "B": "111", "C": "113", "D": "127"},
 "answer": "B"},

# ============================================================
# SECTION 7 - VERBAL (17) - q104-120
# ============================================================

{"id": 104, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Easy",
 "question": "The coach's post-match comments were strikingly ____: they named the exact tactical error and nothing more. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "vague", "B": "lengthy", "C": "evasive", "D": "precise"},
 "answer": "D"},

{"id": 105, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Every account of Pakistan's rise in international snooker lists the individual champions. The list is accurate. But it hides the more interesting fact, which is that most of those champions trained at the same handful of clubs in Karachi under a small circle of coaches -- and it was this concentrated coaching network, not any single player's natural talent, that explains the sustained run of titles.\" Which choice best describes the function of the final clause in the text as a whole?",
 "options": {"A": "It withdraws a claim made earlier in the text.",
             "B": "It provides statistical evidence for the first sentence.",
             "C": "It concedes that the conventional list is factually wrong.",
             "D": "It states the specific point the author believes the conventional account obscures."},
 "answer": "D"},

{"id": 106, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: For decades the government has guaranteed a minimum purchase price for tobacco in parts of Khyber Pakhtunkhwa, above what most competing crops there can expect. The policy works: farmers keep planting tobacco. It also works too well: land that would earn more under maize or vegetables stays under tobacco, because tobacco is the one crop whose price a farmer can bank on before sowing even begins. Which choice best states the main idea of the passage?",
 "options": {"A": "The guaranteed tobacco price has failed to keep farmers planting tobacco.",
             "B": "By removing price risk for tobacco alone, the guarantee succeeds at its aim while locking land into a lower-value crop.",
             "C": "Maize and vegetables are less profitable than tobacco in every district.",
             "D": "Market prices for agricultural produce are impossible to forecast."},
 "answer": "B"},

{"id": 107, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A publisher reissued a set of civil-service exam guides in two versions identical except for cover price: one printed on the cover, one left for the bookshop to add. Copies with no printed price sold 16 per cent more in markets where haggling is common. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "readers prefer guides without any price information at all.",
             "B": "removing a fixed cover price can increase sales where buyers expect to negotiate.",
             "C": "the reissued guides were printed on cheaper paper.",
             "D": "civil-service guides sell better than general non-fiction."},
 "answer": "B"},

{"id": 108, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "A critic argues that Ashfaq Ahmed's radio dramas deliberately end on an unresolved moral dilemma rather than a tidy conclusion, to prompt listener reflection. Which description of an episode's ending, if accurate, would most directly support that argument?",
 "options": {"A": "The narrator explicitly states which character was right in the closing lines.",
             "B": "The episode ends with a summary of the moral for listeners.",
             "C": "The episode closes mid-conversation, with the central dilemma still unresolved and no narratorial comment.",
             "D": "The episode ends with statistics about the era it depicts."},
 "answer": "C"},

{"id": 109, "section": 7, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "Domestic cement demand fell for two consecutive quarters, and one plant reduced its workforce. ____ the industry's exports to Afghanistan rose sharply, offsetting some of the decline. Which transition best completes the text?",
 "options": {"A": "Therefore,", "B": "For example,", "C": "In conclusion,", "D": "Meanwhile,"},
 "answer": "D"},

{"id": 110, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The first phase of the vaccination drive met its target ____ the second phase fell well short in remote districts. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; ", "C": " which ", "D": ", also "},
 "answer": "B"},

{"id": 111, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Easy",
 "question": "Because the ferry service had been suspended for repairs ____ commuters relied on a longer road route for several weeks. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; ", "C": ". ", "D": ": "},
 "answer": "A"},

{"id": 112, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which version of the sentence most clearly means that the stipend covers meals and for nothing else?",
 "options": {"A": "The stipend only covers meals.",
             "B": "Only the stipend covers meals.",
             "C": "The stipend covers only meals.",
             "D": "The stipend covers meals only for first-year students."},
 "answer": "C"},

{"id": 113, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: When a utility switched from estimated monthly electricity bills to readings from smart meters in one district, it billed the change as a fairness measure: households would pay for exactly what they used, not an estimate. On paper, disputed billing complaints in the district fell by nearly half within a year. In practice, the drop was uneven -- households with steady, predictable usage barely filed complaints either way, while households with highly variable usage, often those running small home businesses, saw sharp month-to-month swings in their bills that generated a new wave of complaints of a different kind. The arithmetic that judges the rollout's success almost everywhere counts total complaint volume, because that figure is easy to measure. Until it counts what kind of household is complaining and why, utilities will keep mistaking a lower total for a fully resolved problem. Which choice best states the main idea of the passage?",
 "options": {"A": "Smart metering should be abandoned across the district.",
             "B": "The rollout cut overall complaints but concealed a shift toward a different kind of complaint among variable-usage households that raw totals don't reveal.",
             "C": "Households with steady usage generate more complaints than those with variable usage.",
             "D": "Estimated billing is fairer than smart-meter billing."},
 "answer": "B"},

{"id": 114, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: When a utility switched from estimated monthly electricity bills to readings from smart meters in one district, it billed the change as a fairness measure: households would pay for exactly what they used, not an estimate. On paper, disputed billing complaints in the district fell by nearly half within a year. In practice, the drop was uneven -- households with steady, predictable usage barely filed complaints either way, while households with highly variable usage, often those running small home businesses, saw sharp month-to-month swings in their bills that generated a new wave of complaints of a different kind. The arithmetic that judges the rollout's success almost everywhere counts total complaint volume, because that figure is easy to measure. Until it counts what kind of household is complaining and why, utilities will keep mistaking a lower total for a fully resolved problem. According to the passage, by how much did disputed billing complaints fall within a year?",
 "options": {"A": "By nearly half.", "B": "By a quarter.", "C": "They rose slightly.", "D": "The passage does not say."},
 "answer": "A"},

{"id": 115, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: When a utility switched from estimated monthly electricity bills to readings from smart meters in one district, it billed the change as a fairness measure: households would pay for exactly what they used, not an estimate. On paper, disputed billing complaints in the district fell by nearly half within a year. In practice, the drop was uneven -- households with steady, predictable usage barely filed complaints either way, while households with highly variable usage, often those running small home businesses, saw sharp month-to-month swings in their bills that generated a new wave of complaints of a different kind. The arithmetic that judges the rollout's success almost everywhere counts total complaint volume, because that figure is easy to measure. Until it counts what kind of household is complaining and why, utilities will keep mistaking a lower total for a fully resolved problem. The author's attitude toward measuring the rollout's success purely by total complaint volume is best characterised as",
 "options": {"A": "enthusiastic approval.", "B": "detached and purely descriptive.", "C": "critical of it as a convenient but incomplete measure.", "D": "resigned to it as unavoidable."},
 "answer": "C"},

{"id": 116, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: When a utility switched from estimated monthly electricity bills to readings from smart meters in one district, it billed the change as a fairness measure: households would pay for exactly what they used, not an estimate. On paper, disputed billing complaints in the district fell by nearly half within a year. In practice, the drop was uneven -- households with steady, predictable usage barely filed complaints either way, while households with highly variable usage, often those running small home businesses, saw sharp month-to-month swings in their bills that generated a new wave of complaints of a different kind. The arithmetic that judges the rollout's success almost everywhere counts total complaint volume, because that figure is easy to measure. Until it counts what kind of household is complaining and why, utilities will keep mistaking a lower total for a fully resolved problem. It can most reasonably be inferred that the author would support",
 "options": {"A": "returning to estimated billing for all households.",
             "B": "rolling out smart meters everywhere regardless of usage patterns.",
             "C": "exempting variable-usage households from billing entirely.",
             "D": "tracking complaint types by household usage pattern rather than relying on total complaint volume alone."},
 "answer": "D"},

{"id": 117, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The grant is open to applicants who have completed a relevant certification, who have two years of field experience, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "having a letter of recommendation.",
             "B": "a letter of recommendation.",
             "C": "they have a letter of recommendation.",
             "D": "who have a letter of recommendation."},
 "answer": "D"},

{"id": 118, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as LACONIC.",
 "options": {"A": "talkative", "B": "terse", "C": "anxious", "D": "cheerful"},
 "answer": "B"},

{"id": 119, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to EXPAND.",
 "options": {"A": "grow", "B": "contract", "C": "conceal", "D": "postpone"},
 "answer": "B"},

{"id": 120, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The new ordinance did little to CURTAIL informal street vending,\" the word \"curtail\" most nearly means",
 "options": {"A": "verify.", "B": "mark.", "C": "restrict.", "D": "examine."},
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
#      lums_lcat_sample.py and lums_mock_01.py through lums_mock_07.py. That
#      tuple (with past_paper) is import_mcqs.py's dedupe key -- a collision
#      would make one bank's question silently overwrite another's. Check it
#      before every import, not after.
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
    """(question_text, option_a) must not collide with the sample bank or Mocks 1-7."""
    keys = set()
    sources_checked = []
    try:
        from lums_lcat_sample import QUESTIONS as SAMPLE
        keys |= {(q["question"], q["options"]["A"]) for q in SAMPLE}
        sources_checked.append("lums_lcat_sample")
    except ImportError:
        print("\nCould not import lums_lcat_sample -- that collision check SKIPPED.")
    for modname in (
        "lums_mock_01",
        "lums_mock_02",
        "lums_mock_03",
        "lums_mock_04",
        "lums_mock_05",
        "lums_mock_06",
        "lums_mock_07",
    ):
        try:
            mod = __import__(modname)
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