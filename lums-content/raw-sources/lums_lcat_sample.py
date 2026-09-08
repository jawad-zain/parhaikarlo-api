"""
LUMS Common Admission Test (LCAT) - Sample Question Bank
==========================================================
Sample questions for Verbal & Math sections, based on LUMS' official
"Sample Questions for Verbal & Math Sections" guide.

Sections: Verbal (14 Qs) | Math (10 Qs)
Test format: multiple-choice, no calculator allowed in Math.

Each question is a dict:
    id, subject, topic, difficulty, question, options (A-D), answer (correct letter)

Run this file directly to print a summary / sanity-check the paper.

NOTE: The source PDF did not provide an official answer key. Answers below
were worked out from the question content itself (grammar/logic for Verbal,
calculation for Math). Double-check against an official key if one is
released, and treat this as a study aid rather than a graded past paper.
"""

QUESTIONS = [

# ============================================================
# VERBAL (14) - id 1-14
# ============================================================

{"id":1,"subject":'Verbal',"topic":'Craft and Structure',"difficulty":'Easy',
 "question":"A travelogue about exploring Pakistan's diverse landscapes is structured around different regions, each section highlighting the unique ____ of each area, from the bustling streets of Karachi to the serene valleys of Gilgit-Baltistan.",
 "options":{"A":'challenges', "B":'characteristics', "C":'monotony', "D":'disadvantages'},"answer":'B'},

{"id":2,"subject":'Verbal',"topic":'Information and Ideas',"difficulty":'Medium',
 "question":'In preparation for a presentation on Sadequain, a renowned Pakistani artist, a student compiles observations that his art frequently explores themes of struggle and transformation, that "The Sun" (1962) is characterized by bold calligraphic strokes, and that "Human Suffering" (1971) depicts figures in distress. Which statement best synthesizes these observations to link "The Sun" and "Human Suffering"?',
 "options":{"A":'Sadequain\'s "The Sun" and "Human Suffering" both express themes of struggle and transformation through their distinctive styles.',
            "B":'Both "The Sun" and "Human Suffering" showcase Sadequain\'s expertise in depicting human emotions.',
            "C":'"The Sun" and "Human Suffering" were created in different decades but by the same artist, Sadequain.',
            "D":'"The Sun" uses calligraphy, and "Human Suffering" portrays human figures, illustrating the artist\'s range.'},"answer":'A'},

{"id":3,"subject":'Verbal',"topic":'Craft and Structure',"difficulty":'Medium',
 "question":'A research paper examines the geographical and cultural boundaries within Pakistan, focusing on how these boundaries have ____ over time, influenced by historical, political, and social factors.',
 "options":{"A":'diminished', "B":'fluctuated', "C":'remained static', "D":'become indistinct'},"answer":'B'},

{"id":4,"subject":'Verbal',"topic":'Expression of Ideas',"difficulty":'Easy',
 "question":'Technological advancements have greatly improved life quality. They have led to significant medical breakthroughs and enhanced global communication. Which transition word or phrase would be most appropriate to link these two ideas?',
 "options":{"A":'Nevertheless,', "B":'Consequently,', "C":'In contrast,', "D":'Besides,'},"answer":'B'},

{"id":5,"subject":'Verbal',"topic":'Information and Ideas',"difficulty":'Medium',
 "question":"The book 'The Social Fabric: Understanding Community Dynamics' discusses the evolving nature of community structures in modern society, examining the role of technology, economic shifts, and cultural changes. Which of the following would best support the book's analysis of contemporary community dynamics?",
 "options":{"A":'Historical accounts of community structures in ancient civilizations.',
            "B":'Statistical data on current trends in community living and interaction.',
            "C":'Predictions about future technological innovations.',
            "D":'Personal anecdotes from individuals about their community experiences.'},"answer":'B'},

{"id":6,"subject":'Verbal',"topic":'Information and Ideas',"difficulty":'Medium',
 "question":"In the historical account 'The Age of Exploration,' the author describes explorers' motivations for undertaking risky voyages, their encounters with new lands and peoples, and the impact on global trade and cultural exchanges, portraying their perseverance in the face of adversity. What can be inferred about the author's perspective on the explorers?",
 "options":{"A":"The author disapproves of the explorers' motivations.",
            "B":'The author views the explorers as primarily motivated by greed.',
            "C":"The author admires the explorers' courage and determination.",
            "D":'The author believes the explorers had a negative impact on global trade.'},"answer":'C'},

{"id":7,"subject":'Verbal',"topic":'Standard English Conventions',"difficulty":'Medium',
 "question":'In the world of modern technology, smartphones have become an indispensable tool for communication and convenience ____ revolutionized the way we connect with others, access information, and perform everyday tasks. Which choice completes the text so that it conforms to the conventions of Standard English?',
 "options":{"A":'smartphones, they have', "B":'smartphones, which they', "C":'smartphones, it has', "D":'smartphones, and they have'},"answer":'D'},

{"id":8,"subject":'Verbal',"topic":'Expression of Ideas',"difficulty":'Hard',
 "question":'"...smartphones have become an indispensable tool for communication and convenience. They have revolutionized the way we connect with others, access information, and perform everyday tasks. Many people rely on them for work, social interaction, and entertainment, ____." Choose the option that best completes the sentence while maintaining Standard English grammar.',
 "options":{"A":'making them an integral part of daily life.',
            "B":'therefore, they are seen as essential by many.',
            "C":'which is why they have become so widespread.',
            "D":'and this has led to their widespread use.'},"answer":'A'},

{"id":9,"subject":'Verbal',"topic":'Craft and Structure',"difficulty":'Medium',
 "question":'As the debate over the new environmental policy intensified, proponents argued that it was essential for the future sustainability of the planet, while opponents ____ its potential economic impact as overly burdensome and unnecessary.',
 "options":{"A":'disregarded', "B":'exaggerated', "C":'understated', "D":'evaluated'},"answer":'B'},

{"id":10,"subject":'Verbal',"topic":'Information and Ideas',"difficulty":'Medium',
 "question":'Passage: In the upcoming national elections, young voters have risen from 46.43 million to 56.86 million in six years (a 22.5% increase), now 44.22% of the 128.58 million total voters, and are more informed and engaged thanks to social media. Which statement best summarizes the role and potential influence of this demographic group?',
 "options":{"A":'Young voters, constituting nearly half of the total voter count, have the potential to significantly influence election outcomes, especially with their increased engagement through social media.',
            "B":'The majority of young voters are located in Punjab and Sindh, indicating a probable focus of election campaigns in these regions.',
            "C":'Young female voters are the majority in the young voter demographic, indicating a shift in gender dynamics within the electoral process.',
            "D":'The rise in young voters is primarily concentrated in urban areas, suggesting a shift in political focus to city-based issues.'},"answer":'A'},

{"id":11,"subject":'Verbal',"topic":'Information and Ideas',"difficulty":'Easy',
 "question":'According to the passage, how has social media influenced young voters?',
 "options":{"A":'Reduced their number', "B":'Increased their political engagement', "C":'Decreased voter turnout', "D":'Caused a gender gap'},"answer":'B'},

{"id":12,"subject":'Verbal',"topic":'Information and Ideas',"difficulty":'Easy',
 "question":'What trend is indicated by the narrowing gender gap among young voters in the passage?',
 "options":{"A":'Decreased political interest', "B":'Increased female voter participation', "C":'Unchanged electoral landscape', "D":'Decreased male voter participation'},"answer":'B'},

{"id":13,"subject":'Verbal',"topic":'Information and Ideas',"difficulty":'Medium',
 "question":'According to the passage, what role are young voters expected to play in the upcoming elections?',
 "options":{"A":'Decrease voter turnout', "B":'Have no significant impact', "C":'Play a crucial role in determining outcomes', "D":'Focus only on social media campaigns'},"answer":'C'},

{"id":14,"subject":'Verbal',"topic":'Information and Ideas',"difficulty":'Medium',
 "question":'Which statement best summarizes the passage as a whole?',
 "options":{"A":'The number of young voters has decreased significantly.',
            "B":'Young voters are less informed due to social media.',
            "C":'Young voters are set to have a substantial impact in the upcoming elections.',
            "D":'The gender gap among young voters is increasing.'},"answer":'C'},

# ============================================================
# MATH (10) - id 15-24
# ============================================================

{"id":15,"subject":'Math',"topic":'Advanced Mathematics',"difficulty":'Medium',
 "question":'A company models its profit, P, in thousands of dollars, based on the number of products sold, x, in thousands, with the equation P(x) = x^2 - 3x + 2. Determine the number of thousands of products the company must sell to break even (profit of 0).',
 "options":{"A":'1 thousand products', "B":'2 thousand products', "C":'3 thousand products', "D":'Both options A) and B) are correct'},"answer":'D'},

{"id":16,"subject":'Math',"topic":'Geometry and Trigonometry',"difficulty":'Easy',
 "question":'In a right triangle with legs a and b, and hypotenuse c, if a = 10 and b = 24, what is the value of c?',
 "options":{"A":'26', "B":'28', "C":'30', "D":'32'},"answer":'A'},

{"id":17,"subject":'Math',"topic":'Problem-Solving and Data Analysis',"difficulty":'Medium',
 "question":'A car travels at varying speeds. If it covers 120 miles in the first 2 hours and 160 miles in the next 3 hours, what is its average speed over the entire trip?',
 "options":{"A":'40 mph', "B":'45 mph', "C":'50 mph', "D":'56 mph'},"answer":'D'},

{"id":18,"subject":'Math',"topic":'Algebra',"difficulty":'Easy',
 "question":'An arithmetic sequence has a first term of a1 = 3 and a common difference of d = -2. What is the 8th term of the sequence?',
 "options":{"A":'-11', "B":'-13', "C":'-15', "D":'-17'},"answer":'A'},

{"id":19,"subject":'Math',"topic":'Problem-Solving and Data Analysis',"difficulty":'Medium',
 "question":"A computer's price is reduced by 15% for a sale, and then an additional $50 off is applied. If the original price is $800, what is the final sale price?",
 "options":{"A":'$610', "B":'$630', "C":'$660', "D":'$685'},"answer":'B'},

{"id":20,"subject":'Math',"topic":'Geometry and Trigonometry',"difficulty":'Easy',
 "question":'Calculate the area of a trapezoid with bases of lengths 8 cm and 12 cm and a height of 5 cm.',
 "options":{"A":'50 cm^2', "B":'60 cm^2', "C":'70 cm^2', "D":'80 cm^2'},"answer":'A'},

{"id":21,"subject":'Math',"topic":'Advanced Mathematics',"difficulty":'Medium',
 "question":'What is the sum of the solutions for 2x^2 + 7x - 3 = 0?',
 "options":{"A":'-1', "B":'3', "C":'-7/2', "D":'5'},"answer":'C'},

{"id":22,"subject":'Math',"topic":'Advanced Mathematics',"difficulty":'Hard',
 "question":'Given that log_x 16 = 4 and log_x 2 = y, find the value of y.',
 "options":{"A":'1', "B":'2', "C":'3', "D":'4'},"answer":'A'},

{"id":23,"subject":'Math',"topic":'Geometry and Trigonometry',"difficulty":'Hard',
 "question":'In a circle with radius 5 cm, what is the length of an arc subtending a central angle of 3pi/2 radians?',
 "options":{"A":'7.5pi cm', "B":'20pi cm', "C":'11.78 cm', "D":'15pi cm'},"answer":'A'},

{"id":24,"subject":'Math',"topic":'Geometry and Trigonometry',"difficulty":'Hard',
 "question":'If tan(theta) = 3/4 and sin(theta) < 0, what is the value of cos(theta)?',
 "options":{"A":'-1/5', "B":'-3/5', "C":'-4/5', "D":'-2/5'},"answer":'C'},

]


# ------------------------------------------------------------
# Sanity-check / summary utility
# ------------------------------------------------------------
def summarize(questions):
    from collections import Counter
    subj = Counter(q["subject"] for q in questions)
    topic = Counter(q["topic"] for q in questions)
    diff = Counter(q["difficulty"] for q in questions)
    ans = Counter(q["answer"] for q in questions)
    ids = [q["id"] for q in questions]
    dup_ids = [i for i in set(ids) if ids.count(i) > 1]
    dup_q = [q["question"] for q in questions]
    dup_questions = [t for t in set(dup_q) if dup_q.count(t) > 1]

    print(f"Total questions: {len(questions)}")
    print("\nBy subject:")
    for s, c in subj.items():
        print(f"  {s}: {c}")
    print("\nBy topic:")
    for t, c in topic.items():
        print(f"  {t}: {c}")
    print("\nBy difficulty:")
    for d, c in diff.items():
        print(f"  {d}: {c}")
    print("\nBy correct-answer letter:")
    for L in ["A", "B", "C", "D"]:
        print(f"  {L}: {ans[L]}")
    print(f"\nDuplicate IDs: {dup_ids if dup_ids else 'None'}")
    print(f"Duplicate question text: {dup_questions if dup_questions else 'None'}")

    for q in questions:
        assert set(q["options"].keys()) == {"A", "B", "C", "D"}, f"Q{q['id']} missing an option"
        assert q["answer"] in q["options"], f"Q{q['id']} answer key invalid"
    print("\nAll questions have exactly 4 options (A-D) and a valid answer key. OK.")


def print_answer_key(questions):
    print("\nANSWER KEY")
    print("-" * 40)
    for q in questions:
        print(f"{q['id']:>3}. {q['answer']}", end="   ")
        if q["id"] % 10 == 0:
            print()
    print()


if __name__ == "__main__":
    summarize(QUESTIONS)
    print_answer_key(QUESTIONS)
