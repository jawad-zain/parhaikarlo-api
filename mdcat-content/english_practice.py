"""
MDCAT English Question Bank
===========================
200 MCQs modeled on the MDCAT (Punjab / PMDC) English syllabus,
same Python dict format as the biology / physics banks.

Topic distribution (approx):
    Synonyms .......................... 25
    Antonyms .......................... 20
    Prepositions ...................... 20
    Tenses ............................ 15
    Articles .......................... 10
    Subject-Verb Agreement ............ 10
    Active / Passive Voice ............ 10
    Direct / Indirect Speech .......... 10
    Sentence Correction ............... 20
    Choose the Correct Sentence ....... 15
    Idioms & Phrases .................. 15
    One-Word Substitution ............. 10
    Analogies ......................... 10
    Vocabulary in Context ............. 10
    Total ............................ 200

Difficulty mix ~ 30% Easy / 50% Medium / 20% Hard.

Each question is a dict:
    id, subject, topic, subtopic, difficulty, question, options (A-D), answer
"""

QUESTIONS = [

# ============================================================
# SYNONYMS (25)  id 1-25
# ============================================================

{"id":1,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Easy',
 "question":'Choose the word most similar in meaning to: ABUNDANT',
 "options":{"A":'Scarce',"B":'Plentiful',"C":'Empty',"D":'Rare'},"answer":'B'},

{"id":2,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Easy',
 "question":'Choose the word most similar in meaning to: BRAVE',
 "options":{"A":'Cowardly',"B":'Timid',"C":'Weak',"D":'Courageous'},"answer":'D'},

{"id":3,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Easy',
 "question":'Choose the word most similar in meaning to: BEGIN',
 "options":{"A":'Stop',"B":'End',"C":'Commence',"D":'Finish'},"answer":'C'},

{"id":4,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Easy',
 "question":'Choose the word most similar in meaning to: HAPPY',
 "options":{"A":'Sad',"B":'Angry',"C":'Tired',"D":'Joyful'},"answer":'D'},

{"id":5,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Easy',
 "question":'Choose the word most similar in meaning to: BIG',
 "options":{"A":'Small',"B":'Tiny',"C":'Huge',"D":'Narrow'},"answer":'C'},

{"id":6,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: BENEVOLENT',
 "options":{"A":'Cruel',"B":'Selfish',"C":'Kind',"D":'Rude'},"answer":'C'},

{"id":7,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: CANDID',
 "options":{"A":'Frank',"B":'Secretive',"C":'Dishonest',"D":'Rude'},"answer":'A'},

{"id":8,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: DILIGENT',
 "options":{"A":'Hard-working',"B":'Lazy',"C":'Careless',"D":'Slow'},"answer":'A'},

{"id":9,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: FEROCIOUS',
 "options":{"A":'Gentle',"B":'Fierce',"C":'Calm',"D":'Weak'},"answer":'B'},

{"id":10,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: LUCID',
 "options":{"A":'Clear',"B":'Confusing',"C":'Dark',"D":'Complex'},"answer":'A'},

{"id":11,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: METICULOUS',
 "options":{"A":'Careless',"B":'Rapid',"C":'Careful and precise',"D":'Loud'},"answer":'C'},

{"id":12,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: NOVICE',
 "options":{"A":'Expert',"B":'Master',"C":'Veteran',"D":'Beginner'},"answer":'D'},

{"id":13,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: OBSOLETE',
 "options":{"A":'Modern',"B":'Popular',"C":'Outdated',"D":'Useful'},"answer":'C'},

{"id":14,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: OPTIMISTIC',
 "options":{"A":'Pessimistic',"B":'Hopeful',"C":'Angry',"D":'Doubtful'},"answer":'B'},

{"id":15,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: PROVOKE',
 "options":{"A":'Soothe',"B":'Calm',"C":'Praise',"D":'Incite'},"answer":'D'},

{"id":16,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: RELUCTANT',
 "options":{"A":'Eager',"B":'Willing',"C":'Happy',"D":'Unwilling'},"answer":'D'},

{"id":17,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: SCRUTINIZE',
 "options":{"A":'Examine closely',"B":'Ignore',"C":'Overlook',"D":'Approve'},"answer":'A'},

{"id":18,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: TRIVIAL',
 "options":{"A":'Important',"B":'Serious',"C":'Insignificant',"D":'Huge'},"answer":'C'},

{"id":19,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: VIGILANT',
 "options":{"A":'Watchful',"B":'Careless',"C":'Sleepy',"D":'Weak'},"answer":'A'},

{"id":20,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word most similar in meaning to: ZEAL',
 "options":{"A":'Enthusiasm',"B":'Indifference',"C":'Boredom',"D":'Tiredness'},"answer":'A'},

{"id":21,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Hard',
 "question":'Choose the word most similar in meaning to: EPHEMERAL',
 "options":{"A":'Everlasting',"B":'Eternal',"C":'Permanent',"D":'Short-lived'},"answer":'D'},

{"id":22,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Hard',
 "question":'Choose the word most similar in meaning to: LOQUACIOUS',
 "options":{"A":'Talkative',"B":'Silent',"C":'Shy',"D":'Rude'},"answer":'A'},

{"id":23,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Hard',
 "question":'Choose the word most similar in meaning to: PERNICIOUS',
 "options":{"A":'Harmful',"B":'Beneficial',"C":'Neutral',"D":'Attractive'},"answer":'A'},

{"id":24,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Hard',
 "question":'Choose the word most similar in meaning to: UBIQUITOUS',
 "options":{"A":'Rare',"B":'Hidden',"C":'Present everywhere',"D":'Limited'},"answer":'C'},

{"id":25,"subject":'English',"topic":'Synonyms',"subtopic":'General',"difficulty":'Hard',
 "question":'Choose the word most similar in meaning to: TACITURN',
 "options":{"A":'Talkative',"B":'Cheerful',"C":'Loud',"D":'Reserved'},"answer":'D'},

# ============================================================
# ANTONYMS (20)  id 26-45
# ============================================================

{"id":26,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Easy',
 "question":'Choose the word opposite in meaning to: ANCIENT',
 "options":{"A":'Old',"B":'Aged',"C":'Historic',"D":'Modern'},"answer":'D'},

{"id":27,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Easy',
 "question":'Choose the word opposite in meaning to: FRIEND',
 "options":{"A":'Enemy',"B":'Companion',"C":'Ally',"D":'Partner'},"answer":'A'},

{"id":28,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Easy',
 "question":'Choose the word opposite in meaning to: RICH',
 "options":{"A":'Wealthy',"B":'Prosperous',"C":'Poor',"D":'Affluent'},"answer":'C'},

{"id":29,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Easy',
 "question":'Choose the word opposite in meaning to: STRONG',
 "options":{"A":'Weak',"B":'Powerful',"C":'Sturdy',"D":'Robust'},"answer":'A'},

{"id":30,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Easy',
 "question":'Choose the word opposite in meaning to: HONEST',
 "options":{"A":'Truthful',"B":'Sincere',"C":'Loyal',"D":'Deceitful'},"answer":'D'},

{"id":31,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Easy',
 "question":'Choose the word opposite in meaning to: ACCEPT',
 "options":{"A":'Reject',"B":'Receive',"C":'Take',"D":'Approve'},"answer":'A'},

{"id":32,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word opposite in meaning to: ARROGANT',
 "options":{"A":'Proud',"B":'Confident',"C":'Humble',"D":'Bold'},"answer":'C'},

{"id":33,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word opposite in meaning to: BARREN',
 "options":{"A":'Fertile',"B":'Empty',"C":'Dry',"D":'Bare'},"answer":'A'},

{"id":34,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word opposite in meaning to: CONCEAL',
 "options":{"A":'Reveal',"B":'Hide',"C":'Cover',"D":'Mask'},"answer":'A'},

{"id":35,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word opposite in meaning to: DENSE',
 "options":{"A":'Thick',"B":'Compact',"C":'Heavy',"D":'Sparse'},"answer":'D'},

{"id":36,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word opposite in meaning to: EXPAND',
 "options":{"A":'Grow',"B":'Contract',"C":'Enlarge',"D":'Spread'},"answer":'B'},

{"id":37,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word opposite in meaning to: FRAGILE',
 "options":{"A":'Delicate',"B":'Sturdy',"C":'Weak',"D":'Brittle'},"answer":'B'},

{"id":38,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word opposite in meaning to: GENUINE',
 "options":{"A":'Real',"B":'Authentic',"C":'True',"D":'Fake'},"answer":'D'},

{"id":39,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word opposite in meaning to: HOSTILE',
 "options":{"A":'Friendly',"B":'Aggressive',"C":'Angry',"D":'Rude'},"answer":'A'},

{"id":40,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word opposite in meaning to: IGNORE',
 "options":{"A":'Disregard',"B":'Overlook',"C":'Neglect',"D":'Notice'},"answer":'D'},

{"id":41,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Medium',
 "question":'Choose the word opposite in meaning to: PROSPERITY',
 "options":{"A":'Wealth',"B":'Success',"C":'Fortune',"D":'Adversity'},"answer":'D'},

{"id":42,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Hard',
 "question":'Choose the word opposite in meaning to: ABSTRUSE',
 "options":{"A":'Difficult',"B":'Clear',"C":'Complex',"D":'Obscure'},"answer":'B'},

{"id":43,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Hard',
 "question":'Choose the word opposite in meaning to: CACOPHONY',
 "options":{"A":'Harmony',"B":'Noise',"C":'Din',"D":'Uproar'},"answer":'A'},

{"id":44,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Hard',
 "question":'Choose the word opposite in meaning to: FRUGAL',
 "options":{"A":'Economical',"B":'Thrifty',"C":'Extravagant',"D":'Sparing'},"answer":'C'},

{"id":45,"subject":'English',"topic":'Antonyms',"subtopic":'General',"difficulty":'Hard',
 "question":'Choose the word opposite in meaning to: NADIR',
 "options":{"A":'Bottom',"B":'Depth',"C":'Base',"D":'Zenith'},"answer":'D'},

# ============================================================
# PREPOSITIONS (20)  id 46-65
# ============================================================

{"id":46,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Easy',
 "question":'She is good ___ mathematics.',
 "options":{"A":'in',"B":'at',"C":'on',"D":'with'},"answer":'B'},

{"id":47,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Easy',
 "question":'He is afraid ___ dogs.',
 "options":{"A":'from',"B":'with',"C":'of',"D":'to'},"answer":'C'},

{"id":48,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Easy',
 "question":'The book belongs ___ me.',
 "options":{"A":'with',"B":'for',"C":'to',"D":'of'},"answer":'C'},

{"id":49,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Easy',
 "question":'She has been living in Lahore ___ 2010.',
 "options":{"A":'for',"B":'since',"C":'from',"D":'in'},"answer":'B'},

{"id":50,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Easy',
 "question":'I have known him ___ five years.',
 "options":{"A":'since',"B":'from',"C":'for',"D":'in'},"answer":'C'},

{"id":51,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Medium',
 "question":'He is jealous ___ his brother.',
 "options":{"A":'from',"B":'with',"C":'of',"D":'about'},"answer":'C'},

{"id":52,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Medium',
 "question":'She is fond ___ music.',
 "options":{"A":'for',"B":'of',"C":'with',"D":'in'},"answer":'B'},

{"id":53,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Medium',
 "question":'He is angry ___ me for being late.',
 "options":{"A":'on',"B":'at',"C":'with',"D":'from'},"answer":'C'},

{"id":54,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Medium',
 "question":'The teacher was pleased ___ his answer.',
 "options":{"A":'from',"B":'on',"C":'with',"D":'about'},"answer":'C'},

{"id":55,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Medium',
 "question":'She insisted ___ paying the bill.',
 "options":{"A":'on',"B":'in',"C":'for',"D":'at'},"answer":'A'},

{"id":56,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Medium',
 "question":'He apologized ___ his rude behavior.',
 "options":{"A":'for',"B":'from',"C":'about',"D":'on'},"answer":'A'},

{"id":57,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Medium',
 "question":'They congratulated her ___ her success.',
 "options":{"A":'for',"B":'with',"C":'about',"D":'on'},"answer":'D'},

{"id":58,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Medium',
 "question":'He is married ___ a doctor.',
 "options":{"A":'with',"B":'from',"C":'by',"D":'to'},"answer":'D'},

{"id":59,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Medium',
 "question":'The house is made ___ bricks.',
 "options":{"A":'of',"B":'from',"C":'with',"D":'by'},"answer":'A'},

{"id":60,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Medium',
 "question":'Wine is made ___ grapes.',
 "options":{"A":'of',"B":'from',"C":'with',"D":'by'},"answer":'B'},

{"id":61,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Medium',
 "question":'He died ___ malaria.',
 "options":{"A":'from',"B":'with',"C":'of',"D":'by'},"answer":'C'},

{"id":62,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Hard',
 "question":'She is oblivious ___ her surroundings.',
 "options":{"A":'to',"B":'from',"C":'of',"D":'about'},"answer":'A'},

{"id":63,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Hard',
 "question":'He was accused ___ theft.',
 "options":{"A":'for',"B":'with',"C":'about',"D":'of'},"answer":'D'},

{"id":64,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Hard',
 "question":'The book is dedicated ___ his mother.',
 "options":{"A":'for',"B":'with',"C":'from',"D":'to'},"answer":'D'},

{"id":65,"subject":'English',"topic":'Prepositions',"subtopic":'Verb+Prep',"difficulty":'Hard',
 "question":'He is bent ___ becoming a doctor.',
 "options":{"A":'in',"B":'for',"C":'on',"D":'with'},"answer":'C'},

# ============================================================
# TENSES (15)  id 66-80
# ============================================================

{"id":66,"subject":'English',"topic":'Tenses',"subtopic":'Present',"difficulty":'Easy',
 "question":'She ___ to school every day.',
 "options":{"A":'go',"B":'goes',"C":'going',"D":'gone'},"answer":'B'},

{"id":67,"subject":'English',"topic":'Tenses',"subtopic":'Present Continuous',"difficulty":'Easy',
 "question":'They ___ football right now.',
 "options":{"A":'play',"B":'plays',"C":'are playing',"D":'played'},"answer":'C'},

{"id":68,"subject":'English',"topic":'Tenses',"subtopic":'Past',"difficulty":'Easy',
 "question":'He ___ to Karachi last week.',
 "options":{"A":'went',"B":'go',"C":'goes',"D":'gone'},"answer":'A'},

{"id":69,"subject":'English',"topic":'Tenses',"subtopic":'Present Perfect',"difficulty":'Easy',
 "question":'I ___ my homework already.',
 "options":{"A":'have finished',"B":'finish',"C":'finished',"D":'will finish'},"answer":'A'},

{"id":70,"subject":'English',"topic":'Tenses',"subtopic":'Future',"difficulty":'Easy',
 "question":'She ___ arrive tomorrow.',
 "options":{"A":'is',"B":'has',"C":'was',"D":'will'},"answer":'D'},

{"id":71,"subject":'English',"topic":'Tenses',"subtopic":'Past Continuous',"difficulty":'Medium',
 "question":'While I ___ , the phone rang.',
 "options":{"A":'sleep',"B":'slept',"C":'was sleeping',"D":'have slept'},"answer":'C'},

{"id":72,"subject":'English',"topic":'Tenses',"subtopic":'Past Perfect',"difficulty":'Medium',
 "question":'By the time she arrived, the train ___ .',
 "options":{"A":'leaves',"B":'left',"C":'has left',"D":'had left'},"answer":'D'},

{"id":73,"subject":'English',"topic":'Tenses',"subtopic":'Present Perfect Continuous',"difficulty":'Medium',
 "question":'He ___ here for three hours.',
 "options":{"A":'waits',"B":'has been waiting',"C":'waited',"D":'is waiting'},"answer":'B'},

{"id":74,"subject":'English',"topic":'Tenses',"subtopic":'Future Continuous',"difficulty":'Medium',
 "question":'This time tomorrow, I ___ in the plane.',
 "options":{"A":'sit',"B":'will be sitting',"C":'will sit',"D":'am sitting'},"answer":'B'},

{"id":75,"subject":'English',"topic":'Tenses',"subtopic":'Future Perfect',"difficulty":'Medium',
 "question":'By next year, they ___ their new house.',
 "options":{"A":'complete',"B":'completed',"C":'will complete',"D":'will have completed'},"answer":'D'},

{"id":76,"subject":'English',"topic":'Tenses',"subtopic":'Present',"difficulty":'Medium',
 "question":'Water ___ at 100 degrees Celsius.',
 "options":{"A":'boils',"B":'boil',"C":'is boiling',"D":'boiled'},"answer":'A'},

{"id":77,"subject":'English',"topic":'Tenses',"subtopic":'Past Perfect',"difficulty":'Medium',
 "question":'She said she ___ him before.',
 "options":{"A":'meets',"B":'met',"C":'had met',"D":'has met'},"answer":'C'},

{"id":78,"subject":'English',"topic":'Tenses',"subtopic":'Conditional',"difficulty":'Hard',
 "question":'If I ___ rich, I would travel the world.',
 "options":{"A":'am',"B":'were',"C":'was',"D":'be'},"answer":'B'},

{"id":79,"subject":'English',"topic":'Tenses',"subtopic":'Conditional',"difficulty":'Hard',
 "question":'If it ___ tomorrow, we will cancel the picnic.',
 "options":{"A":'rain',"B":'rains',"C":'rained',"D":'will rain'},"answer":'B'},

{"id":80,"subject":'English',"topic":'Tenses',"subtopic":'Conditional',"difficulty":'Hard',
 "question":'If she had studied, she ___ passed the exam.',
 "options":{"A":'would',"B":'will have',"C":'has',"D":'would have'},"answer":'D'},

# ============================================================
# ARTICLES (10)  id 81-90
# ============================================================

{"id":81,"subject":'English',"topic":'Articles',"subtopic":'a/an/the',"difficulty":'Easy',
 "question":'I saw ___ elephant at the zoo.',
 "options":{"A":'a',"B":'an',"C":'the',"D":'no article'},"answer":'B'},

{"id":82,"subject":'English',"topic":'Articles',"subtopic":'a/an/the',"difficulty":'Easy',
 "question":'She is ___ honest woman.',
 "options":{"A":'a',"B":'the',"C":'an',"D":'no article'},"answer":'C'},

{"id":83,"subject":'English',"topic":'Articles',"subtopic":'a/an/the',"difficulty":'Easy',
 "question":'He is ___ university student.',
 "options":{"A":'an',"B":'the',"C":'a',"D":'no article'},"answer":'C'},

{"id":84,"subject":'English',"topic":'Articles',"subtopic":'a/an/the',"difficulty":'Easy',
 "question":'___ sun rises in the east.',
 "options":{"A":'A',"B":'An',"C":'The',"D":'No article'},"answer":'C'},

{"id":85,"subject":'English',"topic":'Articles',"subtopic":'a/an/the',"difficulty":'Medium',
 "question":'She plays ___ piano beautifully.',
 "options":{"A":'a',"B":'an',"C":'the',"D":'no article'},"answer":'C'},

{"id":86,"subject":'English',"topic":'Articles',"subtopic":'a/an/the',"difficulty":'Medium',
 "question":'I want to become ___ engineer.',
 "options":{"A":'an',"B":'a',"C":'the',"D":'no article'},"answer":'A'},

{"id":87,"subject":'English',"topic":'Articles',"subtopic":'a/an/the',"difficulty":'Medium',
 "question":'___ Nile is the longest river in Africa.',
 "options":{"A":'The',"B":'A',"C":'An',"D":'No article'},"answer":'A'},

{"id":88,"subject":'English',"topic":'Articles',"subtopic":'a/an/the',"difficulty":'Medium',
 "question":'He speaks ___ English very well.',
 "options":{"A":'a',"B":'an',"C":'no article',"D":'the'},"answer":'C'},

{"id":89,"subject":'English',"topic":'Articles',"subtopic":'a/an/the',"difficulty":'Hard',
 "question":'She is ___ MBBS doctor.',
 "options":{"A":'a',"B":'the',"C":'an',"D":'no article'},"answer":'C'},

{"id":90,"subject":'English',"topic":'Articles',"subtopic":'a/an/the',"difficulty":'Hard',
 "question":'He goes to ___ mosque every Friday.',
 "options":{"A":'a',"B":'an',"C":'the',"D":'no article'},"answer":'D'},

# ============================================================
# SUBJECT-VERB AGREEMENT (10)  id 91-100
# ============================================================

{"id":91,"subject":'English',"topic":'Subject-Verb Agreement',"subtopic":'Basic',"difficulty":'Easy',
 "question":'The team ___ playing well.',
 "options":{"A":'are',"B":'is',"C":'were',"D":'be'},"answer":'B'},

{"id":92,"subject":'English',"topic":'Subject-Verb Agreement',"subtopic":'Basic',"difficulty":'Easy',
 "question":'Each of the boys ___ a bag.',
 "options":{"A":'have',"B":'has',"C":'are',"D":'were'},"answer":'B'},

{"id":93,"subject":'English',"topic":'Subject-Verb Agreement',"subtopic":'Basic',"difficulty":'Easy',
 "question":'Neither Ali nor Ahmed ___ present.',
 "options":{"A":'are',"B":'were',"C":'is',"D":'be'},"answer":'C'},

{"id":94,"subject":'English',"topic":'Subject-Verb Agreement',"subtopic":'Basic',"difficulty":'Medium',
 "question":'The news ___ shocking.',
 "options":{"A":'are',"B":'were',"C":'is',"D":'have'},"answer":'C'},

{"id":95,"subject":'English',"topic":'Subject-Verb Agreement',"subtopic":'Basic',"difficulty":'Medium',
 "question":'Mathematics ___ my favorite subject.',
 "options":{"A":'are',"B":'were',"C":'have',"D":'is'},"answer":'D'},

{"id":96,"subject":'English',"topic":'Subject-Verb Agreement',"subtopic":'Basic',"difficulty":'Medium',
 "question":'One of the boys ___ absent.',
 "options":{"A":'are',"B":'is',"C":'were',"D":'have'},"answer":'B'},

{"id":97,"subject":'English',"topic":'Subject-Verb Agreement',"subtopic":'Basic',"difficulty":'Medium',
 "question":'The scissors ___ on the table.',
 "options":{"A":'are',"B":'is',"C":'was',"D":'be'},"answer":'A'},

{"id":98,"subject":'English',"topic":'Subject-Verb Agreement',"subtopic":'Basic',"difficulty":'Medium',
 "question":'Ten kilometers ___ a long distance.',
 "options":{"A":'are',"B":'were',"C":'have',"D":'is'},"answer":'D'},

{"id":99,"subject":'English',"topic":'Subject-Verb Agreement',"subtopic":'Basic',"difficulty":'Hard',
 "question":'Either you or he ___ wrong.',
 "options":{"A":'are',"B":'were',"C":'is',"D":'have'},"answer":'C'},

{"id":100,"subject":'English',"topic":'Subject-Verb Agreement',"subtopic":'Basic',"difficulty":'Hard',
 "question":'A number of students ___ absent today.',
 "options":{"A":'is',"B":'are',"C":'was',"D":'has'},"answer":'B'},

# ============================================================
# ACTIVE / PASSIVE VOICE (10)  id 101-110
# ============================================================

{"id":101,"subject":'English',"topic":'Active-Passive Voice',"subtopic":'Simple Present',"difficulty":'Easy',
 "question":'Change to passive: "She writes a letter."',
 "options":{"A":'A letter was written by her.',"B":'A letter has written by her.',"C":'A letter writes by her.',"D":'A letter is written by her.'},"answer":'D'},

{"id":102,"subject":'English',"topic":'Active-Passive Voice',"subtopic":'Simple Past',"difficulty":'Easy',
 "question":'Change to passive: "He ate an apple."',
 "options":{"A":'An apple was eaten by him.',"B":'An apple is eaten by him.',"C":'An apple has been eaten by him.',"D":'An apple was eating by him.'},"answer":'A'},

{"id":103,"subject":'English',"topic":'Active-Passive Voice',"subtopic":'Simple Future',"difficulty":'Easy',
 "question":'Change to passive: "They will build a house."',
 "options":{"A":'A house will be built by them.',"B":'A house is built by them.',"C":'A house was built by them.',"D":'A house has been built by them.'},"answer":'A'},

{"id":104,"subject":'English',"topic":'Active-Passive Voice',"subtopic":'Present Continuous',"difficulty":'Medium',
 "question":'Change to passive: "She is writing a novel."',
 "options":{"A":'A novel is written by her.',"B":'A novel was written by her.',"C":'A novel has been written by her.',"D":'A novel is being written by her.'},"answer":'D'},

{"id":105,"subject":'English',"topic":'Active-Passive Voice',"subtopic":'Past Continuous',"difficulty":'Medium',
 "question":'Change to passive: "They were painting the wall."',
 "options":{"A":'The wall was painted by them.',"B":'The wall was being painted by them.',"C":'The wall is painted by them.',"D":'The wall has been painted by them.'},"answer":'B'},

{"id":106,"subject":'English',"topic":'Active-Passive Voice',"subtopic":'Present Perfect',"difficulty":'Medium',
 "question":'Change to passive: "She has completed the work."',
 "options":{"A":'The work is completed by her.',"B":'The work has been completed by her.',"C":'The work was completed by her.',"D":'The work will be completed by her.'},"answer":'B'},

{"id":107,"subject":'English',"topic":'Active-Passive Voice',"subtopic":'Past Perfect',"difficulty":'Medium',
 "question":'Change to passive: "He had solved the problem."',
 "options":{"A":'The problem was solved by him.',"B":'The problem has been solved by him.',"C":'The problem had been solved by him.',"D":'The problem is solved by him.'},"answer":'C'},

{"id":108,"subject":'English',"topic":'Active-Passive Voice',"subtopic":'Modals',"difficulty":'Hard',
 "question":'Change to passive: "You must obey the rules."',
 "options":{"A":'The rules must obeyed.',"B":'The rules must been obeyed.',"C":'The rules must be obeyed.',"D":'The rules are obeyed.'},"answer":'C'},

{"id":109,"subject":'English',"topic":'Active-Passive Voice',"subtopic":'Imperative',"difficulty":'Hard',
 "question":'Change to passive: "Close the door."',
 "options":{"A":'The door is closed.',"B":'The door was closed.',"C":'The door has been closed.',"D":'Let the door be closed.'},"answer":'D'},

{"id":110,"subject":'English',"topic":'Active-Passive Voice',"subtopic":'Question',"difficulty":'Hard',
 "question":'Change to passive: "Who broke the window?"',
 "options":{"A":'The window was broken by whom?',"B":'Who was broken the window?',"C":'By whom was the window broken?',"D":'By whom the window was broken?'},"answer":'C'},

# ============================================================
# DIRECT / INDIRECT SPEECH (10)  id 111-120
# ============================================================

{"id":111,"subject":'English',"topic":'Direct-Indirect Speech',"subtopic":'Statement',"difficulty":'Easy',
 "question":'Change to indirect: He said, "I am happy."',
 "options":{"A":'He said that he is happy.',"B":'He said that I am happy.',"C":'He said that I was happy.',"D":'He said that he was happy.'},"answer":'D'},

{"id":112,"subject":'English',"topic":'Direct-Indirect Speech',"subtopic":'Statement',"difficulty":'Easy',
 "question":'Change to indirect: She said, "I will come tomorrow."',
 "options":{"A":'She said that she will come tomorrow.',"B":'She said that she comes tomorrow.',"C":'She said that she would come the next day.',"D":'She said that she came the next day.'},"answer":'C'},

{"id":113,"subject":'English',"topic":'Direct-Indirect Speech',"subtopic":'Statement',"difficulty":'Medium',
 "question":'Change to indirect: He said, "I have finished my work."',
 "options":{"A":'He said that he had finished his work.',"B":'He said that he has finished his work.',"C":'He said that he finished his work.',"D":'He said that he finishes his work.'},"answer":'A'},

{"id":114,"subject":'English',"topic":'Direct-Indirect Speech',"subtopic":'Question',"difficulty":'Medium',
 "question":'Change to indirect: She said to me, "Where do you live?"',
 "options":{"A":'She asked me where I lived.',"B":'She asked me where do I live.',"C":'She asked me where I live.',"D":'She said me where I lived.'},"answer":'A'},

{"id":115,"subject":'English',"topic":'Direct-Indirect Speech',"subtopic":'Question',"difficulty":'Medium',
 "question":'Change to indirect: He said, "Are you a student?"',
 "options":{"A":'He asked that was I a student.',"B":'He asked whether are you a student.',"C":'He asked I was a student.',"D":'He asked if I was a student.'},"answer":'D'},

{"id":116,"subject":'English',"topic":'Direct-Indirect Speech',"subtopic":'Command',"difficulty":'Medium',
 "question":'Change to indirect: The teacher said to us, "Sit down."',
 "options":{"A":'The teacher said us that sit down.',"B":'The teacher told that we sit down.',"C":'The teacher told us to sit down.',"D":'The teacher said sit down.'},"answer":'C'},

{"id":117,"subject":'English',"topic":'Direct-Indirect Speech',"subtopic":'Request',"difficulty":'Medium',
 "question":'Change to indirect: He said to me, "Please help me."',
 "options":{"A":'He told me help him.',"B":'He said me please help him.',"C":'He requested me to help him.',"D":'He asked me that help him.'},"answer":'C'},

{"id":118,"subject":'English',"topic":'Direct-Indirect Speech',"subtopic":'Exclamation',"difficulty":'Hard',
 "question":'Change to indirect: She said, "What a beautiful day!"',
 "options":{"A":'She said that it was a beautiful day.',"B":'She said what a beautiful day.',"C":'She exclaimed that it was a very beautiful day.',"D":'She told that day was beautiful.'},"answer":'C'},

{"id":119,"subject":'English',"topic":'Direct-Indirect Speech',"subtopic":'Statement',"difficulty":'Hard',
 "question":'Change to indirect: He said, "The sun rises in the east."',
 "options":{"A":'He said that the sun rose in the east.',"B":'He said the sun had risen in the east.',"C":'He said that the sun rises in the east.',"D":'He told the sun rose in the east.'},"answer":'C'},

{"id":120,"subject":'English',"topic":'Direct-Indirect Speech',"subtopic":'Question',"difficulty":'Hard',
 "question":'Change to indirect: She said to him, "Why are you late?"',
 "options":{"A":'She asked him why he was late.',"B":'She asked him why was he late.',"C":'She asked him why he is late.',"D":'She told him why he was late.'},"answer":'A'},

# ============================================================
# SENTENCE CORRECTION (20)  id 121-140
# ============================================================

{"id":121,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Easy',
 "question":'Identify the error: "He don\'t like coffee."',
 "options":{"A":'He',"B":"don't","C":'like',"D":'coffee'},"answer":'B'},

{"id":122,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Easy',
 "question":'Identify the error: "She go to school every day."',
 "options":{"A":'She',"B":'go',"C":'to school',"D":'every day'},"answer":'B'},

{"id":123,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Easy',
 "question":'Identify the error: "I have visited Paris last year."',
 "options":{"A":'I have',"B":'visited',"C":'Paris',"D":'last year'},"answer":'A'},

{"id":124,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Identify the error: "The furnitures are new."',
 "options":{"A":'The',"B":'furnitures',"C":'are',"D":'new'},"answer":'B'},

{"id":125,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Identify the error: "He is more taller than his brother."',
 "options":{"A":'He is',"B":'than',"C":'his brother',"D":'more taller'},"answer":'D'},

{"id":126,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Identify the error: "One of the boy is absent."',
 "options":{"A":'One of',"B":'is',"C":'the boy',"D":'absent'},"answer":'C'},

{"id":127,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Identify the error: "He is married with a doctor."',
 "options":{"A":'He is',"B":'with',"C":'married',"D":'a doctor'},"answer":'B'},

{"id":128,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Identify the error: "She discussed about the problem."',
 "options":{"A":'She',"B":'about',"C":'discussed',"D":'the problem'},"answer":'B'},

{"id":129,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Identify the error: "The teacher gave us many informations."',
 "options":{"A":'The teacher',"B":'informations',"C":'gave us',"D":'many'},"answer":'B'},

{"id":130,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Identify the error: "He returned back home yesterday."',
 "options":{"A":'He',"B":'returned back',"C":'home',"D":'yesterday'},"answer":'B'},

{"id":131,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Identify the error: "I am agree with you."',
 "options":{"A":'agree',"B":'I am',"C":'with',"D":'you'},"answer":'B'},

{"id":132,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Identify the error: "Each of the students have a book."',
 "options":{"A":'have',"B":'Each of',"C":'the students',"D":'a book'},"answer":'A'},

{"id":133,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Identify the error: "He has been ill since two weeks."',
 "options":{"A":'He has been',"B":'since',"C":'ill',"D":'two weeks'},"answer":'B'},

{"id":134,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Identify the error: "The scenery of Murree are beautiful."',
 "options":{"A":'The scenery',"B":'of Murree',"C":'are',"D":'beautiful'},"answer":'C'},

{"id":135,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Identify the error: "Neither of the two answers are correct."',
 "options":{"A":'Neither of',"B":'the two answers',"C":'correct',"D":'are'},"answer":'D'},

{"id":136,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Hard',
 "question":'Identify the error: "The reason for his failure is because he was lazy."',
 "options":{"A":'The reason',"B":'for his failure',"C":'he was lazy',"D":'is because'},"answer":'D'},

{"id":137,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Hard',
 "question":'Identify the error: "He prefers tea than coffee."',
 "options":{"A":'than',"B":'He',"C":'prefers',"D":'coffee'},"answer":'A'},

{"id":138,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Hard',
 "question":'Identify the error: "The both brothers are intelligent."',
 "options":{"A":'brothers',"B":'are',"C":'intelligent',"D":'The both'},"answer":'D'},

{"id":139,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Hard',
 "question":'Identify the error: "He is one of the best player in the team."',
 "options":{"A":'He is',"B":'one of the best',"C":'player',"D":'in the team'},"answer":'C'},

{"id":140,"subject":'English',"topic":'Sentence Correction',"subtopic":'Grammar',"difficulty":'Hard',
 "question":'Identify the error: "Hardly had he entered the room when the phone rang."',
 "options":{"A":'Hardly had',"B":'No error',"C":'he entered',"D":'when'},"answer":'B'},

# ============================================================
# CHOOSE THE CORRECT SENTENCE (15)  id 141-155
# ============================================================

{"id":141,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Easy',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":'He go to school every day.',"B":'He goes to school every day.',"C":'He going to school every day.',"D":'He gone to school every day.'},"answer":'B'},

{"id":142,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Easy',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":"She don't like tea.","B":"She doesn't likes tea.","C":'She not like tea.',"D":"She doesn't like tea."},"answer":'D'},

{"id":143,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Easy',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":'I saw him yesterday.',"B":'I have seen him yesterday.',"C":'I seen him yesterday.',"D":'I had saw him yesterday.'},"answer":'A'},

{"id":144,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":'The furniture is expensive.',"B":'The furnitures are expensive.',"C":'The furnitures is expensive.',"D":'The furniture are expensive.'},"answer":'A'},

{"id":145,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":'He is senior than me.',"B":'He is senior to me.',"C":'He is more senior than me.',"D":'He is senior of me.'},"answer":'B'},

{"id":146,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":'One of my friends are a doctor.',"B":'One of my friends is a doctor.',"C":'One of my friend is a doctor.',"D":'One of my friend are a doctor.'},"answer":'B'},

{"id":147,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":'She has been living here since ten years.',"B":'She is living here since ten years.',"C":'She has been living here for ten years.',"D":'She lives here since ten years.'},"answer":'C'},

{"id":148,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":'He is taller than his brother.',"B":'He is more taller than his brother.',"C":'He is tallest than his brother.',"D":'He is more tall than his brother.'},"answer":'A'},

{"id":149,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":'Neither of the answers are right.',"B":'Neither of the answers is right.',"C":'Neither of the answer is right.',"D":'Neither of the answer are right.'},"answer":'B'},

{"id":150,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Medium',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":'He asked where I was going.',"B":'He asked that where I was going.',"C":'He asked where was I going.',"D":'He asked where I going.'},"answer":'A'},

{"id":151,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Hard',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":'The number of students are increasing.',"B":'A number of students is increasing.',"C":'The number of students is increasing.',"D":'The number of student are increasing.'},"answer":'C'},

{"id":152,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Hard',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":'Hardly had I reached the station than the train left.',"B":'Hardly I had reached the station when the train left.',"C":'Hardly had I reached the station when the train left.',"D":'No sooner had I reached the station than the train had left.'},"answer":'C'},

{"id":153,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Hard',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":'He is one of the best students in the class.',"B":'He is one of the best student in the class.',"C":'He is one of the better students in the class.',"D":'He is one of best students in the class.'},"answer":'A'},

{"id":154,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Hard',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":'If I was you, I would accept the offer.',"B":'If I were you, I would accept the offer.',"C":'If I were you, I will accept the offer.',"D":'If I am you, I would accept the offer.'},"answer":'B'},

{"id":155,"subject":'English',"topic":'Choose the Correct Sentence',"subtopic":'Grammar',"difficulty":'Hard',
 "question":'Choose the CORRECT sentence:',
 "options":{"A":'Scarcely he had left when it started raining.',"B":'Scarcely had he left when it started raining.',"C":'Scarcely had he left than it started raining.',"D":'Scarcely he left when it started raining.'},"answer":'B'},

# ============================================================
# IDIOMS & PHRASES (15)  id 156-170
# ============================================================

{"id":156,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Easy',
 "question":'What does the idiom "a piece of cake" mean?',
 "options":{"A":'Something difficult',"B":'Something very easy',"C":'A sweet food',"D":'A tough situation'},"answer":'B'},

{"id":157,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Easy',
 "question":'What does "break the ice" mean?',
 "options":{"A":'To start a conversation and reduce tension',"B":'To cool something',"C":'To damage ice',"D":'To be cold'},"answer":'A'},

{"id":158,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Easy',
 "question":'What does "hit the books" mean?',
 "options":{"A":'To throw books',"B":'To study hard',"C":'To buy books',"D":'To read for fun'},"answer":'B'},

{"id":159,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Medium',
 "question":'What does "let the cat out of the bag" mean?',
 "options":{"A":'To free a cat',"B":'To buy a pet',"C":'To hide something',"D":'To reveal a secret'},"answer":'D'},

{"id":160,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Medium',
 "question":'What does "once in a blue moon" mean?',
 "options":{"A":'Every night',"B":'Every month',"C":'Frequently',"D":'Very rarely'},"answer":'D'},

{"id":161,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Medium',
 "question":'What does "beat around the bush" mean?',
 "options":{"A":'To speak directly',"B":'To avoid the main topic',"C":'To fight in a garden',"D":'To win easily'},"answer":'B'},

{"id":162,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Medium',
 "question":'What does "cost an arm and a leg" mean?',
 "options":{"A":'Very cheap',"B":'To injure someone',"C":'To be free',"D":'Very expensive'},"answer":'D'},

{"id":163,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Medium',
 "question":'What does "under the weather" mean?',
 "options":{"A":'Feeling unwell',"B":'Outside',"C":'Very happy',"D":'In the rain'},"answer":'A'},

{"id":164,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Medium',
 "question":'What does "spill the beans" mean?',
 "options":{"A":'To cook beans',"B":'To drop food',"C":'To waste food',"D":'To reveal a secret'},"answer":'D'},

{"id":165,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Medium',
 "question":'What does "call it a day" mean?',
 "options":{"A":'To name a day',"B":'To stop work for the day',"C":'To celebrate',"D":'To start work'},"answer":'B'},

{"id":166,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Medium',
 "question":'What does "in hot water" mean?',
 "options":{"A":'Bathing',"B":'Cooking',"C":'Feeling warm',"D":'In trouble'},"answer":'D'},

{"id":167,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Hard',
 "question":'What does "burn the midnight oil" mean?',
 "options":{"A":'To work or study late into the night',"B":'To waste fuel',"C":'To set a fire',"D":'To sleep early'},"answer":'A'},

{"id":168,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Hard',
 "question":'What does "the ball is in your court" mean?',
 "options":{"A":'It is your decision or turn to act',"B":'You are playing a game',"C":'You have lost',"D":'The game has ended'},"answer":'A'},

{"id":169,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Hard',
 "question":'What does "bite off more than you can chew" mean?',
 "options":{"A":'To eat too fast',"B":'To take on more than you can handle',"C":'To swallow food',"D":'To finish a meal quickly'},"answer":'B'},

{"id":170,"subject":'English',"topic":'Idioms and Phrases',"subtopic":'Meaning',"difficulty":'Hard',
 "question":'What does "a blessing in disguise" mean?',
 "options":{"A":'A hidden gift',"B":'A religious event',"C":'A costume',"D":'Something that seems bad but turns out to be good'},"answer":'D'},

# ============================================================
# ONE-WORD SUBSTITUTION (10)  id 171-180
# ============================================================

{"id":171,"subject":'English',"topic":'One-Word Substitution',"subtopic":'General',"difficulty":'Easy',
 "question":'One who studies stars and planets:',
 "options":{"A":'Geologist',"B":'Astrologer',"C":'Astronomer',"D":'Biologist'},"answer":'C'},

{"id":172,"subject":'English',"topic":'One-Word Substitution',"subtopic":'General',"difficulty":'Easy',
 "question":'A person who writes for a newspaper:',
 "options":{"A":'Author',"B":'Journalist',"C":'Editor',"D":'Publisher'},"answer":'B'},

{"id":173,"subject":'English',"topic":'One-Word Substitution',"subtopic":'General',"difficulty":'Medium',
 "question":'A person who cannot read or write:',
 "options":{"A":'Ignorant',"B":'Uneducated',"C":'Illiterate',"D":'Unlettered'},"answer":'C'},

{"id":174,"subject":'English',"topic":'One-Word Substitution',"subtopic":'General',"difficulty":'Medium',
 "question":'A person who does not believe in the existence of God:',
 "options":{"A":'Theist',"B":'Agnostic',"C":'Skeptic',"D":'Atheist'},"answer":'D'},

{"id":175,"subject":'English',"topic":'One-Word Substitution',"subtopic":'General',"difficulty":'Medium',
 "question":'A speech made without preparation:',
 "options":{"A":'Prepared',"B":'Rehearsed',"C":'Scripted',"D":'Extempore'},"answer":'D'},

{"id":176,"subject":'English',"topic":'One-Word Substitution',"subtopic":'General',"difficulty":'Medium',
 "question":'A place where medicines are prepared and sold:',
 "options":{"A":'Hospital',"B":'Pharmacy',"C":'Clinic',"D":'Dispensary'},"answer":'B'},

{"id":177,"subject":'English',"topic":'One-Word Substitution',"subtopic":'General',"difficulty":'Medium',
 "question":'One who loves mankind:',
 "options":{"A":'Misanthrope',"B":'Egoist',"C":'Philanthropist',"D":'Altruist'},"answer":'C'},

{"id":178,"subject":'English',"topic":'One-Word Substitution',"subtopic":'General',"difficulty":'Hard',
 "question":'A government run by a single person:',
 "options":{"A":'Democracy',"B":'Oligarchy',"C":'Aristocracy',"D":'Autocracy'},"answer":'D'},

{"id":179,"subject":'English',"topic":'One-Word Substitution',"subtopic":'General',"difficulty":'Hard',
 "question":'The study of ancient societies through remains:',
 "options":{"A":'Anthropology',"B":'Geology',"C":'Ecology',"D":'Archaeology'},"answer":'D'},

{"id":180,"subject":'English',"topic":'One-Word Substitution',"subtopic":'General',"difficulty":'Hard',
 "question":'A short story with a moral lesson, usually about animals:',
 "options":{"A":'Novel',"B":'Epic',"C":'Fable',"D":'Ballad'},"answer":'C'},

# ============================================================
# ANALOGIES (10)  id 181-190
# ============================================================

{"id":181,"subject":'English',"topic":'Analogies',"subtopic":'Word Relations',"difficulty":'Easy',
 "question":'BIRD : FLY :: FISH : ?',
 "options":{"A":'Water',"B":'Swim',"C":'Ocean',"D":'Scale'},"answer":'B'},

{"id":182,"subject":'English',"topic":'Analogies',"subtopic":'Word Relations',"difficulty":'Easy',
 "question":'DOCTOR : HOSPITAL :: TEACHER : ?',
 "options":{"A":'Book',"B":'School',"C":'Student',"D":'Lesson'},"answer":'B'},

{"id":183,"subject":'English',"topic":'Analogies',"subtopic":'Word Relations',"difficulty":'Easy',
 "question":'HOT : COLD :: DAY : ?',
 "options":{"A":'Night',"B":'Sun',"C":'Morning',"D":'Time'},"answer":'A'},

{"id":184,"subject":'English',"topic":'Analogies',"subtopic":'Word Relations',"difficulty":'Medium',
 "question":'PEN : WRITE :: KNIFE : ?',
 "options":{"A":'Cut',"B":'Sharp',"C":'Kitchen',"D":'Blade'},"answer":'A'},

{"id":185,"subject":'English',"topic":'Analogies',"subtopic":'Word Relations',"difficulty":'Medium',
 "question":'PUPPY : DOG :: KITTEN : ?',
 "options":{"A":'Cat',"B":'Mouse',"C":'Pet',"D":'Fur'},"answer":'A'},

{"id":186,"subject":'English',"topic":'Analogies',"subtopic":'Word Relations',"difficulty":'Medium',
 "question":'LIBRARY : BOOKS :: GALLERY : ?',
 "options":{"A":'People',"B":'Walls',"C":'Paintings',"D":'Tickets'},"answer":'C'},

{"id":187,"subject":'English',"topic":'Analogies',"subtopic":'Word Relations',"difficulty":'Medium',
 "question":'CAR : GARAGE :: AIRPLANE : ?',
 "options":{"A":'Pilot',"B":'Sky',"C":'Runway',"D":'Hangar'},"answer":'D'},

{"id":188,"subject":'English',"topic":'Analogies',"subtopic":'Word Relations',"difficulty":'Hard',
 "question":'AUTHOR : NOVEL :: COMPOSER : ?',
 "options":{"A":'Symphony',"B":'Instrument',"C":'Orchestra',"D":'Music note'},"answer":'A'},

{"id":189,"subject":'English',"topic":'Analogies',"subtopic":'Word Relations',"difficulty":'Hard',
 "question":'THIRST : DRINK :: FATIGUE : ?',
 "options":{"A":'Work',"B":'Tired',"C":'Rest',"D":'Sleepy'},"answer":'C'},

{"id":190,"subject":'English',"topic":'Analogies',"subtopic":'Word Relations',"difficulty":'Hard',
 "question":'SCALPEL : SURGEON :: WRENCH : ?',
 "options":{"A":'Nut',"B":'Garage',"C":'Tool',"D":'Mechanic'},"answer":'D'},

# ============================================================
# VOCABULARY IN CONTEXT (10)  id 191-200
# ============================================================

{"id":191,"subject":'English',"topic":'Vocabulary in Context',"subtopic":'Fill Blank',"difficulty":'Easy',
 "question":'She spoke in a ___ voice so as not to wake the baby.',
 "options":{"A":'soft',"B":'loud',"C":'sharp',"D":'harsh'},"answer":'A'},

{"id":192,"subject":'English',"topic":'Vocabulary in Context',"subtopic":'Fill Blank',"difficulty":'Easy',
 "question":'The desert is a ___ region with very little rainfall.',
 "options":{"A":'humid',"B":'lush',"C":'fertile',"D":'arid'},"answer":'D'},

{"id":193,"subject":'English',"topic":'Vocabulary in Context',"subtopic":'Fill Blank',"difficulty":'Medium',
 "question":'The scientist made a ___ discovery that changed the field.',
 "options":{"A":'groundbreaking',"B":'trivial',"C":'minor',"D":'insignificant'},"answer":'A'},

{"id":194,"subject":'English',"topic":'Vocabulary in Context',"subtopic":'Fill Blank',"difficulty":'Medium',
 "question":'His argument was so ___ that no one could refute it.',
 "options":{"A":'weak',"B":'compelling',"C":'confused',"D":'silly'},"answer":'B'},

{"id":195,"subject":'English',"topic":'Vocabulary in Context',"subtopic":'Fill Blank',"difficulty":'Medium',
 "question":'The old man walked with a ___ pace due to his weak legs.',
 "options":{"A":'brisk',"B":'sluggish',"C":'quick',"D":'lively'},"answer":'B'},

{"id":196,"subject":'English',"topic":'Vocabulary in Context',"subtopic":'Fill Blank',"difficulty":'Medium',
 "question":'She was ___ of praise for her son\'s achievements.',
 "options":{"A":'sparse',"B":'lavish',"C":'stingy',"D":'lacking'},"answer":'B'},

{"id":197,"subject":'English',"topic":'Vocabulary in Context',"subtopic":'Fill Blank',"difficulty":'Medium',
 "question":'The judge gave a ___ verdict after considering all the evidence.',
 "options":{"A":'hasty',"B":'biased',"C":'careless',"D":'fair'},"answer":'D'},

{"id":198,"subject":'English',"topic":'Vocabulary in Context',"subtopic":'Fill Blank',"difficulty":'Hard',
 "question":'The politician gave a ___ speech that inspired the crowd.',
 "options":{"A":'rousing',"B":'dull',"C":'boring',"D":'monotonous'},"answer":'A'},

{"id":199,"subject":'English',"topic":'Vocabulary in Context',"subtopic":'Fill Blank',"difficulty":'Hard',
 "question":'The evidence against him was ___ ; he had no chance of acquittal.',
 "options":{"A":'irrefutable',"B":'weak',"C":'doubtful',"D":'flimsy'},"answer":'A'},

{"id":200,"subject":'English',"topic":'Vocabulary in Context',"subtopic":'Fill Blank',"difficulty":'Hard',
 "question":'Her ___ smile suggested she knew something we did not.',
 "options":{"A":'plain',"B":'sad',"C":'confused',"D":'enigmatic'},"answer":'D'},

]


# ------------------------------------------------------------
# Sanity-check / summary utility
# ------------------------------------------------------------
def summarize(questions):
    from collections import Counter
    topic = Counter(q["topic"] for q in questions)
    diff = Counter(q["difficulty"] for q in questions)
    ans = Counter(q["answer"] for q in questions)
    ids = [q["id"] for q in questions]
    dup_ids = [i for i in set(ids) if ids.count(i) > 1]
    dup_q = [q["question"] for q in questions]
    dup_questions = [t for t in set(dup_q) if dup_q.count(t) > 1]

    print(f"Total questions: {len(questions)}")
    print("\nBy topic:")
    for t, c in sorted(topic.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")
    print("\nBy difficulty:")
    for d, c in diff.items():
        print(f"  {d}: {c}")
    print("\nBy correct-answer letter:")
    for L in ["A", "B", "C", "D"]:
        print(f"  {L}: {ans[L]}")
    print(f"\nDuplicate IDs: {dup_ids if dup_ids else 'None'}")
    print(f"Duplicate question text: {len(dup_questions)} duplicates" if dup_questions else "Duplicate question text: None")

    for q in questions:
        assert set(q["options"].keys()) == {"A", "B", "C", "D"}, f"Q{q['id']} missing option"
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