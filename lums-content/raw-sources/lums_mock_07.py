"""
LUMS Common Admission Test (LCAT) - Full-Length Mock Test #7
=============================================================
ParhaiKarlo-prepared full-length mock test. NOT an official LUMS past paper.
Answer keys prepared by content team, pending human verification.

Nothing in this file is taken from LUMS' official "Sample Questions for
Verbal & Math Sections" guide (raw-sources/sample_lcat_2025.pdf), nor from
`lums_mock_01.py` through `lums_mock_06.py`.
Every question below is newly written; the topic and subtopic assigned to
each question slot mirrors the position it occupies in the earlier mocks
(same section, same slot), since those labels were already verified against
the syllabus when those mocks were checked in.

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
and the other mocks.

Each question is a dict:
    id, section, subject, topic, subtopic, difficulty, question,
    options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.
"""

SOURCE = "parhaikarlo_mock_07"

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
 "question": "The restorers working on Lahore's Wazir Khan Mosque mixed their plaster to a centuries-old recipe, a ____ choice that modern cement could have replaced far more cheaply but far less faithfully. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "careless", "B": "deliberate", "C": "accidental", "D": "temporary"},
 "answer": "B"},

{"id": 2, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Medium",
 "question": "Text: \"Empress Market in Karachi is usually described simply as a colonial-era food market. The description undersells what the building has also been: constructed partly using stone salvaged from a demolished garden where 1857 mutineers were executed, the market's foundations carry a political history that its stalls of spices and fruit rarely hint at.\" Which choice best describes the function of the second sentence in the text as a whole?",
 "options": {"A": "It fully confirms the first description.",
             "B": "It adds a layer of history the simple description leaves out.",
             "C": "It denies that Empress Market sells food.",
             "D": "It restates the first sentence in different words."},
 "answer": "B"},

{"id": 3, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: Hingol National Park's mud volcanoes should be read primarily as a geological curiosity, since their eruptions are driven by underground gas rather than volcanic magma and pose no real hazard to nearby communities. Text 2: Communities living near Hingol's mud volcanoes report livestock and grazing land lost to sudden mud flows more than once in living memory; whether or not the mechanism is magma, the outcome for a herder whose field is buried is not merely curious. Based on the texts, how would the author of Text 2 most likely respond to Text 1's claim?",
 "options": {"A": "By agreeing that the volcanoes pose no hazard at all.",
             "B": "By pointing out that regardless of the geological mechanism, the practical consequences for nearby communities are real, not merely curious.",
             "C": "By denying that the volcanoes are driven by gas.",
             "D": "By conceding that the volcanoes are entirely harmless to livestock."},
 "answer": "B"},

{"id": 4, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Easy",
 "question": "Passage: Skardu's apricot orchards are often introduced to visitors as simply scenic, a description that skips the economics. Most orchard income now comes not from fresh fruit, which spoils quickly on the long road to lowland markets, but from sun-dried apricots and apricot-kernel oil, both of which keep for months and travel far better. What is the main idea of the passage?",
 "options": {"A": "Skardu's apricot orchards earn most of their income from fresh fruit sales.",
             "B": "Orchard income now depends mainly on dried apricots and kernel oil because they withstand the long journey to market better than fresh fruit.",
             "C": "Apricot orchards in Skardu have stopped producing fresh fruit.",
             "D": "The road to lowland markets has recently been shortened."},
 "answer": "B"},

{"id": 5, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A survey of date growers in Khairpur found that the number of registered processing units fell by roughly a quarter over eight years, even as the district's total packaged-date output, measured by weight, rose slightly. Which inference most logically follows?",
 "options": {"A": "The remaining processing units are, on average, handling more dates each than before.",
             "B": "Khairpur has stopped producing packaged dates entirely.",
             "C": "Output fell in proportion to the number of units.",
             "D": "Registered units process less efficiently than unregistered ones."},
 "answer": "A"},

{"id": 6, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A researcher claims that a citrus district's rising export revenue was driven more by a larger harvest than by higher prices per crate. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Revenue rose 32%, while crates exported rose 30% and average price per crate rose 2%.",
             "B": "Revenue rose 32%, while crates exported rose 4% and average price per crate rose 27%.",
             "C": "Revenue fell 6%, while crates exported rose 30%.",
             "D": "Revenue rose 32%, and international citrus demand fell 8%."},
 "answer": "A"},

{"id": 7, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student researching Wazir Khan Mosque compiles three notes: it was built in the 17th century under Emperor Shah Jahan; its interior is covered in elaborate fresco and tile work; and it remains an active place of worship as well as a heritage site. Which statement best synthesises these observations?",
 "options": {"A": "Built in the 17th century under Shah Jahan and covered in elaborate fresco and tile work, Wazir Khan Mosque functions today as both an active place of worship and a heritage site.",
             "B": "Wazir Khan Mosque was built without any decorative tile work.",
             "C": "The mosque has been closed to worshippers since its construction.",
             "D": "Wazir Khan Mosque predates the Mughal era."},
 "answer": "A"},

{"id": 8, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "Tarbela Dam's reservoir has lost a measurable share of its storage capacity to accumulated silt since it was built. ____ engineers now study dredging and sediment-flushing techniques that were barely considered when the dam was first designed. Which transition best completes the text?",
 "options": {"A": "Similarly,", "B": "For example,", "C": "As a result,", "D": "In spite of this,"},
 "answer": "C"},

{"id": 9, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: Nankana Sahib is the birthplace of Guru Nanak; it draws Sikh pilgrims from around the world each year; the nearby Kartarpur corridor now lets pilgrims from India cross without a visa; the town's local economy has grown around pilgrim visits. The student wants to emphasise the corridor's role in expanding pilgrim access. Which choice best accomplishes this goal?",
 "options": {"A": "Nankana Sahib is the birthplace of Guru Nanak.",
             "B": "The nearby Kartarpur corridor, opened to let pilgrims from India cross without a visa, has widened access to Nankana Sahib for Sikh pilgrims from around the world.",
             "C": "The town's local economy has grown around pilgrim visits.",
             "D": "Nankana Sahib draws Sikh pilgrims from around the world each year."},
 "answer": "B"},

{"id": 10, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "The set of hand-painted tile panels recovered from the old haveli ____ currently under conservation at the provincial workshop. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "are", "B": "is", "C": "have been", "D": "were"},
 "answer": "B"},

{"id": 11, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "The date growers disputed the new export tariff, and ____ objections were later raised with the commerce ministry. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "its", "B": "their", "C": "it's", "D": "there"},
 "answer": "B"},

{"id": 12, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The survey team reached one firm conclusion ____ the mud volcano's last major eruption predated any nearby settlement. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", that", "B": ", being", "C": "; which", "D": ": "},
 "answer": "D"},

{"id": 13, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Medium",
 "question": "The ferry had crossed to Astola Island twice weekly for years ____ operators suspended the route after a storm damaged the jetty last season. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "; ", "B": ", ", "C": " which ", "D": " and which "},
 "answer": "A"},

{"id": 14, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Having surveyed Hingol National Park's mud volcanoes for two field seasons, ____\"",
 "options": {"A": "the conclusion of the geologists was that gas, not magma, drove the eruptions.",
             "B": "it was concluded by the geologists that gas, not magma, drove the eruptions.",
             "C": "the geologists concluded that gas, not magma, drove the eruptions.",
             "D": "gas-driven eruptions were shown by the geologists to occur."},
 "answer": "C"},

{"id": 15, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: Sargodha's citrus belt is usually promoted for its kinnow harvest volume, marketed each winter as the region's defining crop. The volume figure hides a quieter shift: a growing share of orchard land is being converted to guava and pomegranate, crops that fetch better prices in local markets and require less water than kinnow during the increasingly dry pre-harvest months. Which choice best states the main idea of the passage?",
 "options": {"A": "Sargodha's citrus belt has abandoned kinnow production entirely.",
             "B": "Behind the headline kinnow volume, orchard land is quietly shifting toward guava and pomegranate for better prices and lower water needs.",
             "C": "Guava requires more water than kinnow in Sargodha.",
             "D": "Kinnow harvest volume has fallen sharply in recent years."},
 "answer": "B"},

{"id": 16, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: Sargodha's citrus belt is usually promoted for its kinnow harvest volume, marketed each winter as the region's defining crop. The volume figure hides a quieter shift: a growing share of orchard land is being converted to guava and pomegranate, crops that fetch better prices in local markets and require less water than kinnow during the increasingly dry pre-harvest months. The author's attitude toward the promotional emphasis on kinnow harvest volume is best characterised as",
 "options": {"A": "fully approving.", "B": "mildly corrective.", "C": "openly hostile.", "D": "entirely indifferent."},
 "answer": "B"},

{"id": 17, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as AMICABLE.",
 "options": {"A": "hostile", "B": "friendly", "C": "distant", "D": "secretive"},
 "answer": "B"},

{"id": 18, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to the underlined word as it is used here: \"The negotiator's tone throughout the dispute remained notably PLACID.\"",
 "options": {"A": "turbulent", "B": "careful", "C": "private", "D": "gradual"},
 "answer": "A"},

# ============================================================
# SECTION 2 - MATH (17) - q19-35
# ============================================================

{"id": 19, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Easy",
 "question": "If 3(x - 4) + 7 = 2x + 5, what is the value of x?",
 "options": {"A": "8", "B": "9", "C": "10", "D": "11"},
 "answer": "C"},

{"id": 20, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 3x + 4y = 34 and x - y = 2, what is the value of x?",
 "options": {"A": "5", "B": "6", "C": "7", "D": "8"},
 "answer": "B"},

{"id": 21, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "Which of the following describes all values of x for which 12 - 4x < 4?",
 "options": {"A": "x > 2", "B": "x < 2", "C": "x > -2", "D": "x < -2"},
 "answer": "A"},

{"id": 22, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Medium",
 "question": "An arithmetic sequence has first term 5 and common difference 6. What is the sum of its first 12 terms?",
 "options": {"A": "456", "B": "432", "C": "480", "D": "408"},
 "answer": "A"},

{"id": 23, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "The equation x^2 + kx + 18 = 0 has roots 3 and 6. What is the value of k?",
 "options": {"A": "-9", "B": "9", "C": "-18", "D": "18"},
 "answer": "A"},

{"id": 24, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is the value of 16^(3/4) * 27^(1/3)?",
 "options": {"A": "24", "B": "36", "C": "48", "D": "64"},
 "answer": "A"},

{"id": 25, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "What is the value of (log_3 81) - (log_4 16)?",
 "options": {"A": "2", "B": "-2", "C": "6", "D": "-6"},
 "answer": "A"},

{"id": 26, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "If 3/x + 1/(2x) = 7/10, what is the value of x?",
 "options": {"A": "2", "B": "4", "C": "5", "D": "7"},
 "answer": "C"},

{"id": 27, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "A trader raises the price of an item by 30% and then, in a sale, reduces the new price by 10%. Compared with the original price, the final price is",
 "options": {"A": "17% higher.", "B": "17% lower.", "C": "unchanged.", "D": "20% higher."},
 "answer": "A"},

{"id": 28, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Easy",
 "question": "A sum of Rs. 72,000 is divided between two partners in the ratio 5 : 4. By how much does the larger share exceed the smaller share, in rupees?",
 "options": {"A": "6,000", "B": "8,000", "C": "9,000", "D": "12,000"},
 "answer": "B"},

{"id": 29, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "A class of 18 students has a mean score of 60. Six more students, whose mean score is 88, join the class. What is the mean score of all 24 students?",
 "options": {"A": "65", "B": "67", "C": "69", "D": "71"},
 "answer": "B"},

{"id": 30, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A bag contains 6 red marbles and 8 blue marbles. Two marbles are drawn at random without replacement. What is the probability that both are blue?",
 "options": {"A": "4/13", "B": "8/21", "C": "3/7", "D": "2/7"},
 "answer": "A"},

{"id": 31, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A rectangle has a perimeter of 46 cm, and its length is 5 cm greater than its width. What is its area, in square centimetres?",
 "options": {"A": "126", "B": "110", "C": "140", "D": "117"},
 "answer": "A"},

{"id": 32, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Easy",
 "question": "A right triangle has legs of length 9 cm and 12 cm. What is its perimeter, in centimetres?",
 "options": {"A": "32", "B": "34", "C": "36", "D": "38"},
 "answer": "C"},

{"id": 33, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Easy",
 "question": "A circle has an area of 144pi square centimetres. What is its circumference, in centimetres?",
 "options": {"A": "12pi", "B": "24pi", "C": "48pi", "D": "144pi"},
 "answer": "B"},

{"id": 34, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Ratios", "difficulty": "Medium",
 "question": "In a right triangle, theta is an acute angle and sin(theta) = 20/29. What is the value of cos(theta)?",
 "options": {"A": "21/29", "B": "20/21", "C": "29/21", "D": "20/29"},
 "answer": "A"},

{"id": 35, "section": 2, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the least common multiple of 15 and 20, minus their greatest common divisor?",
 "options": {"A": "50", "B": "55", "C": "60", "D": "65"},
 "answer": "B"},

# ============================================================
# SECTION 3 - VERBAL (17) - q36-52
# ============================================================

{"id": 36, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "Marketed as an affordable rural water-testing kit, the device proved largely ____ where the promised results table required a literacy level and a reference chart few village users had access to. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "indispensable", "B": "affordable", "C": "useless", "D": "durable"},
 "answer": "C"},

{"id": 37, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Agricultural economists have long modelled contract farming as a straightforward substitute for spot-market sales: a farmer simply switches to the buyer offering a fixed pre-season price. The model predicts steadier farmer incomes. That is not what repeated surveys of contract sugarcane growers in southern Punjab show: many growers quietly sell part of their harvest on the spot market anyway, because contract prices, unlike spot prices, don't adjust upward when a poor regional harvest pushes market prices higher.\" Which choice best describes the function of the final sentence in the text as a whole?",
 "options": {"A": "It supplies an example confirming the model's prediction.",
             "B": "It introduces survey evidence that conflicts with the model's prediction and explains why.",
             "C": "It proposes discarding the survey evidence in favour of the model.",
             "D": "It restates the model's claim in more concrete terms."},
 "answer": "B"},

{"id": 38, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: Over a decade, the number of registered cold-storage units near Sargodha grew only modestly, while the total tonnage of citrus they could hold each season grew far faster, because newer facilities use stacked pallet-racking that stores far more fruit per square metre than the older bulk-bin units they gradually replaced. Industry auditors caution against reading the modest growth in unit numbers as reassuring: the real story is how much more fruit a similar number of facilities can now hold. Which choice best states the main idea of the passage?",
 "options": {"A": "The number of cold-storage units near Sargodha has grown dramatically.",
             "B": "Unit count is a more meaningful statistic than storage capacity.",
             "C": "Older cold-storage units hold more fruit than newer ones.",
             "D": "The modest growth in unit numbers conceals a much sharper rise in storage capacity per facility."},
 "answer": "D"},

{"id": 39, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: Pakistan's coastal fisheries are managed province by province, but the tuna stocks that draw the most commercial attention migrate through waters that straddle several provincial boundaries within a single season, and the same shoal is often reported by boats registered to more than one province. It follows that separate provincial tuna-catch counts ____ Which choice most logically completes the text?",
 "options": {"A": "should be conducted more often than they currently are.",
             "B": "cannot simply be summed to produce a reliable national total.",
             "C": "will always overstate the true number in each province.",
             "D": "are the only practical way to track the species."},
 "answer": "B"},

{"id": 40, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "In a study of Nankana Sahib's pilgrimage season, a researcher argues that visitors value the shared communal langar meal less as ritual obligation than as a rare experience of eating alongside strangers as equals. Which quotation from a visitor interview, if authentic, would most directly support that argument?",
 "options": {"A": "\"The langar follows a fixed serving order that volunteers control from start to finish.\"",
             "B": "\"Sitting on that floor, sharing a plate with someone I'd never met, nobody asked who either of us was outside that hall.\"",
             "C": "\"The pilgrimage draws visitors from several countries each year.\"",
             "D": "\"Donations collected during the festival fund the langar kitchen.\""},
 "answer": "B"},

{"id": 41, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student researching Tarbela Dam records three observations: it was completed in the 1970s on the Indus River; it is among the largest earth-filled dams in the world by volume; and it has lost a measurable share of its original storage capacity to silt accumulation since completion. Which statement best synthesises these observations?",
 "options": {"A": "Completed in the 1970s on the Indus and among the largest earth-filled dams in the world by volume, Tarbela has since lost a measurable share of its original storage capacity to silt.",
             "B": "Tarbela Dam was built entirely of concrete.",
             "C": "Tarbela Dam's storage capacity has increased since completion.",
             "D": "Tarbela Dam predates the 20th century."},
 "answer": "A"},

{"id": 42, "section": 3, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "Karachi's old tramline once carried most short-distance passenger traffic along the harbour front. ____ motor buses, cheaper to run and faster through traffic, replaced the entire tram network by the late 1970s. Which transition best completes the text?",
 "options": {"A": "Consequently,", "B": "In short,", "C": "Similarly,", "D": "By contrast,"},
 "answer": "A"},

{"id": 43, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The apprenticeship trains carvers to select the seasoned wood, to rough out the basic form, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "finishing the fine detail by hand.",
             "B": "they finish the fine detail by hand.",
             "C": "to finish the fine detail by hand.",
             "D": "the fine detail is finished by them."},
 "answer": "C"},

{"id": 44, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The itinerary covered three stops along the coast ____ Manora Island, Hingol National Park and Astola Island. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ": ", "B": ", ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 45, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "Each of the seven restored gates of the Walled City ____ lit for evening visitors. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "are", "B": "were", "C": "is", "D": "have been"},
 "answer": "C"},

{"id": 46, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Hard",
 "question": "The jetty at Astola Island was rebuilt in 2018 ____ storm damage to coastal infrastructure has grown more frequent every monsoon since. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ", however ", "C": " and which ", "D": "; nevertheless, "},
 "answer": "D"},

{"id": 47, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: Baluchistan's community-managed date orchards were set up on a simple bargain: households that once sold dates to a single local middleman at a fixed low rate would instead pool their harvest and sell directly to processors through a farmer cooperative. On paper the arrangement has worked -- cooperative membership has grown steadily since the programme began. Agricultural economists caution that the growth rests on a narrower base than the membership figures suggest: nearly all of the cooperative's bargaining power comes from a handful of large member orchards whose harvest volume lets it negotiate at all, and if those few large growers left, the cooperative would lose most of the leverage that benefits its smaller members. Which choice best states the main idea of the passage?",
 "options": {"A": "Baluchistan's date cooperatives have failed to grow membership.",
             "B": "Rising membership conceals how dependent the cooperative's bargaining power is on a small number of large growers.",
             "C": "The local middleman system has been fully restored.",
             "D": "Processors no longer buy dates from Baluchistan."},
 "answer": "B"},

{"id": 48, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: Baluchistan's community-managed date orchards were set up on a simple bargain: households that once sold dates to a single local middleman at a fixed low rate would instead pool their harvest and sell directly to processors through a farmer cooperative. On paper the arrangement has worked -- cooperative membership has grown steadily since the programme began. Agricultural economists caution that the growth rests on a narrower base than the membership figures suggest: nearly all of the cooperative's bargaining power comes from a handful of large member orchards whose harvest volume lets it negotiate at all, and if those few large growers left, the cooperative would lose most of the leverage that benefits its smaller members. According to the passage, where does nearly all of the cooperative's bargaining power come from?",
 "options": {"A": "A handful of large member orchards with high harvest volume.",
             "B": "Annual government grants.",
             "C": "International date-buying charities.",
             "D": "Entry fees paid by small growers."},
 "answer": "A"},

{"id": 49, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: Baluchistan's community-managed date orchards were set up on a simple bargain: households that once sold dates to a single local middleman at a fixed low rate would instead pool their harvest and sell directly to processors through a farmer cooperative. On paper the arrangement has worked -- cooperative membership has grown steadily since the programme began. Agricultural economists caution that the growth rests on a narrower base than the membership figures suggest: nearly all of the cooperative's bargaining power comes from a handful of large member orchards whose harvest volume lets it negotiate at all, and if those few large growers left, the cooperative would lose most of the leverage that benefits its smaller members. The author's attitude toward the cooperative's rising membership figures is best characterised as",
 "options": {"A": "fully reassured.", "B": "openly dismissive.", "C": "cautious about what they may obscure.", "D": "indifferent."},
 "answer": "C"},

{"id": 50, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: Baluchistan's community-managed date orchards were set up on a simple bargain: households that once sold dates to a single local middleman at a fixed low rate would instead pool their harvest and sell directly to processors through a farmer cooperative. On paper the arrangement has worked -- cooperative membership has grown steadily since the programme began. Agricultural economists caution that the growth rests on a narrower base than the membership figures suggest: nearly all of the cooperative's bargaining power comes from a handful of large member orchards whose harvest volume lets it negotiate at all, and if those few large growers left, the cooperative would lose most of the leverage that benefits its smaller members. It can most reasonably be inferred that the author regards the cooperative's bargaining power as",
 "options": {"A": "evenly distributed across all its members.",
             "B": "vulnerable to disruption because it depends heavily on a small number of large growers.",
             "C": "irrelevant to whether smaller growers benefit.",
             "D": "more stable than the previous middleman system in every respect."},
 "answer": "B"},

{"id": 51, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as SCRUPULOUS.",
 "options": {"A": "careless", "B": "conscientious", "C": "hasty", "D": "indifferent"},
 "answer": "B"},

{"id": 52, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The delayed rains will BEAR on the district's date harvest this season,\" the word \"bear\" most nearly means",
 "options": {"A": "carry physically.", "B": "have an effect on.", "C": "tolerate patiently.", "D": "give birth to."},
 "answer": "B"},

# ============================================================
# SECTION 4 - MATH (17) - q53-69
# ============================================================

{"id": 53, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in Two Variables", "difficulty": "Medium",
 "question": "A line in the xy-plane passes through the points (1, 5) and (4, 17). What is the y-coordinate of its y-intercept?",
 "options": {"A": "1", "B": "-1", "C": "3", "D": "-3"},
 "answer": "A"},

{"id": 54, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "The function f is defined by f(x) = 7x - 9. If f(a) = 26, what is the value of a?",
 "options": {"A": "4", "B": "5", "C": "6", "D": "7"},
 "answer": "B"},

{"id": 55, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 3x + 3y = 30 and x - 3y = -6, what is the value of y?",
 "options": {"A": "2", "B": "3", "C": "4", "D": "5"},
 "answer": "C"},

{"id": 56, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "A delivery van weighs 800 kg when empty, and the total weight of the loaded van must not exceed 2,200 kg. If each crate weighs 60 kg, what is the greatest number of whole crates the van can carry?",
 "options": {"A": "22", "B": "23", "C": "24", "D": "25"},
 "answer": "B"},

{"id": 57, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Nonlinear Functions", "difficulty": "Medium",
 "question": "What is the minimum value of the function f(x) = x^2 - 10x + 7?",
 "options": {"A": "-18", "B": "-16", "C": "-20", "D": "-14"},
 "answer": "A"},

{"id": 58, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Polynomial Expressions", "difficulty": "Easy",
 "question": "Which expression is equivalent to (5x - 4)(x + 6)?",
 "options": {"A": "5x^2 + 26x - 24", "B": "5x^2 - 26x - 24", "C": "5x^2 + 34x - 24", "D": "5x^2 + 26x + 24"},
 "answer": "A"},

{"id": 59, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "How many real solutions does the equation x^2 + 2x + 9 = 0 have?",
 "options": {"A": "Two distinct real solutions", "B": "Exactly one real solution", "C": "Infinitely many real solutions", "D": "No real solutions"},
 "answer": "D"},

{"id": 60, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is sqrt(98) + sqrt(50) in simplest radical form?",
 "options": {"A": "12*sqrt(2)", "B": "6*sqrt(37)", "C": "3*sqrt(37)", "D": "sqrt(148)"},
 "answer": "A"},

{"id": 61, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Unit Conversion", "difficulty": "Easy",
 "question": "A car consumes fuel at a rate of 8 litres per 100 kilometres. How many litres will it consume on a 375-kilometre journey at that rate?",
 "options": {"A": "28", "B": "30", "C": "32", "D": "34"},
 "answer": "B"},

{"id": 62, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Two-Variable Data Interpretation (tables/graphs)", "difficulty": "Medium",
 "question": "A shop records the number of units sold on each of five days: Monday 20, Tuesday 28, Wednesday 22, Thursday 33, Friday 36. By what percentage did the number of units sold increase from Wednesday to Thursday?",
 "options": {"A": "40%", "B": "45%", "C": "50%", "D": "55%"},
 "answer": "C"},

{"id": 63, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "For the data set 2, 4, 6, 9, 14, what is the mean minus the median?",
 "options": {"A": "0", "B": "1", "C": "2", "D": "3"},
 "answer": "B"},

{"id": 64, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "After a 20% discount, an item sells for Rs. 3,200. What was its price before the discount, in rupees?",
 "options": {"A": "4,000", "B": "3,900", "C": "3,800", "D": "4,100"},
 "answer": "A"},

{"id": 65, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Medium",
 "question": "A cube has a volume of 1,331 cubic centimetres. What is its total surface area, in square centimetres?",
 "options": {"A": "726", "B": "600", "C": "660", "D": "786"},
 "answer": "A"},

{"id": 66, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Easy",
 "question": "The three interior angles of a triangle are in the ratio 4 : 5 : 6. What is the measure of the largest angle, in degrees?",
 "options": {"A": "60", "B": "66", "C": "72", "D": "78"},
 "answer": "C"},

{"id": 67, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Medium",
 "question": "A sector of a circle of radius 9 cm has a central angle of 40 degrees. What is the area of the sector, in square centimetres?",
 "options": {"A": "9pi", "B": "18pi", "C": "4.5pi", "D": "36pi"},
 "answer": "A"},

{"id": 68, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Identities", "difficulty": "Medium",
 "question": "For any angle theta with cos(theta) defined and not equal to 0, which expression is equivalent to sin(theta) / cos(theta)?",
 "options": {"A": "tan(theta)", "B": "cot(theta)", "C": "1", "D": "sec(theta)"},
 "answer": "A"},

{"id": 69, "section": 4, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Easy",
 "question": "What is the sum of all prime numbers strictly between 60 and 70?",
 "options": {"A": "118", "B": "123", "C": "128", "D": "133"},
 "answer": "C"},

# ============================================================
# SECTION 5 - VERBAL (17) - q70-86
# ============================================================

{"id": 70, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "The inspector's checklist was notable for its ____: it verified every fire exit, every extinguisher and every emergency light in the building. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "brevity", "B": "ambiguity", "C": "leniency", "D": "thoroughness"},
 "answer": "D"},

{"id": 71, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: A single national curriculum, taught identically in every school, is the fairest way to educate students because it removes any individual school's discretion over what gets taught. Text 2: Removing a school's discretion over content does not remove discretion from the process; it simply relocates that discretion to whoever wrote the national curriculum and decided which topics and skills would count as essential. The author of Text 2 would most likely characterise Text 1's claim as",
 "options": {"A": "false, because schools still choose how to teach the material.",
             "B": "correct, and sufficient reason to keep the curriculum unchanged.",
             "C": "accurate about school-level discretion but incomplete about where discretion still enters the process.",
             "D": "irrelevant, because curriculum design has no measurable effect on outcomes."},
 "answer": "C"},

{"id": 72, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: Anarkali Bazaar in Lahore is usually valued for its age, often described as one of the oldest surviving markets in South Asia. The more consequential fact is its continuous commercial use: unlike many historic markets converted into tourist-only heritage sites, Anarkali has remained a working bazaar where residents do everyday shopping, which is why its layout has kept adapting rather than being frozen for display. Which choice best states the main idea of the passage?",
 "options": {"A": "Anarkali Bazaar's chief significance lies in its continuous working use rather than simply its age.",
             "B": "Anarkali Bazaar has been converted entirely into a tourist attraction.",
             "C": "Anarkali Bazaar's layout has remained frozen since it was built.",
             "D": "Anarkali Bazaar no longer serves local shoppers."},
 "answer": "A"},

{"id": 73, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A city introduced a dedicated cycling lane along a single busy market road. In the first year, average delivery-vehicle speeds on that road fell by 8 per cent. Over the same period, delivery traffic on the parallel back lanes rose by 13 per cent. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "the cycling lane had no effect on traffic patterns.",
             "B": "total citywide delivery traffic fell by roughly 8 per cent.",
             "C": "at least part of the change on the market road reflects drivers diverting to back lanes rather than making fewer deliveries overall.",
             "D": "drivers on the back lanes were unaware the cycling lane existed."},
 "answer": "C"},

{"id": 74, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A district education office claims its new teacher-training programme improved reading scores more in rural schools than in urban schools. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Average reading scores in rural schools rose by 14 points, while urban schools rose by 2 points.",
             "B": "The district's overall average reading score rose by 8 points.",
             "C": "Urban schools had the highest reading scores both before and after training.",
             "D": "Enrollment rose across every school type during the study period."},
 "answer": "A"},

{"id": 75, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student compiles three observations about the Kartarpur Corridor: it opened in 2019 through a joint agreement between the Pakistani and Indian governments; it connects Dera Baba Nanak in India with Gurdwara Darbar Sahib Kartarpur in Pakistan; and it lets Sikh pilgrims cross the border without a visa. Which statement best synthesises these observations?",
 "options": {"A": "Opened in 2019 through a joint agreement between the two governments, the Kartarpur Corridor lets Sikh pilgrims cross from Dera Baba Nanak to Gurdwara Darbar Sahib Kartarpur without a visa.",
             "B": "The Kartarpur Corridor requires a full visa application for all pilgrims.",
             "C": "The corridor was opened unilaterally without any agreement between the two countries.",
             "D": "The corridor connects Lahore directly to Amritsar."},
 "answer": "A"},

{"id": 76, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "The provincial archive digitised its collection of colonial-era canal-survey maps over a four-year project. ____ a water-rights researcher in Multan can now examine boundary records that once required a personal visit to a single vault in Lahore. Which transition best completes the text?",
 "options": {"A": "Nevertheless,", "B": "Admittedly,", "C": "By comparison,", "D": "As a result,"},
 "answer": "D"},

{"id": 77, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: the yak-polo matches on the Deosai plateau began as informal herder contests; they now draw a small but growing number of trekking tourists each summer; the plateau sits at over 13,000 feet; matches are still organised informally by local herding families rather than any federation. The student wants to emphasise the event's growth from an informal herder contest into a tourist draw while still being locally run. Which choice best accomplishes this goal?",
 "options": {"A": "The Deosai plateau sits at over 13,000 feet.",
             "B": "What began as an informal herder contest on the Deosai plateau now draws a small but growing number of trekking tourists each summer, while still being organised by local herding families rather than any federation.",
             "C": "Matches are organised by local herding families.",
             "D": "The plateau draws trekking tourists each summer."},
 "answer": "B"},

{"id": 78, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The inquiry's findings ____ released in January, prompted an immediate response from two ministries. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ": ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 79, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "Every one of the surveyed date growers reported that ____ export contract had been delayed at least once that season. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "their", "B": "it's", "C": "its", "D": "whose"},
 "answer": "A"},

{"id": 80, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Kept as a working bazaar rather than a display-only heritage site, ____\"",
 "options": {"A": "historians regard Anarkali Bazaar as a commercial landmark.",
             "B": "the bazaar's layout is what most visitors remember.",
             "C": "Anarkali Bazaar continues to adapt to local shoppers' needs.",
             "D": "it is local shoppers whom Anarkali Bazaar continues to serve."},
 "answer": "C"},

{"id": 81, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The report praised the cooperative's fair pricing, its trained field staff, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "it paid growers promptly.",
             "B": "that its payments were prompt.",
             "C": "paying growers promptly.",
             "D": "the promptness of its payments to growers."},
 "answer": "D"},

{"id": 82, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Hard",
 "question": "Neither the warden nor the two field assistants ____ available to open the reserve gate that week. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "was", "B": "is", "C": "has been", "D": "were"},
 "answer": "D"},

{"id": 83, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Hard",
 "question": "Passage: For decades Sialkot's leather-goods makers have blamed their limited access to premium export markets on tanning-chemical costs and foreign compliance audits, and both complaints are real. Neither explains why so many workshops still export uncertified basic goods while competitors in other countries, facing similar input costs, export goods certified for use by major European retailers. That gap is not chiefly at the tanning vat. It is in batch traceability, effluent-treatment records, and the paperwork that a buyer in Italy now expects before it will place an order at all. Which choice best states the main idea of the passage?",
 "options": {"A": "Tanning-chemical costs and compliance audits are the chief obstacles facing Sialkot's leather exporters.",
             "B": "The industry's limited access to premium markets is better explained by gaps in traceability and compliance documentation than by input costs alone.",
             "C": "Competitors in other countries pay lower tanning-chemical costs than Sialkot workshops do.",
             "D": "Sialkot should stop exporting basic leather goods altogether."},
 "answer": "B"},

{"id": 84, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: For decades Sialkot's leather-goods makers have blamed their limited access to premium export markets on tanning-chemical costs and foreign compliance audits, and both complaints are real. Neither explains why so many workshops still export uncertified basic goods while competitors in other countries, facing similar input costs, export goods certified for use by major European retailers. That gap is not chiefly at the tanning vat. It is in batch traceability, effluent-treatment records, and the paperwork that a buyer in Italy now expects before it will place an order at all. It can most reasonably be inferred that the author would agree with which statement?",
 "options": {"A": "Lowering tanning-chemical costs alone would move Sialkot workshops into premium export markets.",
             "B": "Complaints about compliance audits are fabricated by the industry.",
             "C": "Building stronger traceability and effluent-record systems would address a gap that input-cost relief cannot.",
             "D": "Sialkot workshops are technically less capable than their European competitors."},
 "answer": "C"},

{"id": 85, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as PARSIMONIOUS.",
 "options": {"A": "generous", "B": "stingy", "C": "careless", "D": "cheerful"},
 "answer": "B"},

{"id": 86, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The committee's response to the proposal was carefully MEASURED,\" the word \"measured\" most nearly means",
 "options": {"A": "calculated in exact units.", "B": "deliberate and controlled.", "C": "financially risky.", "D": "legally required."},
 "answer": "B"},

# ============================================================
# SECTION 6 - MATH (17) - q87-103
# ============================================================

{"id": 87, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Medium",
 "question": "If x/5 - 3 = x/10, what is the value of x?",
 "options": {"A": "24", "B": "27", "C": "30", "D": "33"},
 "answer": "C"},

{"id": 88, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Hard",
 "question": "In an arithmetic sequence the 6th term is 20 and the 11th term is 45. What is the first term?",
 "options": {"A": "-5", "B": "0", "C": "5", "D": "10"},
 "answer": "A"},

{"id": 89, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "A taxi charges a fixed Rs. 120 plus Rs. 30 for every kilometre travelled. A journey costs Rs. 510. How many kilometres was the journey?",
 "options": {"A": "11", "B": "12", "C": "13", "D": "14"},
 "answer": "C"},

{"id": 90, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Easy",
 "question": "What is the sum of the solutions of x^2 - 16x + 15 = 0?",
 "options": {"A": "15", "B": "-16", "C": "-15", "D": "16"},
 "answer": "D"},

{"id": 91, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "If log(x) = 5, where log denotes the base-10 logarithm, what is the value of log(100x)?",
 "options": {"A": "6", "B": "7", "C": "500", "D": "10000"},
 "answer": "B"},

{"id": 92, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "For all x other than 7 and -3, which expression is equivalent to (x^2 - 49) / (x^2 - 4x - 21)?",
 "options": {"A": "(x - 7)/(x + 3)", "B": "(x + 7)/(x - 3)", "C": "7/3", "D": "(x + 7)/(x + 3)"},
 "answer": "D"},

{"id": 93, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Medium",
 "question": "Five identical machines together produce 500 units in 4 hours. Working at the same rate, how many units would 8 such machines produce in 3 hours?",
 "options": {"A": "500", "B": "550", "C": "600", "D": "650"},
 "answer": "C"},

{"id": 94, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "The mean of eleven numbers is 30. When one of the numbers is removed, the mean of the remaining ten is 28. What was the number that was removed?",
 "options": {"A": "40", "B": "45", "C": "50", "D": "55"},
 "answer": "C"},

{"id": 95, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A fair six-sided die is rolled twice. What is the probability that the two results add up to 11?",
 "options": {"A": "1/18", "B": "1/9", "C": "1/6", "D": "1/12"},
 "answer": "A"},

{"id": 96, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "Set M is {25, 25, 25, 25, 25} and Set N is {15, 20, 25, 30, 35}. Both sets have a mean of 25. Which set has the larger standard deviation?",
 "options": {"A": "Set M", "B": "They are equal", "C": "It cannot be determined from the information given", "D": "Set N"},
 "answer": "D"},

{"id": 97, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A square and an equilateral triangle each have a perimeter of 48 cm. By how many centimetres does the triangle's side exceed the square's side?",
 "options": {"A": "2", "B": "3", "C": "4", "D": "5"},
 "answer": "C"},

{"id": 98, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Easy",
 "question": "A right circular cylinder has a radius of 4 cm and a height of 10 cm. What is its volume, in cubic centimetres?",
 "options": {"A": "160pi", "B": "140pi", "C": "120pi", "D": "100pi"},
 "answer": "A"},

{"id": 99, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Medium",
 "question": "Two parallel lines are cut by a transversal. One of the two interior angles on the same side of the transversal measures 95 degrees. What is the measure, in degrees, of the other?",
 "options": {"A": "85", "B": "95", "C": "90", "D": "75"},
 "answer": "A"},

{"id": 100, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Medium",
 "question": "In a 30-60-90 right triangle, the shorter leg measures 14 cm. What is the length of the hypotenuse, in centimetres?",
 "options": {"A": "28", "B": "14*sqrt(3)", "C": "28*sqrt(3)", "D": "21"},
 "answer": "A"},

{"id": 101, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Number Properties (odd/even, divisibility)", "difficulty": "Easy",
 "question": "If n is an even integer, which of the following must be odd?",
 "options": {"A": "n^2", "B": "2n", "C": "n + 3", "D": "4n"},
 "answer": "C"},

{"id": 102, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the smallest positive integer that is divisible by 4, 6 and 9?",
 "options": {"A": "36", "B": "72", "C": "24", "D": "108"},
 "answer": "A"},

{"id": 103, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Medium",
 "question": "Which of the following is NOT a prime number?",
 "options": {"A": "79", "B": "81", "C": "83", "D": "89"},
 "answer": "B"},

# ============================================================
# SECTION 7 - VERBAL (17) - q104-120
# ============================================================

{"id": 104, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Easy",
 "question": "The registrar's notice this term was strikingly ____: it listed the new exam schedule and the venue changes and nothing more. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "vague", "B": "lengthy", "C": "evasive", "D": "concise"},
 "answer": "D"},

{"id": 105, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Every retrospective on the Basant kite festival's decline blames the ban on metal-coated string. The explanation is accurate as far as it goes. But it hides the more interesting fact, which is that rooftop kite-flying had already been shrinking for years as those same rooftops filled with satellite dishes and water tanks -- and that it was the disappearing open roof, not the ban alone, that explains the festival's fade.\" Which choice best describes the function of the final clause in the text as a whole?",
 "options": {"A": "It withdraws a claim made earlier in the text.",
             "B": "It supplies statistical evidence for the first sentence.",
             "C": "It concedes that the string-ban explanation is factually wrong.",
             "D": "It states the specific point the author believes the conventional account obscures."},
 "answer": "D"},

{"id": 106, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: For years the provincial government has offered a fixed subsidised rate for canal water delivered to rice fields, well below what the same water would cost a vegetable farm nearby. The policy works: farmers keep planting rice even in years when the market price is weak. It also works too well: land suited to higher-value vegetables stays under rice, because rice is the one crop whose water cost a farmer can count on regardless of the season. Which choice best states the main idea of the passage?",
 "options": {"A": "The subsidised water rate has failed to keep farmers planting rice.",
             "B": "By keeping water costs low for rice alone, the subsidy succeeds at its aim while locking land into a lower-value crop.",
             "C": "Vegetable farms use less water than rice fields in every district.",
             "D": "Canal water rates have remained unchanged for decades."},
 "answer": "B"},

{"id": 107, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A publisher reissued a set of regional poetry collections in two versions identical except for a translator's preface: included on some copies, omitted from others. Copies with the preface sold 19 per cent more in regions where the translator already had name recognition. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "readers prefer poetry collections with no preface at all.",
             "B": "how visibly a well-known translator is featured can affect how many copies are bought.",
             "C": "the preface made the poems more accurately translated.",
             "D": "poetry collections sell better than novels in general."},
 "answer": "B"},

{"id": 108, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "A critic argues that the writer Saadat Hasan Manto deliberately centres a single unsettling detail rather than an overt moral statement even when his stories address the violence of Partition. Which description of a story's content, if accurate, would most directly support that argument?",
 "options": {"A": "The story opens with a narrator explicitly condemning the violence in a lengthy address to the reader.",
             "B": "The story is set during Partition but focuses on a single abandoned toy left in a doorway rather than any explicit commentary.",
             "C": "A narrator delivers an extended speech summarising the political causes of the violence.",
             "D": "The story closes with a direct statement of the moral lesson intended."},
 "answer": "B"},

{"id": 109, "section": 7, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "Domestic cotton production fell for three consecutive seasons, and several ginning mills reduced operating hours. ____ the country's rice exports rose sharply, offsetting some of the agricultural sector's overall decline. Which transition best completes the text?",
 "options": {"A": "Therefore,", "B": "For example,", "C": "In conclusion,", "D": "Meanwhile,"},
 "answer": "D"},

{"id": 110, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The first phase of the canal-desilting project finished on schedule ____ the second phase ran nearly five months behind. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ", also ", "C": " which ", "D": "; "},
 "answer": "D"},

{"id": 111, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Easy",
 "question": "Because the coastal road had been closed by flooding ____ supplies were carried in by boat for nearly two weeks. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; ", "C": ". ", "D": ": "},
 "answer": "A"},

{"id": 112, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which version of the sentence most clearly means that the grant pays for travel and for nothing else?",
 "options": {"A": "The grant only covers travel.",
             "B": "Only the grant covers travel.",
             "C": "The grant covers only travel.",
             "D": "The grant covers travel only for conference presenters."},
 "answer": "C"},

{"id": 113, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: When the new expressway bypassed the old town of Muzaffargarh, several roadside dhabas that had depended on through-traffic were relocated to a new service plaza with proper parking and covered seating -- amenities the old roadside stretch had never had. Officials have cited the new plaza as proof that the relocation helped local vendors. Trader surveys complicate that reading: footfall at the plaza depends on travellers choosing to exit the expressway at all, something few did in the plaza's first two years, and several vendors report that their effective income has fallen even though their premises have visibly improved. A plaza that looks better in tile and glass can still leave a vendor worse off than before, if the relocation was measured only in square footage and not in what a stall could still earn. Which choice best states the main idea of the passage?",
 "options": {"A": "The relocation has improved every measurable aspect of vendors' businesses.",
             "B": "Improved premises at the new plaza may conceal a decline in footfall-based income that facility quality alone does not capture.",
             "C": "Expressway traffic has increased sharply through the old roadside stretch.",
             "D": "Most of the original roadside dhabas had covered seating before relocation."},
 "answer": "B"},

{"id": 114, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: When the new expressway bypassed the old town of Muzaffargarh, several roadside dhabas that had depended on through-traffic were relocated to a new service plaza with proper parking and covered seating -- amenities the old roadside stretch had never had. Officials have cited the new plaza as proof that the relocation helped local vendors. Trader surveys complicate that reading: footfall at the plaza depends on travellers choosing to exit the expressway at all, something few did in the plaza's first two years, and several vendors report that their effective income has fallen even though their premises have visibly improved. A plaza that looks better in tile and glass can still leave a vendor worse off than before, if the relocation was measured only in square footage and not in what a stall could still earn. According to the passage, what amenities did the new service plaza include?",
 "options": {"A": "Proper parking and covered seating.",
             "B": "Only proper parking, with no other facilities.",
             "C": "Direct expressway access for every stall.",
             "D": "The passage does not say."},
 "answer": "A"},

{"id": 115, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: When the new expressway bypassed the old town of Muzaffargarh, several roadside dhabas that had depended on through-traffic were relocated to a new service plaza with proper parking and covered seating -- amenities the old roadside stretch had never had. Officials have cited the new plaza as proof that the relocation helped local vendors. Trader surveys complicate that reading: footfall at the plaza depends on travellers choosing to exit the expressway at all, something few did in the plaza's first two years, and several vendors report that their effective income has fallen even though their premises have visibly improved. A plaza that looks better in tile and glass can still leave a vendor worse off than before, if the relocation was measured only in square footage and not in what a stall could still earn. The author's attitude toward officials' claim that the relocation helped vendors is best characterised as",
 "options": {"A": "fully persuaded.", "B": "openly mocking.", "C": "skeptical, given the survey evidence cited.", "D": "indifferent."},
 "answer": "C"},

{"id": 116, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: When the new expressway bypassed the old town of Muzaffargarh, several roadside dhabas that had depended on through-traffic were relocated to a new service plaza with proper parking and covered seating -- amenities the old roadside stretch had never had. Officials have cited the new plaza as proof that the relocation helped local vendors. Trader surveys complicate that reading: footfall at the plaza depends on travellers choosing to exit the expressway at all, something few did in the plaza's first two years, and several vendors report that their effective income has fallen even though their premises have visibly improved. A plaza that looks better in tile and glass can still leave a vendor worse off than before, if the relocation was measured only in square footage and not in what a stall could still earn. It can most reasonably be inferred that the author would support",
 "options": {"A": "measuring the relocation's success by facility quality alone.",
             "B": "closing the expressway bypass immediately.",
             "C": "treating the new premises as sufficient compensation regardless of lost income.",
             "D": "assessing the relocation's outcomes by vendor income and footfall, not facility quality alone."},
 "answer": "D"},

{"id": 117, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The residency is open to applicants who have completed a relevant portfolio, who have exhibited work publicly, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "having two professional references.",
             "B": "two professional references.",
             "C": "they have two professional references.",
             "D": "who have two professional references."},
 "answer": "D"},

{"id": 118, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as SEDULOUS.",
 "options": {"A": "lazy", "B": "diligent", "C": "careless", "D": "impulsive"},
 "answer": "B"},

{"id": 119, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to AFFLUENCE.",
 "options": {"A": "poverty", "B": "surplus", "C": "wealth", "D": "growth"},
 "answer": "A"},

{"id": 120, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The revised policy did little to CURTAIL illegal sand mining along the riverbank,\" the word \"curtail\" most nearly means",
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
#      bank and from Mocks 1-6. That tuple (with past_paper) is
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
    for modname in ("lums_mock_01", "lums_mock_02", "lums_mock_03",
                    "lums_mock_04", "lums_mock_05", "lums_mock_06"):
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