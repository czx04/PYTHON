from pymongo import MongoClient

client = MongoClient(
    f"mongodb+srv://anhchaiuem:anhchaiuem@pep.ghbx8ax.mongodb.net/?retryWrites=true&w=majority&appName=PEP")

db = client['overview']
collection = db['overview']

datagame = [a for a in collection.find()]

# datagame = [
#     {
#         "game": "Valorant",
#         "platform": [
#             "android",
#             "ios"
#         ],
#         "user_up": {
#             "JAN": "3188",
#             "FEB": "7731",
#             "MAR": "5203",
#             "APR": "2380",
#             "MAY": "7307",
#             "JUN": "7076",
#             "JUL": "4474",
#             "AUG": "6217",
#             "SEP": "5964",
#             "OCT": "4903",
#             "NOV": "6722",
#             "DEC": "7556"
#         },
#         "users/country": {
#             "USA": "29312",
#             "VietNam": "24189",
#             "Korea": "21113",
#             "Japan": "23693",
#             "Taiwan": "19647",
#             "Singapore": "26898",
#             "Thailand": "19023",
#             "Laos": "26003",
#             "Russia": "21710",
#             "North Korea": "23618"
#         },
#         "avg_daily_active_user": {
#             "JAN": "5014",
#             "FEB": "3459",
#             "MAR": "6575",
#             "APR": "3358",
#             "MAY": "3840",
#             "JUN": "4060",
#             "JUL": "3490",
#             "AUG": "5341",
#             "SEP": "7093",
#             "OCT": "3762",
#             "NOV": "2298",
#             "DEC": "5163"
#         },
#         "active_user/country": {
#             "USA": "7446",
#             "VietNam": "9968",
#             "Korea": "25099",
#             "Japan": "8558",
#             "Taiwan": "13385",
#             "Singapore": "24832",
#             "Thailand": "5710",
#             "Laos": "16656",
#             "Russia": "12445",
#             "North Korea": "13229"
#         },
#         "selling_product": [
#             "Classic",
#             "gay",
#             "dao"
#         ],
#         "products": [
#             {
#                 "prd": "dao",
#                 "price": "3500",
#                 "tier": "S",
#                 "sales volume": "4786"
#             },
#             {
#                 "prd": "gay",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "2459"
#             },
#             {
#                 "prd": "Classic",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "1299"
#             }
#         ],
#         "session": [
#             {
#                 "day": "04/11/2024",
#                 "session": "14796"
#             },
#             {
#                 "day": "05/11/2024",
#                 "session": "12465"
#             },
#             {
#                 "day": "06/11/2024",
#                 "session": "26561"
#             },
#             {
#                 "day": "07/11/2024",
#                 "session": "13697"
#             },
#             {
#                 "day": "08/11/2024",
#                 "session": "26729"
#             },
#             {
#                 "day": "09/11/2024",
#                 "session": "21353"
#             },
#             {
#                 "day": "10/11/2024",
#                 "session": "11810"
#             },
#             {
#                 "day": "11/11/2024",
#                 "session": "9653"
#             },
#             {
#                 "day": "12/11/2024",
#                 "session": "14453"
#             }
#         ],
#         "avgtime/day": [
#             {
#                 "day": "04/11/2024",
#                 "avg": "2.21023"
#             },
#             {
#                 "day": "05/11/2024",
#                 "avg": "0.48292"
#             },
#             {
#                 "day": "06/11/2024",
#                 "avg": "1.78124"
#             },
#             {
#                 "day": "07/11/2024",
#                 "avg": "0.40642"
#             },
#             {
#                 "day": "08/11/2024",
#                 "avg": "1.2815"
#             },
#             {
#                 "day": "09/11/2024",
#                 "avg": "2.79395"
#             },
#             {
#                 "day": "10/11/2024",
#                 "avg": "3.09798"
#             },
#             {
#                 "day": "11/11/2024",
#                 "avg": "0.94451"
#             },
#             {
#                 "day": "12/11/2024",
#                 "avg": "1.63295"
#             }
#         ],
#         "retention_data": [
#             {
#                 "day": "30/10/2024",
#                 "retention_day_1": 127,
#                 "retention_day_2": 56,
#                 "retention_day_3": 43,
#                 "retention_day_4": 81,
#                 "retention_day_5": 178,
#                 "retention_day_6": 180,
#                 "retention_day_7": 66
#             },
#             {
#                 "day": "31/10/2024",
#                 "retention_day_1": 520,
#                 "retention_day_2": 322,
#                 "retention_day_3": 107,
#                 "retention_day_4": 11,
#                 "retention_day_5": 81,
#                 "retention_day_6": 87,
#                 "retention_day_7": 177
#             },
#             {
#                 "day": "01/11/2024",
#                 "retention_day_1": 221,
#                 "retention_day_2": 76,
#                 "retention_day_3": 77,
#                 "retention_day_4": 98,
#                 "retention_day_5": 149,
#                 "retention_day_6": 109,
#                 "retention_day_7": 223
#             },
#             {
#                 "day": "02/11/2024",
#                 "retention_day_1": 236,
#                 "retention_day_2": 292,
#                 "retention_day_3": 175,
#                 "retention_day_4": 18,
#                 "retention_day_5": 185,
#                 "retention_day_6": 210,
#                 "retention_day_7": 118
#             },
#             {
#                 "day": "03/11/2024",
#                 "retention_day_1": 693,
#                 "retention_day_2": 297,
#                 "retention_day_3": 55,
#                 "retention_day_4": 29,
#                 "retention_day_5": 304,
#                 "retention_day_6": 71,
#                 "retention_day_7": 88
#             },
#             {
#                 "day": "04/11/2024",
#                 "retention_day_1": 442,
#                 "retention_day_2": 102,
#                 "retention_day_3": 97,
#                 "retention_day_4": 65,
#                 "retention_day_5": 255,
#                 "retention_day_6": 141,
#                 "retention_day_7": 108
#             },
#             {
#                 "day": "05/11/2024",
#                 "retention_day_1": 340,
#                 "retention_day_2": 190,
#                 "retention_day_3": 97,
#                 "retention_day_4": 40,
#                 "retention_day_5": 118,
#                 "retention_day_6": 158,
#                 "retention_day_7": 168
#             },
#             {
#                 "day": "06/11/2024",
#                 "retention_day_1": 492,
#                 "retention_day_2": 359,
#                 "retention_day_3": 93,
#                 "retention_day_4": 61,
#                 "retention_day_5": 139,
#                 "retention_day_6": 235,
#                 "retention_day_7": 80
#             },
#             {
#                 "day": "07/11/2024",
#                 "retention_day_1": 435,
#                 "retention_day_2": 100,
#                 "retention_day_3": 161,
#                 "retention_day_4": 55,
#                 "retention_day_5": 131,
#                 "retention_day_6": 28,
#                 "retention_day_7": 53
#             },
#             {
#                 "day": "08/11/2024",
#                 "retention_day_1": 282,
#                 "retention_day_2": 284,
#                 "retention_day_3": 170,
#                 "retention_day_4": 100,
#                 "retention_day_5": 333,
#                 "retention_day_6": 225,
#                 "retention_day_7": 102
#             },
#             {
#                 "day": "09/11/2024",
#                 "retention_day_1": 538,
#                 "retention_day_2": 380,
#                 "retention_day_3": 170,
#                 "retention_day_4": 53,
#                 "retention_day_5": 317,
#                 "retention_day_6": 42,
#                 "retention_day_7": 132
#             },
#             {
#                 "day": "10/11/2024",
#                 "retention_day_1": 561,
#                 "retention_day_2": 265,
#                 "retention_day_3": 131,
#                 "retention_day_4": 78,
#                 "retention_day_5": 326,
#                 "retention_day_6": 28,
#                 "retention_day_7": 120
#             },
#             {
#                 "day": "11/11/2024",
#                 "retention_day_1": 300,
#                 "retention_day_2": 226,
#                 "retention_day_3": 73,
#                 "retention_day_4": 49,
#                 "retention_day_5": 66,
#                 "retention_day_6": 192,
#                 "retention_day_7": 121
#             },
#             {
#                 "day": "12/11/2024",
#                 "retention_day_1": 293,
#                 "retention_day_2": 391,
#                 "retention_day_3": 59,
#                 "retention_day_4": 20,
#                 "retention_day_5": 252,
#                 "retention_day_6": 234,
#                 "retention_day_7": 90
#             }
#         ],
#         "revenue_data": [
#             {
#                 "day": "04/11/2024",
#                 "revenue": 256
#             },
#             {
#                 "day": "05/11/2024",
#                 "revenue": 439
#             },
#             {
#                 "day": "06/11/2024",
#                 "revenue": 311
#             },
#             {
#                 "day": "07/11/2024",
#                 "revenue": 210
#             },
#             {
#                 "day": "08/11/2024",
#                 "revenue": 168
#             },
#             {
#                 "day": "09/11/2024",
#                 "revenue": 213
#             },
#             {
#                 "day": "10/11/2024",
#                 "revenue": 171
#             },
#             {
#                 "day": "11/11/2024",
#                 "revenue": 335
#             },
#             {
#                 "day": "12/11/2024",
#                 "revenue": 116
#             },
#             {
#                 "day": "13/11/2024",
#                 "revenue": 184
#             }
#         ],
#         "ad_revenue_data": [
#             {"day": "04/11/2024", "ad_rev_median": 100, "ad_rev_avg": 120},
#             {"day": "05/11/2024", "ad_rev_median": 150, "ad_rev_avg": 170},
#             {"day": "06/11/2024", "ad_rev_median": 130, "ad_rev_avg": 140},
#             {"day": "07/11/2024", "ad_rev_median": 180, "ad_rev_avg": 190},
#             {"day": "08/11/2024", "ad_rev_median": 200, "ad_rev_avg": 220},
#             {"day": "09/11/2024", "ad_rev_median": 210, "ad_rev_avg": 230},
#             {"day": "10/11/2024", "ad_rev_median": 220, "ad_rev_avg": 240},
#             {"day": "11/11/2024", "ad_rev_median": 250, "ad_rev_avg": 270},
#             {"day": "12/11/2024", "ad_rev_median": 260, "ad_rev_avg": 280},
#             {"day": "13/11/2024", "ad_rev_median": 270, "ad_rev_avg": 290},
#         ],
#         "user": "22502",
#         "today_revenue": "18567",
#         "request": "43706"
#     }
#     ,
#     {
#         "game": "Blue Archive",
#         "platform": [
#             "android",
#             "ios"
#         ],
#         "ad_revenue_data": [
#             {"day": "04/11/2024", "ad_rev_median": 100, "ad_rev_avg": 120},
#             {"day": "05/11/2024", "ad_rev_median": 150, "ad_rev_avg": 170},
#             {"day": "06/11/2024", "ad_rev_median": 130, "ad_rev_avg": 140},
#             {"day": "07/11/2024", "ad_rev_median": 180, "ad_rev_avg": 190},
#             {"day": "08/11/2024", "ad_rev_median": 200, "ad_rev_avg": 220},
#             {"day": "09/11/2024", "ad_rev_median": 210, "ad_rev_avg": 230},
#             {"day": "10/11/2024", "ad_rev_median": 220, "ad_rev_avg": 240},
#             {"day": "11/11/2024", "ad_rev_median": 250, "ad_rev_avg": 270},
#             {"day": "12/11/2024", "ad_rev_median": 260, "ad_rev_avg": 280},
#             {"day": "13/11/2024", "ad_rev_median": 270, "ad_rev_avg": 290},
#         ],
#         "user_up": {
#             "JAN": "5704",
#             "FEB": "4241",
#             "MAR": "4435",
#             "APR": "2972",
#             "MAY": "5510",
#             "JUN": "5760",
#             "JUL": "2075",
#             "AUG": "2971",
#             "SEP": "2361",
#             "OCT": "4497",
#             "NOV": "4055",
#             "DEC": "5929"
#         },
#         "users/country": {
#             "USA": "23859",
#             "VietNam": "21780",
#             "Korea": "13372",
#             "Japan": "28705",
#             "Taiwan": "9002",
#             "Singapore": "9464",
#             "Thailand": "4043",
#             "Laos": "17024",
#             "Russia": "26401",
#             "North Korea": "23404"
#         },
#         "avg_daily_active_user": {
#             "JAN": "7115",
#             "FEB": "5818",
#             "MAR": "6953",
#             "APR": "2970",
#             "MAY": "4074",
#             "JUN": "3880",
#             "JUL": "6217",
#             "AUG": "3404",
#             "SEP": "6380",
#             "OCT": "6385",
#             "NOV": "4753",
#             "DEC": "3331"
#         },
#         "active_user/country": {
#             "USA": "28307",
#             "VietNam": "14175",
#             "Korea": "7936",
#             "Japan": "23486",
#             "Taiwan": "16981",
#             "Singapore": "25060",
#             "Thailand": "24660",
#             "Laos": "23206",
#             "Russia": "12668",
#             "North Korea": "17796"
#         },
#         "selling_product": [
#             "Classic",
#             "gay",
#             "dao"
#         ],
#         "products": [
#             {
#                 "prd": "dao",
#                 "price": "3500",
#                 "tier": "S",
#                 "sales volume": "4501"
#             },
#             {
#                 "prd": "gay",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "4585"
#             },
#             {
#                 "prd": "Classic",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "4849"
#             }
#         ],
#         "session": [
#             {
#                 "day": "04/11/2024",
#                 "session": "21410"
#             },
#             {
#                 "day": "05/11/2024",
#                 "session": "23575"
#             },
#             {
#                 "day": "06/11/2024",
#                 "session": "9449"
#             },
#             {
#                 "day": "07/11/2024",
#                 "session": "28097"
#             },
#             {
#                 "day": "08/11/2024",
#                 "session": "14585"
#             },
#             {
#                 "day": "09/11/2024",
#                 "session": "22975"
#             },
#             {
#                 "day": "10/11/2024",
#                 "session": "2132"
#             },
#             {
#                 "day": "11/11/2024",
#                 "session": "3431"
#             },
#             {
#                 "day": "12/11/2024",
#                 "session": "5022"
#             }
#         ],
#         "avgtime/day": [
#             {
#                 "day": "04/11/2024",
#                 "avg": "3.11333"
#             },
#             {
#                 "day": "05/11/2024",
#                 "avg": "1.26465"
#             },
#             {
#                 "day": "06/11/2024",
#                 "avg": "2.40262"
#             },
#             {
#                 "day": "07/11/2024",
#                 "avg": "3.12387"
#             },
#             {
#                 "day": "08/11/2024",
#                 "avg": "1.49956"
#             },
#             {
#                 "day": "09/11/2024",
#                 "avg": "3.04761"
#             },
#             {
#                 "day": "10/11/2024",
#                 "avg": "2.06461"
#             },
#             {
#                 "day": "11/11/2024",
#                 "avg": "3.01037"
#             },
#             {
#                 "day": "12/11/2024",
#                 "avg": "1.98222"
#             }
#         ],
#         "retention_data": [
#             {
#                 "day": "30/10/2024",
#                 "retention_day_1": 268,
#                 "retention_day_2": 243,
#                 "retention_day_3": 55,
#                 "retention_day_4": 52,
#                 "retention_day_5": 324,
#                 "retention_day_6": 205,
#                 "retention_day_7": 82
#             },
#             {
#                 "day": "31/10/2024",
#                 "retention_day_1": 571,
#                 "retention_day_2": 292,
#                 "retention_day_3": 81,
#                 "retention_day_4": 31,
#                 "retention_day_5": 228,
#                 "retention_day_6": 83,
#                 "retention_day_7": 205
#             },
#             {
#                 "day": "01/11/2024",
#                 "retention_day_1": 197,
#                 "retention_day_2": 283,
#                 "retention_day_3": 32,
#                 "retention_day_4": 13,
#                 "retention_day_5": 298,
#                 "retention_day_6": 182,
#                 "retention_day_7": 209
#             },
#             {
#                 "day": "02/11/2024",
#                 "retention_day_1": 953,
#                 "retention_day_2": 377,
#                 "retention_day_3": 164,
#                 "retention_day_4": 87,
#                 "retention_day_5": 261,
#                 "retention_day_6": 132,
#                 "retention_day_7": 103
#             },
#             {
#                 "day": "03/11/2024",
#                 "retention_day_1": 488,
#                 "retention_day_2": 132,
#                 "retention_day_3": 120,
#                 "retention_day_4": 47,
#                 "retention_day_5": 212,
#                 "retention_day_6": 175,
#                 "retention_day_7": 18
#             },
#             {
#                 "day": "04/11/2024",
#                 "retention_day_1": 574,
#                 "retention_day_2": 191,
#                 "retention_day_3": 184,
#                 "retention_day_4": 74,
#                 "retention_day_5": 71,
#                 "retention_day_6": 205,
#                 "retention_day_7": 219
#             },
#             {
#                 "day": "05/11/2024",
#                 "retention_day_1": 515,
#                 "retention_day_2": 138,
#                 "retention_day_3": 159,
#                 "retention_day_4": 71,
#                 "retention_day_5": 244,
#                 "retention_day_6": 188,
#                 "retention_day_7": 169
#             },
#             {
#                 "day": "06/11/2024",
#                 "retention_day_1": 1072,
#                 "retention_day_2": 371,
#                 "retention_day_3": 144,
#                 "retention_day_4": 93,
#                 "retention_day_5": 220,
#                 "retention_day_6": 34,
#                 "retention_day_7": 155
#             },
#             {
#                 "day": "07/11/2024",
#                 "retention_day_1": 502,
#                 "retention_day_2": 156,
#                 "retention_day_3": 148,
#                 "retention_day_4": 57,
#                 "retention_day_5": 36,
#                 "retention_day_6": 239,
#                 "retention_day_7": 79
#             },
#             {
#                 "day": "08/11/2024",
#                 "retention_day_1": 581,
#                 "retention_day_2": 50,
#                 "retention_day_3": 162,
#                 "retention_day_4": 16,
#                 "retention_day_5": 97,
#                 "retention_day_6": 27,
#                 "retention_day_7": 56
#             },
#             {
#                 "day": "09/11/2024",
#                 "retention_day_1": 636,
#                 "retention_day_2": 235,
#                 "retention_day_3": 96,
#                 "retention_day_4": 26,
#                 "retention_day_5": 169,
#                 "retention_day_6": 125,
#                 "retention_day_7": 139
#             },
#             {
#                 "day": "10/11/2024",
#                 "retention_day_1": 800,
#                 "retention_day_2": 140,
#                 "retention_day_3": 37,
#                 "retention_day_4": 18,
#                 "retention_day_5": 73,
#                 "retention_day_6": 149,
#                 "retention_day_7": 42
#             },
#             {
#                 "day": "11/11/2024",
#                 "retention_day_1": 858,
#                 "retention_day_2": 74,
#                 "retention_day_3": 51,
#                 "retention_day_4": 73,
#                 "retention_day_5": 302,
#                 "retention_day_6": 208,
#                 "retention_day_7": 214
#             },
#             {
#                 "day": "12/11/2024",
#                 "retention_day_1": 1119,
#                 "retention_day_2": 147,
#                 "retention_day_3": 114,
#                 "retention_day_4": 86,
#                 "retention_day_5": 281,
#                 "retention_day_6": 79,
#                 "retention_day_7": 157
#             }
#         ],
#         "revenue_data": [
#             {
#                 "day": "04/11/2024",
#                 "revenue": 451
#             },
#             {
#                 "day": "05/11/2024",
#                 "revenue": 418
#             },
#             {
#                 "day": "06/11/2024",
#                 "revenue": 449
#             },
#             {
#                 "day": "07/11/2024",
#                 "revenue": 426
#             },
#             {
#                 "day": "08/11/2024",
#                 "revenue": 430
#             },
#             {
#                 "day": "09/11/2024",
#                 "revenue": 331
#             },
#             {
#                 "day": "10/11/2024",
#                 "revenue": 187
#             },
#             {
#                 "day": "11/11/2024",
#                 "revenue": 495
#             },
#             {
#                 "day": "12/11/2024",
#                 "revenue": 253
#             },
#             {
#                 "day": "13/11/2024",
#                 "revenue": 307
#             }
#         ],
#         "user": "29966",
#         "today_revenue": "10361",
#         "request": "44097"
#     }
#     ,
#     {
#         "game": "Clash of Clans",
#         "platform": [
#             "android",
#             "ios"
#         ],
#         "user_up": {
#             "JAN": "7341",
#             "FEB": "5431",
#             "MAR": "6903",
#             "APR": "6235",
#             "MAY": "6295",
#             "JUN": "7312",
#             "JUL": "6921",
#             "AUG": "5312",
#             "SEP": "2224",
#             "OCT": "6053",
#             "NOV": "6866",
#             "DEC": "7309"
#         },
#         "users/country": {
#             "USA": "13471",
#             "VietNam": "21225",
#             "Korea": "23942",
#             "Japan": "12478",
#             "Taiwan": "23239",
#             "Singapore": "24156",
#             "Thailand": "24451",
#             "Laos": "6700",
#             "Russia": "16682",
#             "North Korea": "22873"
#         },
#         "avg_daily_active_user": {
#             "JAN": "3233",
#             "FEB": "5129",
#             "MAR": "7321",
#             "APR": "3206",
#             "MAY": "6637",
#             "JUN": "7075",
#             "JUL": "2394",
#             "AUG": "2784",
#             "SEP": "2272",
#             "OCT": "3340",
#             "NOV": "4714",
#             "DEC": "5671"
#         },
#         "active_user/country": {
#             "USA": "7139",
#             "VietNam": "17774",
#             "Korea": "17660",
#             "Japan": "2812",
#             "Taiwan": "9344",
#             "Singapore": "16482",
#             "Thailand": "10114",
#             "Laos": "14495",
#             "Russia": "15305",
#             "North Korea": "22796"
#         },
#         "selling_product": [
#             "Classic",
#             "gay",
#             "dao"
#         ],
#         "products": [
#             {
#                 "prd": "dao",
#                 "price": "3500",
#                 "tier": "S",
#                 "sales volume": "2366"
#             },
#             {
#                 "prd": "gay",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "2457"
#             },
#             {
#                 "prd": "Classic",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "3050"
#             }
#         ],
#         "session": [
#             {
#                 "day": "04/11/2024",
#                 "session": "25581"
#             },
#             {
#                 "day": "05/11/2024",
#                 "session": "26154"
#             },
#             {
#                 "day": "06/11/2024",
#                 "session": "11807"
#             },
#             {
#                 "day": "07/11/2024",
#                 "session": "6802"
#             },
#             {
#                 "day": "08/11/2024",
#                 "session": "5477"
#             },
#             {
#                 "day": "09/11/2024",
#                 "session": "10856"
#             },
#             {
#                 "day": "10/11/2024",
#                 "session": "13785"
#             },
#             {
#                 "day": "11/11/2024",
#                 "session": "26162"
#             },
#             {
#                 "day": "12/11/2024",
#                 "session": "18617"
#             }
#         ],
#         "avgtime/day": [
#             {
#                 "day": "04/11/2024",
#                 "avg": "3.30032"
#             },
#             {
#                 "day": "05/11/2024",
#                 "avg": "3.13395"
#             },
#             {
#                 "day": "06/11/2024",
#                 "avg": "0.89529"
#             },
#             {
#                 "day": "07/11/2024",
#                 "avg": "0.97332"
#             },
#             {
#                 "day": "08/11/2024",
#                 "avg": "3.11276"
#             },
#             {
#                 "day": "09/11/2024",
#                 "avg": "1.12026"
#             },
#             {
#                 "day": "10/11/2024",
#                 "avg": "1.51725"
#             },
#             {
#                 "day": "11/11/2024",
#                 "avg": "0.70021"
#             },
#             {
#                 "day": "12/11/2024",
#                 "avg": "2.68643"
#             }
#         ],
#         "retention_data": [
#             {
#                 "day": "30/10/2024",
#                 "retention_day_1": 280,
#                 "retention_day_2": 218,
#                 "retention_day_3": 175,
#                 "retention_day_4": 51,
#                 "retention_day_5": 123,
#                 "retention_day_6": 51,
#                 "retention_day_7": 228
#             },
#             {
#                 "day": "31/10/2024",
#                 "retention_day_1": 359,
#                 "retention_day_2": 248,
#                 "retention_day_3": 118,
#                 "retention_day_4": 48,
#                 "retention_day_5": 335,
#                 "retention_day_6": 216,
#                 "retention_day_7": 139
#             },
#             {
#                 "day": "01/11/2024",
#                 "retention_day_1": 900,
#                 "retention_day_2": 352,
#                 "retention_day_3": 42,
#                 "retention_day_4": 29,
#                 "retention_day_5": 87,
#                 "retention_day_6": 81,
#                 "retention_day_7": 45
#             },
#             {
#                 "day": "02/11/2024",
#                 "retention_day_1": 150,
#                 "retention_day_2": 184,
#                 "retention_day_3": 141,
#                 "retention_day_4": 51,
#                 "retention_day_5": 51,
#                 "retention_day_6": 131,
#                 "retention_day_7": 106
#             },
#             {
#                 "day": "03/11/2024",
#                 "retention_day_1": 592,
#                 "retention_day_2": 288,
#                 "retention_day_3": 139,
#                 "retention_day_4": 30,
#                 "retention_day_5": 52,
#                 "retention_day_6": 129,
#                 "retention_day_7": 49
#             },
#             {
#                 "day": "04/11/2024",
#                 "retention_day_1": 253,
#                 "retention_day_2": 181,
#                 "retention_day_3": 70,
#                 "retention_day_4": 17,
#                 "retention_day_5": 325,
#                 "retention_day_6": 190,
#                 "retention_day_7": 18
#             },
#             {
#                 "day": "05/11/2024",
#                 "retention_day_1": 197,
#                 "retention_day_2": 225,
#                 "retention_day_3": 126,
#                 "retention_day_4": 54,
#                 "retention_day_5": 244,
#                 "retention_day_6": 222,
#                 "retention_day_7": 100
#             },
#             {
#                 "day": "06/11/2024",
#                 "retention_day_1": 614,
#                 "retention_day_2": 148,
#                 "retention_day_3": 40,
#                 "retention_day_4": 95,
#                 "retention_day_5": 127,
#                 "retention_day_6": 107,
#                 "retention_day_7": 111
#             },
#             {
#                 "day": "07/11/2024",
#                 "retention_day_1": 1182,
#                 "retention_day_2": 369,
#                 "retention_day_3": 164,
#                 "retention_day_4": 17,
#                 "retention_day_5": 192,
#                 "retention_day_6": 93,
#                 "retention_day_7": 195
#             },
#             {
#                 "day": "08/11/2024",
#                 "retention_day_1": 188,
#                 "retention_day_2": 206,
#                 "retention_day_3": 199,
#                 "retention_day_4": 46,
#                 "retention_day_5": 290,
#                 "retention_day_6": 172,
#                 "retention_day_7": 156
#             },
#             {
#                 "day": "09/11/2024",
#                 "retention_day_1": 944,
#                 "retention_day_2": 207,
#                 "retention_day_3": 144,
#                 "retention_day_4": 37,
#                 "retention_day_5": 249,
#                 "retention_day_6": 70,
#                 "retention_day_7": 109
#             },
#             {
#                 "day": "10/11/2024",
#                 "retention_day_1": 1121,
#                 "retention_day_2": 324,
#                 "retention_day_3": 48,
#                 "retention_day_4": 23,
#                 "retention_day_5": 238,
#                 "retention_day_6": 184,
#                 "retention_day_7": 189
#             },
#             {
#                 "day": "11/11/2024",
#                 "retention_day_1": 221,
#                 "retention_day_2": 285,
#                 "retention_day_3": 72,
#                 "retention_day_4": 74,
#                 "retention_day_5": 290,
#                 "retention_day_6": 210,
#                 "retention_day_7": 102
#             },
#             {
#                 "day": "12/11/2024",
#                 "retention_day_1": 286,
#                 "retention_day_2": 114,
#                 "retention_day_3": 136,
#                 "retention_day_4": 97,
#                 "retention_day_5": 245,
#                 "retention_day_6": 217,
#                 "retention_day_7": 21
#             }
#         ],
#         "revenue_data": [
#             {
#                 "day": "04/11/2024",
#                 "revenue": 344
#             },
#             {
#                 "day": "05/11/2024",
#                 "revenue": 247
#             },
#             {
#                 "day": "06/11/2024",
#                 "revenue": 492
#             },
#             {
#                 "day": "07/11/2024",
#                 "revenue": 396
#             },
#             {
#                 "day": "08/11/2024",
#                 "revenue": 162
#             },
#             {
#                 "day": "09/11/2024",
#                 "revenue": 312
#             },
#             {
#                 "day": "10/11/2024",
#                 "revenue": 264
#             },
#             {
#                 "day": "11/11/2024",
#                 "revenue": 151
#             },
#             {
#                 "day": "12/11/2024",
#                 "revenue": 499
#             },
#             {
#                 "day": "13/11/2024",
#                 "revenue": 127
#             }
#         ],
#         "user": "48498",
#         "today_revenue": "12520",
#         "request": "43157"
#     }
#     ,
#     {
#         "game": "Genshin Impact",
#         "platform": [
#             "android",
#             "ios"
#         ],
#         "user_up": {
#             "JAN": "2887",
#             "FEB": "6466",
#             "MAR": "2186",
#             "APR": "3913",
#             "MAY": "5171",
#             "JUN": "5196",
#             "JUL": "4965",
#             "AUG": "6991",
#             "SEP": "7262",
#             "OCT": "3507",
#             "NOV": "6039",
#             "DEC": "7337"
#         },
#         "users/country": {
#             "USA": "25577",
#             "VietNam": "14849",
#             "Korea": "2470",
#             "Japan": "7929",
#             "Taiwan": "13890",
#             "Singapore": "13985",
#             "Thailand": "15357",
#             "Laos": "5000",
#             "Russia": "7289",
#             "North Korea": "24761"
#         },
#         "avg_daily_active_user": {
#             "JAN": "4480",
#             "FEB": "6743",
#             "MAR": "2537",
#             "APR": "5071",
#             "MAY": "7139",
#             "JUN": "2804",
#             "JUL": "4378",
#             "AUG": "7535",
#             "SEP": "5416",
#             "OCT": "4447",
#             "NOV": "6271",
#             "DEC": "2933"
#         },
#         "active_user/country": {
#             "USA": "7165",
#             "VietNam": "14156",
#             "Korea": "18479",
#             "Japan": "9988",
#             "Taiwan": "14792",
#             "Singapore": "10415",
#             "Thailand": "26925",
#             "Laos": "1558",
#             "Russia": "23851",
#             "North Korea": "14896"
#         },
#         "selling_product": [
#             "Classic",
#             "gay",
#             "dao"
#         ],
#         "products": [
#             {
#                 "prd": "dao",
#                 "price": "3500",
#                 "tier": "S",
#                 "sales volume": "1362"
#             },
#             {
#                 "prd": "gay",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "3183"
#             },
#             {
#                 "prd": "Classic",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "3259"
#             }
#         ],
#         "session": [
#             {
#                 "day": "04/11/2024",
#                 "session": "13861"
#             },
#             {
#                 "day": "05/11/2024",
#                 "session": "9878"
#             },
#             {
#                 "day": "06/11/2024",
#                 "session": "10329"
#             },
#             {
#                 "day": "07/11/2024",
#                 "session": "18644"
#             },
#             {
#                 "day": "08/11/2024",
#                 "session": "9401"
#             },
#             {
#                 "day": "09/11/2024",
#                 "session": "19780"
#             },
#             {
#                 "day": "10/11/2024",
#                 "session": "27816"
#             },
#             {
#                 "day": "11/11/2024",
#                 "session": "18769"
#             },
#             {
#                 "day": "12/11/2024",
#                 "session": "19922"
#             }
#         ],
#         "avgtime/day": [
#             {
#                 "day": "04/11/2024",
#                 "avg": "3.98451"
#             },
#             {
#                 "day": "05/11/2024",
#                 "avg": "2.96242"
#             },
#             {
#                 "day": "06/11/2024",
#                 "avg": "3.55094"
#             },
#             {
#                 "day": "07/11/2024",
#                 "avg": "0.48866"
#             },
#             {
#                 "day": "08/11/2024",
#                 "avg": "2.45491"
#             },
#             {
#                 "day": "09/11/2024",
#                 "avg": "1.19578"
#             },
#             {
#                 "day": "10/11/2024",
#                 "avg": "0.53789"
#             },
#             {
#                 "day": "11/11/2024",
#                 "avg": "3.34307"
#             },
#             {
#                 "day": "12/11/2024",
#                 "avg": "1.54461"
#             }
#         ],
#         "retention_data": [
#             {
#                 "day": "30/10/2024",
#                 "retention_day_1": 1100,
#                 "retention_day_2": 222,
#                 "retention_day_3": 111,
#                 "retention_day_4": 62,
#                 "retention_day_5": 208,
#                 "retention_day_6": 193,
#                 "retention_day_7": 212
#             },
#             {
#                 "day": "31/10/2024",
#                 "retention_day_1": 1180,
#                 "retention_day_2": 286,
#                 "retention_day_3": 36,
#                 "retention_day_4": 15,
#                 "retention_day_5": 265,
#                 "retention_day_6": 83,
#                 "retention_day_7": 129
#             },
#             {
#                 "day": "01/11/2024",
#                 "retention_day_1": 460,
#                 "retention_day_2": 375,
#                 "retention_day_3": 82,
#                 "retention_day_4": 68,
#                 "retention_day_5": 91,
#                 "retention_day_6": 205,
#                 "retention_day_7": 149
#             },
#             {
#                 "day": "02/11/2024",
#                 "retention_day_1": 1115,
#                 "retention_day_2": 194,
#                 "retention_day_3": 65,
#                 "retention_day_4": 43,
#                 "retention_day_5": 228,
#                 "retention_day_6": 60,
#                 "retention_day_7": 99
#             },
#             {
#                 "day": "03/11/2024",
#                 "retention_day_1": 445,
#                 "retention_day_2": 150,
#                 "retention_day_3": 71,
#                 "retention_day_4": 89,
#                 "retention_day_5": 188,
#                 "retention_day_6": 37,
#                 "retention_day_7": 164
#             },
#             {
#                 "day": "04/11/2024",
#                 "retention_day_1": 352,
#                 "retention_day_2": 349,
#                 "retention_day_3": 120,
#                 "retention_day_4": 74,
#                 "retention_day_5": 217,
#                 "retention_day_6": 57,
#                 "retention_day_7": 130
#             },
#             {
#                 "day": "05/11/2024",
#                 "retention_day_1": 897,
#                 "retention_day_2": 327,
#                 "retention_day_3": 32,
#                 "retention_day_4": 17,
#                 "retention_day_5": 217,
#                 "retention_day_6": 57,
#                 "retention_day_7": 69
#             },
#             {
#                 "day": "06/11/2024",
#                 "retention_day_1": 687,
#                 "retention_day_2": 335,
#                 "retention_day_3": 163,
#                 "retention_day_4": 21,
#                 "retention_day_5": 349,
#                 "retention_day_6": 111,
#                 "retention_day_7": 167
#             },
#             {
#                 "day": "07/11/2024",
#                 "retention_day_1": 932,
#                 "retention_day_2": 334,
#                 "retention_day_3": 33,
#                 "retention_day_4": 95,
#                 "retention_day_5": 339,
#                 "retention_day_6": 236,
#                 "retention_day_7": 58
#             },
#             {
#                 "day": "08/11/2024",
#                 "retention_day_1": 851,
#                 "retention_day_2": 373,
#                 "retention_day_3": 144,
#                 "retention_day_4": 91,
#                 "retention_day_5": 155,
#                 "retention_day_6": 205,
#                 "retention_day_7": 73
#             },
#             {
#                 "day": "09/11/2024",
#                 "retention_day_1": 396,
#                 "retention_day_2": 276,
#                 "retention_day_3": 67,
#                 "retention_day_4": 92,
#                 "retention_day_5": 252,
#                 "retention_day_6": 123,
#                 "retention_day_7": 220
#             },
#             {
#                 "day": "10/11/2024",
#                 "retention_day_1": 762,
#                 "retention_day_2": 84,
#                 "retention_day_3": 112,
#                 "retention_day_4": 38,
#                 "retention_day_5": 259,
#                 "retention_day_6": 179,
#                 "retention_day_7": 122
#             },
#             {
#                 "day": "11/11/2024",
#                 "retention_day_1": 424,
#                 "retention_day_2": 167,
#                 "retention_day_3": 110,
#                 "retention_day_4": 38,
#                 "retention_day_5": 163,
#                 "retention_day_6": 98,
#                 "retention_day_7": 208
#             },
#             {
#                 "day": "12/11/2024",
#                 "retention_day_1": 990,
#                 "retention_day_2": 379,
#                 "retention_day_3": 40,
#                 "retention_day_4": 92,
#                 "retention_day_5": 59,
#                 "retention_day_6": 167,
#                 "retention_day_7": 131
#             }
#         ],
#         "revenue_data": [
#             {
#                 "day": "04/11/2024",
#                 "revenue": 260
#             },
#             {
#                 "day": "05/11/2024",
#                 "revenue": 188
#             },
#             {
#                 "day": "06/11/2024",
#                 "revenue": 458
#             },
#             {
#                 "day": "07/11/2024",
#                 "revenue": 410
#             },
#             {
#                 "day": "08/11/2024",
#                 "revenue": 500
#             },
#             {
#                 "day": "09/11/2024",
#                 "revenue": 326
#             },
#             {
#                 "day": "10/11/2024",
#                 "revenue": 241
#             },
#             {
#                 "day": "11/11/2024",
#                 "revenue": 231
#             },
#             {
#                 "day": "12/11/2024",
#                 "revenue": 378
#             },
#             {
#                 "day": "13/11/2024",
#                 "revenue": 250
#             }
#         ],
#         "user": "24618",
#         "today_revenue": "24945",
#         "request": "31812"
#     }
#     ,
#     {
#         "game": "Hay Day",
#         "platform": ["android", "ios"],
#         "user_up": {
#             "JAN": "3783",
#             "FEB": "2225",
#             "MAR": "1508",
#             "APR": "3039",
#             "MAY": "9284",
#             "JUN": "8751",
#             "JUL": "7573",
#             "AUG": "9686",
#             "SEP": "4511",
#             "OCT": "5228",
#             "NOV": "3711",
#             "DEC": "4826",
#         },
#         "users/country": {
#             'USA': "24360",
#             'VietNam': "12471",
#             'Korea': "2101",
#             'Japan': "1344",
#             'Taiwan': "1483",
#             'Singapore': "1041",
#             'Thailand': "1420",
#             'Laos': "263",
#             'Russia': "1196",
#             'North Korea': "1"
#         },
#         "avg_daily_active_user": {
#             "JAN": "2400",
#             "FEB": "3400",
#             "MAR": "2440",
#             "APR": "6400",
#             "MAY": "2400",
#             "JUN": "6400",
#             "JUL": "3400",
#             "AUG": "1240",
#             "SEP": "8400",
#             "OCT": "3400",
#             "NOV": "1400",
#             "DEC": "4400",
#         },
#         "active_user/country": {
#             "USA": "24361",
#             "VietNam": "12471",
#             "Korea": "2101",
#             "Japan": "1344",
#             "Taiwan": "1483",
#             "Singapore": "1041",
#             "Thailand": "1420",
#             "Laos": "263",
#             "Russia": "1196",
#             "North Korea": "1"
#         },
#         "selling_product": ["Classic", "gay", "dao"],
#         "products": [
#             {
#                 "prd": "dao",
#                 "price": "3500",
#                 "tier": "S",
#                 "sales volume": "3500"
#             },
#             {
#                 "prd": "gay",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "3300"
#             },
#             {
#                 "prd": "Classic",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "3100"
#             }
#         ],
#         "session": [
#             {
#                 "day": "04/11/2024",
#                 "session": "124"
#             },
#             {
#                 "day": "05/11/2024",
#                 "session": "13345"
#             },
#             {
#                 "day": "06/11/2024",
#                 "session": "12334"
#             },
#             {
#                 "day": "07/11/2024",
#                 "session": "11134"
#             },
#             {
#                 "day": "08/11/2024",
#                 "session": "21234"
#             },
#             {
#                 "day": "09/11/2024",
#                 "session": "31234"
#             },
#             {
#                 "day": "10/11/2024",
#                 "session": "25234"
#             },
#             {
#                 "day": "11/11/2024",
#                 "session": "17234"
#             },
#             {
#                 "day": "12/11/2024",
#                 "session": "11234"
#             },
#         ],
#         "avgtime/day": [
#             {
#                 "day": "04/11/2024",
#                 "avg": "4.02312"
#             },
#             {
#                 "day": "05/11/2024",
#                 "avg": "1.11"
#             },
#             {
#                 "day": "06/11/2024",
#                 "avg": "0.7011"
#             },
#             {
#                 "day": "07/11/2024",
#                 "avg": "0.2313"
#             },
#             {
#                 "day": "08/11/2024",
#                 "avg": "0.4213"
#             },
#             {
#                 "day": "09/11/2024",
#                 "avg": "0.712"
#             },
#             {
#                 "day": "10/11/2024",
#                 "avg": "1.01"
#             },
#             {
#                 "day": "11/11/2024",
#                 "avg": "0.842"
#             },
#             {
#                 "day": "12/11/2024",
#                 "avg": "0.743"
#             },
#         ],
#         "retention_data": [
#             {"day": "30/10/2024", "retention_day_1": 1190, "retention_day_2": 280, "retention_day_3": 170,
#              "retention_day_4": 60,
#              "retention_day_5": 350, "retention_day_6": 240, "retention_day_7": 130},
#             {"day": "31/10/2024", "retention_day_1": 190, "retention_day_2": 280, "retention_day_3": 170,
#              "retention_day_4": 60,
#              "retention_day_5": 350, "retention_day_6": 240, "retention_day_7": 130},
#             {"day": "01/11/2024", "retention_day_1": 190, "retention_day_2": 280, "retention_day_3": 170,
#              "retention_day_4": 60,
#              "retention_day_5": 350, "retention_day_6": 240, "retention_day_7": 130},
#             {"day": "02/11/2024", "retention_day_1": 190, "retention_day_2": 280, "retention_day_3": 170,
#              "retention_day_4": 60,
#              "retention_day_5": 350, "retention_day_6": 240, "retention_day_7": 130},
#             {"day": "03/11/2024", "retention_day_1": 190, "retention_day_2": 280, "retention_day_3": 170,
#              "retention_day_4": 60,
#              "retention_day_5": 350, "retention_day_6": 240, "retention_day_7": 130},
#             {"day": "04/11/2024", "retention_day_1": 190, "retention_day_2": 280, "retention_day_3": 170,
#              "retention_day_4": 60,
#              "retention_day_5": 350, "retention_day_6": 240, "retention_day_7": 130},
#             {"day": "05/11/2024", "retention_day_1": 120, "retention_day_2": 90, "retention_day_3": 75,
#              "retention_day_4": 65,
#              "retention_day_5": 55, "retention_day_6": 45, "retention_day_7": 35},
#             {"day": "06/11/2024", "retention_day_1": 940, "retention_day_2": 310, "retention_day_3": 200,
#              "retention_day_4": 185,
#              "retention_day_5": 175, "retention_day_6": 165, "retention_day_7": 250},
#             {"day": "07/11/2024", "retention_day_1": 920, "retention_day_2": 300, "retention_day_3": 180,
#              "retention_day_4": 170,
#              "retention_day_5": 160, "retention_day_6": 150, "retention_day_7": 240},
#             {"day": "08/11/2024", "retention_day_1": 900, "retention_day_2": 290, "retention_day_3": 170,
#              "retention_day_4": 160,
#              "retention_day_5": 150, "retention_day_6": 140, "retention_day_7": 230},
#             {"day": "09/11/2024", "retention_day_1": 880, "retention_day_2": 280, "retention_day_3": 160,
#              "retention_day_4": 150,
#              "retention_day_5": 140, "retention_day_6": 130, "retention_day_7": 220},
#             {"day": "10/11/2024", "retention_day_1": 860, "retention_day_2": 270, "retention_day_3": 150,
#              "retention_day_4": 140,
#              "retention_day_5": 130, "retention_day_6": 120, "retention_day_7": 210},
#             {"day": "11/11/2024", "retention_day_1": 840, "retention_day_2": 260, "retention_day_3": 140,
#              "retention_day_4": 130,
#              "retention_day_5": 120, "retention_day_6": 110, "retention_day_7": 200},
#             {"day": "12/11/2024", "retention_day_1": 820, "retention_day_2": 250, "retention_day_3": 130,
#              "retention_day_4": 120,
#              "retention_day_5": 110, "retention_day_6": 100, "retention_day_7": 190},
#             {"day": "13/11/2024", "retention_day_1": 800, "retention_day_2": 240, "retention_day_3": 120,
#              "retention_day_4": 110,
#              "retention_day_5": 100, "retention_day_6": 90, "retention_day_7": 180},
#         ],
#         # Dữ liệu doanh thu
#         "revenue_data": [
#             {"day": "04/11/2024", "revenue": 900},
#             {"day": "05/11/2024", "revenue": 150},
#             {"day": "06/11/2024", "revenue": 120},
#             {"day": "07/11/2024", "revenue": 130},
#             {"day": "08/11/2024", "revenue": 200},
#             {"day": "09/11/2024", "revenue": 180},
#             {"day": "10/11/2024", "revenue": 220},
#             {"day": "11/11/2024", "revenue": 210},
#             {"day": "12/11/2024", "revenue": 250},
#             {"day": "13/11/2024", "revenue": 300},
#         ],
#         "user": "32102",
#         "today_revenue": "15000",
#         "request": "50000"
#     },
#     {
#         "game": "Honkai Impact 3",
#         "platform": [
#             "android",
#             "ios"
#         ],
#         "user_up": {
#             "JAN": "6947",
#             "FEB": "4380",
#             "MAR": "4840",
#             "APR": "2321",
#             "MAY": "6255",
#             "JUN": "4127",
#             "JUL": "6661",
#             "AUG": "5497",
#             "SEP": "6714",
#             "OCT": "2118",
#             "NOV": "5084",
#             "DEC": "3486"
#         },
#         "users/country": {
#             "USA": "29604",
#             "VietNam": "10945",
#             "Korea": "9659",
#             "Japan": "24180",
#             "Taiwan": "6970",
#             "Singapore": "20399",
#             "Thailand": "29760",
#             "Laos": "11167",
#             "Russia": "28355",
#             "North Korea": "3996"
#         },
#         "avg_daily_active_user": {
#             "JAN": "2048",
#             "FEB": "4186",
#             "MAR": "7174",
#             "APR": "4236",
#             "MAY": "7051",
#             "JUN": "5785",
#             "JUL": "7674",
#             "AUG": "5737",
#             "SEP": "5659",
#             "OCT": "4432",
#             "NOV": "2716",
#             "DEC": "6196"
#         },
#         "active_user/country": {
#             "USA": "5863",
#             "VietNam": "25496",
#             "Korea": "11697",
#             "Japan": "21885",
#             "Taiwan": "22730",
#             "Singapore": "14661",
#             "Thailand": "10769",
#             "Laos": "13894",
#             "Russia": "22928",
#             "North Korea": "7016"
#         },
#         "selling_product": [
#             "Classic",
#             "gay",
#             "dao"
#         ],
#         "products": [
#             {
#                 "prd": "dao",
#                 "price": "3500",
#                 "tier": "S",
#                 "sales volume": "4950"
#             },
#             {
#                 "prd": "gay",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "1023"
#             },
#             {
#                 "prd": "Classic",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "1718"
#             }
#         ],
#         "session": [
#             {
#                 "day": "04/11/2024",
#                 "session": "21905"
#             },
#             {
#                 "day": "05/11/2024",
#                 "session": "5486"
#             },
#             {
#                 "day": "06/11/2024",
#                 "session": "3009"
#             },
#             {
#                 "day": "07/11/2024",
#                 "session": "25788"
#             },
#             {
#                 "day": "08/11/2024",
#                 "session": "25011"
#             },
#             {
#                 "day": "09/11/2024",
#                 "session": "22779"
#             },
#             {
#                 "day": "10/11/2024",
#                 "session": "12258"
#             },
#             {
#                 "day": "11/11/2024",
#                 "session": "8072"
#             },
#             {
#                 "day": "12/11/2024",
#                 "session": "3607"
#             }
#         ],
#         "avgtime/day": [
#             {
#                 "day": "04/11/2024",
#                 "avg": "3.78186"
#             },
#             {
#                 "day": "05/11/2024",
#                 "avg": "3.56065"
#             },
#             {
#                 "day": "06/11/2024",
#                 "avg": "2.41668"
#             },
#             {
#                 "day": "07/11/2024",
#                 "avg": "1.94598"
#             },
#             {
#                 "day": "08/11/2024",
#                 "avg": "1.50585"
#             },
#             {
#                 "day": "09/11/2024",
#                 "avg": "3.59334"
#             },
#             {
#                 "day": "10/11/2024",
#                 "avg": "3.44041"
#             },
#             {
#                 "day": "11/11/2024",
#                 "avg": "2.47881"
#             },
#             {
#                 "day": "12/11/2024",
#                 "avg": "1.1896"
#             }
#         ],
#         "retention_data": [
#             {
#                 "day": "30/10/2024",
#                 "retention_day_1": 757,
#                 "retention_day_2": 287,
#                 "retention_day_3": 127,
#                 "retention_day_4": 33,
#                 "retention_day_5": 155,
#                 "retention_day_6": 162,
#                 "retention_day_7": 139
#             },
#             {
#                 "day": "31/10/2024",
#                 "retention_day_1": 247,
#                 "retention_day_2": 55,
#                 "retention_day_3": 152,
#                 "retention_day_4": 39,
#                 "retention_day_5": 245,
#                 "retention_day_6": 81,
#                 "retention_day_7": 191
#             },
#             {
#                 "day": "01/11/2024",
#                 "retention_day_1": 363,
#                 "retention_day_2": 221,
#                 "retention_day_3": 70,
#                 "retention_day_4": 48,
#                 "retention_day_5": 223,
#                 "retention_day_6": 80,
#                 "retention_day_7": 36
#             },
#             {
#                 "day": "02/11/2024",
#                 "retention_day_1": 357,
#                 "retention_day_2": 175,
#                 "retention_day_3": 195,
#                 "retention_day_4": 54,
#                 "retention_day_5": 311,
#                 "retention_day_6": 42,
#                 "retention_day_7": 23
#             },
#             {
#                 "day": "03/11/2024",
#                 "retention_day_1": 978,
#                 "retention_day_2": 279,
#                 "retention_day_3": 191,
#                 "retention_day_4": 76,
#                 "retention_day_5": 234,
#                 "retention_day_6": 191,
#                 "retention_day_7": 69
#             },
#             {
#                 "day": "04/11/2024",
#                 "retention_day_1": 1091,
#                 "retention_day_2": 139,
#                 "retention_day_3": 132,
#                 "retention_day_4": 79,
#                 "retention_day_5": 38,
#                 "retention_day_6": 45,
#                 "retention_day_7": 96
#             },
#             {
#                 "day": "05/11/2024",
#                 "retention_day_1": 1068,
#                 "retention_day_2": 241,
#                 "retention_day_3": 169,
#                 "retention_day_4": 64,
#                 "retention_day_5": 91,
#                 "retention_day_6": 160,
#                 "retention_day_7": 17
#             },
#             {
#                 "day": "06/11/2024",
#                 "retention_day_1": 1111,
#                 "retention_day_2": 251,
#                 "retention_day_3": 199,
#                 "retention_day_4": 38,
#                 "retention_day_5": 155,
#                 "retention_day_6": 223,
#                 "retention_day_7": 172
#             },
#             {
#                 "day": "07/11/2024",
#                 "retention_day_1": 121,
#                 "retention_day_2": 313,
#                 "retention_day_3": 61,
#                 "retention_day_4": 65,
#                 "retention_day_5": 135,
#                 "retention_day_6": 193,
#                 "retention_day_7": 32
#             },
#             {
#                 "day": "08/11/2024",
#                 "retention_day_1": 105,
#                 "retention_day_2": 260,
#                 "retention_day_3": 66,
#                 "retention_day_4": 82,
#                 "retention_day_5": 130,
#                 "retention_day_6": 199,
#                 "retention_day_7": 134
#             },
#             {
#                 "day": "09/11/2024",
#                 "retention_day_1": 1081,
#                 "retention_day_2": 266,
#                 "retention_day_3": 38,
#                 "retention_day_4": 61,
#                 "retention_day_5": 47,
#                 "retention_day_6": 84,
#                 "retention_day_7": 77
#             },
#             {
#                 "day": "10/11/2024",
#                 "retention_day_1": 160,
#                 "retention_day_2": 259,
#                 "retention_day_3": 157,
#                 "retention_day_4": 39,
#                 "retention_day_5": 151,
#                 "retention_day_6": 82,
#                 "retention_day_7": 37
#             },
#             {
#                 "day": "11/11/2024",
#                 "retention_day_1": 881,
#                 "retention_day_2": 128,
#                 "retention_day_3": 76,
#                 "retention_day_4": 38,
#                 "retention_day_5": 298,
#                 "retention_day_6": 80,
#                 "retention_day_7": 204
#             },
#             {
#                 "day": "12/11/2024",
#                 "retention_day_1": 429,
#                 "retention_day_2": 224,
#                 "retention_day_3": 36,
#                 "retention_day_4": 100,
#                 "retention_day_5": 294,
#                 "retention_day_6": 206,
#                 "retention_day_7": 33
#             }
#         ],
#         "revenue_data": [
#             {
#                 "day": "04/11/2024",
#                 "revenue": 276
#             },
#             {
#                 "day": "05/11/2024",
#                 "revenue": 384
#             },
#             {
#                 "day": "06/11/2024",
#                 "revenue": 269
#             },
#             {
#                 "day": "07/11/2024",
#                 "revenue": 426
#             },
#             {
#                 "day": "08/11/2024",
#                 "revenue": 485
#             },
#             {
#                 "day": "09/11/2024",
#                 "revenue": 105
#             },
#             {
#                 "day": "10/11/2024",
#                 "revenue": 205
#             },
#             {
#                 "day": "11/11/2024",
#                 "revenue": 383
#             },
#             {
#                 "day": "12/11/2024",
#                 "revenue": 145
#             },
#             {
#                 "day": "13/11/2024",
#                 "revenue": 257
#             }
#         ],
#         "user": "26955",
#         "today_revenue": "17907",
#         "request": "23912"
#     }
#     ,
#
#     {
#         "game": "Honkai Star Rail",
#         "platform": [
#             "android",
#             "ios"
#         ],
#         "user_up": {
#             "JAN": "4517",
#             "FEB": "3968",
#             "MAR": "5629",
#             "APR": "3993",
#             "MAY": "4496",
#             "JUN": "4606",
#             "JUL": "5541",
#             "AUG": "5386",
#             "SEP": "5937",
#             "OCT": "7387",
#             "NOV": "7620",
#             "DEC": "4414"
#         },
#         "users/country": {
#             "USA": "9444",
#             "VietNam": "17932",
#             "Korea": "10310",
#             "Japan": "2837",
#             "Taiwan": "7069",
#             "Singapore": "13849",
#             "Thailand": "10115",
#             "Laos": "15659",
#             "Russia": "1559",
#             "North Korea": "14504"
#         },
#         "avg_daily_active_user": {
#             "JAN": "6605",
#             "FEB": "4027",
#             "MAR": "2248",
#             "APR": "2735",
#             "MAY": "2051",
#             "JUN": "7416",
#             "JUL": "7669",
#             "AUG": "2180",
#             "SEP": "2621",
#             "OCT": "6890",
#             "NOV": "6373",
#             "DEC": "5992"
#         },
#         "active_user/country": {
#             "USA": "19618",
#             "VietNam": "9186",
#             "Korea": "3457",
#             "Japan": "22054",
#             "Taiwan": "23702",
#             "Singapore": "23081",
#             "Thailand": "17571",
#             "Laos": "27762",
#             "Russia": "13590",
#             "North Korea": "1367"
#         },
#         "selling_product": [
#             "Classic",
#             "gay",
#             "dao"
#         ],
#         "products": [
#             {
#                 "prd": "dao",
#                 "price": "3500",
#                 "tier": "S",
#                 "sales volume": "1891"
#             },
#             {
#                 "prd": "gay",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "3188"
#             },
#             {
#                 "prd": "Classic",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "3192"
#             }
#         ],
#         "session": [
#             {
#                 "day": "04/11/2024",
#                 "session": "29482"
#             },
#             {
#                 "day": "05/11/2024",
#                 "session": "26507"
#             },
#             {
#                 "day": "06/11/2024",
#                 "session": "8430"
#             },
#             {
#                 "day": "07/11/2024",
#                 "session": "5477"
#             },
#             {
#                 "day": "08/11/2024",
#                 "session": "21309"
#             },
#             {
#                 "day": "09/11/2024",
#                 "session": "24090"
#             },
#             {
#                 "day": "10/11/2024",
#                 "session": "10594"
#             },
#             {
#                 "day": "11/11/2024",
#                 "session": "1632"
#             },
#             {
#                 "day": "12/11/2024",
#                 "session": "28630"
#             }
#         ],
#         "avgtime/day": [
#             {
#                 "day": "04/11/2024",
#                 "avg": "2.71474"
#             },
#             {
#                 "day": "05/11/2024",
#                 "avg": "3.99512"
#             },
#             {
#                 "day": "06/11/2024",
#                 "avg": "3.99469"
#             },
#             {
#                 "day": "07/11/2024",
#                 "avg": "2.43193"
#             },
#             {
#                 "day": "08/11/2024",
#                 "avg": "2.09753"
#             },
#             {
#                 "day": "09/11/2024",
#                 "avg": "3.05373"
#             },
#             {
#                 "day": "10/11/2024",
#                 "avg": "2.55531"
#             },
#             {
#                 "day": "11/11/2024",
#                 "avg": "3.15676"
#             },
#             {
#                 "day": "12/11/2024",
#                 "avg": "2.28018"
#             }
#         ],
#         "retention_data": [
#             {
#                 "day": "30/10/2024",
#                 "retention_day_1": 468,
#                 "retention_day_2": 344,
#                 "retention_day_3": 116,
#                 "retention_day_4": 31,
#                 "retention_day_5": 64,
#                 "retention_day_6": 148,
#                 "retention_day_7": 165
#             },
#             {
#                 "day": "31/10/2024",
#                 "retention_day_1": 750,
#                 "retention_day_2": 332,
#                 "retention_day_3": 67,
#                 "retention_day_4": 82,
#                 "retention_day_5": 126,
#                 "retention_day_6": 92,
#                 "retention_day_7": 10
#             },
#             {
#                 "day": "01/11/2024",
#                 "retention_day_1": 1094,
#                 "retention_day_2": 335,
#                 "retention_day_3": 50,
#                 "retention_day_4": 46,
#                 "retention_day_5": 51,
#                 "retention_day_6": 191,
#                 "retention_day_7": 198
#             },
#             {
#                 "day": "02/11/2024",
#                 "retention_day_1": 342,
#                 "retention_day_2": 81,
#                 "retention_day_3": 61,
#                 "retention_day_4": 37,
#                 "retention_day_5": 206,
#                 "retention_day_6": 217,
#                 "retention_day_7": 84
#             },
#             {
#                 "day": "03/11/2024",
#                 "retention_day_1": 1002,
#                 "retention_day_2": 214,
#                 "retention_day_3": 111,
#                 "retention_day_4": 26,
#                 "retention_day_5": 292,
#                 "retention_day_6": 62,
#                 "retention_day_7": 30
#             },
#             {
#                 "day": "04/11/2024",
#                 "retention_day_1": 652,
#                 "retention_day_2": 56,
#                 "retention_day_3": 177,
#                 "retention_day_4": 55,
#                 "retention_day_5": 223,
#                 "retention_day_6": 115,
#                 "retention_day_7": 183
#             },
#             {
#                 "day": "05/11/2024",
#                 "retention_day_1": 1125,
#                 "retention_day_2": 217,
#                 "retention_day_3": 65,
#                 "retention_day_4": 90,
#                 "retention_day_5": 169,
#                 "retention_day_6": 200,
#                 "retention_day_7": 101
#             },
#             {
#                 "day": "06/11/2024",
#                 "retention_day_1": 132,
#                 "retention_day_2": 230,
#                 "retention_day_3": 93,
#                 "retention_day_4": 23,
#                 "retention_day_5": 245,
#                 "retention_day_6": 233,
#                 "retention_day_7": 126
#             },
#             {
#                 "day": "07/11/2024",
#                 "retention_day_1": 1075,
#                 "retention_day_2": 323,
#                 "retention_day_3": 68,
#                 "retention_day_4": 72,
#                 "retention_day_5": 129,
#                 "retention_day_6": 191,
#                 "retention_day_7": 207
#             },
#             {
#                 "day": "08/11/2024",
#                 "retention_day_1": 1131,
#                 "retention_day_2": 375,
#                 "retention_day_3": 184,
#                 "retention_day_4": 81,
#                 "retention_day_5": 144,
#                 "retention_day_6": 82,
#                 "retention_day_7": 90
#             },
#             {
#                 "day": "09/11/2024",
#                 "retention_day_1": 436,
#                 "retention_day_2": 303,
#                 "retention_day_3": 161,
#                 "retention_day_4": 36,
#                 "retention_day_5": 78,
#                 "retention_day_6": 117,
#                 "retention_day_7": 51
#             },
#             {
#                 "day": "10/11/2024",
#                 "retention_day_1": 703,
#                 "retention_day_2": 107,
#                 "retention_day_3": 36,
#                 "retention_day_4": 74,
#                 "retention_day_5": 55,
#                 "retention_day_6": 98,
#                 "retention_day_7": 172
#             },
#             {
#                 "day": "11/11/2024",
#                 "retention_day_1": 734,
#                 "retention_day_2": 141,
#                 "retention_day_3": 128,
#                 "retention_day_4": 84,
#                 "retention_day_5": 330,
#                 "retention_day_6": 122,
#                 "retention_day_7": 228
#             },
#             {
#                 "day": "12/11/2024",
#                 "retention_day_1": 961,
#                 "retention_day_2": 215,
#                 "retention_day_3": 195,
#                 "retention_day_4": 50,
#                 "retention_day_5": 225,
#                 "retention_day_6": 237,
#                 "retention_day_7": 28
#             }
#         ],
#         "revenue_data": [
#             {
#                 "day": "04/11/2024",
#                 "revenue": 271
#             },
#             {
#                 "day": "05/11/2024",
#                 "revenue": 353
#             },
#             {
#                 "day": "06/11/2024",
#                 "revenue": 294
#             },
#             {
#                 "day": "07/11/2024",
#                 "revenue": 477
#             },
#             {
#                 "day": "08/11/2024",
#                 "revenue": 421
#             },
#             {
#                 "day": "09/11/2024",
#                 "revenue": 349
#             },
#             {
#                 "day": "10/11/2024",
#                 "revenue": 457
#             },
#             {
#                 "day": "11/11/2024",
#                 "revenue": 234
#             },
#             {
#                 "day": "12/11/2024",
#                 "revenue": 159
#             },
#             {
#                 "day": "13/11/2024",
#                 "revenue": 178
#             }
#         ],
#         "user": "16806",
#         "today_revenue": "18196",
#         "request": "34934"
#     }
#     ,
#     {
#         "game": "Capypara",
#         "platform": [
#             "android",
#             "ios"
#         ],
#         "user_up": {
#             "JAN": "7584",
#             "FEB": "2871",
#             "MAR": "3689",
#             "APR": "5389",
#             "MAY": "5465",
#             "JUN": "7673",
#             "JUL": "4173",
#             "AUG": "4078",
#             "SEP": "7776",
#             "OCT": "4541",
#             "NOV": "3478",
#             "DEC": "3509"
#         },
#         "users/country": {
#             "USA": "16416",
#             "VietNam": "24239",
#             "Korea": "21064",
#             "Japan": "6617",
#             "Taiwan": "25331",
#             "Singapore": "17699",
#             "Thailand": "22099",
#             "Laos": "8079",
#             "Russia": "18659",
#             "North Korea": "16744"
#         },
#         "avg_daily_active_user": {
#             "JAN": "6427",
#             "FEB": "5807",
#             "MAR": "7289",
#             "APR": "4784",
#             "MAY": "3961",
#             "JUN": "6983",
#             "JUL": "6226",
#             "AUG": "7215",
#             "SEP": "5792",
#             "OCT": "2365",
#             "NOV": "7388",
#             "DEC": "6442"
#         },
#         "active_user/country": {
#             "USA": "3343",
#             "VietNam": "25062",
#             "Korea": "949",
#             "Japan": "21692",
#             "Taiwan": "20386",
#             "Singapore": "25001",
#             "Thailand": "23959",
#             "Laos": "16357",
#             "Russia": "23597",
#             "North Korea": "28871"
#         },
#         "selling_product": [
#             "Classic",
#             "gay",
#             "dao"
#         ],
#         "products": [
#             {
#                 "prd": "dao",
#                 "price": "3500",
#                 "tier": "S",
#                 "sales volume": "4660"
#             },
#             {
#                 "prd": "gay",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "1215"
#             },
#             {
#                 "prd": "Classic",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "2293"
#             }
#         ],
#         "session": [
#             {
#                 "day": "04/11/2024",
#                 "session": "24425"
#             },
#             {
#                 "day": "05/11/2024",
#                 "session": "17457"
#             },
#             {
#                 "day": "06/11/2024",
#                 "session": "18390"
#             },
#             {
#                 "day": "07/11/2024",
#                 "session": "3533"
#             },
#             {
#                 "day": "08/11/2024",
#                 "session": "6782"
#             },
#             {
#                 "day": "09/11/2024",
#                 "session": "6756"
#             },
#             {
#                 "day": "10/11/2024",
#                 "session": "12523"
#             },
#             {
#                 "day": "11/11/2024",
#                 "session": "16786"
#             },
#             {
#                 "day": "12/11/2024",
#                 "session": "20649"
#             }
#         ],
#         "avgtime/day": [
#             {
#                 "day": "04/11/2024",
#                 "avg": "3.78298"
#             },
#             {
#                 "day": "05/11/2024",
#                 "avg": "3.64077"
#             },
#             {
#                 "day": "06/11/2024",
#                 "avg": "1.68255"
#             },
#             {
#                 "day": "07/11/2024",
#                 "avg": "0.20285"
#             },
#             {
#                 "day": "08/11/2024",
#                 "avg": "2.50083"
#             },
#             {
#                 "day": "09/11/2024",
#                 "avg": "1.40082"
#             },
#             {
#                 "day": "10/11/2024",
#                 "avg": "1.44462"
#             },
#             {
#                 "day": "11/11/2024",
#                 "avg": "3.95315"
#             },
#             {
#                 "day": "12/11/2024",
#                 "avg": "3.12703"
#             }
#         ],
#         "retention_data": [
#             {
#                 "day": "30/10/2024",
#                 "retention_day_1": 480,
#                 "retention_day_2": 346,
#                 "retention_day_3": 98,
#                 "retention_day_4": 84,
#                 "retention_day_5": 170,
#                 "retention_day_6": 61,
#                 "retention_day_7": 169
#             },
#             {
#                 "day": "31/10/2024",
#                 "retention_day_1": 1088,
#                 "retention_day_2": 179,
#                 "retention_day_3": 153,
#                 "retention_day_4": 24,
#                 "retention_day_5": 39,
#                 "retention_day_6": 80,
#                 "retention_day_7": 74
#             },
#             {
#                 "day": "01/11/2024",
#                 "retention_day_1": 733,
#                 "retention_day_2": 326,
#                 "retention_day_3": 187,
#                 "retention_day_4": 89,
#                 "retention_day_5": 221,
#                 "retention_day_6": 131,
#                 "retention_day_7": 75
#             },
#             {
#                 "day": "02/11/2024",
#                 "retention_day_1": 365,
#                 "retention_day_2": 362,
#                 "retention_day_3": 186,
#                 "retention_day_4": 62,
#                 "retention_day_5": 94,
#                 "retention_day_6": 212,
#                 "retention_day_7": 213
#             },
#             {
#                 "day": "03/11/2024",
#                 "retention_day_1": 931,
#                 "retention_day_2": 313,
#                 "retention_day_3": 123,
#                 "retention_day_4": 33,
#                 "retention_day_5": 343,
#                 "retention_day_6": 200,
#                 "retention_day_7": 176
#             },
#             {
#                 "day": "04/11/2024",
#                 "retention_day_1": 839,
#                 "retention_day_2": 180,
#                 "retention_day_3": 75,
#                 "retention_day_4": 14,
#                 "retention_day_5": 52,
#                 "retention_day_6": 230,
#                 "retention_day_7": 143
#             },
#             {
#                 "day": "05/11/2024",
#                 "retention_day_1": 1109,
#                 "retention_day_2": 246,
#                 "retention_day_3": 38,
#                 "retention_day_4": 51,
#                 "retention_day_5": 294,
#                 "retention_day_6": 158,
#                 "retention_day_7": 30
#             },
#             {
#                 "day": "06/11/2024",
#                 "retention_day_1": 826,
#                 "retention_day_2": 270,
#                 "retention_day_3": 141,
#                 "retention_day_4": 60,
#                 "retention_day_5": 336,
#                 "retention_day_6": 89,
#                 "retention_day_7": 20
#             },
#             {
#                 "day": "07/11/2024",
#                 "retention_day_1": 194,
#                 "retention_day_2": 176,
#                 "retention_day_3": 77,
#                 "retention_day_4": 22,
#                 "retention_day_5": 321,
#                 "retention_day_6": 40,
#                 "retention_day_7": 95
#             },
#             {
#                 "day": "08/11/2024",
#                 "retention_day_1": 984,
#                 "retention_day_2": 306,
#                 "retention_day_3": 183,
#                 "retention_day_4": 69,
#                 "retention_day_5": 100,
#                 "retention_day_6": 187,
#                 "retention_day_7": 91
#             },
#             {
#                 "day": "09/11/2024",
#                 "retention_day_1": 227,
#                 "retention_day_2": 199,
#                 "retention_day_3": 135,
#                 "retention_day_4": 32,
#                 "retention_day_5": 83,
#                 "retention_day_6": 94,
#                 "retention_day_7": 207
#             },
#             {
#                 "day": "10/11/2024",
#                 "retention_day_1": 768,
#                 "retention_day_2": 119,
#                 "retention_day_3": 69,
#                 "retention_day_4": 55,
#                 "retention_day_5": 65,
#                 "retention_day_6": 83,
#                 "retention_day_7": 92
#             },
#             {
#                 "day": "11/11/2024",
#                 "retention_day_1": 569,
#                 "retention_day_2": 276,
#                 "retention_day_3": 83,
#                 "retention_day_4": 30,
#                 "retention_day_5": 113,
#                 "retention_day_6": 162,
#                 "retention_day_7": 40
#             },
#             {
#                 "day": "12/11/2024",
#                 "retention_day_1": 547,
#                 "retention_day_2": 270,
#                 "retention_day_3": 121,
#                 "retention_day_4": 92,
#                 "retention_day_5": 322,
#                 "retention_day_6": 27,
#                 "retention_day_7": 204
#             }
#         ],
#         "revenue_data": [
#             {
#                 "day": "04/11/2024",
#                 "revenue": 340
#             },
#             {
#                 "day": "05/11/2024",
#                 "revenue": 130
#             },
#             {
#                 "day": "06/11/2024",
#                 "revenue": 479
#             },
#             {
#                 "day": "07/11/2024",
#                 "revenue": 444
#             },
#             {
#                 "day": "08/11/2024",
#                 "revenue": 277
#             },
#             {
#                 "day": "09/11/2024",
#                 "revenue": 238
#             },
#             {
#                 "day": "10/11/2024",
#                 "revenue": 247
#             },
#             {
#                 "day": "11/11/2024",
#                 "revenue": 151
#             },
#             {
#                 "day": "12/11/2024",
#                 "revenue": 243
#             },
#             {
#                 "day": "13/11/2024",
#                 "revenue": 224
#             }
#         ],
#         "user": "19360",
#         "today_revenue": "21474",
#         "request": "15452"
#     },
#     {
#         "game": "Zenless Zone Zero",
#         "platform": [
#             "android",
#             "ios"
#         ],
#         "user_up": {
#             "JAN": "5144",
#             "FEB": "6529",
#             "MAR": "3849",
#             "APR": "7166",
#             "MAY": "7037",
#             "JUN": "2435",
#             "JUL": "3362",
#             "AUG": "6128",
#             "SEP": "3585",
#             "OCT": "4966",
#             "NOV": "7303",
#             "DEC": "6034"
#         },
#         "users/country": {
#             "USA": "17214",
#             "VietNam": "18305",
#             "Korea": "22741",
#             "Japan": "4745",
#             "Taiwan": "11790",
#             "Singapore": "14585",
#             "Thailand": "8129",
#             "Laos": "6966",
#             "Russia": "18281",
#             "North Korea": "28671"
#         },
#         "avg_daily_active_user": {
#             "JAN": "2141",
#             "FEB": "6100",
#             "MAR": "6392",
#             "APR": "2745",
#             "MAY": "2240",
#             "JUN": "5274",
#             "JUL": "4841",
#             "AUG": "7119",
#             "SEP": "2093",
#             "OCT": "5226",
#             "NOV": "6735",
#             "DEC": "6825"
#         },
#         "active_user/country": {
#             "USA": "9376",
#             "VietNam": "4167",
#             "Korea": "10295",
#             "Japan": "11730",
#             "Taiwan": "4698",
#             "Singapore": "21977",
#             "Thailand": "13786",
#             "Laos": "12811",
#             "Russia": "3736",
#             "North Korea": "6997"
#         },
#         "selling_product": [
#             "Classic",
#             "gay",
#             "dao"
#         ],
#         "products": [
#             {
#                 "prd": "dao",
#                 "price": "3500",
#                 "tier": "S",
#                 "sales volume": "4983"
#             },
#             {
#                 "prd": "gay",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "3400"
#             },
#             {
#                 "prd": "Classic",
#                 "price": "3500",
#                 "tier": "A",
#                 "sales volume": "3812"
#             }
#         ],
#         "session": [
#             {
#                 "day": "04/11/2024",
#                 "session": "27304"
#             },
#             {
#                 "day": "05/11/2024",
#                 "session": "8870"
#             },
#             {
#                 "day": "06/11/2024",
#                 "session": "3797"
#             },
#             {
#                 "day": "07/11/2024",
#                 "session": "11081"
#             },
#             {
#                 "day": "08/11/2024",
#                 "session": "2751"
#             },
#             {
#                 "day": "09/11/2024",
#                 "session": "7407"
#             },
#             {
#                 "day": "10/11/2024",
#                 "session": "27384"
#             },
#             {
#                 "day": "11/11/2024",
#                 "session": "15588"
#             },
#             {
#                 "day": "12/11/2024",
#                 "session": "7502"
#             }
#         ],
#         "avgtime/day": [
#             {
#                 "day": "04/11/2024",
#                 "avg": "0.34595"
#             },
#             {
#                 "day": "05/11/2024",
#                 "avg": "2.8883"
#             },
#             {
#                 "day": "06/11/2024",
#                 "avg": "1.94496"
#             },
#             {
#                 "day": "07/11/2024",
#                 "avg": "0.46148"
#             },
#             {
#                 "day": "08/11/2024",
#                 "avg": "0.63048"
#             },
#             {
#                 "day": "09/11/2024",
#                 "avg": "0.61959"
#             },
#             {
#                 "day": "10/11/2024",
#                 "avg": "0.44359"
#             },
#             {
#                 "day": "11/11/2024",
#                 "avg": "1.78616"
#             },
#             {
#                 "day": "12/11/2024",
#                 "avg": "3.26845"
#             }
#         ],
#         "retention_data": [
#             {
#                 "day": "30/10/2024",
#                 "retention_day_1": 178,
#                 "retention_day_2": 247,
#                 "retention_day_3": 88,
#                 "retention_day_4": 77,
#                 "retention_day_5": 203,
#                 "retention_day_6": 212,
#                 "retention_day_7": 228
#             },
#             {
#                 "day": "31/10/2024",
#                 "retention_day_1": 538,
#                 "retention_day_2": 87,
#                 "retention_day_3": 130,
#                 "retention_day_4": 73,
#                 "retention_day_5": 92,
#                 "retention_day_6": 230,
#                 "retention_day_7": 224
#             },
#             {
#                 "day": "01/11/2024",
#                 "retention_day_1": 349,
#                 "retention_day_2": 265,
#                 "retention_day_3": 180,
#                 "retention_day_4": 10,
#                 "retention_day_5": 311,
#                 "retention_day_6": 59,
#                 "retention_day_7": 157
#             },
#             {
#                 "day": "02/11/2024",
#                 "retention_day_1": 367,
#                 "retention_day_2": 197,
#                 "retention_day_3": 168,
#                 "retention_day_4": 54,
#                 "retention_day_5": 226,
#                 "retention_day_6": 33,
#                 "retention_day_7": 168
#             },
#             {
#                 "day": "03/11/2024",
#                 "retention_day_1": 531,
#                 "retention_day_2": 373,
#                 "retention_day_3": 62,
#                 "retention_day_4": 86,
#                 "retention_day_5": 151,
#                 "retention_day_6": 158,
#                 "retention_day_7": 159
#             },
#             {
#                 "day": "04/11/2024",
#                 "retention_day_1": 1074,
#                 "retention_day_2": 273,
#                 "retention_day_3": 71,
#                 "retention_day_4": 71,
#                 "retention_day_5": 331,
#                 "retention_day_6": 139,
#                 "retention_day_7": 211
#             },
#             {
#                 "day": "05/11/2024",
#                 "retention_day_1": 1153,
#                 "retention_day_2": 246,
#                 "retention_day_3": 178,
#                 "retention_day_4": 36,
#                 "retention_day_5": 264,
#                 "retention_day_6": 192,
#                 "retention_day_7": 175
#             },
#             {
#                 "day": "06/11/2024",
#                 "retention_day_1": 750,
#                 "retention_day_2": 90,
#                 "retention_day_3": 200,
#                 "retention_day_4": 33,
#                 "retention_day_5": 270,
#                 "retention_day_6": 198,
#                 "retention_day_7": 179
#             },
#             {
#                 "day": "07/11/2024",
#                 "retention_day_1": 899,
#                 "retention_day_2": 117,
#                 "retention_day_3": 155,
#                 "retention_day_4": 51,
#                 "retention_day_5": 274,
#                 "retention_day_6": 81,
#                 "retention_day_7": 227
#             },
#             {
#                 "day": "08/11/2024",
#                 "retention_day_1": 1069,
#                 "retention_day_2": 79,
#                 "retention_day_3": 152,
#                 "retention_day_4": 44,
#                 "retention_day_5": 220,
#                 "retention_day_6": 41,
#                 "retention_day_7": 127
#             },
#             {
#                 "day": "09/11/2024",
#                 "retention_day_1": 985,
#                 "retention_day_2": 159,
#                 "retention_day_3": 132,
#                 "retention_day_4": 93,
#                 "retention_day_5": 227,
#                 "retention_day_6": 123,
#                 "retention_day_7": 199
#             },
#             {
#                 "day": "10/11/2024",
#                 "retention_day_1": 123,
#                 "retention_day_2": 337,
#                 "retention_day_3": 124,
#                 "retention_day_4": 47,
#                 "retention_day_5": 208,
#                 "retention_day_6": 223,
#                 "retention_day_7": 154
#             },
#             {
#                 "day": "11/11/2024",
#                 "retention_day_1": 922,
#                 "retention_day_2": 214,
#                 "retention_day_3": 161,
#                 "retention_day_4": 20,
#                 "retention_day_5": 139,
#                 "retention_day_6": 63,
#                 "retention_day_7": 208
#             },
#             {
#                 "day": "12/11/2024",
#                 "retention_day_1": 555,
#                 "retention_day_2": 164,
#                 "retention_day_3": 98,
#                 "retention_day_4": 59,
#                 "retention_day_5": 229,
#                 "retention_day_6": 88,
#                 "retention_day_7": 52
#             }
#         ],
#         "revenue_data": [
#             {
#                 "day": "04/11/2024",
#                 "revenue": 291
#             },
#             {
#                 "day": "05/11/2024",
#                 "revenue": 420
#             },
#             {
#                 "day": "06/11/2024",
#                 "revenue": 228
#             },
#             {
#                 "day": "07/11/2024",
#                 "revenue": 375
#             },
#             {
#                 "day": "08/11/2024",
#                 "revenue": 401
#             },
#             {
#                 "day": "09/11/2024",
#                 "revenue": 246
#             },
#             {
#                 "day": "10/11/2024",
#                 "revenue": 234
#             },
#             {
#                 "day": "11/11/2024",
#                 "revenue": 147
#             },
#             {
#                 "day": "12/11/2024",
#                 "revenue": 320
#             },
#             {
#                 "day": "13/11/2024",
#                 "revenue": 250
#             }
#         ],
#         "user": "18797",
#         "today_revenue": "22939",
#         "request": "33299"
#     }
# ]

months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

user_counts = 1500
total_games = 24
total_dau = 4080901
average_playtime = 42736
