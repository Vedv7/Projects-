from G1 import mba_main as g1
from G2 import mba_main as g2
#from G3 import mba_main as g3
from G4 import mba_main as g4
#from G5 import mba_main as g5
#from G6 import mba_main as g6
#from G7 import mba_main as g7
#from G8 import mba_main as g8
#from G9 import mba_main as g9
#from G10 import mba_main as g10
#from G11 import mba_main as g11

test_samples=[
    {'trans_id':'536365',
     'items_id': ['85123A',
                  '71053',
                  '84406B',
                  '84029G',
                  '84029E',
                  '22752',
                  '21730'],
      'items_ds':['WHITE HANGING HEART T-LIGHT HOLDER',
                    'WHITE METAL LANTERN',
                    'CREAM CUPID HEARTS COAT HANGER',
                    'KNITTED UNION FLAG HOT WATER BOTTLE',
                    'RED WOOLLY HOTTIE WHITE HEART.',
                    'SET 7 BABUSHKA NESTING BOXES',
                    'GLASS STAR FROSTED T-LIGHT HOLDER'],
     'customer_id':'17850',
     'country':'United Kingdom',
     'date':'12/1/2010',
     'time':'8:26:00 AM'
     },
    {'trans_id':'536366',
     'items_id': ['22633',
                  '22632'],
      'items_ds':['HAND WARMER UNION JACK',
                    'HAND WARMER RED POLKA DOT'],
     'customer_id':'17850',
     'country':'United Kingdom',
     'date':'12/1/2010',
     'time':'8:28:00 AM'
     },
    {'trans_id':'536367',
     'items_id': ['84879',
                '22745',
                '22748',
                '22749',
                '22310',
                '84969',
                '22623',
                '22622',
                '21754',
                '21755',
                '21777',
                '48187'],
      'items_ds':['ASSORTED COLOUR BIRD ORNAMENT',
                'POPPY\'S PLAYHOUSE BEDROOM ',
                'POPPY\'S PLAYHOUSE KITCHEN',
                'FELTCRAFT PRINCESS CHARLOTTE DOLL',
                'IVORY KNITTED MUG COSY ',
                'BOX OF 6 ASSORTED COLOUR TEASPOONS',
                'BOX OF VINTAGE JIGSAW BLOCKS ',
                'BOX OF VINTAGE ALPHABET BLOCKS',
                'HOME BUILDING BLOCK WORD',
                'LOVE BUILDING BLOCK WORD',
                'RECIPE BOX WITH METAL HEART',
                'DOORMAT NEW ENGLAND'],
     'customer_id':'13047',
     'country':'United Kingdom',
     'date':'12/1/2010',
     'time':'8:34:00 AM'
     },
    {'trans_id': '560571',
     'items_id': ['23296',
                    '23307',
                    '22381',
                    '20725',
                    '20726',
                    '20727',
                    '20728',
                    '22384',
                    '22382',
                    '22662',
                    '22383',
                    '23207',
                    '23209',
                    '23206',
                    '23208',
                    '22896',
                    '22895',
                    '22423',
                    '22551',
                    '21989',
                    '22613',
                    '21078',
                    '84279P',
                    '22326',
                    '21558',
                    '21559',
                    '21561',
                    '22629',
                    '22630',
                    '23293',
                    '23294',
                    '23297',
                    '23308',
                    '23295'
                    ],
     'items_ds': ['SET OF 6 TEA TIME BAKING CASES',
                    'SET OF 60 PANTRY DESIGN CAKE CASES',
                    'TOY TIDY PINK POLKADOT',
                    'LUNCH BAG RED RETROSPOT',
                    'LUNCH BAG WOODLAND',
                    'LUNCH BAG  BLACK SKULL.',
                    'LUNCH BAG CARS BLUE',
                    'LUNCH BAG PINK POLKADOT',
                    'LUNCH BAG SPACEBOY DESIGN',
                    'LUNCH BAG DOLLY GIRL DESIGN',
                    'LUNCH BAG SUKI DESIGN',
                    'LUNCH BAG ALPHABET DESIGN',
                    'LUNCH BAG DOILEY PATTERN',
                    'LUNCH BAG APPLE DESIGN',
                    'LUNCH BAG VINTAGE LEAF DESIGN',
                    'PEG BAG APPLES DESIGN',
                    'SET OF 2 TEA TOWELS APPLE AND PEARS',
                    'REGENCY CAKESTAND 3 TIER',
                    'PLASTERS IN TIN SPACEBOY',
                    'PACK OF 20 SKULL PAPER NAPKINS',
                    'PACK OF 20 SPACEBOY NAPKINS',
                    'SET/20 STRAWBERRY PAPER NAPKINS',
                    'CHERRY BLOSSOM  DECORATIVE FLASK',
                    'ROUND SNACK BOXES SET OF4 WOODLAND',
                    'SKULL LUNCH BOX WITH CUTLERY',
                    'STRAWBERRY LUNCH BOX WITH CUTLERY',
                    'DINOSAUR LUNCH BOX WITH CUTLERY',
                    'SPACEBOY LUNCH BOX',
                    'DOLLY GIRL LUNCH BOX',
                    'SET OF 12 FAIRY CAKE BAKING CASES',
                    'SET OF 6 SNACK LOAF BAKING CASES',
                    'SET 40 HEART SHAPE PETIT FOUR CASES',
                    'SET OF 60 VINTAGE LEAF CAKE CASES',
                    'SET OF 12 MINI LOAF BAKING CASES'
                    ],
     'customer_id':'17735',
     'country':'United Kingdom',
     'date':'7/19/2011',
     'time':'2:29:00 PM'
     },
    {'trans_id': '581587',
     'items_id': ['22631',
                    '22556',
                    '22555',
                    '22728',
                    '22727',
                    '22726',
                    '22730',
                    '22367',
                    '22629',
                    '23256',
                    '22613',
                    '22899',
                    '23254',
                    '23255',
                    '22138'
                    ],
     'items_ds': ['CIRCUS PARADE LUNCH BOX',
                    'PLASTERS IN TIN CIRCUS PARADE',
                    'PLASTERS IN TIN STRONGMAN',
                    'ALARM CLOCK BAKELIKE PINK',
                    'ALARM CLOCK BAKELIKE RED ',
                    'ALARM CLOCK BAKELIKE GREEN',
                    'ALARM CLOCK BAKELIKE IVORY',
                    'CHILDRENS APRON SPACEBOY DESIGN',
                    'SPACEBOY LUNCH BOX ',
                    'CHILDRENS CUTLERY SPACEBOY ',
                    'PACK OF 20 SPACEBOY NAPKINS',
                    'CHILDREN\'S APRON DOLLY GIRL',
                    'CHILDRENS CUTLERY DOLLY GIRL ',
                    'CHILDRENS CUTLERY CIRCUS PARADE',
                    'BAKING SET 9 PIECE RETROSPOT'
                    ],
     'customer_id':'12680',
     'country':'France',
     'date':'12/9/2011',
     'time':'12:50:00 PM'
     },
]

def get_score(recommend_res, current_item, items_list):
    max_score = 0
    if (current_item in recommend_res):
        recommend_res.remove(current_item)
    for i in range(len(recommend_res)):
        cur_recom = recommend_res[i]
        cur_score = 0
        if(cur_recom in items_list):
            if(i == 0):
                cur_score = 5
            elif(i < 5):
                cur_score = 3
            elif(i < 10):
                cur_score = 1
            else:
                cur_score = 0
            if(cur_score > max_score):
                max_score = cur_score
    return max_score

def test_single_sample(g_idx, sample):
    trans_id = sample['trans_id']
    items_id = sample['items_id']
    items_ds = sample['items_ds']
    customer_id = sample['customer_id']
    country = sample['country']
    date = sample['date']
    time = sample['time']

    scores = []
    g5_scores = []
    g6_scores = []
    for i in range(len(items_id)):
        cur_item_id = items_id[i]
        cur_item_ds = items_ds[i]
        use_id = True
        if(g_idx == -1):
            return None
        elif(g_idx == 0):
            cur_res = g1.RecommendItems(cur_item_id, customer_id, country, time, date)
        elif(g_idx == 1):
            cur_res = g2.RecommendItems(cur_item_id, customer_id, country, time, date)
        #elif (g_idx == 2):
        #    cur_res = g3.RecommendItems(cur_item_id, customer_id, country, time, date)
        elif (g_idx == 3):
            cur_res = g4.RecommendItems(cur_item_id, customer_id, country, time, date)
        elif (g_idx == 4):
            cur_res = g5.RecommendItems(cur_item_id, customer_id, country, time, date)
        elif (g_idx == 5):
            cur_res = g6.RecommendItems(cur_item_id, customer_id, country, time, date)
        elif (g_idx == 6):
            cur_res = g7.RecommendItems(cur_item_id, customer_id, country, time, date)
        elif (g_idx == 7):
            cur_res = g8.RecommendItems(cur_item_id, customer_id, country, time, date)
        elif (g_idx == 8):
            cur_res = g9.RecommendItems(cur_item_id, customer_id, country, time, date)
        elif (g_idx == 9):
            cur_res = g10.RecommendItems(cur_item_id, customer_id, country, time, date)
        elif (g_idx == 10):
            cur_res = g11.RecommendItems(cur_item_id, customer_id, country, time, date)
        else:
            return None
        cur_score = 0
        if(use_id):
            cur_score = get_score(cur_res, cur_item_id, items_id)
        else:
            cur_score = get_score(cur_res, cur_item_ds, items_ds)
        scores.append(cur_score)
    #compute average
    total_score_sum = 0
    for cur_score in scores:
        total_score_sum += cur_score
    avg_score = total_score_sum/len(scores)
    return [avg_score, scores]

def compute_performance(g_idx, test_samples):
    raw_res_list = []
    avg_res_list = []
    for cur_sample in test_samples:
        cur_res = test_single_sample(g_idx, cur_sample)
        raw_res_list.append(cur_res)
        avg_res_list.append(cur_res[0])
    total_score_sum = 0
    for cur_score in avg_res_list:
        total_score_sum += cur_score
    avg_score = total_score_sum / len(avg_res_list)
    return [avg_score, raw_res_list]

def test():
    groups = [
        0,#g1 working but slow
        0,#g2 working relatively fast
        -1,#g3 needs install special library
        0,#g4 working relatively
        -1,#g5 not generating result
        -1,#g6 seems working it has test code need to clean it up
        -1,#g7 not working AttributeError: 'DataFrame' object has no attribute 'map'
        -1,#g8 not generating results for most items stuck after Items frequently bought together with 21755:
        -1,#g9 working but scored 0
        -1,#g10 needs install special library
        -1,#g11 not working Unable to allocate 87.1 GiB for an array with shape (313236, 2, 18668) and data type int64
    ]
    groups_res = [
        None,  # g1
        None,  # g2
        None,  # g3
        None,  # g4
        None,  # g5
        None,  # g6
        None,  # g7
        None,  # g8
        None,  # g9
        None,  # g10
        None,  # g11
    ]

    for g_idx in range(len(groups)):
        if(groups[g_idx] == -1):
            continue
        groups_res[g_idx] = compute_performance(g_idx, test_samples)
    max_g_score = -1
    for g_idx in range(len(groups)):
        print(g_idx)
        if (groups[g_idx] == -1):
            continue
        cur_score = groups_res[g_idx][0]
        print('cur_score = ', cur_score)
        if(cur_score > max_g_score):
            max_g_score = cur_score
    print('max_g_score = ', max_g_score)
    groups_grade = []
    for g_idx in range(len(groups)):
        if (groups[g_idx] == -1):
            groups_grade.append(0)
            continue
        groups_grade.append(30*groups_res[g_idx][0]/max_g_score)
    print('============================')
    print('groups_grade= ')
    print(groups_grade)

test()
#groups_grade=[0, 29.999999999999996, 0, 20.312124849939977, 0, 0, 0, 0, 0, 0, 0]
#[20.292496998799518, 29.999999999999996, 0, 19.02641056422569, 0, 0, 0, 0, 0, 0, 0]