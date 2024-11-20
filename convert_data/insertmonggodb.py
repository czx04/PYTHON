from pymongo import MongoClient
from bson import ObjectId

# Kết nối đến MongoDB (giả sử MongoDB đang chạy trên localhost và cổng 27017)
client = MongoClient('mongodb+srv://anhchaiuem:anhchaiuem@pep.ghbx8ax.mongodb.net/?retryWrites=true&w=majority&appName=PEP')

# Chọn database và collection
db = client['overview']  # Database 'overview'
collection = db['overview']  # Collection 'overview'

# Dữ liệu cần insert
data = {
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
    }

# Insert dữ liệu vào collection
collection.insert_one(data)

print("Dữ liệu đã được chèn vào MongoDB thành công.")
