"""
LUMS Common Admission Test (LCAT) - Full-Length Mock Test #1
=============================================================
ParhaiKarlo-prepared full-length mock test. NOT an official LUMS past paper.
Answer keys prepared by content team, pending human verification.

Nothing in this file is taken from LUMS' official "Sample Questions for
Verbal & Math Sections" guide (raw-sources/sample_lcat_2025.pdf). That guide
was read only to calibrate register, passage length, option style and math
difficulty; every question below is newly written. The 24 official sample
questions live in `lums_lcat_sample.py` and are deliberately kept separate --
do not merge the two banks.

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
Groq tagger is skipped for this bank, exactly as it is for lums_lcat_sample.py.

Each question is a dict:
    id, section, subject, topic, subtopic, difficulty, question,
    options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.
"""

SOURCE = "parhaikarlo_mock_01"

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
 "question": "The restoration of the Lahore Fort's Picture Wall proceeded at a ____ pace: conservators spent nearly four years on a single forty-foot panel, lifting centuries of grime one square centimetre at a time. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "deliberate", "B": "reckless", "C": "haphazard", "D": "perfunctory"},
 "answer": "A"},

{"id": 2, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Medium",
 "question": "Text: \"Most accounts of the Indus Valley Civilisation begin with its cities. That is understandable: Mohenjo-daro's drains and granaries are spectacular. But it is the small rural settlements, barely excavated, that will decide whether we are looking at an empire or at a trading network.\" Which choice best describes the function of the third sentence in the text as a whole?",
 "options": {"A": "It concedes a weakness in the evidence the author has just presented.",
             "B": "It summarises a scholarly consensus that the author goes on to endorse.",
             "C": "It offers a specific example that illustrates the claim made in the first sentence.",
             "D": "It redirects attention from a conventional focus toward the evidence the author considers decisive."},
 "answer": "D"},

{"id": 3, "section": 1, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: Karachi's informal minibus network is often called chaotic, but it moves millions of people daily at no cost to the public purse. Any reform must begin by admitting that it works. Text 2: The informal network's apparent efficiency is an accounting illusion. Its costs -- injuries, lost hours, fouled air -- are simply paid by passengers rather than by the city. Based on the texts, how would the author of Text 2 most likely respond to the claim in Text 1 that the network \"works\"?",
 "options": {"A": "By agreeing that it works, but arguing that reform would make it work still better.",
             "B": "By pointing out that ridership figures are unreliable and probably overstated.",
             "C": "By arguing that the claim holds only because the network's real costs have been shifted off the ledger.",
             "D": "By conceding that no public alternative could move comparable numbers of people."},
 "answer": "C"},

{"id": 4, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Easy",
 "question": "Passage: The snow leopard of Gilgit-Baltistan is among the hardest large carnivores to count. It hunts alone, ranges over hundreds of square kilometres, and its coat renders it almost invisible against scree. For decades, population figures were extrapolated from tracks and reported sightings. Camera traps changed that: because every animal's rosette pattern is unique, researchers can now identify particular individuals and estimate numbers from repeat captures. What is the main idea of the passage?",
 "options": {"A": "Snow leopards are the most endangered carnivore in Gilgit-Baltistan.",
             "B": "Camera traps have made it possible to estimate a population that was previously only guessed at.",
             "C": "Tracks and sightings are worthless as sources of ecological evidence.",
             "D": "Snow leopards range more widely than any other cat in Asia."},
 "answer": "B"},

{"id": 5, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: Over an eight-year period, mobile-banking accounts in Pakistan grew more than fivefold, while the number of bank branches per hundred thousand adults barely moved. Rural districts, which had always been the worst served by branches, accounted for the largest share of the new mobile accounts. Which choice most logically completes the reasoning in the passage?",
 "options": {"A": "Therefore, physical branches are likely to disappear from rural districts within a decade.",
             "B": "Therefore, the growth in mobile accounts was driven mainly by urban users opening second accounts.",
             "C": "Therefore, rural customers are more financially sophisticated than urban ones.",
             "D": "Therefore, mobile banking appears to have widened financial access without requiring the branch network to expand."},
 "answer": "D"},

{"id": 6, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A researcher claims that the rise in Pakistan's total tea imports over a given period was driven more by population growth than by any increase in how much tea each person drinks. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Total imports rose 38%, while the population rose 34% and per-person consumption rose 3%.",
             "B": "Total imports rose 38%, while the population rose 6% and per-person consumption rose 30%.",
             "C": "Total imports fell 4%, while the population rose 34%.",
             "D": "Total imports rose 38%, and the average retail price of tea fell 12%."},
 "answer": "A"},

{"id": 7, "section": 1, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "While preparing a report on the poet Faiz Ahmed Faiz, a student compiles three notes: Faiz wrote much of his best-known verse while imprisoned; his poems borrow the stock vocabulary of the classical ghazal, with its beloved and its cupbearer; and critics observe that in his hands that vocabulary consistently carries political meaning. Which statement best synthesises these notes?",
 "options": {"A": "Faiz was imprisoned several times during his career and wrote prolifically throughout.",
             "B": "Faiz preferred the ghazal form to every other form available to him.",
             "C": "Faiz turned the inherited imagery of the classical ghazal into a vehicle for political expression, much of it written under confinement.",
             "D": "Faiz's critics have generally been more interested in his politics than in his craft."},
 "answer": "C"},

{"id": 8, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "Solar panel prices in Pakistan fell sharply after 2022, and rooftop installations multiplied across Punjab. ____ the distribution network was never built to absorb electricity flowing back into it, and utilities have struggled to manage the surplus. Which transition best completes the text?",
 "options": {"A": "Likewise,", "B": "However,", "C": "For instance,", "D": "In addition,"},
 "answer": "B"},

{"id": 9, "section": 1, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: the Khewra Salt Mine is the second-largest salt mine in the world; it has been worked since roughly 1200 CE; it produces around 350,000 tonnes of salt a year; it receives about 250,000 tourists a year. The student wants to emphasise that the mine is at once a working industrial site and a visitor attraction. Which choice best accomplishes this goal?",
 "options": {"A": "The Khewra Salt Mine, worked since roughly 1200 CE, is the second-largest salt mine in the world.",
             "B": "About 250,000 tourists visit the Khewra Salt Mine each year.",
             "C": "Khewra, the world's second-largest salt mine, has been in continuous use for over eight centuries.",
             "D": "Khewra still ships around 350,000 tonnes of salt a year while hosting some 250,000 visitors."},
 "answer": "D"},

{"id": 10, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "The collection of manuscripts housed in the university's rare books room ____ several works copied in Multan in the sixteenth century. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "include", "B": "includes", "C": "are including", "D": "have include"},
 "answer": "B"},

{"id": 11, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "The contractors refused to accept responsibility for the delay, and ____ statements to the press flatly contradicted the engineering report. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "its", "B": "it's", "C": "their", "D": "there"},
 "answer": "C"},

{"id": 12, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The committee had one remaining objection ____ proposed route would cut directly through protected wetland. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ": the", "B": ", that the", "C": "; which the", "D": ", being the"},
 "answer": "A"},

{"id": 13, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Medium",
 "question": "The monsoon arrived three weeks late that year ____ by the time it broke, the cotton crop had already failed. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "; ", "B": ", ", "C": " which ", "D": " and which "},
 "answer": "A"},

{"id": 14, "section": 1, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Having studied the lake's sediment cores for six years, ____\"",
 "options": {"A": "the conclusion of the team was that the basin had dried twice.",
             "B": "it was concluded by the team that the basin had dried twice.",
             "C": "the team concluded that the basin had dried twice.",
             "D": "the basin was shown by the team to have dried twice."},
 "answer": "C"},

{"id": 15, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: Truck art is usually described as decoration, which undersells it. A Pakistani truck's painted panels are commissioned, costed and renewed on a schedule; the owner pays for them out of operating revenue, and drivers report that a well-painted vehicle attracts better freight contracts. Read that way, the paint is not ornament applied to a working machine. It is part of how the machine earns. Which choice best states the main idea of the passage?",
 "options": {"A": "Truck art is more technically accomplished than most gallery painting.",
             "B": "Drivers, rather than owners, decide how a truck is painted.",
             "C": "The cost of repainting a truck has risen faster than freight rates.",
             "D": "Truck art functions as a commercial investment rather than as mere decoration."},
 "answer": "D"},

{"id": 16, "section": 1, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: Truck art is usually described as decoration, which undersells it. A Pakistani truck's painted panels are commissioned, costed and renewed on a schedule; the owner pays for them out of operating revenue, and drivers report that a well-painted vehicle attracts better freight contracts. Read that way, the paint is not ornament applied to a working machine. It is part of how the machine earns. The author's attitude toward the conventional description of truck art is best characterised as",
 "options": {"A": "openly contemptuous.", "B": "gently corrective.", "C": "entirely neutral.", "D": "wistfully nostalgic."},
 "answer": "B"},

{"id": 17, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as PRUDENT.",
 "options": {"A": "circumspect", "B": "lavish", "C": "impulsive", "D": "indifferent"},
 "answer": "A"},

{"id": 18, "section": 1, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to the underlined word as it is used here: \"The minister gave a CANDID account of the negotiations.\"",
 "options": {"A": "lengthy", "B": "informal", "C": "evasive", "D": "pessimistic"},
 "answer": "C"},

# ============================================================
# SECTION 2 - MATH (17) - q19-35
# ============================================================

{"id": 19, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Easy",
 "question": "If 5(x - 3) + 2 = 3x + 7, what is the value of x?",
 "options": {"A": "6", "B": "8", "C": "10", "D": "12"},
 "answer": "C"},

{"id": 20, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 2x + 3y = 12 and x - y = 1, what is the value of x?",
 "options": {"A": "2", "B": "3", "C": "4", "D": "5"},
 "answer": "B"},

{"id": 21, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "Which of the following describes all values of x for which 3 - 2x > 11?",
 "options": {"A": "x > 4", "B": "x < 4", "C": "x > -4", "D": "x < -4"},
 "answer": "D"},

{"id": 22, "section": 2, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Medium",
 "question": "An arithmetic sequence has first term 5 and common difference 3. What is the sum of its first 20 terms?",
 "options": {"A": "670", "B": "640", "C": "610", "D": "700"},
 "answer": "A"},

{"id": 23, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "The equation x^2 + kx + 12 = 0 has roots 3 and 4. What is the value of k?",
 "options": {"A": "-7", "B": "7", "C": "-12", "D": "12"},
 "answer": "A"},

{"id": 24, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is the value of 8^(2/3) * 9^(1/2)?",
 "options": {"A": "6", "B": "12", "C": "18", "D": "24"},
 "answer": "B"},

{"id": 25, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "What is the value of (log_3 81) - (log_2 8)?",
 "options": {"A": "7", "B": "2", "C": "1", "D": "0"},
 "answer": "C"},

{"id": 26, "section": 2, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "If 1/x + 1/(2x) = 3/4, what is the value of x?",
 "options": {"A": "1/2", "B": "1", "C": "2", "D": "4"},
 "answer": "C"},

{"id": 27, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "A shopkeeper raises the price of an item by 25% and then, in a sale, reduces the new price by 20%. Compared with the original price, the final price is",
 "options": {"A": "5% higher.", "B": "5% lower.", "C": "unchanged.", "D": "45% higher."},
 "answer": "C"},

{"id": 28, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Easy",
 "question": "A sum of Rs. 96,000 is divided between two partners in the ratio 3 : 5. By how much does the larger share exceed the smaller share, in rupees?",
 "options": {"A": "24,000", "B": "12,000", "C": "18,000", "D": "30,000"},
 "answer": "A"},

{"id": 29, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "A class of 20 students has a mean score of 72. Five more students, whose mean score is 82, join the class. What is the mean score of all 25 students?",
 "options": {"A": "77", "B": "76", "C": "75", "D": "74"},
 "answer": "D"},

{"id": 30, "section": 2, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A bag contains 4 red marbles and 6 blue marbles. Two marbles are drawn at random without replacement. What is the probability that both are red?",
 "options": {"A": "1/6", "B": "2/15", "C": "4/25", "D": "3/20"},
 "answer": "B"},

{"id": 31, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A rectangle has a perimeter of 36 cm, and its length is 4 cm greater than its width. What is its area, in square centimetres?",
 "options": {"A": "70", "B": "72", "C": "77", "D": "80"},
 "answer": "C"},

{"id": 32, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Easy",
 "question": "A right triangle has legs of length 9 cm and 12 cm. What is its perimeter, in centimetres?",
 "options": {"A": "36", "B": "33", "C": "30", "D": "40"},
 "answer": "A"},

{"id": 33, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Easy",
 "question": "A circle has an area of 36pi square centimetres. What is its circumference, in centimetres?",
 "options": {"A": "6pi", "B": "18pi", "C": "36pi", "D": "12pi"},
 "answer": "D"},

{"id": 34, "section": 2, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Ratios", "difficulty": "Medium",
 "question": "In a right triangle, theta is an acute angle and sin(theta) = 5/13. What is the value of tan(theta)?",
 "options": {"A": "5/12", "B": "12/5", "C": "13/12", "D": "12/13"},
 "answer": "A"},

{"id": 35, "section": 2, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the least common multiple of 12 and 18, minus their greatest common divisor?",
 "options": {"A": "24", "B": "30", "C": "36", "D": "42"},
 "answer": "B"},

# ============================================================
# SECTION 3 - VERBAL (17) - q36-52
# ============================================================

{"id": 36, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "Though the agreement was signed with great ceremony, several of its provisions proved largely ____: within two years neither party was observing the delivery schedule at all. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "nominal", "B": "binding", "C": "contentious", "D": "onerous"},
 "answer": "A"},

{"id": 37, "section": 3, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Economists have long modelled remittances as a pure income transfer. The model is tidy, and it predicts that receiving households will simply consume more. That is not what household survey data from rural Punjab show: those households build, insure and lend.\" Which choice best describes the function of the final sentence in the text as a whole?",
 "options": {"A": "It supplies an example that confirms the prediction described earlier.",
             "B": "It restates the model's central claim in more concrete terms.",
             "C": "It proposes a refinement that would make the model easier to apply.",
             "D": "It introduces empirical evidence that conflicts with the prediction described earlier."},
 "answer": "D"},

{"id": 38, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: Over three decades, Pakistan's total cotton output barely changed, while the area planted with cotton shrank by nearly a quarter. Yield per hectare therefore rose. Agronomists caution against reading this as progress: most of the gain came from taking marginal land out of production, not from any improvement in how the remaining land is farmed. Which choice best states the main idea of the passage?",
 "options": {"A": "Cotton farming in Pakistan has become substantially more efficient over three decades.",
             "B": "The rise in cotton yield per hectare reflects which land was abandoned rather than better farming practice.",
             "C": "Pakistan should return marginal land to cotton production to raise total output.",
             "D": "Total cotton output is a more useful statistic than yield per hectare."},
 "answer": "B"},

{"id": 39, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: Pakistan's national parks are administered province by province, but the species that most often draw visitors -- markhor, ibex, snow leopard -- range freely across provincial boundaries, and individual animals are routinely recorded on both sides. It follows that a set of separate provincial surveys ____ Which choice most logically completes the text?",
 "options": {"A": "should be conducted more frequently than they currently are.",
             "B": "will always undercount the number of animals in each province.",
             "C": "cannot simply be added together to produce a reliable national total.",
             "D": "is the only practical method of counting mountain wildlife."},
 "answer": "C"},

{"id": 40, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "In a study of Karachi's private water-tanker market, a researcher argues that households buy tanker water not because piped supply is absent but because its timing is unpredictable. Which quotation from a household interview, if authentic, would most directly support that argument?",
 "options": {"A": "\"We have had no piped connection on this street for eleven years.\"",
             "B": "\"The piped water comes -- but it might be Tuesday, it might be Friday, so we keep the tank filled either way.\"",
             "C": "\"Tanker water costs us nearly a fifth of what we earn in a month.\"",
             "D": "\"The tanker drivers know everyone on this lane by name.\""},
 "answer": "B"},

{"id": 41, "section": 3, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student researching the Karakoram Highway records three observations: the route follows a branch of an ancient Silk Road trading corridor; construction took two decades and cost hundreds of workers their lives; and the highway remains the only paved land link between Pakistan and China. Which statement best synthesises these observations?",
 "options": {"A": "The Karakoram Highway took two decades to build and crosses some of the highest terrain in the world.",
             "B": "Silk Road routes through the Karakoram were used for centuries before any road was paved.",
             "C": "Trade between Pakistan and China has grown steadily since the highway opened.",
             "D": "The Karakoram Highway is a modern road built at heavy human cost along an ancient trading corridor, and it is still the only paved land link between the two countries."},
 "answer": "D"},

{"id": 42, "section": 3, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "The 1935 Quetta earthquake flattened almost every masonry building in the city. ____ the timber-framed structures in the cantonment, lighter and far more flexible, came through largely intact. Which transition best completes the text?",
 "options": {"A": "Consequently,", "B": "By contrast,", "C": "Similarly,", "D": "In short,"},
 "answer": "B"},

{"id": 43, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The programme trains volunteers to test water samples, to record household symptoms, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "reporting outbreaks to the district office.",
             "B": "they report outbreaks to the district office.",
             "C": "to report outbreaks to the district office.",
             "D": "outbreaks are reported to the district office."},
 "answer": "C"},

{"id": 44, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The delegation visited three cities in southern Punjab ____ Multan, Bahawalpur and Rahim Yar Khan. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ": ", "B": ", ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 45, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Easy",
 "question": "Each of the twelve district offices ____ required to file a monthly return. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "are", "B": "have been", "C": "were", "D": "is"},
 "answer": "D"},

{"id": 46, "section": 3, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Hard",
 "question": "The canal was widened in 2011 ____ the flooding downstream has grown worse every year since. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; nevertheless, ", "C": " and which ", "D": ", however "},
 "answer": "B"},

{"id": 47, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: The Indus river dolphin is functionally blind. In the silt-heavy water it evolved in, eyes were of little use, and its lens degenerated to a pinhole that registers little more than the direction of light. It navigates by echolocation instead, swimming on its side and trailing one flipper along the riverbed. For most of the last century this was treated as a curiosity. It is better read as a warning: the dolphin's range has contracted by roughly four-fifths since the barrages went up, and an animal that hunts entirely by sound is exactly the kind of animal a river full of engines and concrete will fail. Conservation work since the 1990s has stabilised numbers in one stretch between two barrages -- but 'stabilised' there means a fragmented population has stopped shrinking, not that the river has been made whole. Which choice best states the main idea of the passage?",
 "options": {"A": "The Indus river dolphin's blindness is an evolutionary accident with no practical consequences.",
             "B": "Echolocation is a more efficient way of hunting than sight in any aquatic environment.",
             "C": "The dolphin's blindness, long treated as a curiosity, is better understood as a measure of how river engineering has harmed it.",
             "D": "Conservation efforts since the 1990s have restored the Indus river dolphin's historic range."},
 "answer": "C"},

{"id": 48, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: The Indus river dolphin is functionally blind. In the silt-heavy water it evolved in, eyes were of little use, and its lens degenerated to a pinhole that registers little more than the direction of light. It navigates by echolocation instead, swimming on its side and trailing one flipper along the riverbed. For most of the last century this was treated as a curiosity. It is better read as a warning: the dolphin's range has contracted by roughly four-fifths since the barrages went up, and an animal that hunts entirely by sound is exactly the kind of animal a river full of engines and concrete will fail. Conservation work since the 1990s has stabilised numbers in one stretch between two barrages -- but 'stabilised' there means a fragmented population has stopped shrinking, not that the river has been made whole. According to the passage, how does the Indus river dolphin locate its way along the riverbed?",
 "options": {"A": "By echolocating while swimming on its side with one flipper trailing.",
             "B": "By following the direction of light through its pinhole lens.",
             "C": "By following the current between successive barrages.",
             "D": "By tracking the movement of silt in the water column."},
 "answer": "A"},

{"id": 49, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: The Indus river dolphin is functionally blind. In the silt-heavy water it evolved in, eyes were of little use, and its lens degenerated to a pinhole that registers little more than the direction of light. It navigates by echolocation instead, swimming on its side and trailing one flipper along the riverbed. For most of the last century this was treated as a curiosity. It is better read as a warning: the dolphin's range has contracted by roughly four-fifths since the barrages went up, and an animal that hunts entirely by sound is exactly the kind of animal a river full of engines and concrete will fail. Conservation work since the 1990s has stabilised numbers in one stretch between two barrages -- but 'stabilised' there means a fragmented population has stopped shrinking, not that the river has been made whole. The author's attitude toward the conservation work described in the final sentence is best characterised as",
 "options": {"A": "dismissive of any benefit it has produced.",
             "B": "confident that the species has now been secured.",
             "C": "appreciative but unwilling to call it a recovery.",
             "D": "indifferent to its outcome either way."},
 "answer": "C"},

{"id": 50, "section": 3, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: The Indus river dolphin is functionally blind. In the silt-heavy water it evolved in, eyes were of little use, and its lens degenerated to a pinhole that registers little more than the direction of light. It navigates by echolocation instead, swimming on its side and trailing one flipper along the riverbed. For most of the last century this was treated as a curiosity. It is better read as a warning: the dolphin's range has contracted by roughly four-fifths since the barrages went up, and an animal that hunts entirely by sound is exactly the kind of animal a river full of engines and concrete will fail. Conservation work since the 1990s has stabilised numbers in one stretch between two barrages -- but 'stabilised' there means a fragmented population has stopped shrinking, not that the river has been made whole. It can most reasonably be inferred from the passage that the author regards the barrages as",
 "options": {"A": "a necessary trade-off that conservation work has now offset.",
             "B": "a recent development whose effects cannot yet be measured.",
             "C": "irrelevant to the dolphin, which navigates by sound rather than sight.",
             "D": "the principal reason the dolphin's range has collapsed and remains fragmented."},
 "answer": "D"},

{"id": 51, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as EPHEMERAL.",
 "options": {"A": "fleeting", "B": "enormous", "C": "mysterious", "D": "repetitive"},
 "answer": "A"},

{"id": 52, "section": 3, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The new tariff schedule will TELL on small exporters within a single quarter,\" the word \"tell\" most nearly means",
 "options": {"A": "narrate.", "B": "count aloud.", "C": "distinguish.", "D": "have a noticeable effect."},
 "answer": "D"},

# ============================================================
# SECTION 4 - MATH (17) - q53-69
# ============================================================

{"id": 53, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in Two Variables", "difficulty": "Medium",
 "question": "A line in the xy-plane passes through the points (2, 5) and (6, 13). What is the y-coordinate of its y-intercept?",
 "options": {"A": "1", "B": "2", "C": "3", "D": "-1"},
 "answer": "A"},

{"id": 54, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "The function f is defined by f(x) = 3x - 7. If f(a) = 11, what is the value of a?",
 "options": {"A": "7", "B": "6", "C": "5", "D": "4"},
 "answer": "B"},

{"id": 55, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Systems of Linear Equations", "difficulty": "Medium",
 "question": "If 3x + 2y = 16 and 5x - 2y = 0, what is the value of y?",
 "options": {"A": "2", "B": "3", "C": "4", "D": "5"},
 "answer": "D"},

{"id": 56, "section": 4, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Inequalities", "difficulty": "Medium",
 "question": "A delivery van weighs 1,200 kg when empty, and the total weight of the loaded van must not exceed 2,000 kg. If each crate weighs 45 kg, what is the greatest number of whole crates the van can carry?",
 "options": {"A": "16", "B": "18", "C": "19", "D": "17"},
 "answer": "D"},

{"id": 57, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Nonlinear Functions", "difficulty": "Medium",
 "question": "What is the minimum value of the function f(x) = x^2 - 4x + 1?",
 "options": {"A": "-1", "B": "1", "C": "-3", "D": "3"},
 "answer": "C"},

{"id": 58, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Polynomial Expressions", "difficulty": "Easy",
 "question": "Which expression is equivalent to (2x - 3)(x + 5)?",
 "options": {"A": "2x^2 - 7x - 15", "B": "2x^2 + 13x - 15", "C": "2x^2 + 7x - 15", "D": "2x^2 + 7x + 15"},
 "answer": "C"},

{"id": 59, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Medium",
 "question": "How many real solutions does the equation x^2 + 4x + 7 = 0 have?",
 "options": {"A": "Two distinct real solutions", "B": "Exactly one real solution", "C": "Infinitely many real solutions", "D": "No real solutions"},
 "answer": "D"},

{"id": 60, "section": 4, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Exponents and Radicals", "difficulty": "Medium",
 "question": "What is sqrt(50) + sqrt(18) in simplest radical form?",
 "options": {"A": "8*sqrt(2)", "B": "4*sqrt(17)", "C": "2*sqrt(17)", "D": "sqrt(68)"},
 "answer": "A"},

{"id": 61, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Unit Conversion", "difficulty": "Easy",
 "question": "A car consumes fuel at a rate of 8 litres per 100 kilometres. How many litres will it consume on a 350-kilometre journey at that rate?",
 "options": {"A": "30", "B": "26", "C": "24", "D": "28"},
 "answer": "D"},

{"id": 62, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Two-Variable Data Interpretation (tables/graphs)", "difficulty": "Medium",
 "question": "A shop records the number of units sold on each of five days: Monday 42, Tuesday 51, Wednesday 40, Thursday 50, Friday 55. By what percentage did the number of units sold increase from Wednesday to Thursday?",
 "options": {"A": "25%", "B": "20%", "C": "10%", "D": "40%"},
 "answer": "A"},

{"id": 63, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "For the data set 4, 7, 7, 9, 13, what is the mean minus the median?",
 "options": {"A": "0", "B": "1", "C": "2", "D": "3"},
 "answer": "B"},

{"id": 64, "section": 4, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Percentages", "difficulty": "Medium",
 "question": "After a 20% discount, a jacket sells for Rs. 3,600. What was its price before the discount, in rupees?",
 "options": {"A": "4,800", "B": "4,500", "C": "4,320", "D": "4,200"},
 "answer": "B"},

{"id": 65, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Medium",
 "question": "A cube has a volume of 216 cubic centimetres. What is its total surface area, in square centimetres?",
 "options": {"A": "216", "B": "144", "C": "180", "D": "252"},
 "answer": "A"},

{"id": 66, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Easy",
 "question": "The three interior angles of a triangle are in the ratio 2 : 3 : 4. What is the measure of the largest angle, in degrees?",
 "options": {"A": "90", "B": "70", "C": "80", "D": "60"},
 "answer": "C"},

{"id": 67, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Circles (arcs, sectors, equations)", "difficulty": "Medium",
 "question": "A sector of a circle of radius 9 cm has a central angle of 60 degrees. What is the area of the sector, in square centimetres?",
 "options": {"A": "27pi", "B": "13.5pi", "C": "9pi", "D": "4.5pi"},
 "answer": "B"},

{"id": 68, "section": 4, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Trigonometric Identities", "difficulty": "Medium",
 "question": "For any angle theta with sin(theta) not equal to 0, which expression is equivalent to (1 - cos^2(theta)) / sin(theta)?",
 "options": {"A": "cos(theta)", "B": "tan(theta)", "C": "sin(theta)", "D": "1"},
 "answer": "C"},

{"id": 69, "section": 4, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Easy",
 "question": "What is the sum of all prime numbers strictly between 20 and 30?",
 "options": {"A": "46", "B": "52", "C": "58", "D": "75"},
 "answer": "B"},

# ============================================================
# SECTION 5 - VERBAL (17) - q70-86
# ============================================================

{"id": 70, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Medium",
 "question": "The auditor's report was admired above all for its ____: every claim carried a footnote, and no figure appeared without the document it came from. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "brevity", "B": "elegance", "C": "rigour", "D": "optimism"},
 "answer": "C"},

{"id": 71, "section": 5, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Cross-Text Connections", "difficulty": "Hard",
 "question": "Text 1: A standardised entry test is the only instrument we have that treats every applicant identically. Remove it and admission turns on who can afford coaching and a polished personal essay. Text 2: The test treats applicants identically only inside the examination hall. Long before they reach it, it has already sorted them by who could afford years of preparation. Based on the texts, the author of Text 2 would most likely characterise Text 1's claim about identical treatment as",
 "options": {"A": "false, because examiners in practice apply different standards to different candidates.",
             "B": "correct, and a sufficient reason to keep the test in place.",
             "C": "irrelevant, because coaching has little measurable effect on scores.",
             "D": "accurate about the examination itself but misleading about the process that leads to it."},
 "answer": "D"},

{"id": 72, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: The Indus delta holds one of the largest arid-climate mangrove forests in the world. Mangroves are usually valued as nurseries for fish, and the delta's are. But their more consequential function here is structural: their roots hold sediment in place, and where they have been cleared, seawater has pushed inland far enough to sour farmland twenty kilometres from the coast. Which choice best states the main idea of the passage?",
 "options": {"A": "Beyond their familiar role as fish nurseries, the delta's mangroves matter chiefly because they hold back seawater intrusion.",
             "B": "The Indus delta's mangrove forest is the largest of its kind anywhere in the world.",
             "C": "Fish nurseries are of little economic value compared with farmland.",
             "D": "Seawater intrusion in the delta has been caused mainly by upstream water diversion."},
 "answer": "A"},

{"id": 73, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A city introduced a congestion charge covering only its central business district. In the first year, traffic entering that district fell by 18 per cent. Over the same period, traffic on the uncharged ring road rose by 21 per cent. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "the charge failed to change any driver's behaviour.",
             "B": "the total number of vehicle trips in the city fell by roughly 18 per cent.",
             "C": "at least part of the fall in central traffic reflects trips diverted elsewhere rather than trips given up.",
             "D": "ring-road drivers were unaware that the congestion charge had been introduced."},
 "answer": "C"},

{"id": 74, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (quantitative)", "difficulty": "Medium",
 "question": "A school claims that its new reading programme helped its weakest readers more than its strongest. Which finding, if true, would most directly support that claim?",
 "options": {"A": "Students in the lowest-scoring quartile gained an average of 14 points, while students in the highest-scoring quartile gained an average of 2.",
             "B": "The school's overall average reading score rose by 9 points.",
             "C": "Students in the highest-scoring quartile finished the year with the highest scores in the school.",
             "D": "Attendance at the programme's optional sessions was highest among the lowest-scoring quartile."},
 "answer": "A"},

{"id": 75, "section": 5, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Synthesizing Multiple Observations", "difficulty": "Medium",
 "question": "A student compiles three observations about the Rohtas Fort: it was raised in the 1540s on the orders of Sher Shah Suri; its walls were never breached in battle; and it was positioned to hold the local Gakhar tribes in check rather than to repel an invading army. Which statement best synthesises these observations?",
 "options": {"A": "Rohtas Fort is among the largest surviving sixteenth-century forts in South Asia.",
             "B": "Sher Shah Suri built more fortifications than any other ruler of his era.",
             "C": "The Gakhar tribes were the most persistent military threat of the period.",
             "D": "Rohtas Fort was built as an instrument of internal control rather than frontier defence, and it was never tested in a siege."},
 "answer": "D"},

{"id": 76, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Easy",
 "question": "The library digitised its entire manuscript collection over a five-year programme. ____ a scholar in Quetta or Peshawar can now consult folios that once required a journey to Lahore. Which transition best completes the text?",
 "options": {"A": "Nevertheless,", "B": "As a result,", "C": "By comparison,", "D": "Admittedly,"},
 "answer": "B"},

{"id": 77, "section": 5, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Rhetorical Synthesis", "difficulty": "Medium",
 "question": "A student has taken these notes: apricots in Hunza are dried on flat rooftops; some thirty local cultivars are still grown; the kernels are pressed for an oil that is sold abroad; the harvest lasts about six weeks. The student wants to emphasise that the crop serves more than one purpose. Which choice best accomplishes this goal?",
 "options": {"A": "Hunza's apricots are dried on rooftops as winter food and pressed for a kernel oil that is sold abroad.",
             "B": "Some thirty apricot cultivars are still grown in Hunza.",
             "C": "The Hunza apricot harvest lasts roughly six weeks each year.",
             "D": "Apricots have been cultivated in Hunza for a very long time."},
 "answer": "A"},

{"id": 78, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The committee's findings ____ published in March, were challenged by two provincial departments within a week. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": ": ", "C": "; ", "D": " and "},
 "answer": "A"},

{"id": 79, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Pronoun Agreement and Reference", "difficulty": "Medium",
 "question": "Every one of the surveyed households reported that ____ water supply had been interrupted at least twice that month. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "their", "B": "its", "C": "it's", "D": "whose"},
 "answer": "B"},

{"id": 80, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which choice completes the text so that it conforms to the conventions of Standard English? \"Raised in the 1540s and never breached in battle, ____\"",
 "options": {"A": "historians regard Rohtas Fort as a remarkable survival.",
             "B": "the walls of Rohtas Fort are what visitors remember.",
             "C": "Rohtas Fort still commands the approach to the Kahan river.",
             "D": "it is the Kahan river that Rohtas Fort overlooks."},
 "answer": "C"},

{"id": 81, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The report praised the plant's thermal efficiency, its safety record, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "it produced electricity cheaply.",
             "B": "that its electricity was cheap.",
             "C": "producing electricity at low cost.",
             "D": "the low cost of its electricity."},
 "answer": "D"},

{"id": 82, "section": 5, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Subject-Verb Agreement", "difficulty": "Hard",
 "question": "Neither the site supervisor nor the two junior engineers ____ willing to sign the inspection sheet. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "was", "B": "were", "C": "has been", "D": "is"},
 "answer": "B"},

{"id": 83, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Hard",
 "question": "Passage: For half a century Pakistan's export earnings have leaned on cotton textiles, and for half a century the industry has complained about the same two things: the cost of power and the cost of finance. Both complaints are legitimate. Neither explains why the country still ships mostly yarn and grey cloth while competitors with worse power and dearer credit ship finished garments. The gap is not in the spinning sheds. It is in design, in compliance paperwork, and in the ability to fill a buyer's order in six weeks rather than sixteen. Which choice best states the main idea of the passage?",
 "options": {"A": "Power and finance costs are the chief obstacles facing Pakistan's textile exporters.",
             "B": "Pakistan's competitors enjoy cheaper electricity and cheaper credit than Pakistani mills do.",
             "C": "The industry's failure to move beyond low-value exports is better explained by capabilities outside the factory than by input costs.",
             "D": "Pakistan should stop exporting yarn and grey cloth altogether."},
 "answer": "C"},

{"id": 84, "section": 5, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: For half a century Pakistan's export earnings have leaned on cotton textiles, and for half a century the industry has complained about the same two things: the cost of power and the cost of finance. Both complaints are legitimate. Neither explains why the country still ships mostly yarn and grey cloth while competitors with worse power and dearer credit ship finished garments. The gap is not in the spinning sheds. It is in design, in compliance paperwork, and in the ability to fill a buyer's order in six weeks rather than sixteen. It can most reasonably be inferred that the author would agree with which statement?",
 "options": {"A": "Reducing electricity tariffs would be enough on its own to move the industry into finished garments.",
             "B": "Complaints about the cost of finance are fabricated by the industry.",
             "C": "Pakistani mills are technically less capable than those of their competitors.",
             "D": "Cheaper power alone would not move the industry up the value chain."},
 "answer": "D"},

{"id": 85, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Easy",
 "question": "Select the word that is most nearly the same in meaning as MITIGATE.",
 "options": {"A": "intensify", "B": "alleviate", "C": "postpone", "D": "clarify"},
 "answer": "B"},

{"id": 86, "section": 5, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The chairman's closing remarks were a shade too POINTED for the occasion,\" the word \"pointed\" most nearly means",
 "options": {"A": "precise.", "B": "brief.", "C": "cutting.", "D": "formal."},
 "answer": "C"},

# ============================================================
# SECTION 6 - MATH (17) - q87-103
# ============================================================

{"id": 87, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Equations in One Variable", "difficulty": "Medium",
 "question": "If x/3 - 4 = x/5, what is the value of x?",
 "options": {"A": "20", "B": "24", "C": "30", "D": "36"},
 "answer": "C"},

{"id": 88, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Arithmetic Sequences and Series", "difficulty": "Hard",
 "question": "In an arithmetic sequence the 7th term is 23 and the 12th term is 43. What is the first term?",
 "options": {"A": "-1", "B": "1", "C": "3", "D": "-3"},
 "answer": "A"},

{"id": 89, "section": 6, "subject": "Math", "topic": "Algebra",
 "subtopic": "Linear Functions", "difficulty": "Easy",
 "question": "A taxi charges a fixed Rs. 150 plus Rs. 45 for every kilometre travelled. A journey costs Rs. 645. How many kilometres was the journey?",
 "options": {"A": "12", "B": "11", "C": "10", "D": "9"},
 "answer": "B"},

{"id": 90, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Quadratic Equations and Functions", "difficulty": "Easy",
 "question": "What is the sum of the solutions of x^2 - 6x + 5 = 0?",
 "options": {"A": "5", "B": "-6", "C": "-5", "D": "6"},
 "answer": "D"},

{"id": 91, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Logarithms", "difficulty": "Medium",
 "question": "If log(x) = 3, where log denotes the base-10 logarithm, what is the value of log(100x)?",
 "options": {"A": "6", "B": "5", "C": "30", "D": "300"},
 "answer": "B"},

{"id": 92, "section": 6, "subject": "Math", "topic": "Advanced Mathematics",
 "subtopic": "Rational Expressions and Equations", "difficulty": "Medium",
 "question": "For all x other than 3 and -2, which expression is equivalent to (x^2 - 9) / (x^2 - x - 6)?",
 "options": {"A": "(x - 3)/(x - 2)", "B": "(x + 3)/(x - 2)", "C": "3/2", "D": "(x + 3)/(x + 2)"},
 "answer": "D"},

{"id": 93, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Ratios, Rates, and Proportions", "difficulty": "Medium",
 "question": "Six identical machines together produce 900 units in 5 hours. Working at the same rate, how many units would 10 such machines produce in 4 hours?",
 "options": {"A": "1,000", "B": "1,080", "C": "1,200", "D": "1,500"},
 "answer": "C"},

{"id": 94, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Averages and Weighted Averages", "difficulty": "Medium",
 "question": "The mean of five numbers is 18. When one of the numbers is removed, the mean of the remaining four is 20. What was the number that was removed?",
 "options": {"A": "8", "B": "10", "C": "12", "D": "14"},
 "answer": "B"},

{"id": 95, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Probability", "difficulty": "Medium",
 "question": "A fair six-sided die is rolled twice. What is the probability that the two results add up to 9?",
 "options": {"A": "1/9", "B": "1/6", "C": "1/12", "D": "5/36"},
 "answer": "A"},

{"id": 96, "section": 6, "subject": "Math", "topic": "Problem-Solving and Data Analysis",
 "subtopic": "Statistics (mean, median, mode, standard deviation)", "difficulty": "Medium",
 "question": "Set P is {10, 10, 10, 10, 10} and Set Q is {6, 8, 10, 12, 14}. Both sets have a mean of 10. Which set has the larger standard deviation?",
 "options": {"A": "Set P", "B": "They are equal", "C": "It cannot be determined from the information given", "D": "Set Q"},
 "answer": "D"},

{"id": 97, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Area and Perimeter", "difficulty": "Medium",
 "question": "A square and an equilateral triangle each have a perimeter of 36 cm. By how many centimetres does the triangle's side exceed the square's side?",
 "options": {"A": "3", "B": "2", "C": "4", "D": "6"},
 "answer": "A"},

{"id": 98, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Volume and Surface Area", "difficulty": "Easy",
 "question": "A right circular cylinder has a radius of 3 cm and a height of 10 cm. What is its volume, in cubic centimetres?",
 "options": {"A": "30pi", "B": "60pi", "C": "90pi", "D": "180pi"},
 "answer": "C"},

{"id": 99, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Lines, Angles, and Triangles", "difficulty": "Medium",
 "question": "Two parallel lines are cut by a transversal. One of the two interior angles on the same side of the transversal measures 65 degrees. What is the measure, in degrees, of the other?",
 "options": {"A": "65", "B": "125", "C": "130", "D": "115"},
 "answer": "D"},

{"id": 100, "section": 6, "subject": "Math", "topic": "Geometry and Trigonometry",
 "subtopic": "Right Triangles and the Pythagorean Theorem", "difficulty": "Medium",
 "question": "In a 30-60-90 right triangle, the shorter leg measures 7 cm. What is the length of the hypotenuse, in centimetres?",
 "options": {"A": "14", "B": "7*sqrt(3)", "C": "14*sqrt(3)", "D": "10.5"},
 "answer": "A"},

{"id": 101, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Number Properties (odd/even, divisibility)", "difficulty": "Easy",
 "question": "If n is an odd integer, which of the following expressions must be an even integer?",
 "options": {"A": "n^2", "B": "3n", "C": "n + 3", "D": "2n + 1"},
 "answer": "C"},

{"id": 102, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Factors and Multiples", "difficulty": "Easy",
 "question": "What is the smallest positive integer that is divisible by 4, 6 and 15?",
 "options": {"A": "120", "B": "45", "C": "30", "D": "60"},
 "answer": "D"},

{"id": 103, "section": 6, "subject": "Math", "topic": "Number Theory",
 "subtopic": "Prime Numbers", "difficulty": "Medium",
 "question": "Which of the following is NOT a prime number?",
 "options": {"A": "53", "B": "51", "C": "59", "D": "61"},
 "answer": "B"},

# ============================================================
# SECTION 7 - VERBAL (17) - q104-120
# ============================================================

{"id": 104, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Words in Context (vocabulary-in-blank)", "difficulty": "Easy",
 "question": "The minister's reply was unusually ____: it answered the question that had been asked, gave a single figure, and stopped. Which choice completes the text with the most logical and precise word?",
 "options": {"A": "evasive", "B": "succinct", "C": "rambling", "D": "ambiguous"},
 "answer": "B"},

{"id": 105, "section": 7, "subject": "Verbal", "topic": "Craft and Structure",
 "subtopic": "Text Structure and Purpose", "difficulty": "Hard",
 "question": "Text: \"Every history of Pakistani cricket lists the fast bowlers. The list is not wrong. But it conceals the more interesting fact, which is that the country produced them in pairs -- and that it was the pairing, not the individual, that unsettled batsmen.\" Which choice best describes the function of the final clause in the text as a whole?",
 "options": {"A": "It withdraws the objection raised in the preceding sentence.",
             "B": "It supplies statistical evidence for a claim made earlier.",
             "C": "It acknowledges that the conventional list is factually inaccurate.",
             "D": "It states the specific point the author believes the conventional account obscures."},
 "answer": "D"},

{"id": 106, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Central Ideas and Details", "difficulty": "Medium",
 "question": "Passage: For decades the government has set a guaranteed purchase price for wheat, above the prevailing market rate, so that farmers keep planting it. The policy works: wheat gets planted. It also works too well. Land that would return more under other crops stays under wheat, because wheat is the one crop whose price a farmer knows before sowing. Which choice best states the main idea of the passage?",
 "options": {"A": "The guaranteed wheat price has failed to keep farmers planting wheat.",
             "B": "By removing price risk for wheat alone, the support price succeeds at its aim while locking land into a lower-value crop.",
             "C": "Wheat is the most profitable crop available to Pakistani farmers.",
             "D": "Market prices for agricultural produce are impossible to forecast."},
 "answer": "B"},

{"id": 107, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Inferences", "difficulty": "Medium",
 "question": "Passage: A publisher reissued a set of translated novels in two versions that were identical except for one detail: on some copies the translator was named on the front cover, and on others only on an inside page. Copies naming the translator on the cover sold 12 per cent more. It can most reasonably be concluded that ____ Which choice most logically completes the text?",
 "options": {"A": "readers prefer translated novels to novels written in their own language.",
             "B": "the translator's name on the cover made the translations more accurate.",
             "C": "how prominently a translation is credited can affect how many copies are bought.",
             "D": "the inside-page editions were priced higher than the cover-credited ones."},
 "answer": "C"},

{"id": 108, "section": 7, "subject": "Verbal", "topic": "Information and Ideas",
 "subtopic": "Command of Evidence (textual)", "difficulty": "Hard",
 "question": "A critic argues that Saadat Hasan Manto's short stories deliberately withhold the moral verdict his readers expected a story to deliver. Which description of a story's ending, if accurate, would most directly support that argument?",
 "options": {"A": "The narrator explains at length why the protagonist's choice was indefensible.",
             "B": "The narrator reports what happened, names no one as guilty, and closes on a detail of weather.",
             "C": "The protagonist is punished by the authorities in the final paragraph.",
             "D": "A secondary character delivers a speech summarising the story's lesson."},
 "answer": "B"},

{"id": 109, "section": 7, "subject": "Verbal", "topic": "Expression of Ideas",
 "subtopic": "Transitions", "difficulty": "Medium",
 "question": "Domestic cement demand fell for six consecutive quarters, and two plants suspended production altogether. ____ the industry's export volumes rose sharply, cushioning the decline. Which transition best completes the text?",
 "options": {"A": "Therefore,", "B": "For example,", "C": "In conclusion,", "D": "Meanwhile,"},
 "answer": "D"},

{"id": 110, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Punctuation (commas, semicolons, colons)", "difficulty": "Medium",
 "question": "The first phase of the scheme was completed on time ____ the second ran eighteen months late. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; ", "C": " which ", "D": ", also "},
 "answer": "B"},

{"id": 111, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Sentence Boundaries", "difficulty": "Easy",
 "question": "Because the bridge had been closed for repairs ____ traffic was routed through the old town for six weeks. Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": ", ", "B": "; ", "C": ". ", "D": ": "},
 "answer": "A"},

{"id": 112, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Modifier Placement", "difficulty": "Medium",
 "question": "Which version of the sentence most clearly means that the grant pays for tuition and for nothing else?",
 "options": {"A": "The grant only covers tuition.",
             "B": "Only the grant covers tuition.",
             "C": "The grant covers only tuition.",
             "D": "The grant covers tuition only for first-year students."},
 "answer": "C"},

{"id": 113, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage Main Idea", "difficulty": "Medium",
 "question": "Passage: When the city widened its canal road it removed some six hundred mature trees and planted two thousand saplings in their place. On paper the city gained. In practice it did not: a forty-year-old sheesham cools the air around it in a way no five-year-old sapling can, and it is canopy volume, not stem count, that decides whether a street is walkable in June. The arithmetic that governs urban forestry almost everywhere counts trunks, because trunks are easy to count. Until it counts canopy instead, cities will keep trading shade for the appearance of it. Which choice best states the main idea of the passage?",
 "options": {"A": "Planting saplings is a waste of municipal money.",
             "B": "The canal road should never have been widened.",
             "C": "Mature sheesham trees are the only species suited to city streets.",
             "D": "Measuring urban forests by number of trunks rather than canopy lets cities lose real shade while appearing to gain trees."},
 "answer": "D"},

{"id": 114, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Supporting Detail Recall", "difficulty": "Easy",
 "question": "Passage: When the city widened its canal road it removed some six hundred mature trees and planted two thousand saplings in their place. On paper the city gained. In practice it did not: a forty-year-old sheesham cools the air around it in a way no five-year-old sapling can, and it is canopy volume, not stem count, that decides whether a street is walkable in June. The arithmetic that governs urban forestry almost everywhere counts trunks, because trunks are easy to count. Until it counts canopy instead, cities will keep trading shade for the appearance of it. According to the passage, how many trees were removed and how many planted during the road widening?",
 "options": {"A": "About 600 removed and about 2,000 planted.",
             "B": "About 2,000 removed and about 600 planted.",
             "C": "About 600 removed and about 600 planted.",
             "D": "The passage does not give either figure."},
 "answer": "A"},

{"id": 115, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Author's Tone and Perspective", "difficulty": "Medium",
 "question": "Passage: When the city widened its canal road it removed some six hundred mature trees and planted two thousand saplings in their place. On paper the city gained. In practice it did not: a forty-year-old sheesham cools the air around it in a way no five-year-old sapling can, and it is canopy volume, not stem count, that decides whether a street is walkable in June. The arithmetic that governs urban forestry almost everywhere counts trunks, because trunks are easy to count. Until it counts canopy instead, cities will keep trading shade for the appearance of it. The author's attitude toward the practice of counting trunks is best characterised as",
 "options": {"A": "enthusiastic approval.",
             "B": "detached and purely descriptive.",
             "C": "critical of it as a convenient but misleading measure.",
             "D": "resigned to it as the only method available."},
 "answer": "C"},

{"id": 116, "section": 7, "subject": "Verbal", "topic": "Reading Comprehension",
 "subtopic": "Passage-Based Inference", "difficulty": "Hard",
 "question": "Passage: When the city widened its canal road it removed some six hundred mature trees and planted two thousand saplings in their place. On paper the city gained. In practice it did not: a forty-year-old sheesham cools the air around it in a way no five-year-old sapling can, and it is canopy volume, not stem count, that decides whether a street is walkable in June. The arithmetic that governs urban forestry almost everywhere counts trunks, because trunks are easy to count. Until it counts canopy instead, cities will keep trading shade for the appearance of it. It can most reasonably be inferred that the author would support",
 "options": {"A": "a moratorium on all road-widening projects.",
             "B": "planting a far greater number of saplings for every mature tree removed.",
             "C": "restricting street planting to species that mature quickly.",
             "D": "replacing stem counts with canopy measurement as the standard municipal metric."},
 "answer": "D"},

{"id": 117, "section": 7, "subject": "Verbal", "topic": "Standard English Conventions",
 "subtopic": "Parallel Structure", "difficulty": "Medium",
 "question": "The fellowship is open to candidates who have completed a master's degree, who have published at least one peer-reviewed paper, and ____ Which choice completes the text so that it conforms to the conventions of Standard English?",
 "options": {"A": "having taught for two years.",
             "B": "two years of teaching.",
             "C": "they have taught for two years.",
             "D": "who have taught for two years."},
 "answer": "D"},

{"id": 118, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Synonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly the same in meaning as LACONIC.",
 "options": {"A": "terse", "B": "talkative", "C": "cheerful", "D": "bewildered"},
 "answer": "A"},

{"id": 119, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Antonyms", "difficulty": "Medium",
 "question": "Select the word that is most nearly OPPOSITE in meaning to AUGMENT.",
 "options": {"A": "diminish", "B": "enlarge", "C": "sustain", "D": "transfer"},
 "answer": "A"},

{"id": 120, "section": 7, "subject": "Verbal", "topic": "Vocabulary",
 "subtopic": "Contextual Word Meaning", "difficulty": "Medium",
 "question": "As used in the sentence \"The settlement did nothing to ARREST the decline in enrolment,\" the word \"arrest\" most nearly means",
 "options": {"A": "seize.", "B": "accuse.", "C": "halt.", "D": "reverse."},
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
#      lums_lcat_sample.py. That tuple (with past_paper) is import_mcqs.py's
#      dedupe key -- a collision would make one bank's question silently
#      overwrite the other's. The MDCAT mocks hit this repeatedly; check it
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


def check_sample_bank_collisions(questions):
    """(question_text, option_a) must not collide with the official sample bank."""
    try:
        from lums_lcat_sample import QUESTIONS as SAMPLE
    except ImportError:
        print("\nCould not import lums_lcat_sample -- collision check SKIPPED.")
        return []
    sample_keys = {(q["question"], q["options"]["A"]) for q in SAMPLE}
    clashes = [q["id"] for q in questions if (q["question"], q["options"]["A"]) in sample_keys]
    if clashes:
        print(f"\nCOLLISION with lums_lcat_sample.py on ids: {clashes}")
    else:
        print("Zero (question_text, option_a) overlap with the official sample bank. OK.")
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
    check_sample_bank_collisions(questions)


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
