from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb+srv://anhchaiuem:anhchaiuem@pep.ghbx8ax.mongodb.net/?retryWrites=true&w=majority&appName=PEP')

db = client['overview']
collection = db['overview']

data = {
    "game": "Honkai Star Rail",
    "platform": ["android", "ios"],
    "user_up": {
        "JAN": "1200",
        "FEB": "3500",
        "MAR": "4000",
        "APR": "4700",
        "MAY": "5200",
        "JUN": "5800",
        "JUL": "6300",
        "AUG": "6700",
        "SEP": "7000",
        "OCT": "7500",
        "NOV": "7900",
        "DEC": "8500"
    },
    "users/country": {
        "USA": "27000",
        "VietNam": "22000",
        "Korea": "18000",
        "Japan": "15000",
        "Taiwan": "13000",
        "Singapore": "11000",
        "Thailand": "10000",
        "Laos": "3500",
        "Russia": "14000",
        "North Korea": "800"
    },
    "avg_daily_active_user": {
        "JAN": "2600",
        "FEB": "3000",
        "MAR": "3500",
        "APR": "4000",
        "MAY": "4500",
        "JUN": "5000",
        "JUL": "5500",
        "AUG": "6000",
        "SEP": "6500",
        "OCT": "7000",
        "NOV": "7500",
        "DEC": "8000"
    },
    "active_user/country": {
        "USA": "27500",
        "VietNam": "22500",
        "Korea": "18500",
        "Japan": "15500",
        "Taiwan": "13500",
        "Singapore": "11500",
        "Thailand": "10500",
        "Laos": "3700",
        "Russia": "14500",
        "North Korea": "900"
    },
    "selling_product": ["Gwen", "Yasuo", "Ahri"]
}





# Insert dữ liệu vào collection
collection.insert_one(data)

print("Dữ liệu đã được chèn vào MongoDB thành công.")
