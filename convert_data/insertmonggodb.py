from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb+srv://anhchaiuem:anhchaiuem@pep.ghbx8ax.mongodb.net/?retryWrites=true&w=majority&appName=PEP')

db = client['overview']
collection = db['overview']

data = {
    "game": "Honkai Star Rail",
    "platform": [
        "android",
        "ios"
    ],
    "user_up": {
        "JAN": "3044",
        "FEB": "7565",
        "MAR": "3002",
        "APR": "3416",
        "MAY": "7966",
        "JUN": "2441",
        "JUL": "6189",
        "AUG": "2784",
        "SEP": "5444",
        "OCT": "6247",
        "NOV": "5099",
        "DEC": "4231"
    },
    "users/country": {
        "USA": "4769",
        "VietNam": "20330",
        "Korea": "10030",
        "Japan": "24160",
        "Taiwan": "14830",
        "Singapore": "15797",
        "Thailand": "14567",
        "Laos": "25388",
        "Russia": "1391",
        "North Korea": "17127"
    },
    "avg_daily_active_user": {
        "JAN": "2332",
        "FEB": "6870",
        "MAR": "5340",
        "APR": "3910",
        "MAY": "4018",
        "JUN": "2782",
        "JUL": "4239",
        "AUG": "3937",
        "SEP": "5731",
        "OCT": "7881",
        "NOV": "6443",
        "DEC": "5547"
    },
    "active_user/country": {
        "USA": "28957",
        "VietNam": "1000",
        "Korea": "7107",
        "Japan": "11284",
        "Taiwan": "11108",
        "Singapore": "19630",
        "Thailand": "28197",
        "Laos": "5158",
        "Russia": "19649",
        "North Korea": "24517"
    },
    "selling_product": [
        "Veroll",
        "Upvk",
        "Exp"
    ],
    "products": [
        {
            "prd": "Exp",
            "price": "3962",
            "tier": "S",
            "sales volume": "4147"
        },
        {
            "prd": "Upvk",
            "price": "1407",
            "tier": "A",
            "sales volume": "1619"
        },
        {
            "prd": "Veroll",
            "price": "1734",
            "tier": "A",
            "sales volume": "2309"
        }
    ],
    "session": [
        {
            "day": "04/11/2024",
            "session": "10876"
        },
        {
            "day": "05/11/2024",
            "session": "4840"
        },
        {
            "day": "06/11/2024",
            "session": "5520"
        },
        {
            "day": "07/11/2024",
            "session": "8740"
        },
        {
            "day": "08/11/2024",
            "session": "23445"
        },
        {
            "day": "09/11/2024",
            "session": "11806"
        },
        {
            "day": "10/11/2024",
            "session": "18742"
        },
        {
            "day": "11/11/2024",
            "session": "9413"
        },
        {
            "day": "12/11/2024",
            "session": "22621"
        }
    ],
    "avgtime/day": [
        {
            "day": "04/11/2024",
            "avg": "3.98765"
        },
        {
            "day": "05/11/2024",
            "avg": "0.11014"
        },
        {
            "day": "06/11/2024",
            "avg": "2.3281"
        },
        {
            "day": "07/11/2024",
            "avg": "3.64519"
        },
        {
            "day": "08/11/2024",
            "avg": "0.40791"
        },
        {
            "day": "09/11/2024",
            "avg": "1.40985"
        },
        {
            "day": "10/11/2024",
            "avg": "2.19556"
        },
        {
            "day": "11/11/2024",
            "avg": "0.17036"
        },
        {
            "day": "12/11/2024",
            "avg": "2.97861"
        }
    ],
    "retention_data": [
        {
            "day": "30/10/2024",
            "retention_day_1": 295,
            "retention_day_2": 168,
            "retention_day_3": 146,
            "retention_day_4": 90,
            "retention_day_5": 197,
            "retention_day_6": 91,
            "retention_day_7": 40
        },
        {
            "day": "31/10/2024",
            "retention_day_1": 324,
            "retention_day_2": 67,
            "retention_day_3": 76,
            "retention_day_4": 186,
            "retention_day_5": 219,
            "retention_day_6": 233,
            "retention_day_7": 152
        },
        {
            "day": "01/11/2024",
            "retention_day_1": 336,
            "retention_day_2": 88,
            "retention_day_3": 185,
            "retention_day_4": 77,
            "retention_day_5": 136,
            "retention_day_6": 212,
            "retention_day_7": 186
        },
        {
            "day": "02/11/2024",
            "retention_day_1": 239,
            "retention_day_2": 75,
            "retention_day_3": 105,
            "retention_day_4": 59,
            "retention_day_5": 119,
            "retention_day_6": 221,
            "retention_day_7": 79
        },
        {
            "day": "03/11/2024",
            "retention_day_1": 123,
            "retention_day_2": 227,
            "retention_day_3": 152,
            "retention_day_4": 168,
            "retention_day_5": 111,
            "retention_day_6": 230,
            "retention_day_7": 152
        },
        {
            "day": "04/11/2024",
            "retention_day_1": 63,
            "retention_day_2": 245,
            "retention_day_3": 166,
            "retention_day_4": 77,
            "retention_day_5": 300,
            "retention_day_6": 172,
            "retention_day_7": 145
        },
        {
            "day": "05/11/2024",
            "retention_day_1": 52,
            "retention_day_2": 161,
            "retention_day_3": 36,
            "retention_day_4": 128,
            "retention_day_5": 284,
            "retention_day_6": 114,
            "retention_day_7": 187
        },
        {
            "day": "06/11/2024",
            "retention_day_1": 266,
            "retention_day_2": 209,
            "retention_day_3": 199,
            "retention_day_4": 152,
            "retention_day_5": 201,
            "retention_day_6": 96,
            "retention_day_7": 105
        },
        {
            "day": "07/11/2024",
            "retention_day_1": 333,
            "retention_day_2": 149,
            "retention_day_3": 33,
            "retention_day_4": 171,
            "retention_day_5": 174,
            "retention_day_6": 227,
            "retention_day_7": 160
        },
        {
            "day": "08/11/2024",
            "retention_day_1": 336,
            "retention_day_2": 276,
            "retention_day_3": 123,
            "retention_day_4": 192,
            "retention_day_5": 171,
            "retention_day_6": 140,
            "retention_day_7": 219
        },
        {
            "day": "09/11/2024",
            "retention_day_1": 181,
            "retention_day_2": 199,
            "retention_day_3": 57,
            "retention_day_4": 106,
            "retention_day_5": 222,
            "retention_day_6": 198,
            "retention_day_7": 94
        },
        {
            "day": "10/11/2024",
            "retention_day_1": 95,
            "retention_day_2": 92,
            "retention_day_3": 191,
            "retention_day_4": 120,
            "retention_day_5": 154,
            "retention_day_6": 166,
            "retention_day_7": 108
        },
        {
            "day": "11/11/2024",
            "retention_day_1": 244,
            "retention_day_2": 50,
            "retention_day_3": 150,
            "retention_day_4": 75,
            "retention_day_5": 74,
            "retention_day_6": 161,
            "retention_day_7": 167
        },
        {
            "day": "12/11/2024",
            "retention_day_1": 317,
            "retention_day_2": 207,
            "retention_day_3": 110,
            "retention_day_4": 196,
            "retention_day_5": 237,
            "retention_day_6": 223,
            "retention_day_7": 209
        }
    ],
    "revenue_data": [
        {
            "day": "04/11/2024",
            "revenue": 162
        },
        {
            "day": "05/11/2024",
            "revenue": 165
        },
        {
            "day": "06/11/2024",
            "revenue": 408
        },
        {
            "day": "07/11/2024",
            "revenue": 312
        },
        {
            "day": "08/11/2024",
            "revenue": 470
        },
        {
            "day": "09/11/2024",
            "revenue": 236
        },
        {
            "day": "10/11/2024",
            "revenue": 500
        },
        {
            "day": "11/11/2024",
            "revenue": 351
        },
        {
            "day": "12/11/2024",
            "revenue": 416
        },
        {
            "day": "13/11/2024",
            "revenue": 298
        }
    ],
    "ad_revenue_data": [
        {
            "day": "04/11/2024",
            "ad_rev_median": 239,
            "ad_rev_avg": 243
        },
        {
            "day": "05/11/2024",
            "ad_rev_median": 203,
            "ad_rev_avg": 302
        },
        {
            "day": "06/11/2024",
            "ad_rev_median": 160,
            "ad_rev_avg": 237
        },
        {
            "day": "07/11/2024",
            "ad_rev_median": 174,
            "ad_rev_avg": 296
        },
        {
            "day": "08/11/2024",
            "ad_rev_median": 239,
            "ad_rev_avg": 133
        },
        {
            "day": "09/11/2024",
            "ad_rev_median": 191,
            "ad_rev_avg": 274
        },
        {
            "day": "10/11/2024",
            "ad_rev_median": 134,
            "ad_rev_avg": 238
        },
        {
            "day": "11/11/2024",
            "ad_rev_median": 204,
            "ad_rev_avg": 194
        },
        {
            "day": "12/11/2024",
            "ad_rev_median": 284,
            "ad_rev_avg": 198
        },
        {
            "day": "13/11/2024",
            "ad_rev_median": 286,
            "ad_rev_avg": 345
        }
    ],
    "user": "40898",
    "today_revenue": "17128",
    "request": "18157"
}






# Insert dữ liệu vào collection
collection.insert_one(data)

print("Dữ liệu đã được chèn vào MongoDB thành công.")
