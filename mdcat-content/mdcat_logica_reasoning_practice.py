"""
MDCAT Logical Reasoning Question Bank
=====================================
300 MCQs modeled on the KIPS KDP Logical Reasoning MDCAT 2025 book.

Chapter distribution:
    1. Letters and Symbol Series ....... 120  (id 1-120)
    2. Logical Problems ................  40  (id 121-160)
    3. Logical Deductions (Syllogism)..   40  (id 161-200)
    4. Course of Action ...............   40  (id 201-240)
    5. Cause and Effect ...............   30  (id 241-270)
    6. Critical Thinking ..............   30  (id 271-300)

Difficulty mix: ~30% Easy / 50% Medium / 20% Hard.

Each question is a dict:
    id, subject, topic, subtopic, difficulty, question, options (A-D), answer
"""

QUESTIONS = [

# =====================================================================
# TOPIC 1: LETTERS AND SYMBOL SERIES (120)  id 1-120
# =====================================================================

# ---- Number Series: missing term (30) ----
{"id":1,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing term: 3, 6, 9, 12, 15, ?',
 "options":{"A":'16',"B":'17',"C":'18',"D":'19'},"answer":'C'},

{"id":2,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing term: 5, 10, 15, 20, ?',
 "options":{"A":'22',"B":'24',"C":'25',"D":'30'},"answer":'C'},

{"id":3,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing term: 2, 4, 8, 16, ?',
 "options":{"A":'24',"B":'32',"C":'20',"D":'18'},"answer":'B'},

{"id":4,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing term: 1, 4, 9, 16, 25, ?',
 "options":{"A":'30',"B":'32',"C":'36',"D":'49'},"answer":'C'},

{"id":5,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing term: 1, 8, 27, 64, ?',
 "options":{"A":'125',"B":'100',"C":'216',"D":'81'},"answer":'A'},

{"id":6,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing term: 7, 14, 21, 28, ?',
 "options":{"A":'32',"B":'35',"C":'36',"D":'42'},"answer":'B'},

{"id":7,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing term: 100, 90, 80, 70, ?',
 "options":{"A":'50',"B":'60',"C":'65',"D":'55'},"answer":'B'},

{"id":8,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Easy',
 "question":'Find the missing term: 2, 3, 5, 8, 12, ?',
 "options":{"A":'15',"B":'16',"C":'17',"D":'18'},"answer":'C'},

{"id":9,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 2, 5, 10, 17, 26, ?',
 "options":{"A":'35',"B":'36',"C":'37',"D":'40'},"answer":'C'},

{"id":10,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 3, 4, 7, 11, 18, ?',
 "options":{"A":'25',"B":'27',"C":'29',"D":'32'},"answer":'C'},

{"id":11,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 1, 3, 7, 15, 31, ?',
 "options":{"A":'47',"B":'63',"C":'55',"D":'62'},"answer":'B'},

{"id":12,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 6, 11, 21, 36, 56, ?',
 "options":{"A":'71',"B":'76',"C":'81',"D":'86'},"answer":'C'},

{"id":13,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 4, 9, 19, 39, 79, ?',
 "options":{"A":'139',"B":'159',"C":'149',"D":'119'},"answer":'B'},

{"id":14,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 5, 11, 23, 47, ?',
 "options":{"A":'94',"B":'95',"C":'96',"D":'93'},"answer":'B'},

{"id":15,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 2, 6, 12, 20, 30, ?',
 "options":{"A":'40',"B":'42',"C":'44',"D":'46'},"answer":'B'},

{"id":16,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 1, 2, 6, 24, 120, ?',
 "options":{"A":'240',"B":'480',"C":'600',"D":'720'},"answer":'D'},

{"id":17,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 1, 1, 2, 3, 5, 8, ?',
 "options":{"A":'11',"B":'12',"C":'13',"D":'14'},"answer":'C'},

{"id":18,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 48, 24, 12, 6, ?',
 "options":{"A":'2',"B":'3',"C":'4',"D":'1'},"answer":'B'},

{"id":19,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 625, 125, 25, 5, ?',
 "options":{"A":'0',"B":'1',"C":'2',"D":'5'},"answer":'B'},

{"id":20,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 8, 27, 64, 125, ?',
 "options":{"A":'196',"B":'216',"C":'225',"D":'256'},"answer":'B'},

{"id":21,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Hard',
 "question":'Find the missing term: 2, 3, 6, 15, 42, ?',
 "options":{"A":'123',"B":'110',"C":'115',"D":'120'},"answer":'A'},

{"id":22,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Hard',
 "question":'Find the missing term: 3, 7, 15, 31, 63, ?',
 "options":{"A":'127',"B":'125',"C":'128',"D":'129'},"answer":'A'},

{"id":23,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Hard',
 "question":'Find the missing term: 5, 6, 13, 40, 161, ?',
 "options":{"A":'645',"B":'806',"C":'810',"D":'800'},"answer":'B'},

{"id":24,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Hard',
 "question":'Find the missing term: 11, 13, 17, 19, 23, ?',
 "options":{"A":'25',"B":'27',"C":'29',"D":'31'},"answer":'C'},

{"id":25,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Hard',
 "question":'Find the missing term: 0, 3, 8, 15, 24, ?',
 "options":{"A":'33',"B":'34',"C":'35',"D":'36'},"answer":'C'},

{"id":26,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 7, 10, 8, 11, 9, 12, ?',
 "options":{"A":'7',"B":'10',"C":'13',"D":'14'},"answer":'B'},

{"id":27,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 4, 7, 12, 19, 28, ?',
 "options":{"A":'37',"B":'39',"C":'41',"D":'43'},"answer":'B'},

{"id":28,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the missing term: 10, 20, 40, 80, ?',
 "options":{"A":'100',"B":'120',"C":'160',"D":'200'},"answer":'C'},

{"id":29,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Hard',
 "question":'Find the missing term: 1, 4, 27, 256, ?',
 "options":{"A":'625',"B":'1024',"C":'3125',"D":'729'},"answer":'C'},

{"id":30,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Number Series',"difficulty":'Medium',
 "question":'Find the wrong term: 4, 9, 16, 23, 36, 49',
 "options":{"A":'9',"B":'16',"C":'23',"D":'36'},"answer":'C'},

# ---- Alphabetical Series (25) ----
{"id":31,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Easy',
 "question":'Find the missing letter: A, C, E, G, ?',
 "options":{"A":'H',"B":'I',"C":'J',"D":'K'},"answer":'B'},

{"id":32,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Easy',
 "question":'Find the missing letter: B, D, F, H, ?',
 "options":{"A":'I',"B":'J',"C":'K',"D":'L'},"answer":'B'},

{"id":33,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Easy',
 "question":'Find the missing letter: Z, X, V, T, ?',
 "options":{"A":'R',"B":'S',"C":'Q',"D":'P'},"answer":'A'},

{"id":34,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Easy',
 "question":'Find the missing letter: A, E, I, O, ?',
 "options":{"A":'P',"B":'S',"C":'U',"D":'Y'},"answer":'C'},

{"id":35,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: A, E, J, P, W, ?',
 "options":{"A":'E',"B":'F',"C":'G',"D":'D'},"answer":'D'},

{"id":36,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: B, D, G, K, ?',
 "options":{"A":'M',"B":'N',"C":'O',"D":'P'},"answer":'D'},

{"id":37,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: C, F, I, L, ?',
 "options":{"A":'N',"B":'O',"C":'P',"D":'M'},"answer":'B'},

{"id":38,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: A, B, D, G, K, ?',
 "options":{"A":'N',"B":'O',"C":'P',"D":'M'},"answer":'C'},

{"id":39,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: Y, W, T, P, K, ?',
 "options":{"A":'E',"B":'F',"C":'G',"D":'H'},"answer":'A'},

{"id":40,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: BZ, EW, HT, KQ, ?',
 "options":{"A":'NN',"B":'MM',"C":'OO',"D":'LL'},"answer":'A'},

{"id":41,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: AZ, CX, EV, GT, ?',
 "options":{"A":'IR',"B":'IS',"C":'HR',"D":'JQ'},"answer":'A'},

{"id":42,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: AB, CD, EF, GH, ?',
 "options":{"A":'HI',"B":'IJ',"C":'JK',"D":'KL'},"answer":'B'},

{"id":43,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: AC, EG, IK, MO, ?',
 "options":{"A":'PR',"B":'QR',"C":'QS',"D":'PQ'},"answer":'C'},

{"id":44,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: DEF, HIJ, MNO, ?',
 "options":{"A":'PQR',"B":'RST',"C":'STU',"D":'TUV'},"answer":'C'},

{"id":45,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Hard',
 "question":'Find the missing term: AZ, GT, MN, ?, YB',
 "options":{"A":'JH',"B":'SH',"C":'SK',"D":'TS'},"answer":'B'},

{"id":46,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Hard',
 "question":'Find the missing term: BAZ, DBY, FCX, ?',
 "options":{"A":'HDV',"B":'GDW',"C":'HDW',"D":'GCW'},"answer":'C'},

{"id":47,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: Z, Y, X, W, V, ?',
 "options":{"A":'S',"B":'T',"C":'U',"D":'R'},"answer":'C'},

{"id":48,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: A, D, H, M, ?',
 "options":{"A":'R',"B":'S',"C":'T',"D":'U'},"answer":'B'},

{"id":49,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: BC, EF, HI, KL, ?',
 "options":{"A":'MN',"B":'NO',"C":'OP',"D":'LM'},"answer":'B'},

{"id":50,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Hard',
 "question":'Find the missing term: AZ, BY, CX, ?',
 "options":{"A":'DW',"B":'EV',"C":'DV',"D":'EW'},"answer":'A'},

{"id":51,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: JAK, KBL, LCM, MDN, ?',
 "options":{"A":'NEO',"B":'MEN',"C":'OEP',"D":'PFQ'},"answer":'A'},

{"id":52,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: A, C, F, J, O, ?',
 "options":{"A":'T',"B":'U',"C":'V',"D":'S'},"answer":'B'},

{"id":53,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Hard',
 "question":'Find the missing term: PMT, OOS, NQR, MSQ, ?',
 "options":{"A":'LUP',"B":'KUP',"C":'LVP',"D":'LUQ'},"answer":'A'},

{"id":54,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Find the missing term: WFB, TGD, QHG, NIK, ?',
 "options":{"A":'KJP',"B":'JIP',"C":'KIP',"D":'LJO'},"answer":'A'},

{"id":55,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alphabetical Series',"difficulty":'Medium',
 "question":'Which letter is 8th to the right of the 12th letter from the left in the English alphabet?',
 "options":{"A":'T',"B":'S',"C":'U',"D":'R'},"answer":'A'},

# ---- Alpha-Numeric Series (15) ----
{"id":56,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Easy',
 "question":'Find the missing term: A1, B2, C3, D4, ?',
 "options":{"A":'E5',"B":'D5',"C":'E4',"D":'F5'},"answer":'A'},

{"id":57,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Easy',
 "question":'Find the missing term: A2, B4, C6, D8, ?',
 "options":{"A":'E9',"B":'E10',"C":'F10',"D":'D10'},"answer":'B'},

{"id":58,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Medium',
 "question":'Find the missing term: 6, H, 9, K, 11, M, 14, P, 16, R, 19, U, 21, ?',
 "options":{"A":'W',"B":'X',"C":'V',"D":'Y'},"answer":'B'},

{"id":59,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Medium',
 "question":'Find the missing term: 2A, 4B, 8C, 16D, ?',
 "options":{"A":'32E',"B":'24E',"C":'20E',"D":'30E'},"answer":'A'},

{"id":60,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Medium',
 "question":'Find the missing term: Z1A, X2D, V6G, T21J, ?',
 "options":{"A":'R88M',"B":'R66M',"C":'S88M',"D":'S66N'},"answer":'A'},

{"id":61,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Medium',
 "question":'Find the missing term: C4X, F9U, I16R, ?',
 "options":{"A":'L25P',"B":'L25O',"C":'K25P',"D":'M20O'},"answer":'B'},

{"id":62,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Medium',
 "question":'Find the missing term: A5, D25, G125, J625, ?',
 "options":{"A":'M3125',"B":'K3125',"C":'M2500',"D":'L1250'},"answer":'A'},

{"id":63,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Medium',
 "question":'Find the missing term: B2, D4, F6, H8, ?',
 "options":{"A":'I10',"B":'J10',"C":'J9',"D":'K10'},"answer":'B'},

{"id":64,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Hard',
 "question":'Find the missing term: W1F, T3H, Q5J, N7L, ?',
 "options":{"A":'K9N',"B":'K10N',"C":'L9N',"D":'K9M'},"answer":'A'},

{"id":65,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Medium',
 "question":'Find the missing term: 1A, 3B, 5C, 7D, ?',
 "options":{"A":'8E',"B":'9E',"C":'10E',"D":'9F'},"answer":'B'},

{"id":66,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Medium',
 "question":'Find the missing term: A1B, C3D, E5F, G7H, ?',
 "options":{"A":'I9J',"B":'H9I',"C":'I8J',"D":'H8I'},"answer":'A'},

{"id":67,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Hard',
 "question":'Find the missing term: 3F, 6G, 11I, 18L, ?',
 "options":{"A":'25O',"B":'27P',"C":'27O',"D":'25P'},"answer":'B'},

{"id":68,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Medium',
 "question":'Find the missing term: Z26, Y25, X24, W23, ?',
 "options":{"A":'V22',"B":'U21',"C":'V23',"D":'W22'},"answer":'A'},

{"id":69,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Medium',
 "question":'Find the missing term: A3, E5, I7, M9, ?',
 "options":{"A":'Q11',"B":'P11',"C":'Q10',"D":'R11'},"answer":'A'},

{"id":70,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Alpha-Numeric Series',"difficulty":'Hard',
 "question":'Find the missing term: 2Z5, 7Y7, 14X9, 23W11, ?',
 "options":{"A":'34V14',"B":'34V13',"C":'33V13',"D":'34U13'},"answer":'B'},

# ---- Coding-Decoding (20) ----
{"id":71,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Easy',
 "question":'If CAT is coded as DBU, how is DOG coded?',
 "options":{"A":'EPH',"B":'EPG',"C":'DPH',"D":'FQI'},"answer":'A'},

{"id":72,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Easy',
 "question":'If PEN is coded as QFO, how is INK coded?',
 "options":{"A":'JOL',"B":'JOK',"C":'JNL',"D":'HMJ'},"answer":'A'},

{"id":73,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If PLANET is coded as QMBOFU, how is JUPITER coded?',
 "options":{"A":'KVQJUFS',"B":'KVQJUFR',"C":'JVQJUFS',"D":'KVQIUFS'},"answer":'A'},

{"id":74,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If ROSE is coded as PQMC, how is TREE coded?',
 "options":{"A":'RPCC',"B":'RPDD',"C":'RQCC',"D":'SPDD'},"answer":'A'},

{"id":75,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If A=1, B=2, C=3, ..., then DOG = ?',
 "options":{"A":'26',"B":'25',"C":'27',"D":'24'},"answer":'A'},

{"id":76,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If A=1, B=2, ..., then CAT = ?',
 "options":{"A":'22',"B":'24',"C":'23',"D":'20'},"answer":'B'},

{"id":77,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If BIRD is coded as CJSE, how is SWAN coded?',
 "options":{"A":'TXBO',"B":'TXBM',"C":'TWBO',"D":'UXBO'},"answer":'A'},

{"id":78,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If MANGO is coded as LZMFN, how is APPLE coded?',
 "options":{"A":'ZOOKD',"B":'BQQMF',"C":'ZQOKD',"D":'BOOKD'},"answer":'A'},

{"id":79,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If HAPPY is coded as IBQQZ, how is JOLLY coded?',
 "options":{"A":'KPMMZ',"B":'KOMMZ',"C":'KPNNZ',"D":'JPMMZ'},"answer":'A'},

{"id":80,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Hard',
 "question":'If in a code, GARDEN is coded as GNRAED, how is COUNTER coded?',
 "options":{"A":'CRUOETN',"B":'CRONUET',"C":'CROENUT',"D":'CRUETNO'},"answer":'A'},

{"id":81,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If DELHI is coded as CDKGH, how is BOMBAY coded?',
 "options":{"A":'ANLAZX',"B":'ANMAZX',"C":'ANLBZX',"D":'CPNCBZ'},"answer":'A'},

{"id":82,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If NEW is coded as PGY, how is OLD coded?',
 "options":{"A":'QNF',"B":'QMF',"C":'PNE',"D":'RNF'},"answer":'A'},

{"id":83,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If in a code, WATER is written as YCVGT, how is CHILD written?',
 "options":{"A":'EJKNF',"B":'EJKMF',"C":'EJLNF',"D":'FJKNG'},"answer":'A'},

{"id":84,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Hard',
 "question":'If SISTER is coded as RHRSDQ, how is UNCLE coded?',
 "options":{"A":'TMBKD',"B":'TMDKD',"C":'TNBKD',"D":'SMBKD'},"answer":'A'},

{"id":85,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If FRIEND is coded as HTKGPF, how is CANDLE coded?',
 "options":{"A":'ECPFNG',"B":'DBPFNG',"C":'ECPENG',"D":'ECOENG'},"answer":'A'},

{"id":86,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If TEACHER is coded as VGCEJGT, how is STUDENT coded?',
 "options":{"A":'UVWFGPV',"B":'UWVFGPV',"C":'UVWGFPV',"D":'VUWFGPV'},"answer":'A'},

{"id":87,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Hard',
 "question":'In a certain code, MONKEY is written as XDJMNL. How is TIGER written in that code?',
 "options":{"A":'QDFHS',"B":'SDFHQ',"C":'QDHFS',"D":'RDFHS'},"answer":'A'},

{"id":88,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If ROAD is coded as URDG, how is SWAN coded?',
 "options":{"A":'VZDQ',"B":'VZCQ',"C":'UZDQ',"D":'VYDQ'},"answer":'A'},

{"id":89,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Medium',
 "question":'If FACE is coded as 6135, how is CAB coded (A=1, B=2, C=3, ..., Z=26)?',
 "options":{"A":'312',"B":'321',"C":'313',"D":'213'},"answer":'A'},

{"id":90,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Coding-Decoding',"difficulty":'Hard',
 "question":'If in a code language, MOUSE is written as PRXVH, how is SHIFT written?',
 "options":{"A":'VKLIW',"B":'VJLIW',"C":'VKLJW',"D":'UKLIW'},"answer":'A'},

# ---- Analogies / Word Analogy (15) ----
{"id":91,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Easy',
 "question":'Painter is to Canvas as Writer is to:',
 "options":{"A":'Pen',"B":'Paper',"C":'Book',"D":'Story'},"answer":'B'},

{"id":92,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Easy',
 "question":'Dog is to Puppy as Cat is to:',
 "options":{"A":'Kitten',"B":'Cub',"C":'Calf',"D":'Foal'},"answer":'A'},

{"id":93,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Easy',
 "question":'Bird is to Nest as Bee is to:',
 "options":{"A":'Web',"B":'Hive',"C":'Den',"D":'Hole'},"answer":'B'},

{"id":94,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Easy',
 "question":'Doctor is to Hospital as Teacher is to:',
 "options":{"A":'Library',"B":'Office',"C":'School',"D":'Class'},"answer":'C'},

{"id":95,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Medium',
 "question":'Engine is to Car as Heart is to:',
 "options":{"A":'Blood',"B":'Lungs',"C":'Body',"D":'Brain'},"answer":'C'},

{"id":96,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Medium',
 "question":'Ophthalmologist is to Eye as Cardiologist is to:',
 "options":{"A":'Brain',"B":'Heart',"C":'Skin',"D":'Kidney'},"answer":'B'},

{"id":97,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Medium',
 "question":'Hunger is to Food as Thirst is to:',
 "options":{"A":'Drink',"B":'Water',"C":'Juice',"D":'Cup'},"answer":'B'},

{"id":98,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Medium',
 "question":'AB : YZ :: CD : ?',
 "options":{"A":'WX',"B":'VW',"C":'UV',"D":'XY'},"answer":'A'},

{"id":99,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Medium',
 "question":'ACE : BDF :: PRT : ?',
 "options":{"A":'QSU',"B":'QST',"C":'QRT',"D":'QSV'},"answer":'A'},

{"id":100,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Medium',
 "question":'25 : 36 :: 49 : ?',
 "options":{"A":'60',"B":'64',"C":'72',"D":'81'},"answer":'B'},

{"id":101,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Medium',
 "question":'8 : 27 :: 64 : ?',
 "options":{"A":'125',"B":'216',"C":'100',"D":'128'},"answer":'A'},

{"id":102,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Medium',
 "question":'Book : Library :: Painting : ?',
 "options":{"A":'Museum',"B":'Frame',"C":'Artist',"D":'Studio'},"answer":'A'},

{"id":103,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Medium',
 "question":'Knife : Cut :: Pen : ?',
 "options":{"A":'Ink',"B":'Paper',"C":'Write',"D":'Nib'},"answer":'C'},

{"id":104,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Hard',
 "question":'Hammer : Carpenter :: Scalpel : ?',
 "options":{"A":'Butcher',"B":'Surgeon',"C":'Barber',"D":'Chef'},"answer":'B'},

{"id":105,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Analogies',"difficulty":'Hard',
 "question":'Oasis : Desert :: Island : ?',
 "options":{"A":'Ocean',"B":'River',"C":'Land',"D":'Beach'},"answer":'A'},

# ---- Odd One Out (15) ----
{"id":106,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Easy',
 "question":'Find the odd one out:',
 "options":{"A":'Apple',"B":'Banana',"C":'Mango',"D":'Carrot'},"answer":'D'},

{"id":107,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Easy',
 "question":'Find the odd one out:',
 "options":{"A":'Cow',"B":'Goat',"C":'Lion',"D":'Sheep'},"answer":'C'},

{"id":108,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Easy',
 "question":'Find the odd one out:',
 "options":{"A":'Rose',"B":'Lily',"C":'Tulip',"D":'Oak'},"answer":'D'},

{"id":109,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Easy',
 "question":'Find the odd one out:',
 "options":{"A":'Copper',"B":'Iron',"C":'Silver',"D":'Wood'},"answer":'D'},

{"id":110,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Medium',
 "question":'Find the odd one out:',
 "options":{"A":'Square',"B":'Triangle',"C":'Circle',"D":'Cube'},"answer":'D'},

{"id":111,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Medium',
 "question":'Find the odd one out:',
 "options":{"A":'25',"B":'36',"C":'49',"D":'50'},"answer":'D'},

{"id":112,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Medium',
 "question":'Find the odd one out:',
 "options":{"A":'8',"B":'27',"C":'64',"D":'100'},"answer":'D'},

{"id":113,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Medium',
 "question":'Find the odd one out:',
 "options":{"A":'11',"B":'13',"C":'17',"D":'21'},"answer":'D'},

{"id":114,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Medium',
 "question":'Find the odd one out:',
 "options":{"A":'BDF',"B":'GIK',"C":'MNO',"D":'PRT'},"answer":'C'},

{"id":115,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Medium',
 "question":'Find the odd one out:',
 "options":{"A":'ACE',"B":'FHJ',"C":'KMO',"D":'PRS'},"answer":'D'},

{"id":116,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Medium',
 "question":'Find the odd one out:',
 "options":{"A":'Kilogram',"B":'Litre',"C":'Metre',"D":'Second'},"answer":'B'},

{"id":117,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Hard',
 "question":'Find the odd one out:',
 "options":{"A":'Mercury',"B":'Venus',"C":'Moon',"D":'Mars'},"answer":'C'},

{"id":118,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Hard',
 "question":'Find the odd one out:',
 "options":{"A":'Newton',"B":'Pascal',"C":'Joule',"D":'Ampere'},"answer":'D'},

{"id":119,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Medium',
 "question":'Find the odd one out:',
 "options":{"A":'Hindi',"B":'English',"C":'India',"D":'Urdu'},"answer":'C'},

{"id":120,"subject":'Logical Reasoning',"topic":'Letters and Symbol Series',"subtopic":'Odd One Out',"difficulty":'Hard',
 "question":'Find the odd one out:',
 "options":{"A":'121',"B":'144',"C":'169',"D":'155'},"answer":'D'},

# =====================================================================
# TOPIC 2: LOGICAL PROBLEMS (40)  id 121-160
# =====================================================================

# ---- Blood Relations (10) ----
{"id":121,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Blood Relations',"difficulty":'Easy',
 "question":"Pointing to a photograph, a man said, 'She is the daughter of my mother's only daughter.' How is he related to the girl in the photograph?",
 "options":{"A":'Father',"B":'Uncle',"C":'Brother',"D":'Cousin'},"answer":'B'},

{"id":122,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Blood Relations',"difficulty":'Medium',
 "question":"Pointing to a man, a woman said, 'His son is my son's father.' How is the man related to the woman?",
 "options":{"A":'Brother',"B":'Grandfather',"C":'Husband',"D":'Father-in-law'},"answer":'D'},

{"id":123,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Blood Relations',"difficulty":'Medium',
 "question":"A is B's brother. C is A's mother. D is C's father. B is D's:",
 "options":{"A":'Son',"B":'Granddaughter',"C":'Grandson',"D":'Grandfather'},"answer":'B'},

{"id":124,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Blood Relations',"difficulty":'Medium',
 "question":"Pointing to a lady, Rahim said, 'She is the daughter of the only son of my grandmother.' How is the lady related to Rahim?",
 "options":{"A":'Sister',"B":'Cousin',"C":'Aunt',"D":'Niece'},"answer":'A'},

{"id":125,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Blood Relations',"difficulty":'Medium',
 "question":"Introducing a boy, a girl said, 'He is the son of the daughter of the father of my uncle.' How is the boy related to the girl?",
 "options":{"A":'Brother',"B":'Nephew',"C":'Cousin',"D":'Uncle'},"answer":'A'},

{"id":126,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Blood Relations',"difficulty":'Hard',
 "question":"Pointing to a man in a photograph, Asha said, 'His mother's only daughter is my mother.' How is Asha related to that man?",
 "options":{"A":'Nephew',"B":'Sister',"C":'Wife',"D":'Niece'},"answer":'D'},

{"id":127,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Blood Relations',"difficulty":'Medium',
 "question":"P is Q's brother. R is Q's mother. S is R's father. T is S's mother. How is P related to T?",
 "options":{"A":'Grandson',"B":'Great-grandson',"C":'Grandmother',"D":'Daughter'},"answer":'B'},

{"id":128,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Blood Relations',"difficulty":'Medium',
 "question":"If A + B means A is the father of B; A - B means A is the wife of B; A x B means A is the brother of B; A / B means A is the daughter of B, then in P / R + S / T, who is the father?",
 "options":{"A":'R',"B":'S',"C":'T',"D":'P'},"answer":'A'},

{"id":129,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Blood Relations',"difficulty":'Hard',
 "question":"Pointing to a man, Neha said, 'His only brother is the father of my daughter's father.' How is the man related to Neha?",
 "options":{"A":'Father',"B":'Grandfather',"C":'Uncle',"D":'Brother-in-law'},"answer":'C'},

{"id":130,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Blood Relations',"difficulty":'Medium',
 "question":"X is the wife of Y. Z is the son of Y. W is the brother of Y. If P is the son of W, then which of the following statements is correct?",
 "options":{"A":'P is the cousin of Z',"B":'P is the brother of Z',"C":'X is the mother of P',"D":'P is the uncle of Z'},"answer":'A'},

# ---- Direction Sense (8) ----
{"id":131,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Direction Sense',"difficulty":'Easy',
 "question":'A man walks 12 km south, then turns west and walks 5 km. How far is he from his starting point?',
 "options":{"A":'17 km',"B":'7 km',"C":'60 km',"D":'13 km'},"answer":'D'},

{"id":132,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Direction Sense',"difficulty":'Easy',
 "question":'A person walks 3 km east, then 4 km north. How far is he from the starting point?',
 "options":{"A":'5 km',"B":'7 km',"C":'6 km',"D":'1 km'},"answer":'A'},

{"id":133,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Direction Sense',"difficulty":'Medium',
 "question":'Aslam walks 10 m east, then turns right and walks 6 m, then turns right again and walks 10 m. How far is he from the starting point?',
 "options":{"A":'6 m',"B":'10 m',"C":'16 m',"D":'4 m'},"answer":'A'},

{"id":134,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Direction Sense',"difficulty":'Medium',
 "question":'A man starts walking north, turns right, then right again, then left. In which direction is he now walking?',
 "options":{"A":'North',"B":'South',"C":'East',"D":'West'},"answer":'C'},

{"id":135,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Direction Sense',"difficulty":'Medium',
 "question":'A boy walks 5 km north, then 3 km east, then 5 km south. How far is he from the starting point?',
 "options":{"A":'13 km',"B":'3 km',"C":'8 km',"D":'5 km'},"answer":'B'},

{"id":136,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Direction Sense',"difficulty":'Medium',
 "question":'Facing east, a man turns 135 degrees clockwise, then another 180 degrees clockwise. Which direction is he now facing?',
 "options":{"A":'North-east',"B":'North-west',"C":'South-west',"D":'South-east'},"answer":'B'},

{"id":137,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Direction Sense',"difficulty":'Hard',
 "question":'Ali walks 8 m north, then 6 m west, then 4 m south, then 3 m east. How far is he from the starting point?',
 "options":{"A":'5 m',"B":'7 m',"C":'11 m',"D":'21 m'},"answer":'A'},

{"id":138,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Direction Sense',"difficulty":'Hard',
 "question":'A person walks 20 m towards north, then turns right and walks 30 m, then turns right again and walks 35 m. Which direction is he from the starting point?',
 "options":{"A":'North-west',"B":'North-east',"C":'South-east',"D":'South-west'},"answer":'C'},

# ---- Seating / Arrangement Puzzles (12) ----
{"id":139,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Arrangement',"difficulty":'Medium',
 "question":'There are four friends P, Q, R and S. Each likes a different game: Cricket, Football, Chess and Badminton. P does not like Cricket and Chess. Q likes Football. R does not like Chess. S does not like Badminton and Football. Who likes Chess?',
 "options":{"A":'P',"B":'Q',"C":'R',"D":'S'},"answer":'D'},

{"id":140,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Arrangement',"difficulty":'Medium',
 "question":'Five people A, B, C, D, E sit in a row facing north. C sits at the extreme right. A sits to the immediate left of C. B sits at the extreme left. Where does D sit if he is next to B?',
 "options":{"A":'Second from left',"B":'Second from right',"C":'Middle',"D":'Cannot be determined'},"answer":'A'},

{"id":141,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Arrangement',"difficulty":'Medium',
 "question":'In a queue, Ali is 7th from the front and 11th from the back. How many people are in the queue?',
 "options":{"A":'18',"B":'17',"C":'19',"D":'16'},"answer":'B'},

{"id":142,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Arrangement',"difficulty":'Medium',
 "question":'In a row, Sana is 10th from the left and 15th from the right. Total number of students in the row is:',
 "options":{"A":'23',"B":'24',"C":'25',"D":'26'},"answer":'B'},

{"id":143,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Arrangement',"difficulty":'Medium',
 "question":'Six friends A, B, C, D, E, F are sitting around a circle facing the center. B is between A and C. D is opposite A. E is between D and F. Who is opposite B?',
 "options":{"A":'E',"B":'F',"C":'D',"D":'C'},"answer":'A'},

{"id":144,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Arrangement',"difficulty":'Hard',
 "question":'Five books P, Q, R, S, T are placed one above the other. R is below T but above S. P is above T. Q is below S. Which book is at the bottom?',
 "options":{"A":'S',"B":'Q',"C":'R',"D":'T'},"answer":'B'},

{"id":145,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Arrangement',"difficulty":'Hard',
 "question":'Five houses are arranged in a row. The red house is left of the blue house. The green house is right of the blue house. The yellow house is left of the red house. The white house is right of the green house. Which is in the middle?',
 "options":{"A":'Red',"B":'Blue',"C":'Green',"D":'White'},"answer":'B'},

{"id":146,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Arrangement',"difficulty":'Medium',
 "question":'In a class of 40, Ahmed ranks 12th from the top. What is his rank from the bottom?',
 "options":{"A":'28',"B":'29',"C":'30',"D":'27'},"answer":'B'},

{"id":147,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Arrangement',"difficulty":'Medium',
 "question":'Six people M, N, O, P, Q, R are seated in a row facing north. M sits at the extreme left. R is second from the right. N is immediate right of M. Q is between P and R. Who sits at extreme right?',
 "options":{"A":'O',"B":'P',"C":'R',"D":'Cannot be determined'},"answer":'A'},

{"id":148,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Arrangement',"difficulty":'Hard',
 "question":'Four persons A, B, C, D have different professions: doctor, engineer, teacher, lawyer. A is not a doctor or teacher. B is a lawyer. C is not a doctor. Then D is:',
 "options":{"A":'Doctor',"B":'Engineer',"C":'Teacher',"D":'Lawyer'},"answer":'A'},

{"id":149,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Arrangement',"difficulty":'Medium',
 "question":'Aslam is taller than Bilal but shorter than Zia. Kamran is taller than Aslam but shorter than Zia. Who is the tallest?',
 "options":{"A":'Aslam',"B":'Bilal',"C":'Zia',"D":'Kamran'},"answer":'C'},

{"id":150,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Arrangement',"difficulty":'Hard',
 "question":'Six students sit around a round table. A is between B and C. D is opposite A. E is to the immediate right of D. F is to the immediate left of B. Who is to the immediate left of D?',
 "options":{"A":'F',"B":'C',"C":'B',"D":'A'},"answer":'B'},

# ---- Ranking / Age / Time-based (10) ----
{"id":151,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Ranking',"difficulty":'Easy',
 "question":"A father is 30 years older than his son. In 5 years, the father's age will be twice the son's. What is the son's present age?",
 "options":{"A":'20',"B":'25',"C":'22',"D":'30'},"answer":'B'},

{"id":152,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Ranking',"difficulty":'Medium',
 "question":"The average age of 4 members of a family is 25 years. If a fifth member of age 15 joins, the new average is:",
 "options":{"A":'22',"B":'23',"C":'24',"D":'25'},"answer":'B'},

{"id":153,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Ranking',"difficulty":'Medium',
 "question":"5 years ago, A was twice as old as B. Today A is 30. How old is B today?",
 "options":{"A":'15',"B":'17',"C":'20',"D":'25'},"answer":'B'},

{"id":154,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Ranking',"difficulty":'Medium',
 "question":"If January 1, 2020 was a Wednesday, what day was January 1, 2021 (2020 was a leap year)?",
 "options":{"A":'Thursday',"B":'Friday',"C":'Saturday',"D":'Sunday'},"answer":'B'},

{"id":155,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Ranking',"difficulty":'Medium',
 "question":"If today is Monday, what day will it be 100 days from today?",
 "options":{"A":'Tuesday',"B":'Wednesday',"C":'Thursday',"D":'Friday'},"answer":'B'},

{"id":156,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Ranking',"difficulty":'Hard',
 "question":"An angle between the hour hand and minute hand of a clock at 3:15 is:",
 "options":{"A":'0 degrees',"B":'7.5 degrees',"C":'15 degrees',"D":'22.5 degrees'},"answer":'B'},

{"id":157,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Ranking',"difficulty":'Hard',
 "question":"At what time between 4 and 5 o'clock will the hands of a clock coincide?",
 "options":{"A":'4:20',"B":'4:21 and 9/11 min',"C":'4:22',"D":'4:23'},"answer":'B'},

{"id":158,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Ranking',"difficulty":'Medium',
 "question":"In a class of 60 students, Kamal ranks 20th. There are 5 students below him with the same rank. How many students rank above him?",
 "options":{"A":'19',"B":'20',"C":'34',"D":'35'},"answer":'A'},

{"id":159,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Ranking',"difficulty":'Medium',
 "question":"Ali's rank in class is 7 from top and 32 from bottom. How many students are in the class?",
 "options":{"A":'38',"B":'39',"C":'40',"D":'37'},"answer":'A'},

{"id":160,"subject":'Logical Reasoning',"topic":'Logical Problems',"subtopic":'Ranking',"difficulty":'Hard',
 "question":"A is older than B, but younger than C. D is younger than E but older than A. If C is younger than D, then who is the oldest?",
 "options":{"A":'A',"B":'C',"C":'D',"D":'E'},"answer":'D'},

# =====================================================================
# TOPIC 3: LOGICAL DEDUCTIONS / SYLLOGISM (40)  id 161-200
# =====================================================================

{"id":161,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Easy',
 "question":'Statements: All roses are flowers. All flowers are plants. Conclusion: All roses are plants.',
 "options":{"A":'Conclusion follows',"B":'Conclusion does not follow',"C":'Data inadequate',"D":'Conclusion is uncertain'},"answer":'A'},

{"id":162,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Easy',
 "question":'Statements: All dogs are animals. Some animals are cats. Conclusion: Some dogs are cats.',
 "options":{"A":'Conclusion follows',"B":'Conclusion does not follow',"C":'Data inadequate',"D":'Either follows or does not'},"answer":'B'},

{"id":163,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Easy',
 "question":'Statements: All boys are students. All students are humans. Conclusion: All boys are humans.',
 "options":{"A":'Conclusion follows',"B":'Conclusion does not follow',"C":'Data inadequate',"D":'Uncertain'},"answer":'A'},

{"id":164,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All athletes are fit. Some fit people are fast runners. Which conclusion logically follows?',
 "options":{"A":'All athletes are fast runners',"B":'No definite conclusion about athletes being fast runners',"C":'Some athletes are fast runners',"D":'No athlete is a fast runner'},"answer":'B'},

{"id":165,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: Some pens are books. All books are papers. Conclusions: I. Some pens are papers. II. All papers are pens. Which follows?',
 "options":{"A":'Only I follows',"B":'Only II follows',"C":'Both follow',"D":'Neither follows'},"answer":'A'},

{"id":166,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: No man is honest. All those who are honest are dutiful. Conclusion: No man is dutiful.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Cannot say'},"answer":'B'},

{"id":167,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All students are boys. No boy is dull. Conclusion: No student is dull.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Cannot be determined'},"answer":'A'},

{"id":168,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: Some cats are rats. All rats are trees. Some trees are not cats. Conclusions: I. Some trees are cats. II. All cats are trees. III. All rats are cats. IV. No tree are cats. Which is valid?',
 "options":{"A":'Only I',"B":'Only II',"C":'Only III',"D":'II and III'},"answer":'A'},

{"id":169,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All apples are fruits. Some fruits are sweet. Conclusion: Some apples are sweet.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Both true'},"answer":'B'},

{"id":170,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Easy',
 "question":'Statements: All cats are mammals. Some mammals give live birth. Conclusion: All cats give live birth.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'True by fact'},"answer":'B'},

{"id":171,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: Some doctors are fools. Some fools are rich. Conclusion: Some doctors are rich.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Certainly true'},"answer":'B'},

{"id":172,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All actors are singers. All singers are dancers. Conclusions: I. All actors are dancers. II. Some dancers are actors. Which follows?',
 "options":{"A":'Only I',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'C'},

{"id":173,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: No teacher is a student. Some students are toppers. Conclusion: Some toppers are not teachers.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Contradiction'},"answer":'A'},

{"id":174,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All fish live in water. All whales live in water. Conclusion: All whales are fish.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Partly true'},"answer":'B'},

{"id":175,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All mangoes are yellow. Some yellow are sweet. Conclusions: I. All mangoes are sweet. II. Some mangoes are sweet. Which follows?',
 "options":{"A":'Only I',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'D'},

{"id":176,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Hard',
 "question":'Statements: All squares are rectangles. All rectangles are parallelograms. Conclusions: I. All squares are parallelograms. II. Some parallelograms are squares. Which follows?',
 "options":{"A":'Only I',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'C'},

{"id":177,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Hard',
 "question":'Statements: No book is a copy. Some copies are pens. Conclusion: Some pens are not books.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Uncertain'},"answer":'A'},

{"id":178,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All engineers are graduates. Some graduates are managers. Conclusion: Some engineers are managers.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Partially true'},"answer":'B'},

{"id":179,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All ships are boats. All boats are vehicles. Conclusion: All ships are vehicles.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Depends'},"answer":'A'},

{"id":180,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: Some men are honest. All honest people are trustworthy. Conclusion: Some men are trustworthy.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Uncertain'},"answer":'A'},

{"id":181,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All flowers are trees. No fruit is a tree. Conclusion: No fruit is a flower.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Cannot say'},"answer":'A'},

{"id":182,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Hard',
 "question":'Statements: All chairs are tables. Some tables are desks. Conclusions: I. Some chairs are desks. II. Some desks are chairs. III. No desk is a chair. IV. All chairs are desks. Which follows?',
 "options":{"A":'Only I and II',"B":'Only either I or III',"C":'Only either II or III',"D":'Only IV'},"answer":'B'},

{"id":183,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All windows are doors. All doors are walls. Conclusion: All windows are walls.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'False'},"answer":'A'},

{"id":184,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Hard',
 "question":'Statements: Some pens are pencils. All pencils are erasers. Conclusions: I. Some pens are erasers. II. Some erasers are pens. Which follows?',
 "options":{"A":'Only I',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'C'},

{"id":185,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All lions are wild. Some wild animals are dangerous. Conclusion: Some lions are dangerous.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Certain'},"answer":'B'},

{"id":186,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All cars are vehicles. Some vehicles are trucks. Conclusion: Some cars may be trucks.',
 "options":{"A":'Follows definitely',"B":'Only a possibility, not definite',"C":'Cannot be inferred at all',"D":'Contradicts'},"answer":'B'},

{"id":187,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All bags are boxes. Some boxes are baskets. Conclusion: Some bags are baskets.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Both possible'},"answer":'B'},

{"id":188,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All poets are dreamers. All dreamers are optimists. Conclusions: I. All poets are optimists. II. Some optimists are poets. Which follows?',
 "options":{"A":'Only I',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'C'},

{"id":189,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Hard',
 "question":'Statements: No student is lazy. Rahim is lazy. Conclusion: Rahim is not a student.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Uncertain'},"answer":'A'},

{"id":190,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: Some managers are workers. No worker is a leader. Conclusion: Some managers are not leaders.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Cannot say'},"answer":'A'},

{"id":191,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All keys are locks. No lock is a door. Conclusion: No key is a door.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Cannot say'},"answer":'A'},

{"id":192,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All singers are musicians. Some musicians are guitarists. Conclusion: Some singers are guitarists.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Certain'},"answer":'B'},

{"id":193,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Hard',
 "question":'Statements: All roses are red. All red things are attractive. Conclusions: I. All roses are attractive. II. Some attractive things are roses. Which follows?',
 "options":{"A":'Only I',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'C'},

{"id":194,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All computers are machines. All machines need power. Conclusion: All computers need power.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Uncertain'},"answer":'A'},

{"id":195,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: Some birds are parrots. All parrots are green. Conclusion: Some birds are green.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Cannot say'},"answer":'A'},

{"id":196,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: No child is old. Some old people are sick. Conclusion: Some sick are not children.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Cannot say'},"answer":'A'},

{"id":197,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Hard',
 "question":'Statements: All rich people are educated. Some educated people are honest. Conclusion: Some rich people are honest.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Certain'},"answer":'B'},

{"id":198,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: All hens are birds. No bird is a mammal. Conclusion: No hen is a mammal.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Cannot say'},"answer":'A'},

{"id":199,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Medium',
 "question":'Statements: Some artists are painters. All painters are creative. Conclusions: I. Some artists are creative. II. All artists are creative. Which follows?',
 "options":{"A":'Only I',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'A'},

{"id":200,"subject":'Logical Reasoning',"topic":'Logical Deductions',"subtopic":'Syllogism',"difficulty":'Hard',
 "question":'Statements: All chemists are scientists. Some scientists are researchers. No researcher is a poet. Conclusion: Some chemists are not poets.',
 "options":{"A":'Follows',"B":'Does not follow',"C":'Data inadequate',"D":'Cannot say'},"answer":'B'},

# =====================================================================
# TOPIC 4: COURSE OF ACTION (40)  id 201-240
# =====================================================================

{"id":201,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: The Management of School M has decided to give free breakfast from next academic year to all the students in its primary section through its canteen even though they will not get any government grant. Courses of Action: I. The school will have to admit many poor students who will seek admission. II. The canteen facilities and utensils have to be checked and new purchases to be made. III. Funds will have to be raised to support the scheme for years to come. Which follow?",
 "options":{"A":'Only II and III follow',"B":'Only I and III follow',"C":'Only II and III follow',"D":'Only I follows'},"answer":'A'},

{"id":202,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: The number of road accidents in the city has increased sharply in the last few months. Courses of Action: I. Strict enforcement of traffic rules should be undertaken. II. Speed limits should be enforced and monitored. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both I and II follow',"D":'Neither'},"answer":'C'},

{"id":203,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: A large number of primary schools in a rural area are non-functional because of the shortage of teachers. Courses of Action: I. The Government should immediately close down these schools. II. The Government should recruit qualified teachers on an urgent basis. Which follow?",
 "options":{"A":'Only I',"B":'Only II follows',"C":'Both',"D":'Neither'},"answer":'B'},

{"id":204,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: Many people fall sick after eating stale food from a wedding function. Courses of Action: I. The organizer of the function should be arrested. II. Health inspection at wedding halls should be tightened by the authorities. Which follow?",
 "options":{"A":'Only I',"B":'Only II follows',"C":'Both',"D":'Neither'},"answer":'B'},

{"id":205,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: The water level in most of the dams supplying water to the city has fallen to less than 15% of the total capacity. Courses of Action: I. The government should immediately impose water cuts in the city to make the water available for a longer duration. II. The government should ask citizens to use water judiciously. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both I and II follow',"D":'Neither'},"answer":'C'},

{"id":206,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: Air pollution has reached alarming levels in the city, affecting people's health. Courses of Action: I. Strict emission standards should be enforced for vehicles and industries. II. Public transport and green cover should be expanded. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":207,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: A number of students in a hostel have been complaining about the poor quality of food. Courses of Action: I. The hostel authorities should form a food committee including students to review menu and quality. II. The hostel should be closed down. Which follow?",
 "options":{"A":'Only I follows',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'A'},

{"id":208,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: The dropout rate of girls in schools is very high in rural areas. Courses of Action: I. Separate girls' schools with female teachers should be established. II. Free bicycles and stipends should be offered to girl students. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both I and II follow',"D":'Neither'},"answer":'C'},

{"id":209,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: Cases of dengue have increased sharply in the last month. Courses of Action: I. Anti-larval spraying should be intensified. II. Public awareness campaigns should be conducted. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":210,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: Employees of a company have not received their salaries for the last two months. Courses of Action: I. The employees should immediately stop working. II. The management should investigate financial reasons and communicate with employees. Which follow?",
 "options":{"A":'Only I',"B":'Only II follows',"C":'Both',"D":'Neither'},"answer":'B'},

{"id":211,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: The number of students failing in the board examination has increased significantly this year. Courses of Action: I. The examination system should be scrapped. II. Remedial classes and improved teaching methods should be introduced. Which follow?",
 "options":{"A":'Only I',"B":'Only II follows',"C":'Both',"D":'Neither'},"answer":'B'},

{"id":212,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: Many bridges in the city are old and structurally weak. Courses of Action: I. All bridges should be immediately demolished. II. Structural audit and repair/replacement plan should be undertaken. Which follow?",
 "options":{"A":'Only I',"B":'Only II follows',"C":'Both',"D":'Neither'},"answer":'B'},

{"id":213,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: The city's garbage disposal system has completely broken down. Courses of Action: I. The residents should stop generating garbage. II. Additional workers and vehicles should be deployed and disposal sites reactivated. Which follow?",
 "options":{"A":'Only I',"B":'Only II follows',"C":'Both',"D":'Neither'},"answer":'B'},

{"id":214,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: A large section of consumers is complaining about high prices of essential goods. Courses of Action: I. The government should regulate prices of essential items and check hoarding. II. Import of essential items should be considered. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":215,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: Farmers are committing suicide due to crop failure and heavy debt. Courses of Action: I. The government should provide crop insurance and loan waivers. II. Farmers should stop cultivating crops altogether. Which follow?",
 "options":{"A":'Only I follows',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'A'},

{"id":216,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: The town has been hit by an outbreak of cholera. Courses of Action: I. Clean drinking water should be supplied and hygiene camps set up. II. Medical teams should be deployed. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":217,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: A national bank suffered heavy losses due to fraudulent loans. Courses of Action: I. All bank branches should be closed. II. An internal audit should be conducted and stricter loan approval systems introduced. Which follow?",
 "options":{"A":'Only I',"B":'Only II follows',"C":'Both',"D":'Neither'},"answer":'B'},

{"id":218,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: A large number of college students spend excessive time on social media, affecting studies. Courses of Action: I. Colleges should ban all mobile phones on campus. II. Awareness and counselling programs on digital wellbeing should be introduced. Which follow?",
 "options":{"A":'Only I',"B":'Only II follows',"C":'Both',"D":'Neither'},"answer":'B'},

{"id":219,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: There has been a sharp rise in cases of cybercrime in the country. Courses of Action: I. A dedicated cybercrime cell should be strengthened with trained personnel. II. Internet services in the country should be shut down. Which follow?",
 "options":{"A":'Only I follows',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'A'},

{"id":220,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: Public transport buses have been running with poor maintenance leading to frequent breakdowns. Courses of Action: I. Regular maintenance schedules should be enforced. II. Buses beyond their working life should be replaced. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both I and II follow',"D":'Neither'},"answer":'C'},

{"id":221,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: Many small shops in a town have been closing due to competition from a new supermarket. Courses of Action: I. The supermarket should be forced to close. II. Small shop owners should form cooperatives and diversify offerings. Which follow?",
 "options":{"A":'Only I',"B":'Only II follows',"C":'Both',"D":'Neither'},"answer":'B'},

{"id":222,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: Many students of a coaching centre have failed the entrance test. Courses of Action: I. The coaching centre should be shut down. II. Teaching methodology and student assessment at the centre should be reviewed. Which follow?",
 "options":{"A":'Only I',"B":'Only II follows',"C":'Both',"D":'Neither'},"answer":'B'},

{"id":223,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: The number of complaints about poor mobile network coverage has risen sharply. Courses of Action: I. The regulator should review service quality standards. II. Operators should invest in expanding tower infrastructure. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":224,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: A rare species of bird is on the verge of extinction. Courses of Action: I. Protected sanctuaries should be established for the species. II. Hunting and trade of the species should be banned. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":225,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: The city hospital is overwhelmed with patients during flu season. Courses of Action: I. Additional temporary wards and staff should be arranged. II. Home-treatment guidelines for mild cases should be publicised. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":226,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: A rural village suffers frequent power cuts of several hours daily. Courses of Action: I. Solar power installations should be promoted at household level. II. All villagers should be told to stop using electricity. Which follow?",
 "options":{"A":'Only I follows',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'A'},

{"id":227,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: A large multinational company plans layoffs due to a downturn. Courses of Action: I. Reskilling and outplacement support should be provided to affected employees. II. Alternative cost-cutting options should be evaluated first. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":228,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: Increasing incidents of stray dog attacks in a city. Courses of Action: I. Sterilisation and vaccination programme for stray dogs should be intensified. II. Reporting and rapid-response mechanism should be set up. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":229,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: A university's research output has fallen behind global peers. Courses of Action: I. Research funding and international collaborations should be enhanced. II. All faculty members should be dismissed. Which follow?",
 "options":{"A":'Only I follows',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'A'},

{"id":230,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: Complaints of adulteration of milk are pouring in from all parts of the city. Courses of Action: I. Surprise testing of milk vendors should be undertaken by the food safety authority. II. Consumers should be educated on how to check basic adulteration at home. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":231,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Hard',
 "question":"Statement: A new highway has caused increased noise pollution in nearby villages. Courses of Action: I. Sound barriers should be installed along the highway. II. Villagers should be relocated. Which follow?",
 "options":{"A":'Only I follows',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'A'},

{"id":232,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Hard',
 "question":"Statement: Students from a certain minority community are dropping out of college in large numbers. Courses of Action: I. Scholarships and mentorship programmes targeted at the community should be launched. II. Reasons for dropout should be studied through a formal survey. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both I and II follow',"D":'Neither'},"answer":'C'},

{"id":233,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: Repeated cases of pilferage have been reported at a large warehouse. Courses of Action: I. CCTV coverage and internal audit should be strengthened. II. All warehouse employees should be sacked. Which follow?",
 "options":{"A":'Only I follows',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'A'},

{"id":234,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: The literacy rate in a state has stagnated for the past decade. Courses of Action: I. Adult literacy programmes should be re-launched. II. School infrastructure and teacher availability should be reviewed. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":235,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: A large number of tourists have complained about overcharging by local operators at a hill station. Courses of Action: I. Standard tariff cards should be enforced. II. A tourist grievance helpline should be set up. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":236,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: The number of vehicles registered in the city has doubled in five years, worsening traffic. Courses of Action: I. Registration of new vehicles should be capped and public transport upgraded. II. Congestion pricing should be introduced in the central business district. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":237,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: Attendance in government offices has dropped significantly since work-from-home was allowed. Courses of Action: I. Attendance and output should be monitored through digital systems. II. All work-from-home should be immediately withdrawn. Which follow?",
 "options":{"A":'Only I follows',"B":'Only II',"C":'Both',"D":'Neither'},"answer":'A'},

{"id":238,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Hard',
 "question":"Statement: A neighbouring country has imposed steep tariffs on imports from us. Courses of Action: I. Trade negotiations should be initiated at the diplomatic level. II. Alternative export markets should be explored. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":239,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Medium',
 "question":"Statement: A new drug has shown severe side effects after being launched in the market. Courses of Action: I. The drug should be withdrawn from the market pending investigation. II. Regulatory approval procedures should be reviewed. Which follow?",
 "options":{"A":'Only I',"B":'Only II',"C":'Both follow',"D":'Neither'},"answer":'C'},

{"id":240,"subject":'Logical Reasoning',"topic":'Course of Action',"subtopic":'Course of Action',"difficulty":'Hard',
 "question":"Statement: Fake news on social media is causing communal tensions. Courses of Action: I. Social media platforms should be permanently banned. II. Fact-checking mechanisms and legal action against habitual offenders should be strengthened. Which follow?",
 "options":{"A":'Only I',"B":'Only II follows',"C":'Both',"D":'Neither'},"answer":'B'},

# =====================================================================
# TOPIC 5: CAUSE AND EFFECT (30)  id 241-270
# =====================================================================

{"id":241,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. All the sweets were rotten. II. Many people got sick after eating sweets from a local shop. Which is correct?",
 "options":{"A":'Statement I is the cause and II is its effect',"B":'Statement II is the cause and I is its effect',"C":'Both statements I and II are independent causes',"D":'Both statements I and II are effects of independent causes'},"answer":'A'},

{"id":242,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. Heavy rains lashed the city yesterday. II. Traffic movement was slow and jams were reported. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'A'},

{"id":243,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. The Government has recently increased its taxes on petrol. II. Prices of vegetables and other essential items have risen. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'A'},

{"id":244,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. The number of cars sold in the city increased sharply this year. II. The city recorded the highest ever levels of PM2.5 pollution this year. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'A'},

{"id":245,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. Many students of the school opted for private tuitions. II. The school announced additional revision classes on weekends. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'A'},

{"id":246,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. The government banned single-use plastic bags. II. Traders and consumers started using cloth bags. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'A'},

{"id":247,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. There is a sudden increase in demand for air-conditioners. II. The temperature this summer has crossed all-time highs. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":248,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. A large number of children in the village suffer from malnutrition. II. The village has poor access to clean water and healthcare. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":249,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. The average score in the mathematics test was very low this year. II. The syllabus was revised and made more difficult from this year. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":250,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. The stock market crashed heavily on Monday. II. A major international bank announced bankruptcy on Sunday. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":251,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. The state government has decided to increase the electricity tariff for domestic consumers. II. The state electricity board has been running in heavy losses for many years. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":252,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. Fuel prices have gone up significantly. II. Airline ticket fares have been increased. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'A'},

{"id":253,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. Rice production has dropped this year. II. There has been a poor monsoon this year. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":254,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. There has been an unprecedented rise in the number of dengue cases in the city. II. The civic body failed to carry out anti-larval spraying in most areas. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":255,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. Many companies are announcing layoffs. II. The economy is going through a recession. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":256,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. Prices of onions have shot up in the past month. II. The onion crop was damaged due to unseasonal rains in the growing region. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":257,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. The examination board postponed its board exams by one month. II. A major cyclone was forecast to hit the region during the original exam dates. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":258,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. Air quality in the capital deteriorated to hazardous levels. II. Schools in the capital were ordered closed for a week. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'A'},

{"id":259,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. A large number of vehicles ran out of fuel on the highway. II. A nationwide strike by fuel pump operators entered its third day. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":260,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. Water levels in dams supplying the city are at a five-year low. II. The civic body has announced a 25 percent cut in water supply. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'A'},

{"id":261,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Hard',
 "question":"Statements: I. Sales of electric two-wheelers have increased sharply this year. II. The government has extended purchase subsidies on electric two-wheelers. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":262,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Hard',
 "question":"Statements: I. Enrolment in engineering colleges has dropped this year. II. The job market for fresh engineering graduates has been weak for the past two years. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":263,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. Farmers in the state are protesting on the streets. II. The state government withdrew its support price for major crops. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":264,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. Rail traffic has been suspended between two major cities. II. Heavy landslides have blocked the railway line at two places. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":265,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. The number of deaths on the highway has reduced this year. II. New speed cameras and lane discipline enforcement began this year. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":266,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. A prominent business daily reported a scam in a leading bank. II. The bank's share price fell sharply on the same day. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'A'},

{"id":267,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. Ticket sales for the movie fell in the second week. II. Reviewers gave the film very poor ratings after release. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":268,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Hard',
 "question":"Statements: I. Rate of literacy in the district has improved. II. A large number of new primary schools were opened in the district in the last 5 years. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

{"id":269,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Hard',
 "question":"Statements: I. There have been reports of contaminated water in a residential locality. II. Cases of diarrhoea and stomach infections have risen sharply in that locality. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'A'},

{"id":270,"subject":'Logical Reasoning',"topic":'Cause and Effect',"subtopic":'Cause and Effect',"difficulty":'Medium',
 "question":"Statements: I. The city corporation has hiked property tax by 30 percent. II. Corporation revenues had been falling short of expenditure for three years. Which is correct?",
 "options":{"A":'I is the cause and II is its effect',"B":'II is the cause and I is its effect',"C":'Both are independent causes',"D":'Both are effects of independent causes'},"answer":'B'},

# =====================================================================
# TOPIC 6: CRITICAL THINKING (30)  id 271-300
# =====================================================================
# Format: statement / passage + inference; answer among Definitely true / Probably true / Data inadequate / Definitely false.

{"id":271,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Inference',"difficulty":'Medium',
 "question":"Direction: It will be a substantial achievement in the field of education if one provides one school for every village in our country and enforces attendance. Inference: Children in villages do not attend school regularly.",
 "options":{"A":'Definitely true',"B":'Probably true',"C":'Data inadequate',"D":'Definitely false'},"answer":'A'},

{"id":272,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Inference',"difficulty":'Medium',
 "question":"Statement: Regular exercise helps in maintaining good health and preventing many diseases. Inference: A person who does not exercise regularly will fall sick.",
 "options":{"A":'Definitely true',"B":'Probably true',"C":'Data inadequate',"D":'Definitely false'},"answer":'B'},

{"id":273,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Inference',"difficulty":'Medium',
 "question":"Statement: All top-ranked students in the class attend the coaching centre. Inference: Attending the coaching centre guarantees a top rank.",
 "options":{"A":'Definitely true',"B":'Probably true',"C":'Data inadequate',"D":'Definitely false'},"answer":'D'},

{"id":274,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Inference',"difficulty":'Medium',
 "question":"Statement: The traffic police has issued a notice to install speed governors in all commercial vehicles by next month. Inference: Commercial vehicles have been involved in many over-speeding accidents.",
 "options":{"A":'Definitely true',"B":'Probably true',"C":'Data inadequate',"D":'Definitely false'},"answer":'B'},

{"id":275,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Inference',"difficulty":'Medium',
 "question":"Statement: The government has decided to make Aadhaar mandatory for booking train tickets. Inference: The current booking system is being misused.",
 "options":{"A":'Definitely true',"B":'Probably true',"C":'Data inadequate',"D":'Definitely false'},"answer":'B'},

{"id":276,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Inference',"difficulty":'Easy',
 "question":"Statement: All fruits contain vitamins. Mango is a fruit. Inference: Mango contains vitamins.",
 "options":{"A":'Definitely true',"B":'Probably true',"C":'Data inadequate',"D":'Definitely false'},"answer":'A'},

{"id":277,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Inference',"difficulty":'Medium',
 "question":"Statement: The company recorded its highest ever profits last quarter. Inference: The company sold more products last quarter than in any previous quarter.",
 "options":{"A":'Definitely true',"B":'Probably true',"C":'Data inadequate',"D":'Definitely false'},"answer":'C'},

{"id":278,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Inference',"difficulty":'Medium',
 "question":"Statement: More than 60 percent of the citizens in a survey said they support the new tax reform. Inference: The reform will definitely be passed in the parliament.",
 "options":{"A":'Definitely true',"B":'Probably true',"C":'Data inadequate',"D":'Definitely false'},"answer":'C'},

{"id":279,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Inference',"difficulty":'Medium',
 "question":"Statement: Reading books improves vocabulary and concentration. Inference: A person who reads books regularly has good vocabulary and concentration.",
 "options":{"A":'Definitely true',"B":'Probably true',"C":'Data inadequate',"D":'Definitely false'},"answer":'B'},

{"id":280,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Inference',"difficulty":'Medium',
 "question":"Statement: The city recorded the highest ever rainfall in a single day last week. Inference: The city was better prepared than ever for the rains.",
 "options":{"A":'Definitely true',"B":'Probably true',"C":'Data inadequate',"D":'Definitely false'},"answer":'C'},

{"id":281,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Assumption',"difficulty":'Medium',
 "question":"Statement: The advertisement says: 'For a healthier lifestyle, drink Brand X fruit juice every morning.' Assumption: People are interested in a healthier lifestyle.",
 "options":{"A":'Assumption is implicit',"B":'Assumption is not implicit',"C":'Data inadequate',"D":'Assumption contradicts statement'},"answer":'A'},

{"id":282,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Assumption',"difficulty":'Medium',
 "question":"Statement: The Principal has instructed all teachers to reach school 15 minutes before start time. Assumption: Teachers are currently coming to school late.",
 "options":{"A":'Assumption is implicit',"B":'Assumption is not implicit',"C":'Data inadequate',"D":'Assumption contradicts statement'},"answer":'A'},

{"id":283,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Assumption',"difficulty":'Medium',
 "question":"Statement: 'Please switch off your mobile phones during the lecture.' Assumption: Mobile phones can disturb the lecture.",
 "options":{"A":'Assumption is implicit',"B":'Assumption is not implicit',"C":'Data inadequate',"D":'Assumption contradicts statement'},"answer":'A'},

{"id":284,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Assumption',"difficulty":'Medium',
 "question":"Statement: The Government has decided to hike the fees of professional courses in government institutes. Assumption: The Government has enough funds to run the courses even without a fee hike.",
 "options":{"A":'Assumption is implicit',"B":'Assumption is not implicit',"C":'Data inadequate',"D":'Assumption contradicts statement'},"answer":'B'},

{"id":285,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Assumption',"difficulty":'Hard',
 "question":"Statement: A warning at the swimming pool: 'Children below 12 must be accompanied by a parent.' Assumption: Children below 12 may not be able to swim safely on their own.",
 "options":{"A":'Assumption is implicit',"B":'Assumption is not implicit',"C":'Data inadequate',"D":'Assumption contradicts statement'},"answer":'A'},

{"id":286,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Strong and Weak Arguments',"difficulty":'Medium',
 "question":"Statement: Should smoking be banned in all public places? Argument: Yes, because passive smoking is harmful to the health of non-smokers. Is this argument strong or weak?",
 "options":{"A":'Strong',"B":'Weak',"C":'Cannot be determined',"D":'Data inadequate'},"answer":'A'},

{"id":287,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Strong and Weak Arguments',"difficulty":'Medium',
 "question":"Statement: Should students be given laptops free of cost in schools? Argument: No, because they will damage them. Is this argument strong or weak?",
 "options":{"A":'Strong',"B":'Weak',"C":'Cannot be determined',"D":'Data inadequate'},"answer":'B'},

{"id":288,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Strong and Weak Arguments',"difficulty":'Medium',
 "question":"Statement: Should there be a maximum age limit of 65 years for a person to hold a political office? Argument: Yes, because at this age a person loses his mental and physical fitness. Is this argument strong or weak?",
 "options":{"A":'Strong',"B":'Weak',"C":'Cannot be determined',"D":'Data inadequate'},"answer":'B'},

{"id":289,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Strong and Weak Arguments',"difficulty":'Medium',
 "question":"Statement: Should there be a common syllabus for all subjects at graduate level throughout the country? Argument: Yes, this is the only way to bring uniformity in the educational system of the country. Is this argument strong or weak?",
 "options":{"A":'Strong',"B":'Weak',"C":'Cannot be determined',"D":'Data inadequate'},"answer":'B'},

{"id":290,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Strong and Weak Arguments',"difficulty":'Hard',
 "question":"Statement: Should mobile phones be permitted inside examination halls? Argument: No, because students may misuse them for cheating. Is this argument strong or weak?",
 "options":{"A":'Strong',"B":'Weak',"C":'Cannot be determined',"D":'Data inadequate'},"answer":'A'},

{"id":291,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Conclusion',"difficulty":'Medium',
 "question":"Statement: The Government has decided to open up medical education to the private sector. Conclusion: The Government is not able to meet the growing demand for medical education on its own.",
 "options":{"A":'Conclusion follows',"B":'Conclusion does not follow',"C":'Data inadequate',"D":'Uncertain'},"answer":'A'},

{"id":292,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Conclusion',"difficulty":'Medium',
 "question":"Statement: In a village survey, 70 percent of the households reported no access to piped water. Conclusion: A majority of households in the village depend on other sources of water.",
 "options":{"A":'Conclusion follows',"B":'Conclusion does not follow',"C":'Data inadequate',"D":'Uncertain'},"answer":'A'},

{"id":293,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Conclusion',"difficulty":'Medium',
 "question":"Statement: All boys of Class X play cricket every day. Conclusion: Some boys of Class X are good cricketers.",
 "options":{"A":'Conclusion follows',"B":'Conclusion does not follow',"C":'Data inadequate',"D":'Uncertain'},"answer":'B'},

{"id":294,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Conclusion',"difficulty":'Medium',
 "question":"Statement: The new highway will pass through many villages, offering them faster access to the city. Conclusion: All villagers will benefit equally from the highway.",
 "options":{"A":'Conclusion follows',"B":'Conclusion does not follow',"C":'Data inadequate',"D":'Uncertain'},"answer":'B'},

{"id":295,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Conclusion',"difficulty":'Hard',
 "question":"Statement: Prices of essential commodities have risen sharply in the last six months. Conclusion: The purchasing power of ordinary households has decreased.",
 "options":{"A":'Conclusion follows',"B":'Conclusion does not follow',"C":'Data inadequate',"D":'Uncertain'},"answer":'A'},

{"id":296,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Inference',"difficulty":'Medium',
 "question":"Statement: Every year, thousands of people migrate to the city from villages in search of jobs. Inference: The villages do not offer enough employment opportunities.",
 "options":{"A":'Definitely true',"B":'Probably true',"C":'Data inadequate',"D":'Definitely false'},"answer":'B'},

{"id":297,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Inference',"difficulty":'Medium',
 "question":"Statement: The bookshop offers a 20% discount on the purchase of books above Rs. 500. Inference: The bookshop wants to increase its sales.",
 "options":{"A":'Definitely true',"B":'Probably true',"C":'Data inadequate',"D":'Definitely false'},"answer":'B'},

{"id":298,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Inference',"difficulty":'Hard',
 "question":"Statement: The government has decided to invest heavily in renewable energy over the next decade. Inference: Renewable energy is more expensive to generate than conventional energy today.",
 "options":{"A":'Definitely true',"B":'Probably true',"C":'Data inadequate',"D":'Definitely false'},"answer":'C'},

{"id":299,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Assumption',"difficulty":'Hard',
 "question":"Statement: The Principal announced that the school library will now stay open until 8 PM. Assumption: Students would like to use the library beyond regular school hours.",
 "options":{"A":'Assumption is implicit',"B":'Assumption is not implicit',"C":'Data inadequate',"D":'Contradiction'},"answer":'A'},

{"id":300,"subject":'Logical Reasoning',"topic":'Critical Thinking',"subtopic":'Statement and Conclusion',"difficulty":'Hard',
 "question":"Statement: A recent study shows that students who sleep for at least 7 hours a night perform better academically than those who sleep less. Conclusion: Sleep deprivation is a contributing factor to poor academic performance.",
 "options":{"A":'Conclusion follows',"B":'Conclusion does not follow',"C":'Data inadequate',"D":'Uncertain'},"answer":'A'},

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
    for t, c in topic.items():
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