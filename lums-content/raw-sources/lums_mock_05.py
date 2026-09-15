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
and the earlier mocks.

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
 "question": "The restoration team working on Hunza's Baltit Fort used entirely ____ materials wherever possible, replacing crumbling mud-brick with mud-brick mixed to the original nineteenth-century recipe rather than modern cement. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "synthetic", "B": "experimental", "C": "imported", "D": "traditional"},
 "answer": "D"},

{"id": 2, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Medium",
 "question": "Text: \"Sialkot's surgical-instrument industry is routinely described as a colonial leftover, a trade the British happened to start and locals happened to keep going. The description undersells what actually happened next: local workshops re-engineered instruments to meet European sterilisation standards decades after the British left, and it is that adaptation, not colonial inheritance, that explains the industry's continued export success.\" Which choice best describes the function of the second sentence in the text as a whole?",
 "options": {"A": "It concedes that the conventional description is entirely accurate.",
             "B": "It offers an example confirming the first sentence.",
             "C": "It corrects the conventional description by identifying a later adaptation as the real explanation for success.",
             "D": "It summarises a scholarly consensus the author endorses."},
 "answer": "C"},

{"id": 3, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: Resettling fishing families away from Gwadar's old town to purpose-built housing gives them modern infrastructure -- piped water, paved roads, reliable electricity -- that their original settlement never had. Text 2: Modern infrastructure is little comfort to families moved kilometres from the harbour where their boats are moored; a fisherman who can no longer walk to his boat before dawn has lost his livelihood, however good his new water pipes are. Based on the texts, how would the author of Text 2 most likely respond to Text 1's claim about the infrastructure improvement?",
 "options": {"A": "By agreeing fully that infrastructure is what matters most to fishing families.",
             "B": "By arguing that the infrastructure gain is real but doesn't offset the loss of practical access to the harbour that the move causes.",
             "C": "By denying that any new infrastructure was actually built.",
             "D": "By conceding that the resettlement has had no economic effect at all."},
 "answer": "B"},

{"id": 4, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Easy",
 "question": "Passage: Balochistan's Ziarat juniper forest is often cited simply as the world's second-largest, a fact that says nothing about age. Some of its trees are estimated at over a thousand years old, growing barely a millimetre in girth in some years because the surrounding soil holds so little water. Loggers who once cleared junipers for firewood were, without realising it, cutting trees older than any building in the province; a single mature tree, once felled, cannot be meaningfully replaced within a human lifetime. What is the main idea of the passage?",
 "options": {"A": "The Ziarat juniper forest is the largest juniper forest in the world.",
             "B": "Juniper wood is unsuitable for construction.",
             "C": "Firewood collection in Ziarat has stopped completely in recent years.",
             "D": "The forest's slow growth means felled ancient junipers represent a loss no lifetime of replanting can restore."},
 "answer": "D"},

{"id": 5, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: Over a twelve-year period, the number of registered camel-milk dairies in Tharparkar roughly tripled, while the share of camel milk reaching organised retail chains barely grew. Most of the new dairies sold directly to nearby households and small shops rather than investing in the chilling and packaging equipment retail chains require. Which choice most logically completes the reasoning in the passage?",
 "options": {"A": "Therefore, camel-milk retail chains are likely to disappear within the decade.",
             "B": "Therefore, the growth in dairies appears to have expanded informal local sales without closing the gap that keeps camel milk out of organised retail.",
             "C": "Therefore, Tharparkar's camel-milk dairies mainly export their product abroad.",
             "D": "Therefore, chilling equipment has become standard practice across the industry."},
 "answer": "B"},

{"id": 6, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A researcher claims that a district's rise in total citrus exports was driven more by an increase in orchard area than by any improvement in yield per hectare. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Exports rose 36%, while orchard area rose 33% and yield per hectare rose 2%.",
             "B": "Exports rose 36%, while orchard area rose 6% and yield per hectare rose 28%.",
             "C": "Exports fell 4%, while orchard area rose 33%.",
             "D": "Exports rose 36%, and the international price of citrus fell 8%."},
 "answer": "A"},

{"id": 7, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "While researching Sialkot's sports-goods cluster, a student compiles three notes: workshops there stitch footballs for several major international tournaments; most stitching is still done by hand rather than machine; and the cluster grew out of small family workshops rather than a single large factory, and buyers audit workshops directly for labour conditions. Which statement best synthesises these notes?",
 "options": {"A": "Sialkot's sports-goods cluster, built from small family workshops rather than one large factory, still hand-stitches footballs for major tournaments under direct buyer audits.",
             "B": "Sialkot's football stitching is done entirely by machine.",
             "C": "International buyers rarely audit Sialkot's workshops.",
             "D": "Sialkot's sports-goods cluster began as a single large state-owned factory."},
 "answer": "A"},

{"id": 8, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "Battery-powered rickshaws spread quickly across smaller Punjab towns once import duties on the batteries were cut. ____ the informal charging stations that sprang up to serve them draw power through unmetered connections, and several towns have reported unexplained spikes in transmission losses since. Which transition best completes the text?",
 "options": {"A": "Similarly,", "B": "For example,", "C": "Consequently,", "D": "In addition,"},
 "answer": "C"},

{"id": 9, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: rilli quilt-making in Sindh uses small triangular and diamond patches cut from worn-out cloth; a single large rilli can take a group of women several weeks working together to finish; the craft has traditionally been a communal rather than solitary activity; finished quilts are used at home and increasingly sold to urban buyers. The student wants to emphasise the craft's communal, collaborative nature. Which choice best accomplishes this goal?",
 "options": {"A": "Rilli quilts are pieced from small triangular and diamond patches cut from worn-out cloth.",
             "B": "Rilli quilts have long been used inside the home.",
             "C": "Rilli quilts are increasingly sold to urban buyers today.",
             "D": "A large rilli traditionally takes a group of women several weeks of shared work to finish, reflecting the craft's communal rather than solitary character."},
 "answer": "D"},

{"id": 10, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "The set of nineteenth-century revenue records held at the provincial archive ____ several volumes never previously catalogued. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "include", "B": "are including", "C": "includes", "D": "have include"},
 "answer": "C"},

{"id": 11, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "The orchard growers rejected the new pesticide-spraying schedule, and ____ objections were later raised with the agriculture department. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "its", "B": "their", "C": "it's", "D": "there"},
 "answer": "B"},

{"id": 12, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The survey team reached one firm conclusion ____ the juniper stand had not been logged in at least four decades. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", that", "B": ", being", "C": "; which", "D": ": "},
 "answer": "D"},

{"id": 13, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Medium",
 "question": "The ferry had crossed Manchar Lake twice daily for decades ____ operators suspended the route after water levels dropped sharply last year. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "; ", "B": ", ", "C": " which ", "D": " and which "},
 "answer": "A"},

{"id": 14, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Having studied the acoustics of Thatta's Shah Jahan Mosque for two seasons, ____\"",
 "options": {"A": "the conclusion of the researchers was that the tiled domes amplified a reciter's voice without any electronic aid.",
             "B": "it was concluded by the researchers that the tiled domes amplified a reciter's voice without any electronic aid.",
             "C": "the researchers concluded that the tiled domes amplified a reciter's voice without any electronic aid.",
             "D": "amplification was shown by the researchers to occur without any electronic aid."},
 "answer": "C"},

{"id": 15, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: Peshawar's Qissa Khwani Bazaar translates roughly as the Storytellers' Bazaar, a name usually explained as a nod to caravan travellers who once gathered there to swap news along the trade routes. The name undersells what the bazaar still does: shopkeepers there continue to trade in news as much as goods, and a rumour about tomorrow's wheat price can move through its lanes faster than any newspaper could carry it. Read that way, the bazaar's oldest function has not faded into history; it has simply kept pace with what there is to trade. Which choice best states the main idea of the passage?",
 "options": {"A": "Qissa Khwani Bazaar has abandoned its historical role as a centre for news.",
             "B": "The bazaar's traditional role as a place where news travels quickly has persisted alongside its trade in goods.",
             "C": "The bazaar's name has no connection to its actual function today.",
             "D": "Newspapers have replaced the bazaar as the primary source of local news."},
 "answer": "B"},

{"id": 16, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: Peshawar's Qissa Khwani Bazaar translates roughly as the Storytellers' Bazaar, a name usually explained as a nod to caravan travellers who once gathered there to swap news along the trade routes. The name undersells what the bazaar still does: shopkeepers there continue to trade in news as much as goods, and a rumour about tomorrow's wheat price can move through its lanes faster than any newspaper could carry it. Read that way, the bazaar's oldest function has not faded into history; it has simply kept pace with what there is to trade. The author's attitude toward the conventional explanation of the bazaar's name is best characterised as",
 "options": {"A": "openly contemptuous.", "B": "mildly corrective.", "C": "entirely neutral.", "D": "wistfully nostalgic."},
 "answer": "B"},

{"id": 17, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as TENACIOUS.",
 "options": {"A": "fickle", "B": "careless", "C": "timid", "D": "persistent"},
 "answer": "D"},

{"id": 18, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to the underlined word as it is used here: \"The negotiator's manner throughout the talks was notably CONCILIATORY.\"",
 "options": {"A": "confrontational", "B": "brief", "C": "informal", "D": "private"},
 "answer": "A"},

# ============================================================
# SECTION 2 - MATH (17) - q19-35
# ============================================================

{"id": 19, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Easy",
 "question": "If 5(x - 2) + 6 = 3x + 10, what is the value of x?",
 "options": {"A": "5", "B": "6", "C": "7", "D": "8"},
 "answer": "C"},

{"id": 20, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 3x + 2y = 23 and x - y = 1, what is the value of x?",
 "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
 "answer": "C"},

{"id": 21, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "Which of the following describes all values of x for which 9 - 4x > 17?",
 "options": {"A": "x > -2", "B": "x < 2", "C": "x > 2", "D": "x < -2"},
 "answer": "D"},

{"id": 22, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Medium",
 "question": "An arithmetic sequence has first term 6 and common difference 3. What is the sum of its first 18 terms?",
 "options": {"A": "567", "B": "540", "C": "594", "D": "513"},
 "answer": "A"},

{"id": 23, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "The equation x^2 + kx + 21 = 0 has roots 3 and 7. What is the value of k?",
 "options": {"A": "-10", "B": "10", "C": "-21", "D": "21"},
 "answer": "A"},

{"id": 24, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is the value of 25^(3/2) * 4^(1/2)?",
 "options": {"A": "125", "B": "200", "C": "250", "D": "500"},
 "answer": "C"},

{"id": 25, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "What is the value of (log_5 125) - (log_2 16)?",
 "options": {"A": "-1", "B": "1", "C": "7", "D": "-7"},
 "answer": "A"},

{"id": 26, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "If 1/x + 1/(5x) = 3/5, what is the value of x?",
 "options": {"A": "1", "B": "3/2", "C": "2", "D": "3"},
 "answer": "C"},

{"id": 27, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "A shopkeeper raises the price of an item by 40% and then, in a sale, reduces the new price by 30%. Compared with the original price, the final price is",
 "options": {"A": "2% higher.", "B": "2% lower.", "C": "unchanged.", "D": "10% lower."},
 "answer": "B"},

{"id": 28, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Easy",
 "question": "A sum of Rs. 96,000 is divided between two partners in the ratio 3 : 5. By how much does the larger share exceed the smaller share, in rupees?",
 "options": {"A": "18,000", "B": "20,000", "C": "24,000", "D": "28,000"},
 "answer": "C"},

{"id": 29, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "A class of 16 students has a mean score of 70. Four more students, whose mean score is 90, join the class. What is the mean score of all 20 students?",
 "options": {"A": "72", "B": "78", "C": "76", "D": "74"},
 "answer": "D"},

{"id": 30, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A bag contains 4 red marbles and 6 blue marbles. Two marbles are drawn at random without replacement. What is the probability that both are blue?",
 "options": {"A": "1/3", "B": "2/5", "C": "3/10", "D": "1/5"},
 "answer": "A"},

{"id": 31, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A rectangle has a perimeter of 42 cm, and its length is 5 cm greater than its width. What is its area, in square centimetres?",
 "options": {"A": "96", "B": "104", "C": "112", "D": "91"},
 "answer": "B"},

{"id": 32, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Easy",
 "question": "A right triangle has legs of length 7 cm and 24 cm. What is its perimeter, in centimetres?",
 "options": {"A": "50", "B": "52", "C": "56", "D": "60"},
 "answer": "C"},

{"id": 33, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Easy",
 "question": "A circle has an area of 81pi square centimetres. What is its circumference, in centimetres?",
 "options": {"A": "9pi", "B": "36pi", "C": "81pi", "D": "18pi"},
 "answer": "D"},

{"id": 34, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Ratios", "difficulty": "Medium",
 "question": "In a right triangle, theta is an acute angle and sin(theta) = 9/41. What is the value of cos(theta)?",
 "options": {"A": "40/41", "B": "9/40", "C": "41/40", "D": "9/41"},
 "answer": "A"},

{"id": 35, "section": 2, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the least common multiple of 10 and 15, minus their greatest common divisor?",
 "options": {"A": "20", "B": "25", "C": "30", "D": "35"},
 "answer": "B"},

# ============================================================
# SECTION 3 - VERBAL (17) - q36-52
# ============================================================

{"id": 36, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "Though marketed as a breakthrough irrigation gadget, the soil-moisture sensor turned out to be largely ____ for smallholders: its readings meant little without a smartphone app that required a data connection few of the villages actually had. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "indispensable", "B": "affordable", "C": "useless", "D": "durable"},
 "answer": "C"},

{"id": 37, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Economists have long modelled remittances from overseas workers as a straightforward substitute for local wages: a household with a migrant abroad simply spends the money it would otherwise have earned at home. The model is elegant, and it predicts unchanged household spending patterns. That is not what repeated surveys of remittance-receiving households in Azad Kashmir show: many of those households shift spending sharply toward home construction and education, categories they had underinvested in before.\" Which choice best describes the function of the final sentence in the text as a whole?",
 "options": {"A": "It supplies an example confirming the model's prediction.",
             "B": "It introduces survey evidence that conflicts with the model's prediction.",
             "C": "It proposes a refinement to make the model more accurate.",
             "D": "It restates the model's claim in more concrete terms."},
 "answer": "B"},

{"id": 38, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: Over two decades, the total number of registered timber mills in Kalam grew only modestly, while the volume of timber they processed each year grew far faster, because newer mills run larger saws and longer shifts than the older ones they gradually replaced. Forestry auditors warn against reading the modest growth in mill numbers as reassuring: the real story is how much more timber a similar number of mills can now cut from the same surrounding forest. Which choice best states the main idea of the passage?",
 "options": {"A": "The number of registered timber mills in Kalam has grown dramatically.",
             "B": "Total mill count is a more important statistic than processing volume.",
             "C": "Older timber mills process more wood than newer ones.",
             "D": "The modest growth in mill numbers understates a much sharper rise in the volume of timber being cut from the surrounding forest."},
 "answer": "D"},

{"id": 39, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: Pakistan's national parks are managed province by province, but the snow leopards that draw the most attention range across territories that straddle several provincial boundaries in a single season, and the same animal is often photographed by camera traps registered to more than one province. It follows that separate provincial snow leopard counts ____ Which choice most logically completes the text?",
 "options": {"A": "should be conducted more often than they currently are.",
             "B": "cannot simply be summed to produce a reliable national total.",
             "C": "will always overstate the true number in each province.",
             "D": "are the only practical way to track the species."},
 "answer": "B"},

{"id": 40, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "In a study of Sehwan Sharif's annual urs festival, a researcher argues that pilgrims value the shrine's dhamaal dance less as formal ritual than as a shared release from ordinary social hierarchy. Which quotation from a pilgrim interview, if authentic, would most directly support that argument?",
 "options": {"A": "\"The dhamaal follows a strict sequence that a trained custodian leads from start to finish.\"",
             "B": "\"When the drums start, nobody asks who you are outside this courtyard -- we all just dance.\"",
             "C": "\"The urs festival draws pilgrims from across the province each year.\"",
             "D": "\"Donations collected during the urs fund the shrine's free kitchen.\""},
 "answer": "B"},

{"id": 41, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student researching Baltit Fort in Hunza records three observations: it was built roughly six centuries ago as the residence of the local mirs (rulers); it was restored in the 1990s using traditional mud-brick and timber techniques rather than modern materials; and it now operates as a museum rather than a residence. Which statement best synthesises these observations?",
 "options": {"A": "Baltit Fort, built roughly six centuries ago as a ruler's residence, was restored in the 1990s using traditional techniques and now operates as a museum.",
             "B": "Baltit Fort was built using modern materials from the outset.",
             "C": "Baltit Fort remains the private residence of Hunza's mirs today.",
             "D": "The 1990s restoration of Baltit Fort used entirely new architectural designs."},
 "answer": "A"},

{"id": 42, "section": 3, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "Lahore's horse-drawn tongas once carried the bulk of short-distance traffic through the old city's narrow lanes. ____ motorised rickshaws, cheaper to run and faster through traffic, have replaced all but a handful of tongas kept mainly for tourists. Which transition best completes the text?",
 "options": {"A": "Consequently,", "B": "In short,", "C": "Similarly,", "D": "By contrast,"},
 "answer": "D"},

{"id": 43, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The programme trains volunteer wardens to monitor glacial lake levels, to maintain the early-warning sirens, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "coordinating evacuation drills with nearby villages.",
             "B": "they coordinate evacuation drills with nearby villages.",
             "C": "to coordinate evacuation drills with nearby villages.",
             "D": "evacuation drills are coordinated with nearby villages."},
 "answer": "C"},

{"id": 44, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The tour covered three stops in Gilgit-Baltistan ____ Baltit Fort, Attabad Lake and the Passu cones. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ": ", "B": ", ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 45, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "Each of the eleven glacial-lake sites ____ monitored by a locally trained warden. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "are", "B": "were", "C": "is", "D": "have been"},
 "answer": "C"},

{"id": 46, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Hard",
 "question": "The spillway was widened in 2016 ____ outburst floods along the same valley have grown more frequent every summer since. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ", however ", "C": " and which ", "D": "; nevertheless, "},
 "answer": "D"},

{"id": 47, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: Sindh's community-managed game reserves were set up on a simple bargain: villages that once poached urial and ibex for meat would instead protect the herds and earn income from a small number of permitted trophy hunts sold to outside hunters each season. On paper the arrangement has worked -- herd counts in the reserves have risen steadily since the programme began. Wildlife economists caution that the recovery rests on a narrower base than the herd numbers suggest: nearly all of the reserves' conservation budget comes from a handful of high-value permits sold in a single short hunting season, and a bad season, whether from fewer hunters travelling or a change in export rules for trophies, would remove most of the funding that pays for anti-poaching patrols the rest of the year. Which choice best states the main idea of the passage?",
 "options": {"A": "Sindh's community game reserves have failed to increase urial and ibex populations.",
             "B": "Rising herd counts conceal how dependent the reserves' conservation funding is on a small, potentially fragile hunting-permit income.",
             "C": "Poaching has been eliminated entirely from Sindh's community reserves.",
             "D": "Trophy hunting permits are sold year-round in Sindh's reserves."},
 "answer": "B"},

{"id": 48, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: Sindh's community-managed game reserves were set up on a simple bargain: villages that once poached urial and ibex for meat would instead protect the herds and earn income from a small number of permitted trophy hunts sold to outside hunters each season. On paper the arrangement has worked -- herd counts in the reserves have risen steadily since the programme began. Wildlife economists caution that the recovery rests on a narrower base than the herd numbers suggest: nearly all of the reserves' conservation budget comes from a handful of high-value permits sold in a single short hunting season, and a bad season, whether from fewer hunters travelling or a change in export rules for trophies, would remove most of the funding that pays for anti-poaching patrols the rest of the year. According to the passage, where does nearly all of the reserves' conservation budget come from?",
 "options": {"A": "A handful of high-value trophy-hunting permits sold in a single short season.",
             "B": "Annual government grants.",
             "C": "International conservation charities.",
             "D": "Entry fees paid by ordinary tourists."},
 "answer": "A"},

{"id": 49, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: Sindh's community-managed game reserves were set up on a simple bargain: villages that once poached urial and ibex for meat would instead protect the herds and earn income from a small number of permitted trophy hunts sold to outside hunters each season. On paper the arrangement has worked -- herd counts in the reserves have risen steadily since the programme began. Wildlife economists caution that the recovery rests on a narrower base than the herd numbers suggest: nearly all of the reserves' conservation budget comes from a handful of high-value permits sold in a single short hunting season, and a bad season, whether from fewer hunters travelling or a change in export rules for trophies, would remove most of the funding that pays for anti-poaching patrols the rest of the year. The author's attitude toward the reserves' rising herd counts is best characterised as",
 "options": {"A": "fully reassured by them.", "B": "openly dismissive of them.", "C": "cautious about what they may be concealing.", "D": "indifferent to them."},
 "answer": "C"},

{"id": 50, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: Sindh's community-managed game reserves were set up on a simple bargain: villages that once poached urial and ibex for meat would instead protect the herds and earn income from a small number of permitted trophy hunts sold to outside hunters each season. On paper the arrangement has worked -- herd counts in the reserves have risen steadily since the programme began. Wildlife economists caution that the recovery rests on a narrower base than the herd numbers suggest: nearly all of the reserves' conservation budget comes from a handful of high-value permits sold in a single short hunting season, and a bad season, whether from fewer hunters travelling or a change in export rules for trophies, would remove most of the funding that pays for anti-poaching patrols the rest of the year. It can most reasonably be inferred that the author regards the reserves' current funding model as",
 "options": {"A": "diversified enough to withstand a poor hunting season.",
             "B": "vulnerable to disruption because it depends heavily on a narrow, season-limited income source.",
             "C": "irrelevant to whether poaching resumes.",
             "D": "more stable than government-funded conservation programmes."},
 "answer": "B"},

{"id": 51, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as CIRCUMSPECT.",
 "options": {"A": "reckless", "B": "talkative", "C": "generous", "D": "cautious"},
 "answer": "D"},

{"id": 52, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The new export quota will TELL against smaller trophy-hunting operators within a season,\" the word \"tell\" most nearly means",
 "options": {"A": "narrate.", "B": "have a noticeable effect.", "C": "distinguish.", "D": "count aloud."},
 "answer": "B"},

# ============================================================
# SECTION 4 - MATH (17) - q53-69
# ============================================================

{"id": 53, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in Two Variables", "difficulty": "Medium",
 "question": "A line in the xy-plane passes through the points (2, 5) and (6, 21). What is the y-coordinate of its y-intercept?",
 "options": {"A": "-3", "B": "3", "C": "6", "D": "-6"},
 "answer": "A"},

{"id": 54, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "The function f is defined by f(x) = 6x - 11. If f(a) = 25, what is the value of a?",
 "options": {"A": "5", "B": "8", "C": "7", "D": "6"},
 "answer": "D"},

{"id": 55, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 6x + 3y = 33 and 2x - 3y = -1, what is the value of y?",
 "options": {"A": "2", "B": "3", "C": "4", "D": "5"},
 "answer": "B"},

{"id": 56, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "A delivery van weighs 900 kg when empty, and the total weight of the loaded van must not exceed 1,800 kg. If each crate weighs 45 kg, what is the greatest number of whole crates the van can carry?",
 "options": {"A": "18", "B": "19", "C": "20", "D": "21"},
 "answer": "C"},

{"id": 57, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Nonlinear Functions", "difficulty": "Medium",
 "question": "What is the minimum value of the function f(x) = x^2 - 10x + 9?",
 "options": {"A": "-14", "B": "16", "C": "-18", "D": "-16"},
 "answer": "D"},

{"id": 58, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Polynomial Expressions", "difficulty": "Easy",
 "question": "Which expression is equivalent to (5x - 2)(x + 3)?",
 "options": {"A": "5x^2 + 13x - 6", "B": "5x^2 - 13x - 6", "C": "5x^2 + 17x - 6", "D": "5x^2 + 13x + 6"},
 "answer": "A"},

{"id": 59, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "How many real solutions does the equation x^2 + 4x + 8 = 0 have?",
 "options": {"A": "Two distinct real solutions", "B": "Exactly one real solution", "C": "Infinitely many real solutions", "D": "No real solutions"},
 "answer": "D"},

{"id": 60, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is sqrt(48) + sqrt(12) in simplest radical form?",
 "options": {"A": "6*sqrt(3)", "B": "4*sqrt(15)", "C": "2*sqrt(15)", "D": "sqrt(60)"},
 "answer": "A"},

{"id": 61, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Unit Conversion", "difficulty": "Easy",
 "question": "A car consumes fuel at a rate of 5 litres per 100 kilometres. How many litres will it consume on a 380-kilometre journey at that rate?",
 "options": {"A": "17", "B": "21", "C": "19", "D": "15"},
 "answer": "C"},

{"id": 62, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Two-Variable Data Interpretation (tables/graphs)", "difficulty": "Medium",
 "question": "A shop records the number of units sold on each of five days: Monday 30, Tuesday 38, Wednesday 28, Thursday 42, Friday 46. By what percentage did the number of units sold increase from Wednesday to Thursday?",
 "options": {"A": "40%", "B": "45%", "C": "50%", "D": "55%"},
 "answer": "C"},

{"id": 63, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "For the data set 4, 6, 6, 9, 10, what is the mean minus the median?",
 "options": {"A": "0", "B": "3", "C": "2", "D": "1"},
 "answer": "D"},

{"id": 64, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "After a 30% discount, an item sells for Rs. 2,800. What was its price before the discount, in rupees?",
 "options": {"A": "4,000", "B": "3,640", "C": "3,500", "D": "3,800"},
 "answer": "A"},

{"id": 65, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Medium",
 "question": "A cube has a volume of 729 cubic centimetres. What is its total surface area, in square centimetres?",
 "options": {"A": "486", "B": "324", "C": "405", "D": "729"},
 "answer": "A"},

{"id": 66, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Easy",
 "question": "The three interior angles of a triangle are in the ratio 3 : 4 : 5. What is the measure of the largest angle, in degrees?",
 "options": {"A": "60", "B": "65", "C": "75", "D": "80"},
 "answer": "C"},

{"id": 67, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Medium",
 "question": "A sector of a circle of radius 8 cm has a central angle of 90 degrees. What is the area of the sector, in square centimetres?",
 "options": {"A": "16pi", "B": "8pi", "C": "32pi", "D": "64pi"},
 "answer": "A"},

{"id": 68, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Identities", "difficulty": "Medium",
 "question": "For any angle theta with tan(theta) defined and not equal to 0, which expression is equivalent to sin(theta) / tan(theta)?",
 "options": {"A": "sin(theta)", "B": "cos(theta)", "C": "1", "D": "csc(theta)"},
 "answer": "B"},

{"id": 69, "section": 4, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Easy",
 "question": "What is the sum of all prime numbers strictly between 60 and 70?",
 "options": {"A": "120", "B": "124", "C": "128", "D": "132"},
 "answer": "C"},

# ============================================================
# SECTION 5 - VERBAL (17) - q70-86
# ============================================================

{"id": 70, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "The ombudsman's report was notable for its ____: it addressed each of the fourteen citizen complaints in turn, with a separate finding for every one. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "brevity", "B": "ambiguity", "C": "leniency", "D": "thoroughness"},
 "answer": "D"},

{"id": 71, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: A single standardised university entrance test, scored by machine, is the fairest way to select students because it removes any examiner's personal judgment from the process. Text 2: Removing an examiner's judgment does not remove judgment from the process; it simply moves the judgment earlier, into whoever designed which questions to ask and which skills the machine would be permitted to score. The author of Text 2 would most likely characterise Text 1's claim about removing judgment as",
 "options": {"A": "false, because examiners still score the test by hand.",
             "B": "correct, and sufficient reason to keep the test unchanged.",
             "C": "accurate about the scoring step but incomplete about where judgment still enters the process.",
             "D": "irrelevant, because question design has no measurable effect on outcomes."},
 "answer": "C"},

{"id": 72, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: Bala Hisar Fort in Peshawar is usually valued for its age, having occupied the same rise above the city in some form for more than two thousand years. The more consequential fact is its continuous military use: unlike many historic forts that were abandoned once their original purpose passed, Bala Hisar has been garrisoned by every power that has controlled Peshawar since, which is why so little of its interior is open to the public even now. Which choice best states the main idea of the passage?",
 "options": {"A": "Bala Hisar Fort's chief significance lies in its continuous military use rather than simply its age.",
             "B": "Bala Hisar Fort has stood empty and abandoned for most of its history.",
             "C": "Peshawar has never been controlled by more than one power.",
             "D": "Bala Hisar Fort's interior is fully open to public visitors today."},
 "answer": "A"},

{"id": 73, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A city introduced a dedicated cycling lane along a single busy avenue. In the first year, average car speeds on that avenue fell by 9 per cent. Over the same period, traffic on the parallel side streets rose by 14 per cent. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "the cycling lane had no effect on traffic patterns.",
             "B": "total citywide traffic fell by roughly 9 per cent.",
             "C": "at least part of the change on the avenue reflects drivers diverting to side streets rather than driving less overall.",
             "D": "drivers on the side streets were unaware the cycling lane existed."},
 "answer": "C"},

{"id": 74, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A district health office claims its new referral system reduced delays more for maternal emergencies than for routine appointments. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Average referral delay for maternal emergencies fell by 25 minutes, while delay for routine appointments fell by 4 minutes.",
             "B": "The office's overall average referral delay fell by 14 minutes.",
             "C": "Routine appointments had the shortest delays both before and after the change.",
             "D": "Staffing levels rose across every department during the study period."},
 "answer": "A"},

{"id": 75, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student compiles three observations about Frere Hall in Karachi: it was built under British colonial administration as a town hall; its interior ceiling was later painted with a large mural by the artist Sadequain; and the surrounding gardens remain a public park today, while the building itself now mainly houses a public library. Which statement best synthesises these observations?",
 "options": {"A": "Frere Hall, built as a colonial-era town hall, now houses a public library beneath a ceiling mural by Sadequain, set within gardens still open to the public.",
             "B": "Frere Hall was built specifically to display Sadequain's artwork.",
             "C": "The gardens around Frere Hall have been closed to the public since colonial rule ended.",
             "D": "Frere Hall predates British colonial administration in Karachi."},
 "answer": "A"},

{"id": 76, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "The provincial archive digitised its collection of nineteenth-century revenue maps over a five-year project. ____ a researcher in Multan can now examine boundary records that once required a personal visit to a single vault in Lahore. Which transition best completes the text?",
 "options": {"A": "Nevertheless,", "B": "Admittedly,", "C": "By comparison,", "D": "As a result,"},
 "answer": "D"},

{"id": 77, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: the Cholistan Desert Jeep Rally began as a small local motoring event; it now draws competitors and spectators from across the country over several days; the route crosses dunes near the historic Derawar Fort; the event has been held nearly every year since the 1980s. The student wants to emphasise the rally's growth from a local event into a major public draw. Which choice best accomplishes this goal?",
 "options": {"A": "The Cholistan Desert Jeep Rally has been held nearly every year since the 1980s.",
             "B": "What began as a small local motoring event now draws competitors and spectators from across the country over several days near Derawar Fort.",
             "C": "The rally's route crosses dunes near Derawar Fort.",
             "D": "The event draws spectators from across the country each year."},
 "answer": "B"},

{"id": 78, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The tribunal's findings ____ released in November, prompted an immediate response from two departments. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ": ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 79, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "Every one of the interviewed orchard owners reported that ____ irrigation allocation had been cut at least once that year. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "their", "B": "it's", "C": "its", "D": "whose"},
 "answer": "A"},

{"id": 80, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Garrisoned continuously for over two thousand years, ____\"",
 "options": {"A": "historians regard Bala Hisar Fort as a strategic landmark.",
             "B": "the fort's walls are what most visitors remember.",
             "C": "Bala Hisar Fort still overlooks Peshawar from the same rise it always has.",
             "D": "it is Peshawar that Bala Hisar Fort overlooks."},
 "answer": "C"},

{"id": 81, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The report praised the cooperative's fair pricing, its trained staff, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "it paid members promptly.",
             "B": "that its payments were prompt.",
             "C": "paying members promptly.",
             "D": "the promptness of its payments to members."},
 "answer": "D"},

{"id": 82, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Hard",
 "question": "Neither the warden nor the two volunteers ____ available to staff the monitoring post that week. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "was", "B": "is", "C": "has been", "D": "were"},
 "answer": "D"},

{"id": 83, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Hard",
 "question": "Passage: For decades Sialkot's surgical-instrument makers have blamed their limited access to premium export markets on the cost of steel and on foreign certification fees, and both complaints are real. Neither explains why so many workshops still export uncertified general-purpose instruments while competitors in other countries, facing similar input costs, export instruments certified for use in European hospitals. That gap is not chiefly in the forging sheds. It is in quality-management systems, batch traceability, and the paperwork that a hospital buyer in Germany now expects before it will place an order at all. Which choice best states the main idea of the passage?",
 "options": {"A": "Steel costs and certification fees are the chief obstacles facing Sialkot's exporters.",
             "B": "The industry's limited access to premium markets is better explained by gaps in quality documentation than by input costs alone.",
             "C": "Competitors in other countries pay lower steel costs than Sialkot workshops do.",
             "D": "Sialkot should stop exporting general-purpose surgical instruments altogether."},
 "answer": "B"},

{"id": 84, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: For decades Sialkot's surgical-instrument makers have blamed their limited access to premium export markets on the cost of steel and on foreign certification fees, and both complaints are real. Neither explains why so many workshops still export uncertified general-purpose instruments while competitors in other countries, facing similar input costs, export instruments certified for use in European hospitals. That gap is not chiefly in the forging sheds. It is in quality-management systems, batch traceability, and the paperwork that a hospital buyer in Germany now expects before it will place an order at all. It can most reasonably be inferred that the author would agree with which statement?",
 "options": {"A": "Lowering steel costs alone would move Sialkot workshops into premium export markets.",
             "B": "Complaints about certification fees are fabricated by the industry.",
             "C": "Building stronger quality-management and traceability systems would address a gap that input-cost relief cannot.",
             "D": "Sialkot workshops are technically less capable than their European competitors."},
 "answer": "C"},

{"id": 85, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as AUSTERE.",
 "options": {"A": "lavish", "B": "plain", "C": "generous", "D": "cheerful"},
 "answer": "B"},

{"id": 86, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The council's decision to delay the vote was largely a GUARDED move,\" the word \"guarded\" most nearly means",
 "options": {"A": "protected by security.", "B": "cautious rather than open.", "C": "financially risky.", "D": "legally mandated."},
 "answer": "B"},

# ============================================================
# SECTION 6 - MATH (17) - q87-103
# ============================================================

{"id": 87, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Medium",
 "question": "If x/3 - 6 = x/9, what is the value of x?",
 "options": {"A": "24", "B": "27", "C": "30", "D": "33"},
 "answer": "B"},

{"id": 88, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Hard",
 "question": "In an arithmetic sequence the 7th term is 25 and the 12th term is 50. What is the first term?",
 "options": {"A": "-5", "B": "0", "C": "5", "D": "10"},
 "answer": "A"},

{"id": 89, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "A taxi charges a fixed Rs. 130 plus Rs. 42 for every kilometre travelled. A journey costs Rs. 550. How many kilometres was the journey?",
 "options": {"A": "9", "B": "12", "C": "11", "D": "10"},
 "answer": "D"},

{"id": 90, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Easy",
 "question": "What is the sum of the solutions of x^2 - 12x + 11 = 0?",
 "options": {"A": "11", "B": "-12", "C": "-11", "D": "12"},
 "answer": "D"},

{"id": 91, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "If log(x) = 3, where log denotes the base-10 logarithm, what is the value of log(100x)?",
 "options": {"A": "5", "B": "6", "C": "300", "D": "30000"},
 "answer": "A"},

{"id": 92, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "For all x other than 6 and -2, which expression is equivalent to (x^2 - 36) / (x^2 - 4x - 12)?",
 "options": {"A": "(x - 6)/(x + 2)", "B": "(x + 6)/(x - 2)", "C": "3", "D": "(x + 6)/(x + 2)"},
 "answer": "D"},

{"id": 93, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Medium",
 "question": "Six identical machines together produce 900 units in 5 hours. Working at the same rate, how many units would 9 such machines produce in 4 hours?",
 "options": {"A": "900", "B": "1,000", "C": "1,080", "D": "1,200"},
 "answer": "C"},

{"id": 94, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "The mean of eight numbers is 22. When one of the numbers is removed, the mean of the remaining seven is 24. What was the number that was removed?",
 "options": {"A": "6", "B": "8", "C": "10", "D": "12"},
 "answer": "B"},

{"id": 95, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A fair six-sided die is rolled twice. What is the probability that the two results add up to 7?",
 "options": {"A": "1/9", "B": "5/36", "C": "1/6", "D": "1/12"},
 "answer": "C"},

{"id": 96, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "Set P is {20, 20, 20, 20, 20} and Set Q is {10, 15, 20, 25, 30}. Both sets have a mean of 20. Which set has the larger standard deviation?",
 "options": {"A": "Set P", "B": "They are equal", "C": "It cannot be determined from the information given", "D": "Set Q"},
 "answer": "D"},

{"id": 97, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A square and an equilateral triangle each have a perimeter of 84 cm. By how many centimetres does the triangle's side exceed the square's side?",
 "options": {"A": "5", "B": "6", "C": "7", "D": "8"},
 "answer": "C"},

{"id": 98, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Easy",
 "question": "A right circular cylinder has a radius of 6 cm and a height of 7 cm. What is its volume, in cubic centimetres?",
 "options": {"A": "252pi", "B": "168pi", "C": "126pi", "D": "84pi"},
 "answer": "A"},

{"id": 99, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Medium",
 "question": "Two parallel lines are cut by a transversal. One of the two interior angles on the same side of the transversal measures 80 degrees. What is the measure, in degrees, of the other?",
 "options": {"A": "80", "B": "100", "C": "90", "D": "110"},
 "answer": "B"},

{"id": 100, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Medium",
 "question": "In a 30-60-90 right triangle, the shorter leg measures 6 cm. What is the length of the hypotenuse, in centimetres?",
 "options": {"A": "12", "B": "6*sqrt(3)", "C": "12*sqrt(3)", "D": "9"},
 "answer": "A"},

{"id": 101, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Number Properties (odd/even, divisibility)", "difficulty": "Easy",
 "question": "If m is an even integer, which of the following expressions must be an odd integer?",
 "options": {"A": "m^2", "B": "3m", "C": "m + 9", "D": "6m"},
 "answer": "C"},

{"id": 102, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the smallest positive integer that is divisible by 8, 10 and 15?",
 "options": {"A": "120", "B": "240", "C": "80", "D": "150"},
 "answer": "A"},

{"id": 103, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Medium",
 "question": "Which of the following is NOT a prime number?",
 "options": {"A": "89", "B": "91", "C": "97", "D": "101"},
 "answer": "B"},

# ============================================================
# SECTION 7 - VERBAL (17) - q104-120
# ============================================================

{"id": 104, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Easy",
 "question": "The registrar's memo was strikingly ____: it stated the new deadline, the required documents, and nothing else. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "vague", "B": "lengthy", "C": "evasive", "D": "precise"},
 "answer": "D"},

{"id": 105, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Every retrospective on Pakistani squash lists the champions. The list is accurate. But it hides the more interesting fact, which is that the sport's dominant decades coincided almost exactly with a single family's private training court in Peshawar -- and that it was access to that court, not any one generation's talent alone, that explains the run of titles.\" Which choice best describes the function of the final clause in the text as a whole?",
 "options": {"A": "It withdraws a claim made earlier in the text.",
             "B": "It supplies statistical evidence for the first sentence.",
             "C": "It concedes that the conventional list is factually wrong.",
             "D": "It states the specific point the author believes the conventional account obscures."},
 "answer": "D"},

{"id": 106, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: For years the provincial government has offered a fixed subsidised rate for canal water delivered to sugarcane fields, well below what the same water would cost a fruit orchard nearby. The policy works: farmers keep planting cane even in years when the market price is weak. It also works too well: land suited to higher-value orchards stays under cane, because cane is the one crop whose water cost a farmer can count on regardless of the season. Which choice best states the main idea of the passage?",
 "options": {"A": "The subsidised water rate has failed to keep farmers planting sugarcane.",
             "B": "By keeping water costs low for cane alone, the subsidy succeeds at its aim while locking land into a lower-value crop.",
             "C": "Fruit orchards use less water than sugarcane in every district.",
             "D": "Canal water rates have remained unchanged for decades."},
 "answer": "B"},

{"id": 107, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A publisher reissued a set of local cookbooks in two versions identical except for the author's photograph: printed on some covers, omitted from others. Copies with the author's photograph sold 17 per cent more in markets where that author already had a local following. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "readers prefer cookbooks with no author information at all.",
             "B": "how visibly a locally known author is featured can affect how many copies are bought.",
             "C": "the author's photograph made the recipes more accurately printed.",
             "D": "cookbooks sell better than novels in general."},
 "answer": "B"},

{"id": 108, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "A critic argues that the short-story writer Khadija Mastoor deliberately centres domestic, everyday detail rather than dramatic public events even when her stories touch on major historical upheaval. Which description of a story's content, if accurate, would most directly support that argument?",
 "options": {"A": "The story opens with a detailed account of a political rally and its aftermath.",
             "B": "The story is set during Partition but focuses on a family dividing kitchen utensils before departure.",
             "C": "A narrator delivers an extended speech summarising national events.",
             "D": "The story closes with a description of a battlefield with no domestic scene at all."},
 "answer": "B"},

{"id": 109, "section": 7, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "Domestic sugar production fell for three consecutive seasons, and two mills suspended crushing altogether. ____ the industry's molasses exports rose sharply, offsetting some of the decline. Which transition best completes the text?",
 "options": {"A": "Therefore,", "B": "For example,", "C": "In conclusion,", "D": "Meanwhile,"},
 "answer": "D"},

{"id": 110, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The first phase of the spillway repair finished on schedule ____ the second phase ran nearly six months behind. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ", also ", "C": " which ", "D": "; "},
 "answer": "D"},

{"id": 111, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Easy",
 "question": "Because the mountain road had been closed by a landslide ____ supplies were carried in on foot for nearly three weeks. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; ", "C": ". ", "D": ": "},
 "answer": "A"},

{"id": 112, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which version of the sentence most clearly means that the grant pays for equipment and for nothing else?",
 "options": {"A": "The grant only covers equipment.",
             "B": "Only the grant covers equipment.",
             "C": "The grant covers only equipment.",
             "D": "The grant covers equipment only for first-year researchers."},
 "answer": "C"},

{"id": 113, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: When mining began at the Thar coalfield, several villages sitting above the seam were relocated to purpose-built settlements with concrete housing, a school and a clinic -- amenities most of the original villages had never had. Officials have cited the new housing as proof that resettlement improved residents' lives. Household surveys complicate that reading: livestock, which many families' income depended on, cannot graze near the new settlements the way it once did on open communal land, and several families report that their effective income has fallen even though their housing has visibly improved. A settlement that looks better in concrete and tin can still leave a household worse off than before, if the resettlement was measured only in square footage and not in what a family could still earn. Which choice best states the main idea of the passage?",
 "options": {"A": "Resettlement at Thar has improved every measurable aspect of residents' lives.",
             "B": "Improved housing at the resettlement sites may conceal a decline in livestock-based income that housing quality alone does not capture.",
             "C": "Livestock grazing has expanded near the new settlements.",
             "D": "Most of the original villages had clinics and schools before resettlement."},
 "answer": "B"},

{"id": 114, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: When mining began at the Thar coalfield, several villages sitting above the seam were relocated to purpose-built settlements with concrete housing, a school and a clinic -- amenities most of the original villages had never had. Officials have cited the new housing as proof that resettlement improved residents' lives. Household surveys complicate that reading: livestock, which many families' income depended on, cannot graze near the new settlements the way it once did on open communal land, and several families report that their effective income has fallen even though their housing has visibly improved. A settlement that looks better in concrete and tin can still leave a household worse off than before, if the resettlement was measured only in square footage and not in what a family could still earn. According to the passage, what amenities did the purpose-built resettlement housing include?",
 "options": {"A": "Concrete housing, a school and a clinic.",
             "B": "Only concrete housing, with no other facilities.",
             "C": "Grazing land set aside for livestock.",
             "D": "The passage does not say."},
 "answer": "A"},

{"id": 115, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: When mining began at the Thar coalfield, several villages sitting above the seam were relocated to purpose-built settlements with concrete housing, a school and a clinic -- amenities most of the original villages had never had. Officials have cited the new housing as proof that resettlement improved residents' lives. Household surveys complicate that reading: livestock, which many families' income depended on, cannot graze near the new settlements the way it once did on open communal land, and several families report that their effective income has fallen even though their housing has visibly improved. A settlement that looks better in concrete and tin can still leave a household worse off than before, if the resettlement was measured only in square footage and not in what a family could still earn. The author's attitude toward officials' claim that resettlement improved residents' lives is best characterised as",
 "options": {"A": "fully persuaded.", "B": "openly mocking.", "C": "skeptical, given the survey evidence cited.", "D": "indifferent."},
 "answer": "C"},

{"id": 116, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: When mining began at the Thar coalfield, several villages sitting above the seam were relocated to purpose-built settlements with concrete housing, a school and a clinic -- amenities most of the original villages had never had. Officials have cited the new housing as proof that resettlement improved residents' lives. Household surveys complicate that reading: livestock, which many families' income depended on, cannot graze near the new settlements the way it once did on open communal land, and several families report that their effective income has fallen even though their housing has visibly improved. A settlement that looks better in concrete and tin can still leave a household worse off than before, if the resettlement was measured only in square footage and not in what a family could still earn. It can most reasonably be inferred that the author would support",
 "options": {"A": "measuring resettlement success by housing quality alone.",
             "B": "ending all coal mining at Thar immediately.",
             "C": "treating the new housing as sufficient compensation regardless of lost income.",
             "D": "assessing resettlement outcomes by household income and livelihood, not housing quality alone."},
 "answer": "D"},

{"id": 117, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The internship is open to students who have completed two years of coursework, who have relevant volunteer experience, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "having a faculty recommendation.",
             "B": "a faculty recommendation.",
             "C": "they have a faculty recommendation.",
             "D": "who have a faculty recommendation."},
 "answer": "D"},

{"id": 118, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as DILIGENT.",
 "options": {"A": "lazy", "B": "industrious", "C": "careless", "D": "impulsive"},
 "answer": "B"},

{"id": 119, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to ABUNDANCE.",
 "options": {"A": "scarcity", "B": "surplus", "C": "wealth", "D": "growth"},
 "answer": "A"},

{"id": 120, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The new bylaw did little to CURB unlicensed street vending,\" the word \"curb\" most nearly means",
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
#      bank and from Mocks 1, 2 and 3. That tuple (with past_paper) is
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
    for modname in ("lums_mock_01", "lums_mock_02", "lums_mock_03", "lums_mock_04"):
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