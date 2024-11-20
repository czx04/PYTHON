from pymongo import MongoClient
client = MongoClient(f"mongodb+srv://anhchaiuem:anhchaiuem@pep.ghbx8ax.mongodb.net/?retryWrites=true&w=majority&appName=PEP")

db = client['overview']
collection = db['overview']


def convert_game_name(gamex):
    return gamex.lower().replace(' ', '')


datagame = [
    {
        "game": "Valorant",
        "platform": ["android", "ios"],
        "user_up": {
            "JAN": "2400",
            "FEB": "3400",
            "MAR": "2440",
            "APR": "6400",
            "MAY": "2400",
            "JUN": "6400",
            "JUL": "3400",
            "AUG": "1240",
            "SEP": "8400",
            "OCT": "3400",
            "NOV": "1400",
            "DEC": "4400",
        },
        "users/country": {
            'USA': "24360",
            'VietNam': "12471",
            'Korea': "2101",
            'Japan': "1344",
            'Taiwan': "1483",
            'Singapore': "1041",
            'Thailand': "1420",
            'Laos': "263",
            'Russia': "1196",
            'North Korea': "1"
        },
        "avg_daily_active_user": {
            "JAN": "2401",
            "FEB": "3400",
            "MAR": "2440",
            "APR": "6400",
            "MAY": "2400",
            "JUN": "6400",
            "JUL": "3400",
            "AUG": "1240",
            "SEP": "8400",
            "OCT": "3400",
            "NOV": "1400",
            "DEC": "4400",
        },
        "active_user/country": {
            "USA": "24361",
            "VietNam": "12471",
            "Korea": "2101",
            "Japan": "1344",
            "Taiwan": "1483",
            "Singapore": "1041",
            "Thailand": "1420",
            "Laos": "263",
            "Russia": "1196",
            "North Korea": "1"
        },
        "selling_product": ["Classic", "dao", "Gay"],
        "user":"32102",
        "today_revenue":"12345",
        "request":"40000",
    },
    {
        "game": "Blue Archive",
        "platform": ["android", "windows"],
        "user_up": {
            "JAN": "2700",
            "FEB": "3300",
            "MAR": "2240",
            "APR": "3400",
            "MAY": "9400",
            "JUN": "10400",
            "JUL": "9400",
            "AUG": "8240",
            "SEP": "7400",
            "OCT": "8400",
            "NOV": "9400",
            "DEC": "8400",
        },
        "users/country": {
            'USA': "24360",
            'VietNam': "12471",
            'Korea': "2101",
            'Japan': "1344",
            'Taiwan': "1483",
            'Singapore': "1041",
            'Thailand': "1420",
            'Laos': "263",
            'Russia': "1196",
            'North Korea': "1"
        },
        "avg_daily_active_user": {
            "JAN": "2401",
            "FEB": "3400",
            "MAR": "2440",
            "APR": "6400",
            "MAY": "2400",
            "JUN": "6400",
            "JUL": "3400",
            "AUG": "1240",
            "SEP": "8400",
            "OCT": "3400",
            "NOV": "1400",
            "DEC": "4400",
        },
        "active_user/country": {
            "USA": "24361",
            "VietNam": "12471",
            "Korea": "2101",
            "Japan": "1344",
            "Taiwan": "1483",
            "Singapore": "1041",
            "Thailand": "1420",
            "Laos": "263",
            "Russia": "1196",
            "North Korea": "1"
        },
        "selling_product": ["Gwen", "Yasuo", "Ahri"]
    },
    {
        "game": "Clash of Clans",
        "platform": ["android", "ios"],
        "user_up": {
            "JAN": "3623",
            "FEB": "1071",
            "MAR": "9731",
            "APR": "8854",
            "MAY": "5372",
            "JUN": "4305",
            "JUL": "5583",
            "AUG": "2211",
            "SEP": "3610",
            "OCT": "4722",
            "NOV": "9814",
            "DEC": "6170",
        },
        "users/country": {
            'USA': "24360",
            'VietNam': "12471",
            'Korea': "2101",
            'Japan': "1344",
            'Taiwan': "1483",
            'Singapore': "1041",
            'Thailand': "1420",
            'Laos': "263",
            'Russia': "1196",
            'North Korea': "1"
        },
        "avg_daily_active_user": {
            "JAN": "2400",
            "FEB": "3400",
            "MAR": "2440",
            "APR": "6400",
            "MAY": "2400",
            "JUN": "6400",
            "JUL": "3400",
            "AUG": "1240",
            "SEP": "8400",
            "OCT": "3400",
            "NOV": "1400",
            "DEC": "4400",
        },
        "active_user/country": {
            "USA": "24361",
            "VietNam": "12471",
            "Korea": "2101",
            "Japan": "1344",
            "Taiwan": "1483",
            "Singapore": "1041",
            "Thailand": "1420",
            "Laos": "263",
            "Russia": "1196",
            "North Korea": "1"
        },
        "selling_product": ["Gwen", "Yasuo", "Ahri"]
    },
    {
        "game": "Genshin Impact",
        "platform": ["macos", "ios"],
        "user_up": {
            "JAN": "3886",
            "FEB": "6660",
            "MAR": "8281",
            "APR": "4767",
            "MAY": "5551",
            "JUN": "9656",
            "JUL": "9159",
            "AUG": "8001",
            "SEP": "5772",
            "OCT": "6356",
            "NOV": "6776",
            "DEC": "9817",
        },
        "users/country": {
            'USA': "24360",
            'VietNam': "12471",
            'Korea': "2101",
            'Japan': "1344",
            'Taiwan': "1483",
            'Singapore': "1041",
            'Thailand': "1420",
            'Laos': "263",
            'Russia': "1196",
            'North Korea': "1"
        },
        "avg_daily_active_user": {
            "JAN": "2400",
            "FEB": "3400",
            "MAR": "2440",
            "APR": "6400",
            "MAY": "2400",
            "JUN": "6400",
            "JUL": "3400",
            "AUG": "1240",
            "SEP": "8400",
            "OCT": "3400",
            "NOV": "1400",
            "DEC": "4400",
        }, "active_user/country": {
        "USA": "24361",
        "VietNam": "12471",
        "Korea": "2101",
        "Japan": "1344",
        "Taiwan": "1483",
        "Singapore": "1041",
        "Thailand": "1420",
        "Laos": "263",
        "Russia": "1196",
        "North Korea": "1"
    },
        "selling_product": ["Gwen", "Yasuo", "Ahri"]
    },
    {
        "game": "Hay Day",
        "platform": ["android", "ios"],
        "user_up": {
            "JAN": "3783",
            "FEB": "2225",
            "MAR": "1508",
            "APR": "3039",
            "MAY": "9284",
            "JUN": "8751",
            "JUL": "7573",
            "AUG": "9686",
            "SEP": "4511",
            "OCT": "5228",
            "NOV": "3711",
            "DEC": "4826",
        },
        "users/country": {
            'USA': "24360",
            'VietNam': "12471",
            'Korea': "2101",
            'Japan': "1344",
            'Taiwan': "1483",
            'Singapore': "1041",
            'Thailand': "1420",
            'Laos': "263",
            'Russia': "1196",
            'North Korea': "1"
        },
        "avg_daily_active_user": {
            "JAN": "2400",
            "FEB": "3400",
            "MAR": "2440",
            "APR": "6400",
            "MAY": "2400",
            "JUN": "6400",
            "JUL": "3400",
            "AUG": "1240",
            "SEP": "8400",
            "OCT": "3400",
            "NOV": "1400",
            "DEC": "4400",
        }, "active_user/country": {
        "USA": "24361",
        "VietNam": "12471",
        "Korea": "2101",
        "Japan": "1344",
        "Taiwan": "1483",
        "Singapore": "1041",
        "Thailand": "1420",
        "Laos": "263",
        "Russia": "1196",
        "North Korea": "1"
    }, "selling_product": ["Gwen", "Yasuo", "Ahri"]
    },
    {
        "game": "Honkai Impact 3",
        "platform": ["android", "ios"],
        "user_up": {
            "JAN": "1055",
            "FEB": "5511",
            "MAR": "6298",
            "APR": "1930",
            "MAY": "4236",
            "JUN": "4219",
            "JUL": "4984",
            "AUG": "2464",
            "SEP": "3694",
            "OCT": "9692",
            "NOV": "9068",
            "DEC": "5955",
        },
        "users/country": {
            'USA': "24360",
            'VietNam': "12471",
            'Korea': "2101",
            'Japan': "1344",
            'Taiwan': "1483",
            'Singapore': "1041",
            'Thailand': "1420",
            'Laos': "263",
            'Russia': "1196",
            'North Korea': "1"
        },
        "avg_daily_active_user": {
            "JAN": "2400",
            "FEB": "3400",
            "MAR": "2440",
            "APR": "6400",
            "MAY": "2400",
            "JUN": "6400",
            "JUL": "3400",
            "AUG": "1240",
            "SEP": "8400",
            "OCT": "3400",
            "NOV": "1400",
            "DEC": "4400",
        }, "active_user/country": {
        "USA": "24361",
        "VietNam": "12471",
        "Korea": "2101",
        "Japan": "1344",
        "Taiwan": "1483",
        "Singapore": "1041",
        "Thailand": "1420",
        "Laos": "263",
        "Russia": "1196",
        "North Korea": "1"
    },
        "selling_product": ["Gwen", "Yasuo", "Ahri"]
    },
    {
        "game": "Honkai Star Rail",
        "platform": ["android", "ios"],
        "user_up": {
            "JAN": "1080",
            "FEB": "5448",
            "MAR": "4476",
            "APR": "5984",
            "MAY": "3684",
            "JUN": "4040",
            "JUL": "5559",
            "AUG": "4780",
            "SEP": "9012",
            "OCT": "2635",
            "NOV": "4748",
            "DEC": "6746",
        },
        "users/country": {
            'USA': "24360",
            'VietNam': "12471",
            'Korea': "2101",
            'Japan': "1344",
            'Taiwan': "1483",
            'Singapore': "1041",
            'Thailand': "1420",
            'Laos': "263",
            'Russia': "1196",
            'North Korea': "1"
        },
        "avg_daily_active_user": {
            "JAN": "2400",
            "FEB": "3400",
            "MAR": "2440",
            "APR": "6400",
            "MAY": "2400",
            "JUN": "6400",
            "JUL": "3400",
            "AUG": "1240",
            "SEP": "8400",
            "OCT": "3400",
            "NOV": "1400",
            "DEC": "4400",
        },
        "active_user/country": {
            "USA": "24361",
            "VietNam": "12471",
            "Korea": "2101",
            "Japan": "1344",
            "Taiwan": "1483",
            "Singapore": "1041",
            "Thailand": "1420",
            "Laos": "263",
            "Russia": "1196",
            "North Korea": "1"
        },
        "selling_product": ["Gwen", "Yasuo", "Ahri"]
    },
    {
        "game": "League of Legends",
        "platform": ["android", "ios"],
        "user_up": {
            "JAN": "1860",
            "FEB": "4354",
            "MAR": "8487",
            "APR": "9498",
            "MAY": "5309",
            "JUN": "4981",
            "JUL": "8770",
            "AUG": "8247",
            "SEP": "2986",
            "OCT": "6187",
            "NOV": "8612",
            "DEC": "5959",
        },
        "users/country": {
            'USA': "24360",
            'VietNam': "12471",
            'Korea': "2101",
            'Japan': "1344",
            'Taiwan': "1483",
            'Singapore': "1041",
            'Thailand': "1420",
            'Laos': "263",
            'Russia': "1196",
            'North Korea': "1"
        },
        "avg_daily_active_user": {
            "JAN": "2400",
            "FEB": "3400",
            "MAR": "2440",
            "APR": "6400",
            "MAY": "2400",
            "JUN": "6400",
            "JUL": "3400",
            "AUG": "1240",
            "SEP": "8400",
            "OCT": "3400",
            "NOV": "1400",
            "DEC": "4400",
        },
        "active_user/country": {
            "USA": "24361",
            "VietNam": "12471",
            "Korea": "2101",
            "Japan": "1344",
            "Taiwan": "1483",
            "Singapore": "1041",
            "Thailand": "1420",
            "Laos": "263",
            "Russia": "1196",
            "North Korea": "1"
        },
        "selling_product": ["Gwen", "Yasuo", "Ahri"]
    },
    {
        "game": "Zenless Zone Zero",
        "platform": ["android", "ios"],
        "user_up": {
            "JAN": "1360",
            "FEB": "1327",
            "MAR": "3270",
            "APR": "1087",
            "MAY": "1826",
            "JUN": "1647",
            "JUL": "6888",
            "AUG": "5592",
            "SEP": "7974",
            "OCT": "4641",
            "NOV": "1540",
            "DEC": "3759",
        },
        "users/country": {
            'USA': "24360",
            'VietNam': "12471",
            'Korea': "2101",
            'Japan': "1344",
            'Taiwan': "1483",
            'Singapore': "1041",
            'Thailand': "1420",
            'Laos': "263",
            'Russia': "1196",
            'North Korea': "1"
        },
        "avg_daily_active_user": {
            "JAN": "2400",
            "FEB": "3400",
            "MAR": "2440",
            "APR": "6400",
            "MAY": "2400",
            "JUN": "6400",
            "JUL": "3400",
            "AUG": "1240",
            "SEP": "8400",
            "OCT": "3400",
            "NOV": "1400",
            "DEC": "4400",
        },
        "active_user/country": {
            "USA": "24361",
            "Viet Nam": "12471",
            "Korea": "2101",
            "Japan": "1344",
            "Taiwan": "1483",
            "Singapore": "1041",
            "Thailand": "1420",
            "Laos": "263",
            "Russia": "1196",
            "North Korea": "1"
        },
        "selling_product": ["Gwen", "Yasuo", "Ahri"]
    }
]

# lấy 3 sản phẩm bán chạy nhất
products = [
    {
        "prd": "dao",
        "price": "3500",
        "tier": "S",
        "sales volume": "3232"
    },
    {
        "prd": "Yasuo",
        "price": "3500",
        "tier": "A",
        "sales volume": "3232"
    },
    {
        "prd": "Ahri",
        "price": "3500",
        "tier": "A",
        "sales volume": "3232"
    }
]

# lấy 7 ngày gần nhất
session = [
    {
        "day": "04/11/2024",
        "session": "12344"
    },
    {
        "day": "05/11/2024",
        "session": "13345"
    },
    {
        "day": "06/11/2024",
        "session": "12334"
    },
    {
        "day": "07/11/2024",
        "session": "11134"
    },
    {
        "day": "08/11/2024",
        "session": "21234"
    },
    {
        "day": "09/11/2024",
        "session": "31234"
    },
    {
        "day": "10/11/2024",
        "session": "25234"
    },
    {
        "day": "11/11/2024",
        "session": "17234"
    },
    {
        "day": "12/11/2024",
        "session": "11234"
    },
]
# lấy 7 ngày gần nhất
avgtime = [
    {
        "day": "04/11/2024",
        "avg": "1.02312"
    },
    {
        "day": "05/11/2024",
        "avg": "1.11"
    },
    {
        "day": "06/11/2024",
        "avg": "0.7011"
    },
    {
        "day": "07/11/2024",
        "avg": "0.2313"
    },
    {
        "day": "08/11/2024",
        "avg": "0.4213"
    },
    {
        "day": "09/11/2024",
        "avg": "0.712"
    },
    {
        "day": "10/11/2024",
        "avg": "1.01"
    },
    {
        "day": "11/11/2024",
        "avg": "0.842"
    },
    {
        "day": "12/11/2024",
        "avg": "0.743"
    },
]

retention_data = [
{"day": "30/10/2024", "retention_day_1": 190, "retention_day_2": 280, "retention_day_3": 170, "retention_day_4": 60,
     "retention_day_5": 350, "retention_day_6": 240, "retention_day_7": 130},
{"day": "31/10/2024", "retention_day_1": 190, "retention_day_2": 280, "retention_day_3": 170, "retention_day_4": 60,
     "retention_day_5": 350, "retention_day_6": 240, "retention_day_7": 130},
{"day": "01/11/2024", "retention_day_1": 190, "retention_day_2": 280, "retention_day_3": 170, "retention_day_4": 60,
     "retention_day_5": 350, "retention_day_6": 240, "retention_day_7": 130},
{"day": "02/11/2024", "retention_day_1": 190, "retention_day_2": 280, "retention_day_3": 170, "retention_day_4": 60,
     "retention_day_5": 350, "retention_day_6": 240, "retention_day_7": 130},
{"day": "03/11/2024", "retention_day_1": 190, "retention_day_2": 280, "retention_day_3": 170, "retention_day_4": 60,
     "retention_day_5": 350, "retention_day_6": 240, "retention_day_7": 130},
    {"day": "04/11/2024", "retention_day_1": 190, "retention_day_2": 280, "retention_day_3": 170, "retention_day_4": 60,
     "retention_day_5": 350, "retention_day_6": 240, "retention_day_7": 130},
    {"day": "05/11/2024", "retention_day_1": 120, "retention_day_2": 90, "retention_day_3": 75, "retention_day_4": 65,
     "retention_day_5": 55, "retention_day_6": 45, "retention_day_7": 35},
    {"day": "06/11/2024", "retention_day_1": 940, "retention_day_2": 310, "retention_day_3": 200, "retention_day_4": 185,
     "retention_day_5": 175, "retention_day_6": 165, "retention_day_7": 250},
    {"day": "07/11/2024", "retention_day_1": 920, "retention_day_2": 300, "retention_day_3": 180, "retention_day_4": 170,
     "retention_day_5": 160, "retention_day_6": 150, "retention_day_7": 240},
    {"day": "08/11/2024", "retention_day_1": 900, "retention_day_2": 290, "retention_day_3": 170, "retention_day_4": 160,
     "retention_day_5": 150, "retention_day_6": 140, "retention_day_7": 230},
    {"day": "09/11/2024", "retention_day_1": 880, "retention_day_2": 280, "retention_day_3": 160, "retention_day_4": 150,
     "retention_day_5": 140, "retention_day_6": 130, "retention_day_7": 220},
    {"day": "10/11/2024", "retention_day_1": 860, "retention_day_2": 270, "retention_day_3": 150, "retention_day_4": 140,
     "retention_day_5": 130, "retention_day_6": 120, "retention_day_7": 210},
    {"day": "11/11/2024", "retention_day_1": 840, "retention_day_2": 260, "retention_day_3": 140, "retention_day_4": 130,
     "retention_day_5": 120, "retention_day_6": 110, "retention_day_7": 200},
    {"day": "12/11/2024", "retention_day_1": 820, "retention_day_2": 250, "retention_day_3": 130, "retention_day_4": 120,
     "retention_day_5": 110, "retention_day_6": 100, "retention_day_7": 190},
    {"day": "13/11/2024", "retention_day_1": 800, "retention_day_2": 240, "retention_day_3": 120, "retention_day_4": 110,
     "retention_day_5": 100, "retention_day_6": 90, "retention_day_7": 180},
]

# Dữ liệu doanh thu
revenue_data = [
    {"day": "04/11/2024", "revenue": 100},
    {"day": "05/11/2024", "revenue": 150},
    {"day": "06/11/2024", "revenue": 120},
    {"day": "07/11/2024", "revenue": 130},
    {"day": "08/11/2024", "revenue": 200},
    {"day": "09/11/2024", "revenue": 180},
    {"day": "10/11/2024", "revenue": 220},
    {"day": "11/11/2024", "revenue": 210},
    {"day": "12/11/2024", "revenue": 250},
    {"day": "13/11/2024", "revenue": 300},
]

ad_revenue_data = [
    {"day": "04/11/2024", "ad_rev_median": 100, "ad_rev_avg": 120},
    {"day": "05/11/2024", "ad_rev_median": 150, "ad_rev_avg": 170},
    {"day": "06/11/2024", "ad_rev_median": 130, "ad_rev_avg": 140},
    {"day": "07/11/2024", "ad_rev_median": 180, "ad_rev_avg": 190},
    {"day": "08/11/2024", "ad_rev_median": 200, "ad_rev_avg": 220},
    {"day": "09/11/2024", "ad_rev_median": 210, "ad_rev_avg": 230},
    {"day": "10/11/2024", "ad_rev_median": 220, "ad_rev_avg": 240},
    {"day": "11/11/2024", "ad_rev_median": 250, "ad_rev_avg": 270},
    {"day": "12/11/2024", "ad_rev_median": 260, "ad_rev_avg": 280},
    {"day": "13/11/2024", "ad_rev_median": 270, "ad_rev_avg": 290},
]

months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

user_counts = 1500
total_games = 24
total_dau = 4080901
average_playtime = 42736
