"""
LUMS Common Admission Test (LCAT) - Full-Length Mock Test #2
=============================================================
ParhaiKarlo-prepared full-length mock test. NOT an official LUMS past paper.
Answer keys prepared by content team, pending human verification.

Nothing in this file is taken from LUMS' official "Sample Questions for
Verbal & Math Sections" guide (raw-sources/sample_lcat_2025.pdf), nor from
`lums_lcat_mock_01.py`, `lums_lcat_mock_03.py` or `lums_lcat_mock_04.py`.
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
 "question": "Multan's blue-pottery artisans still apply each cobalt-and-turquoise pattern by hand, a slow, ____ process that a factory press could finish in seconds but never quite replicate. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "careless", "B": "meticulous", "C": "rushed", "D": "accidental"},
 "answer": "B"},

{"id": 2, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Medium",
 "question": "Text: \"Rohtas Fort is usually described in tourist brochures as a fortress built to defend against a single rival chieftain. The description is not wrong, but it is thin: the fort's sixty-eight bastions and its position astride the Grand Trunk Road suggest a garrison built to control trade and troop movement across an entire region, not merely to repel one local threat.\" Which choice best describes the function of the second sentence in the text as a whole?",
 "options": {"A": "It fully endorses the brochure's description.",
             "B": "It expands the brochure's narrow description by pointing to evidence of a broader strategic purpose.",
             "C": "It denies that Rohtas Fort was ever a defensive structure.",
             "D": "It restates the brochure's description verbatim."},
 "answer": "B"},

{"id": 3, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: Makli's necropolis, with hundreds of thousands of graves spread over several square kilometres, should be read primarily as a record of dynastic wealth, since only rulers and nobles could commission its elaborately carved tombs. Text 2: Most of Makli's graves are plain, unmarked mounds with no carving at all; the elaborate tombs that draw visitors' attention are a small, unrepresentative fraction of who is actually buried there. Based on the texts, how would the author of Text 2 most likely respond to Text 1's claim?",
 "options": {"A": "By agreeing that the necropolis records mainly dynastic wealth.",
             "B": "By pointing out that the carved tombs Text 1 relies on represent only a small share of the burials, so the site as a whole reflects more than elite wealth.",
             "C": "By denying that any tombs at Makli are carved.",
             "D": "By conceding that ordinary graves outnumber elite ones but agreeing this doesn't matter."},
 "answer": "B"},

{"id": 4, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Easy",
 "question": "Passage: Katas Raj's sacred pool is often introduced to visitors purely as a pilgrimage site, a fact that omits its hydrology. The pool is fed by an underground spring rather than rainfall, which is why decades of nearby cement-factory drilling, not drought, caused its water level to drop sharply in the early 2000s before conservation work partly restored it. What is the main idea of the passage?",
 "options": {"A": "Katas Raj's pool level dropped mainly because of drought.",
             "B": "The pool's decline was driven by nearby industrial drilling into its underground spring source, not by weather.",
             "C": "Katas Raj has never been used as a pilgrimage site.",
             "D": "Conservation work has had no effect on the pool."},
 "answer": "B"},

{"id": 5, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A survey of handloom weavers in Multan found that the number of registered looms fell by nearly a third over ten years, even as the city's total fabric output, measured by weight, stayed roughly flat. Which inference most logically follows?",
 "options": {"A": "The remaining looms are, on average, producing more fabric each than before.",
             "B": "Multan has stopped producing handloom fabric entirely.",
             "C": "Fabric output fell in proportion to the loom count.",
             "D": "Registered looms are less productive than unregistered ones."},
 "answer": "A"},

{"id": 6, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A researcher claims that a mango orchard's rising export revenue was driven more by higher prices per crate than by a larger harvest. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Revenue rose 40%, while crates exported rose 3% and average price per crate rose 36%.",
             "B": "Revenue rose 40%, while crates exported rose 34% and average price per crate rose 4%.",
             "C": "Revenue fell 5%, while crates exported rose 34%.",
             "D": "Revenue rose 40%, and international mango demand fell 10%."},
 "answer": "A"},

{"id": 7, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student researching Rohtas Fort compiles three notes: it was built in the 16th century by Sher Shah Suri; it has sixty-eight bastions along its walls; and it sits on the historic Grand Trunk Road and has been listed as a UNESCO World Heritage Site. Which statement best synthesises these observations?",
 "options": {"A": "Built in the 16th century by Sher Shah Suri along the Grand Trunk Road, Rohtas Fort's sixty-eight bastions have helped earn it UNESCO World Heritage status.",
             "B": "Rohtas Fort was built after the Grand Trunk Road was abandoned.",
             "C": "UNESCO has declined to recognise Rohtas Fort.",
             "D": "Rohtas Fort has no defensive bastions."},
 "answer": "A"},

{"id": 8, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "Faisalabad's textile mills have automated much of their spinning process over the past decade. ____ the number of workers employed directly in spinning has fallen even as total yarn output has risen. Which transition best completes the text?",
 "options": {"A": "Similarly,", "B": "For instance,", "C": "As a result,", "D": "On the other hand,"},
 "answer": "C"},

{"id": 9, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: Namal Lake was originally built as an irrigation reservoir; it now also supports a small local fishery; migratory birds stop there each winter; a nearby university uses it for water-quality research. The student wants to emphasise the lake's shift from a single-purpose reservoir to a site serving multiple uses. Which choice best accomplishes this goal?",
 "options": {"A": "Namal Lake was originally built as an irrigation reservoir.",
             "B": "Migratory birds stop at Namal Lake each winter.",
             "C": "Originally built purely as an irrigation reservoir, Namal Lake now also sustains a local fishery, hosts wintering migratory birds, and supports university water research.",
             "D": "A nearby university studies Namal Lake's water quality."},
 "answer": "C"},

{"id": 10, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "The collection of hand-carved wooden screens removed from the old haveli ____ now displayed at the provincial museum. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "are", "B": "is", "C": "have been", "D": "were"},
 "answer": "B"},

{"id": 11, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "The cotton growers rejected the revised pricing formula, and ____ concerns were forwarded to the provincial board. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "its", "B": "their", "C": "it's", "D": "there"},
 "answer": "B"},

{"id": 12, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The expedition reached one clear verdict ____ the glacier had retreated more than 200 metres since the previous survey. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", that", "B": ", being", "C": "; which", "D": ": "},
 "answer": "D"},

{"id": 13, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Medium",
 "question": "The mill had operated on coal power for six decades ____ its owners switched entirely to a gas-fired boiler last year. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "; ", "B": ", ", "C": " which ", "D": " and which "},
 "answer": "A"},

{"id": 14, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Having surveyed the Makli necropolis for three field seasons, ____\"",
 "options": {"A": "the conclusion of the archaeologists was that most graves were unmarked.",
             "B": "it was concluded by the archaeologists that most graves were unmarked.",
             "C": "the archaeologists concluded that most graves were unmarked.",
             "D": "unmarked graves were shown by the archaeologists to predominate."},
 "answer": "C"},

{"id": 15, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: Khewra's salt mine is usually promoted for its scale, marketed as one of the largest in the world. The scale figure hides a more telling detail: most of the mine's current output is not table salt at all but salt destined for industrial de-icing and chemical processing, a shift that happened gradually as global demand for food-grade salt flattened while demand for industrial salt kept climbing. Which choice best states the main idea of the passage?",
 "options": {"A": "Khewra's mine has stopped producing salt of any kind.",
             "B": "The mine's headline scale obscures a quiet shift toward industrial rather than food-grade salt production.",
             "C": "Food-grade salt demand has grown faster than industrial demand.",
             "D": "Khewra is no longer among the largest salt mines in the world."},
 "answer": "B"},

{"id": 16, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: Khewra's salt mine is usually promoted for its scale, marketed as one of the largest in the world. The scale figure hides a more telling detail: most of the mine's current output is not table salt at all but salt destined for industrial de-icing and chemical processing, a shift that happened gradually as global demand for food-grade salt flattened while demand for industrial salt kept climbing. The author's attitude toward the marketing emphasis on the mine's scale is best characterised as",
 "options": {"A": "fully approving.", "B": "mildly corrective.", "C": "openly hostile.", "D": "entirely indifferent."},
 "answer": "B"},

{"id": 17, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as SKEPTICAL.",
 "options": {"A": "gullible", "B": "doubtful", "C": "confident", "D": "cheerful"},
 "answer": "B"},

{"id": 18, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to the underlined word as it is used here: \"The committee's approach to the budget dispute was notably CONCILIATORY.\"",
 "options": {"A": "confrontational", "B": "careful", "C": "private", "D": "gradual"},
 "answer": "A"},

# ============================================================
# SECTION 2 - MATH (17) - q19-35
# ============================================================

{"id": 19, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Easy",
 "question": "If 4(x + 3) - 5 = 2x + 21, what is the value of x?",
 "options": {"A": "5", "B": "6", "C": "7", "D": "8"},
 "answer": "C"},

{"id": 20, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 2x + 3y = 29 and x + y = 12, what is the value of y?",
 "options": {"A": "4", "B": "5", "C": "6", "D": "7"},
 "answer": "B"},

{"id": 21, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "Which of the following describes all values of x for which 15 - 3x < 6?",
 "options": {"A": "x > 3", "B": "x < 3", "C": "x > -3", "D": "x < -3"},
 "answer": "A"},

{"id": 22, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Medium",
 "question": "An arithmetic sequence has first term 8 and common difference 4. What is the sum of its first 15 terms?",
 "options": {"A": "540", "B": "510", "C": "560", "D": "525"},
 "answer": "A"},

{"id": 23, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "The equation x^2 + kx + 24 = 0 has roots 4 and 6. What is the value of k?",
 "options": {"A": "-10", "B": "10", "C": "-24", "D": "24"},
 "answer": "A"},

{"id": 24, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is the value of 9^(3/2) * 8^(1/3)?",
 "options": {"A": "27", "B": "45", "C": "54", "D": "72"},
 "answer": "C"},

{"id": 25, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "What is the value of (log_4 64) - (log_3 9)?",
 "options": {"A": "-1", "B": "1", "C": "5", "D": "-5"},
 "answer": "B"},

{"id": 26, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "If 2/x + 1/(3x) = 7/12, what is the value of x?",
 "options": {"A": "2", "B": "3", "C": "4", "D": "6"},
 "answer": "C"},

{"id": 27, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "A trader raises the price of an item by 20% and then, in a sale, reduces the new price by 25%. Compared with the original price, the final price is",
 "options": {"A": "10% higher.", "B": "10% lower.", "C": "unchanged.", "D": "5% lower."},
 "answer": "B"},

{"id": 28, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Easy",
 "question": "A sum of Rs. 84,000 is divided between two partners in the ratio 4 : 3. By how much does the larger share exceed the smaller share, in rupees?",
 "options": {"A": "9,000", "B": "12,000", "C": "15,000", "D": "18,000"},
 "answer": "B"},

{"id": 29, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "A class of 20 students has a mean score of 65. Five more students, whose mean score is 85, join the class. What is the mean score of all 25 students?",
 "options": {"A": "67", "B": "69", "C": "71", "D": "73"},
 "answer": "B"},

{"id": 30, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A bag contains 4 red marbles and 9 blue marbles. Two marbles are drawn at random without replacement. What is the probability that both are red?",
 "options": {"A": "1/13", "B": "4/39", "C": "3/13", "D": "1/9"},
 "answer": "A"},

{"id": 31, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A rectangle has a perimeter of 50 cm, and its length is 7 cm greater than its width. What is its area, in square centimetres?",
 "options": {"A": "144", "B": "136", "C": "126", "D": "154"},
 "answer": "A"},

{"id": 32, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Easy",
 "question": "A right triangle has legs of length 9 cm and 40 cm. What is its perimeter, in centimetres?",
 "options": {"A": "80", "B": "85", "C": "90", "D": "95"},
 "answer": "C"},

{"id": 33, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Easy",
 "question": "A circle has an area of 121pi square centimetres. What is its circumference, in centimetres?",
 "options": {"A": "11pi", "B": "22pi", "C": "44pi", "D": "121pi"},
 "answer": "B"},

{"id": 34, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Ratios", "difficulty": "Medium",
 "question": "In a right triangle, theta is an acute angle and cos(theta) = 7/25. What is the value of sin(theta)?",
 "options": {"A": "24/25", "B": "7/24", "C": "25/24", "D": "7/25"},
 "answer": "A"},

{"id": 35, "section": 2, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the least common multiple of 9 and 15, minus their greatest common divisor?",
 "options": {"A": "36", "B": "42", "C": "39", "D": "45"},
 "answer": "B"},

# ============================================================
# SECTION 3 - VERBAL (17) - q36-52
# ============================================================

{"id": 36, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "Marketed as a low-cost solution for rural clinics, the portable ultrasound device proved largely ____ without a trained technician, since its readings required interpretation few clinic staff had been taught to provide. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "indispensable", "B": "affordable", "C": "useless", "D": "durable"},
 "answer": "C"},

{"id": 37, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Development economists have long modelled microfinance loans as a straightforward substitute for informal moneylenders: a household simply switches its borrowing to the cheaper, formal source. The model predicts declining reliance on moneylenders. That is not what repeated surveys of microfinance borrowers in rural Punjab show: many households keep borrowing from moneylenders for emergencies precisely because microfinance loans, unlike moneylenders, come with fixed repayment schedules that don't bend around a bad month.\" Which choice best describes the function of the final sentence in the text as a whole?",
 "options": {"A": "It supplies an example confirming the model's prediction.",
             "B": "It introduces survey evidence that conflicts with the model's prediction and explains why.",
             "C": "It proposes discarding the survey evidence in favour of the model.",
             "D": "It restates the model's claim in more concrete terms."},
 "answer": "B"},

{"id": 38, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: Over fifteen years, the number of registered brick kilns near Lahore grew only slightly, while the volume of bricks they fired each year grew far faster, as newer kilns use zigzag technology that fires more bricks per batch than the older bull's-trench kilns they gradually replaced. Environmental auditors caution against reading the modest growth in kiln numbers as reassuring: the real story is how much more fuel and clay a similar number of kilns can now consume. Which choice best states the main idea of the passage?",
 "options": {"A": "The number of brick kilns near Lahore has grown dramatically.",
             "B": "Kiln count is a more meaningful statistic than firing volume.",
             "C": "Older kilns fire more bricks than newer ones.",
             "D": "The modest growth in kiln numbers conceals a much sharper rise in fuel and clay consumption."},
 "answer": "D"},

{"id": 39, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: Pakistan's wetlands are managed province by province, but the migratory cranes that draw the most birdwatching attention pass through wetlands that straddle several provincial boundaries in a single migration season, and the same flock is often counted by observers registered to more than one province. It follows that separate provincial crane counts ____ Which choice most logically completes the text?",
 "options": {"A": "should be conducted more often than they currently are.",
             "B": "cannot simply be summed to produce a reliable national total.",
             "C": "will always overstate the true number in each province.",
             "D": "are the only practical way to track the species."},
 "answer": "B"},

{"id": 40, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "In a study of Uch Sharif's annual urs, a researcher argues that visitors value the shrine's qawwali sessions less as formal performance than as a shared emotional release across social lines. Which quotation from a visitor interview, if authentic, would most directly support that argument?",
 "options": {"A": "\"The qawwali follows a set order that the lead singer controls from start to finish.\"",
             "B": "\"When the qawwali reaches its peak, nobody here cares who you are outside this courtyard -- we're all just swaying together.\"",
             "C": "\"The urs draws visitors from across southern Punjab each year.\"",
             "D": "\"Donations collected during the urs fund the shrine's langar.\""},
 "answer": "B"},

{"id": 41, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student researching Lahore's Shahi Qila records three observations: it was expanded under several Mughal emperors over centuries; it combines Persian, Central Asian, and local Punjabi architectural styles; and it now operates partly as a museum while parts remain closed for ongoing restoration. Which statement best synthesises these observations?",
 "options": {"A": "Expanded under several Mughal emperors over centuries, the Shahi Qila blends Persian, Central Asian and Punjabi styles and now serves partly as a museum while restoration continues elsewhere within it.",
             "B": "The Shahi Qila was built entirely within a single decade.",
             "C": "The Shahi Qila uses only Central Asian architectural styles.",
             "D": "The Shahi Qila is now fully closed to the public."},
 "answer": "A"},

{"id": 42, "section": 3, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "Karachi's horse-drawn victoria carriages once carried tourists along the seafront each evening. ____ battery rickshaws, quieter and cheaper to operate, have taken over most of that route, leaving only a few carriages for special occasions. Which transition best completes the text?",
 "options": {"A": "Consequently,", "B": "In short,", "C": "Similarly,", "D": "By contrast,"},
 "answer": "A"},

{"id": 43, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The workshop trains apprentices to prepare the natural dyes, to set up the traditional loom, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "weaving the first few rows themselves.",
             "B": "they weave the first few rows themselves.",
             "C": "to weave the first few rows themselves.",
             "D": "the first few rows are woven by them."},
 "answer": "C"},

{"id": 44, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The trip covered three stops in southern Punjab ____ Multan's blue-pottery quarter, Uch Sharif's shrines and the Katas Raj temple pool. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ": ", "B": ", ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 45, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "Each of the nine restored havelis in the Walled City ____ open to visitors on weekends. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "are", "B": "were", "C": "is", "D": "have been"},
 "answer": "C"},

{"id": 46, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Hard",
 "question": "The spillway gates were repaired in 2015 ____ flash floods along the same valley have grown more frequent every monsoon since. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ", however ", "C": " and which ", "D": "; nevertheless, "},
 "answer": "D"},

{"id": 47, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: Sindh's community-managed mangrove nurseries were set up on a simple bargain: fishing villages that once cleared mangroves for firewood would instead replant them and earn income from a small number of carbon-credit contracts sold to outside buyers. On paper the arrangement has worked -- mangrove cover in the managed zones has expanded steadily since the programme began. Environmental economists caution that the recovery rests on a narrower base than the cover figures suggest: nearly all of the programme's funding comes from a handful of long-term carbon contracts, and a shift in international carbon-credit prices could remove most of the funding that pays for nursery maintenance the rest of the year. Which choice best states the main idea of the passage?",
 "options": {"A": "Sindh's mangrove nurseries have failed to expand cover.",
             "B": "Expanding mangrove cover conceals how dependent the programme's funding is on a narrow, price-sensitive carbon-credit income.",
             "C": "Firewood cutting has resumed at full scale in the managed zones.",
             "D": "Carbon-credit contracts are renegotiated monthly."},
 "answer": "B"},

{"id": 48, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: Sindh's community-managed mangrove nurseries were set up on a simple bargain: fishing villages that once cleared mangroves for firewood would instead replant them and earn income from a small number of carbon-credit contracts sold to outside buyers. On paper the arrangement has worked -- mangrove cover in the managed zones has expanded steadily since the programme began. Environmental economists caution that the recovery rests on a narrower base than the cover figures suggest: nearly all of the programme's funding comes from a handful of long-term carbon contracts, and a shift in international carbon-credit prices could remove most of the funding that pays for nursery maintenance the rest of the year. According to the passage, where does nearly all of the programme's funding come from?",
 "options": {"A": "A handful of long-term carbon-credit contracts.",
             "B": "Annual government grants.",
             "C": "International conservation charities.",
             "D": "Entry fees from ecotourists."},
 "answer": "A"},

{"id": 49, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: Sindh's community-managed mangrove nurseries were set up on a simple bargain: fishing villages that once cleared mangroves for firewood would instead replant them and earn income from a small number of carbon-credit contracts sold to outside buyers. On paper the arrangement has worked -- mangrove cover in the managed zones has expanded steadily since the programme began. Environmental economists caution that the recovery rests on a narrower base than the cover figures suggest: nearly all of the programme's funding comes from a handful of long-term carbon contracts, and a shift in international carbon-credit prices could remove most of the funding that pays for nursery maintenance the rest of the year. The author's attitude toward the programme's rising mangrove cover figures is best characterised as",
 "options": {"A": "fully reassured.", "B": "openly dismissive.", "C": "cautious about what they may obscure.", "D": "indifferent."},
 "answer": "C"},

{"id": 50, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: Sindh's community-managed mangrove nurseries were set up on a simple bargain: fishing villages that once cleared mangroves for firewood would instead replant them and earn income from a small number of carbon-credit contracts sold to outside buyers. On paper the arrangement has worked -- mangrove cover in the managed zones has expanded steadily since the programme began. Environmental economists caution that the recovery rests on a narrower base than the cover figures suggest: nearly all of the programme's funding comes from a handful of long-term carbon contracts, and a shift in international carbon-credit prices could remove most of the funding that pays for nursery maintenance the rest of the year. It can most reasonably be inferred that the author regards the programme's funding model as",
 "options": {"A": "diversified enough to withstand a price shift.",
             "B": "vulnerable to disruption because it depends heavily on a narrow, price-sensitive income source.",
             "C": "irrelevant to whether mangrove clearing resumes.",
             "D": "more stable than government-funded conservation programmes."},
 "answer": "B"},

{"id": 51, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as PRUDENT.",
 "options": {"A": "reckless", "B": "wasteful", "C": "careful", "D": "loud"},
 "answer": "C"},

{"id": 52, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The delayed monsoon will WEIGH on smallholder cotton yields this season,\" the word \"weigh\" most nearly means",
 "options": {"A": "measure precisely.", "B": "have a burdensome effect.", "C": "balance evenly.", "D": "increase in mass."},
 "answer": "B"},

# ============================================================
# SECTION 4 - MATH (17) - q53-69
# ============================================================

{"id": 53, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in Two Variables", "difficulty": "Medium",
 "question": "A line in the xy-plane passes through the points (3, 8) and (7, 24). What is the y-coordinate of its y-intercept?",
 "options": {"A": "-4", "B": "4", "C": "-8", "D": "8"},
 "answer": "A"},

{"id": 54, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "The function f is defined by f(x) = 8x - 15. If f(a) = 33, what is the value of a?",
 "options": {"A": "4", "B": "5", "C": "6", "D": "7"},
 "answer": "C"},

{"id": 55, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 4x + 2y = 28 and x - 2y = -3, what is the value of y?",
 "options": {"A": "2", "B": "3", "C": "4", "D": "5"},
 "answer": "C"},

{"id": 56, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "A delivery van weighs 750 kg when empty, and the total weight of the loaded van must not exceed 2,100 kg. If each crate weighs 50 kg, what is the greatest number of whole crates the van can carry?",
 "options": {"A": "25", "B": "26", "C": "27", "D": "28"},
 "answer": "C"},

{"id": 57, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Nonlinear Functions", "difficulty": "Medium",
 "question": "What is the minimum value of the function f(x) = x^2 - 8x + 5?",
 "options": {"A": "-11", "B": "-9", "C": "-13", "D": "-16"},
 "answer": "A"},

{"id": 58, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Polynomial Expressions", "difficulty": "Easy",
 "question": "Which expression is equivalent to (4x - 3)(x + 5)?",
 "options": {"A": "4x^2 + 17x - 15", "B": "4x^2 - 17x - 15", "C": "4x^2 + 23x - 15", "D": "4x^2 + 17x + 15"},
 "answer": "A"},

{"id": 59, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "How many real solutions does the equation x^2 + 6x + 10 = 0 have?",
 "options": {"A": "Two distinct real solutions", "B": "Exactly one real solution", "C": "Infinitely many real solutions", "D": "No real solutions"},
 "answer": "D"},

{"id": 60, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is sqrt(75) + sqrt(27) in simplest radical form?",
 "options": {"A": "8*sqrt(3)", "B": "4*sqrt(21)", "C": "2*sqrt(21)", "D": "sqrt(102)"},
 "answer": "A"},

{"id": 61, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Unit Conversion", "difficulty": "Easy",
 "question": "A car consumes fuel at a rate of 6 litres per 100 kilometres. How many litres will it consume on a 500-kilometre journey at that rate?",
 "options": {"A": "28", "B": "30", "C": "32", "D": "34"},
 "answer": "B"},

{"id": 62, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Two-Variable Data Interpretation (tables/graphs)", "difficulty": "Medium",
 "question": "A shop records the number of units sold on each of five days: Monday 25, Tuesday 33, Wednesday 24, Thursday 36, Friday 39. By what percentage did the number of units sold increase from Wednesday to Thursday?",
 "options": {"A": "40%", "B": "45%", "C": "50%", "D": "55%"},
 "answer": "C"},

{"id": 63, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "For the data set 3, 5, 5, 8, 9, what is the mean minus the median?",
 "options": {"A": "0", "B": "1", "C": "2", "D": "3"},
 "answer": "B"},

{"id": 64, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "After a 25% discount, an item sells for Rs. 2,250. What was its price before the discount, in rupees?",
 "options": {"A": "3,000", "B": "2,900", "C": "2,800", "D": "3,100"},
 "answer": "A"},

{"id": 65, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Medium",
 "question": "A cube has a volume of 1,000 cubic centimetres. What is its total surface area, in square centimetres?",
 "options": {"A": "600", "B": "500", "C": "550", "D": "1,000"},
 "answer": "A"},

{"id": 66, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Easy",
 "question": "The three interior angles of a triangle are in the ratio 5 : 6 : 7. What is the measure of the largest angle, in degrees?",
 "options": {"A": "60", "B": "70", "C": "65", "D": "75"},
 "answer": "B"},

{"id": 67, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Medium",
 "question": "A sector of a circle of radius 6 cm has a central angle of 60 degrees. What is the area of the sector, in square centimetres?",
 "options": {"A": "6pi", "B": "3pi", "C": "12pi", "D": "36pi"},
 "answer": "A"},

{"id": 68, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Identities", "difficulty": "Medium",
 "question": "For any angle theta with cos(theta) defined and not equal to 0, which expression is equivalent to tan(theta) * cos(theta)?",
 "options": {"A": "sin(theta)", "B": "cos(theta)", "C": "1", "D": "sec(theta)"},
 "answer": "A"},

{"id": 69, "section": 4, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Easy",
 "question": "What is the sum of all prime numbers strictly between 80 and 90?",
 "options": {"A": "160", "B": "168", "C": "172", "D": "176"},
 "answer": "C"},

# ============================================================
# SECTION 5 - VERBAL (17) - q70-86
# ============================================================

{"id": 70, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "The auditor's report was notable for its ____: it traced every rupee of the relief fund from donor to final recipient. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "brevity", "B": "ambiguity", "C": "leniency", "D": "thoroughness"},
 "answer": "D"},

{"id": 71, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: A single centralised matriculation exam, machine-graded, is the fairest way to rank students because it removes any individual teacher's bias from the process. Text 2: Removing a teacher's bias from grading does not remove bias from the process; it simply relocates that bias to whoever decided which topics the exam would cover and which skills a machine could be trusted to score. The author of Text 2 would most likely characterise Text 1's claim about removing bias as",
 "options": {"A": "false, because teachers still grade the exam by hand.",
             "B": "correct, and sufficient reason to keep the exam unchanged.",
             "C": "accurate about the grading step but incomplete about where bias still enters the process.",
             "D": "irrelevant, because topic selection has no measurable effect on outcomes."},
 "answer": "C"},

{"id": 72, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: The Shahi Hamam in Lahore's Walled City is usually valued for its age, having stood for roughly four centuries. The more consequential fact is its continuous public use: unlike many Mughal-era bathhouses abandoned once their original purpose passed, the Shahi Hamam has been restored and reopened rather than converted into a private building, which is why its original frescoes survive largely intact. Which choice best states the main idea of the passage?",
 "options": {"A": "The Shahi Hamam's chief significance lies in its continuous restoration and public use rather than simply its age.",
             "B": "The Shahi Hamam has stood empty and abandoned for most of its history.",
             "C": "The Shahi Hamam's frescoes were destroyed long ago.",
             "D": "The Shahi Hamam was converted into a private residence."},
 "answer": "A"},

{"id": 73, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A city introduced a dedicated bus lane along a single busy corridor. In the first year, average car speeds on that corridor rose by 11 per cent. Over the same period, traffic on the parallel side streets rose by 16 per cent. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "the bus lane had no effect on traffic patterns.",
             "B": "total citywide traffic fell by roughly 11 per cent.",
             "C": "at least part of the speed gain on the corridor reflects drivers diverting to side streets rather than a genuine reduction in total traffic.",
             "D": "drivers on the side streets were unaware of the bus lane."},
 "answer": "C"},

{"id": 74, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A district health office claims its new triage system reduced wait times more for trauma cases than for routine check-ups. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Average wait for trauma cases fell by 22 minutes, while wait for routine check-ups fell by 3 minutes.",
             "B": "The office's overall average wait fell by 12 minutes.",
             "C": "Routine check-ups had the shortest waits both before and after the change.",
             "D": "Staffing levels rose across every department during the study period."},
 "answer": "A"},

{"id": 75, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student compiles three observations about Mohatta Palace in Karachi: it was built in the early 20th century as a private summer residence; it later became a government building for some decades; and it now operates as a public art and cultural museum. Which statement best synthesises these observations?",
 "options": {"A": "Built in the early 20th century as a private summer residence, Mohatta Palace later served as a government building before becoming today's public art and cultural museum.",
             "B": "Mohatta Palace was built specifically to be a museum.",
             "C": "Mohatta Palace has remained a private residence throughout its history.",
             "D": "Mohatta Palace predates the 20th century."},
 "answer": "A"},

{"id": 76, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "The provincial forestry department digitised its decades of tree-survey logs over a three-year project. ____ a district officer in Chitral can now check planting records that once required a personal visit to a single archive in Peshawar. Which transition best completes the text?",
 "options": {"A": "Nevertheless,", "B": "Admittedly,", "C": "By comparison,", "D": "As a result,"},
 "answer": "D"},

{"id": 77, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: the Shandur Polo Festival began as an informal match between two valleys; it now draws teams and spectators from across the country over several days; the ground sits at over 12,000 feet, among the highest polo grounds in the world; the event has been held nearly every summer since the mid-20th century. The student wants to emphasise the festival's growth from an informal local match into a major public draw. Which choice best accomplishes this goal?",
 "options": {"A": "The Shandur Polo Festival has been held nearly every summer since the mid-20th century.",
             "B": "What began as an informal match between two valleys now draws teams and spectators from across the country over several days at one of the world's highest polo grounds.",
             "C": "The polo ground sits at over 12,000 feet.",
             "D": "The event draws spectators from across the country each year."},
 "answer": "B"},

{"id": 78, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The tribunal's findings ____ released in December, prompted an immediate response from three departments. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ": ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 79, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "Every one of the surveyed cotton farmers reported that ____ water allocation had been cut at least once that season. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "their", "B": "it's", "C": "its", "D": "whose"},
 "answer": "A"},

{"id": 80, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Restored and reopened after decades of disuse, ____\"",
 "options": {"A": "historians regard the Shahi Hamam as an architectural landmark.",
             "B": "the hamam's frescoes are what most visitors remember.",
             "C": "the Shahi Hamam still occupies the same courtyard it always has.",
             "D": "it is the courtyard that the Shahi Hamam occupies."},
 "answer": "C"},

{"id": 81, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The report praised the cooperative's fair pricing, its trained field staff, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "it paid farmers promptly.",
             "B": "that its payments were prompt.",
             "C": "paying farmers promptly.",
             "D": "the promptness of its payments to farmers."},
 "answer": "D"},

{"id": 82, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Hard",
 "question": "Neither the curator nor the two research assistants ____ available to open the archive that week. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "was", "B": "is", "C": "has been", "D": "were"},
 "answer": "D"},

{"id": 83, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Hard",
 "question": "Passage: For decades Faisalabad's power-loom operators have blamed their limited access to premium export markets on the cost of imported yarn and on foreign compliance audits, and both complaints are real. Neither explains why so many mills still export uncertified basic fabric while competitors in other countries, facing similar input costs, export fabric certified for use by major European retailers. That gap is not chiefly on the loom floor. It is in dye-lot traceability, effluent-treatment records, and the paperwork that a buyer in Germany now expects before it will place an order at all. Which choice best states the main idea of the passage?",
 "options": {"A": "Yarn costs and compliance audits are the chief obstacles facing Faisalabad's exporters.",
             "B": "The industry's limited access to premium markets is better explained by gaps in traceability and compliance documentation than by input costs alone.",
             "C": "Competitors in other countries pay lower yarn costs than Faisalabad mills do.",
             "D": "Faisalabad should stop exporting basic fabric altogether."},
 "answer": "B"},

{"id": 84, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: For decades Faisalabad's power-loom operators have blamed their limited access to premium export markets on the cost of imported yarn and on foreign compliance audits, and both complaints are real. Neither explains why so many mills still export uncertified basic fabric while competitors in other countries, facing similar input costs, export fabric certified for use by major European retailers. That gap is not chiefly on the loom floor. It is in dye-lot traceability, effluent-treatment records, and the paperwork that a buyer in Germany now expects before it will place an order at all. It can most reasonably be inferred that the author would agree with which statement?",
 "options": {"A": "Lowering yarn costs alone would move Faisalabad mills into premium export markets.",
             "B": "Complaints about compliance audits are fabricated by the industry.",
             "C": "Building stronger traceability and effluent-record systems would address a gap that input-cost relief cannot.",
             "D": "Faisalabad mills are technically less capable than their European competitors."},
 "answer": "C"},

{"id": 85, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as ASTUTE.",
 "options": {"A": "foolish", "B": "shrewd", "C": "careless", "D": "naive"},
 "answer": "B"},

{"id": 86, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The manager's response to the proposal was carefully GUARDED,\" the word \"guarded\" most nearly means",
 "options": {"A": "protected by security.", "B": "cautious rather than open.", "C": "financially risky.", "D": "legally mandated."},
 "answer": "B"},

# ============================================================
# SECTION 6 - MATH (17) - q87-103
# ============================================================

{"id": 87, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Medium",
 "question": "If x/4 - 5 = x/12, what is the value of x?",
 "options": {"A": "24", "B": "27", "C": "30", "D": "33"},
 "answer": "C"},

{"id": 88, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Hard",
 "question": "In an arithmetic sequence the 5th term is 18 and the 10th term is 38. What is the first term?",
 "options": {"A": "-2", "B": "0", "C": "2", "D": "4"},
 "answer": "C"},

{"id": 89, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "A taxi charges a fixed Rs. 100 plus Rs. 35 for every kilometre travelled. A journey costs Rs. 485. How many kilometres was the journey?",
 "options": {"A": "9", "B": "10", "C": "11", "D": "12"},
 "answer": "C"},

{"id": 90, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Easy",
 "question": "What is the sum of the solutions of x^2 - 14x + 13 = 0?",
 "options": {"A": "13", "B": "-14", "C": "-13", "D": "14"},
 "answer": "D"},

{"id": 91, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "If log(x) = 5, where log denotes the base-10 logarithm, what is the value of log(1000x)?",
 "options": {"A": "8", "B": "9", "C": "5000", "D": "80000"},
 "answer": "A"},

{"id": 92, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "For all x other than 5 and -3, which expression is equivalent to (x^2 - 25) / (x^2 - 2x - 15)?",
 "options": {"A": "(x - 5)/(x + 3)", "B": "(x + 5)/(x - 3)", "C": "3", "D": "(x + 5)/(x + 3)"},
 "answer": "D"},

{"id": 93, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Medium",
 "question": "Four identical machines together produce 600 units in 3 hours. Working at the same rate, how many units would 6 such machines produce in 5 hours?",
 "options": {"A": "1,200", "B": "1,350", "C": "1,500", "D": "1,650"},
 "answer": "C"},

{"id": 94, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "The mean of nine numbers is 26. When one of the numbers is removed, the mean of the remaining eight is 24. What was the number that was removed?",
 "options": {"A": "32", "B": "38", "C": "42", "D": "46"},
 "answer": "C"},

{"id": 95, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A fair six-sided die is rolled twice. What is the probability that the two results add up to 6?",
 "options": {"A": "1/9", "B": "5/36", "C": "1/6", "D": "7/36"},
 "answer": "B"},

{"id": 96, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "Set M is {15, 15, 15, 15, 15} and Set N is {5, 10, 15, 20, 25}. Both sets have a mean of 15. Which set has the larger standard deviation?",
 "options": {"A": "Set M", "B": "They are equal", "C": "It cannot be determined from the information given", "D": "Set N"},
 "answer": "D"},

{"id": 97, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A square and an equilateral triangle each have a perimeter of 96 cm. By how many centimetres does the triangle's side exceed the square's side?",
 "options": {"A": "6", "B": "7", "C": "8", "D": "9"},
 "answer": "C"},

{"id": 98, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Easy",
 "question": "A right circular cylinder has a radius of 5 cm and a height of 9 cm. What is its volume, in cubic centimetres?",
 "options": {"A": "225pi", "B": "180pi", "C": "150pi", "D": "90pi"},
 "answer": "A"},

{"id": 99, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Medium",
 "question": "Two parallel lines are cut by a transversal. One of the two interior angles on the same side of the transversal measures 110 degrees. What is the measure, in degrees, of the other?",
 "options": {"A": "70", "B": "110", "C": "90", "D": "80"},
 "answer": "A"},

{"id": 100, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Medium",
 "question": "In a 30-60-90 right triangle, the shorter leg measures 5 cm. What is the length of the hypotenuse, in centimetres?",
 "options": {"A": "10", "B": "5*sqrt(3)", "C": "10*sqrt(3)", "D": "7.5"},
 "answer": "A"},

{"id": 101, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Number Properties (odd/even, divisibility)", "difficulty": "Easy",
 "question": "If n is an odd integer, which of the following must be even?",
 "options": {"A": "n^2", "B": "3n", "C": "n + 5", "D": "5n"},
 "answer": "C"},

{"id": 102, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the smallest positive integer that is divisible by 6, 9 and 10?",
 "options": {"A": "90", "B": "180", "C": "60", "D": "120"},
 "answer": "A"},

{"id": 103, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Medium",
 "question": "Which of the following is NOT a prime number?",
 "options": {"A": "83", "B": "87", "C": "89", "D": "97"},
 "answer": "B"},

# ============================================================
# SECTION 7 - VERBAL (17) - q104-120
# ============================================================

{"id": 104, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Easy",
 "question": "The dean's circular was strikingly ____: it gave the revised fee schedule and the payment deadline and nothing else. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "vague", "B": "lengthy", "C": "evasive", "D": "concise"},
 "answer": "D"},

{"id": 105, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Every retrospective on Pakistani hockey lists the Olympic medals. The list is accurate. But it hides the more interesting fact, which is that the sport's dominant decades coincided almost exactly with a handful of departmental teams that could offer players a salaried job for life -- and that it was that job security, not any one generation's talent alone, that explains the run of medals.\" Which choice best describes the function of the final clause in the text as a whole?",
 "options": {"A": "It withdraws a claim made earlier in the text.",
             "B": "It supplies statistical evidence for the first sentence.",
             "C": "It concedes that the medal list is factually wrong.",
             "D": "It states the specific point the author believes the conventional account obscures."},
 "answer": "D"},

{"id": 106, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: For years the provincial government has offered a fixed subsidised rate for tube-well electricity used on wheat fields, well below what the same electricity would cost an orchard nearby. The policy works: farmers keep planting wheat even in years when the market price is weak. It also works too well: land suited to higher-value orchards stays under wheat, because wheat is the one crop whose electricity cost a farmer can count on regardless of the season. Which choice best states the main idea of the passage?",
 "options": {"A": "The subsidised electricity rate has failed to keep farmers planting wheat.",
             "B": "By keeping electricity costs low for wheat alone, the subsidy succeeds at its aim while locking land into a lower-value crop.",
             "C": "Orchards use less electricity than wheat fields in every district.",
             "D": "Tube-well electricity rates have remained unchanged for decades."},
 "answer": "B"},

{"id": 107, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A publisher reissued a set of regional folktale collections in two versions identical except for a foreword by a locally known storyteller: included on some copies, omitted from others. Copies with the foreword sold 21 per cent more in regions where that storyteller already had a following. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "readers prefer folktale collections with no foreword at all.",
             "B": "how visibly a locally known storyteller is featured can affect how many copies are bought.",
             "C": "the foreword made the folktales more accurately transcribed.",
             "D": "folktale collections sell better than novels in general."},
 "answer": "B"},

{"id": 108, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "A critic argues that the poet Parveen Shakir deliberately centres intimate, private emotion rather than public political statement even when her poems touch on broader social expectations. Which description of a poem's content, if accurate, would most directly support that argument?",
 "options": {"A": "The poem opens with a detailed account of a political rally and its aftermath.",
             "B": "The poem addresses a broken engagement through a single image of a closed window rather than any public commentary.",
             "C": "A narrator delivers an extended speech summarising national politics.",
             "D": "The poem closes with a description of a parliamentary session with no personal voice at all."},
 "answer": "B"},

{"id": 109, "section": 7, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "Domestic wheat production fell for two consecutive seasons, and several flour mills cut operating hours. ____ the country's rice exports rose sharply, offsetting some of the agricultural sector's overall decline. Which transition best completes the text?",
 "options": {"A": "Therefore,", "B": "For example,", "C": "In conclusion,", "D": "Meanwhile,"},
 "answer": "D"},

{"id": 110, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The first phase of the canal-lining project finished on schedule ____ the second phase ran nearly eight months behind. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ", also ", "C": " which ", "D": "; "},
 "answer": "D"},

{"id": 111, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Easy",
 "question": "Because the mountain pass had been closed by early snowfall ____ supplies were flown in by helicopter for nearly a month. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; ", "C": ". ", "D": ": "},
 "answer": "A"},

{"id": 112, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which version of the sentence most clearly means that the scholarship pays for tuition and for nothing else?",
 "options": {"A": "The scholarship only covers tuition.",
             "B": "Only the scholarship covers tuition.",
             "C": "The scholarship covers only tuition.",
             "D": "The scholarship covers tuition only for first-year students."},
 "answer": "C"},

{"id": 113, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: When the highway bypass opened around the old town of Uch Sharif, several roadside shops that had depended on through-traffic were relocated to a new commercial plaza with proper parking and covered walkways -- amenities the old roadside stretch had never had. Officials have cited the new plaza as proof that the relocation helped local shopkeepers. Trader surveys complicate that reading: footfall at the plaza depends on travellers choosing to exit the highway at all, something few did in the plaza's first two years, and several shopkeepers report that their effective income has fallen even though their premises have visibly improved. A plaza that looks better in tile and glass can still leave a shopkeeper worse off than before, if the relocation was measured only in square footage and not in what a shop could still earn. Which choice best states the main idea of the passage?",
 "options": {"A": "The relocation has improved every measurable aspect of shopkeepers' businesses.",
             "B": "Improved premises at the new plaza may conceal a decline in footfall-based income that facility quality alone does not capture.",
             "C": "Highway traffic has increased sharply through the old roadside stretch.",
             "D": "Most of the original roadside shops had covered walkways before relocation."},
 "answer": "B"},

{"id": 114, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: When the highway bypass opened around the old town of Uch Sharif, several roadside shops that had depended on through-traffic were relocated to a new commercial plaza with proper parking and covered walkways -- amenities the old roadside stretch had never had. Officials have cited the new plaza as proof that the relocation helped local shopkeepers. Trader surveys complicate that reading: footfall at the plaza depends on travellers choosing to exit the highway at all, something few did in the plaza's first two years, and several shopkeepers report that their effective income has fallen even though their premises have visibly improved. A plaza that looks better in tile and glass can still leave a shopkeeper worse off than before, if the relocation was measured only in square footage and not in what a shop could still earn. According to the passage, what amenities did the new commercial plaza include?",
 "options": {"A": "Proper parking and covered walkways.",
             "B": "Only proper parking, with no other facilities.",
             "C": "Direct highway access for every shop.",
             "D": "The passage does not say."},
 "answer": "A"},

{"id": 115, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: When the highway bypass opened around the old town of Uch Sharif, several roadside shops that had depended on through-traffic were relocated to a new commercial plaza with proper parking and covered walkways -- amenities the old roadside stretch had never had. Officials have cited the new plaza as proof that the relocation helped local shopkeepers. Trader surveys complicate that reading: footfall at the plaza depends on travellers choosing to exit the highway at all, something few did in the plaza's first two years, and several shopkeepers report that their effective income has fallen even though their premises have visibly improved. A plaza that looks better in tile and glass can still leave a shopkeeper worse off than before, if the relocation was measured only in square footage and not in what a shop could still earn. The author's attitude toward officials' claim that the relocation helped shopkeepers is best characterised as",
 "options": {"A": "fully persuaded.", "B": "openly mocking.", "C": "skeptical, given the survey evidence cited.", "D": "indifferent."},
 "answer": "C"},

{"id": 116, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: When the highway bypass opened around the old town of Uch Sharif, several roadside shops that had depended on through-traffic were relocated to a new commercial plaza with proper parking and covered walkways -- amenities the old roadside stretch had never had. Officials have cited the new plaza as proof that the relocation helped local shopkeepers. Trader surveys complicate that reading: footfall at the plaza depends on travellers choosing to exit the highway at all, something few did in the plaza's first two years, and several shopkeepers report that their effective income has fallen even though their premises have visibly improved. A plaza that looks better in tile and glass can still leave a shopkeeper worse off than before, if the relocation was measured only in square footage and not in what a shop could still earn. It can most reasonably be inferred that the author would support",
 "options": {"A": "measuring the relocation's success by facility quality alone.",
             "B": "closing the highway bypass immediately.",
             "C": "treating the new premises as sufficient compensation regardless of lost income.",
             "D": "assessing the relocation's outcomes by shopkeeper income and footfall, not facility quality alone."},
 "answer": "D"},

{"id": 117, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The fellowship is open to applicants who have completed a relevant degree, who have published research in the field, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "having two academic references.",
             "B": "two academic references.",
             "C": "they have two academic references.",
             "D": "who have two academic references."},
 "answer": "D"},

{"id": 118, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as ASSIDUOUS.",
 "options": {"A": "lazy", "B": "hardworking", "C": "careless", "D": "impulsive"},
 "answer": "B"},

{"id": 119, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to PROSPERITY.",
 "options": {"A": "poverty", "B": "surplus", "C": "wealth", "D": "growth"},
 "answer": "A"},

{"id": 120, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The revised policy did little to CHECK illegal timber felling in the reserve,\" the word \"check\" most nearly means",
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
#      bank and from Mocks 1, 3 and 4. That tuple (with past_paper) is
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
    for modname in ("lums_mock_01", "lums_mock_02", "lums_mock_03", "lums_mock_04", "lums_mock_05"):
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