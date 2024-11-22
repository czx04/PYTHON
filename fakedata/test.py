import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Danh sách các game và item tương ứng
games = [
    {
        "game": "Blue Archive",
        "items": ["CafeRank", "Exp", "Hat"]
    },
    {
        "game": "Clash of Clans",
        "items": ["Gold", "Elixir", "Dark Elixir"]
    },
    {
        "game": "Genshin Impact",
        "items": ["Primogem", "Mora", "Artifact"]
    },
    {
        "game": "Hay Day",
        "items": ["Wheat", "Corn", "Egg"]
    },
    {
        "game": "Honkai Impact 3",
        "items": ["Crystal", "Weapon", "Stigmata"]
    },
    {
        "game": "Honkai Star Rail",
        "items": ["Star Rail Pass", "Credit", "Relic"]
    },
    {
        "game": "League of Legends",
        "items": ["Riot Point", "Skin", "Champion"]
    }
]

# Danh sách các quốc gia
countries = ["USA", "Vietnam", "Korea", "Japan", "Taiwan", "Singapore", "Thailand", "Laos", "Russia", "North Korea"]

# Danh sách các nền tảng
platforms_list = ["android", "ios"]

# Tháng trong năm
months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
          "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

# Ngày bắt đầu cho dữ liệu ngày
start_date = datetime(2024, 11, 4)

# Tạo dữ liệu cho từng sheet
# Sheet1: Game Info
game_info_data = []
for game_entry in games:
    game = game_entry['game']
    game_info_data.append({
        "game": game,
        "platform": ",".join(random.sample(platforms_list, k=random.randint(1, 2))),
        "user": random.randint(10000, 50000),
        "today_revenue": random.randint(10000, 30000),
        "request": random.randint(10000, 50000)
    })
game_info_df = pd.DataFrame(game_info_data)

# Sheet2: User Up
user_up_data = []
for game_entry in games:
    game = game_entry['game']
    data = {"game": game}
    for month in months:
        data[month] = random.randint(2000, 8000)
    user_up_data.append(data)
user_up_df = pd.DataFrame(user_up_data)

# Sheet3: Users_Country
users_country_data = []
for game_entry in games:
    game = game_entry['game']
    for country in countries:
        users_country_data.append({
            "game": game,
            "country": country,
            "users": random.randint(800, 30000)
        })
users_country_df = pd.DataFrame(users_country_data)

# Sheet4: Avg Daily Active User
avg_dau_data = []
for game_entry in games:
    game = game_entry['game']
    data = {"game": game}
    for month in months:
        data[month] = random.randint(2000, 8000)
    avg_dau_data.append(data)
avg_dau_df = pd.DataFrame(avg_dau_data)

# Sheet5: ActiveUserCountry
active_users_country_data = []
for game_entry in games:
    game = game_entry['game']
    for country in countries:
        active_users_country_data.append({
            "game": game,
            "country": country,
            "active_users": random.randint(800, 30000)
        })
active_users_country_df = pd.DataFrame(active_users_country_data)

# Sheet6: Products
products_data = []
tiers = ["S", "A", "B"]
for game_entry in games:
    game = game_entry['game']
    items = game_entry['items']
    for item in items:
        products_data.append({
            "game": game,
            "prd": item,
            "price": random.randint(1000, 5000),
            "tier": random.choice(tiers),
            "sales volume": random.randint(1000, 5000)
        })
products_df = pd.DataFrame(products_data)

# Sheet7: Session
session_data = []
for game_entry in games:
    game = game_entry['game']
    for i in range(9):
        day = (start_date + timedelta(days=i)).strftime("%d/%m/%Y")
        session_data.append({
            "game": game,
            "day": day,
            "session": random.randint(1000, 30000)
        })
session_df = pd.DataFrame(session_data)

# Sheet8: Avg Time/Day
avg_time_day_data = []
for game_entry in games:
    game = game_entry['game']
    for i in range(9):
        day = (start_date + timedelta(days=i)).strftime("%d/%m/%Y")
        avg_time_day_data.append({
            "game": game,
            "day": day,
            "avg": round(random.uniform(0.1, 4.0), 5)
        })
avg_time_day_df = pd.DataFrame(avg_time_day_data)

# Sheet9: Retention Data
retention_data = []
retention_start_date = datetime(2024, 10, 30)
for game_entry in games:
    game = game_entry['game']
    for i in range(14):
        day = (retention_start_date + timedelta(days=i)).strftime("%d/%m/%Y")
        retention_data.append({
            "game": game,
            "day": day,
            "retention_day_1": random.randint(50, 340),
            "retention_day_2": random.randint(50, 300),
            "retention_day_3": random.randint(30, 200),
            "retention_day_4": random.randint(40, 200),
            "retention_day_5": random.randint(30, 350),
            "retention_day_6": random.randint(60, 240),
            "retention_day_7": random.randint(40, 230)
        })
retention_data_df = pd.DataFrame(retention_data)

# Sheet10: Revenue Data
revenue_data = []
for game_entry in games:
    game = game_entry['game']
    for i in range(10):
        day = (start_date + timedelta(days=i)).strftime("%d/%m/%Y")
        revenue_data.append({
            "game": game,
            "day": day,
            "revenue": random.randint(100, 500)
        })
revenue_data_df = pd.DataFrame(revenue_data)

# Sheet11: Ad Revenue Data
ad_revenue_data = []
for game_entry in games:
    game = game_entry['game']
    for i in range(10):
        day = (start_date + timedelta(days=i)).strftime("%d/%m/%Y")
        ad_revenue_data.append({
            "game": game,
            "day": day,
            "ad_rev_median": random.randint(100, 300),
            "ad_rev_avg": random.randint(120, 350)
        })
ad_revenue_data_df = pd.DataFrame(ad_revenue_data)

# Ghi dữ liệu vào file Excel
with pd.ExcelWriter('games_data.xlsx', engine='openpyxl') as writer:
    game_info_df.to_excel(writer, sheet_name='Game Info', index=False)
    user_up_df.to_excel(writer, sheet_name='User Up', index=False)
    users_country_df.to_excel(writer, sheet_name='Users_Country', index=False)
    avg_dau_df.to_excel(writer, sheet_name='Avg Daily Active User', index=False)
    active_users_country_df.to_excel(writer, sheet_name='ActiveUserCountry', index=False)
    products_df.to_excel(writer, sheet_name='Products', index=False)
    session_df.to_excel(writer, sheet_name='Session', index=False)
    avg_time_day_df.to_excel(writer, sheet_name='Avg Time Day', index=False)
    retention_data_df.to_excel(writer, sheet_name='Retention Data', index=False)
    revenue_data_df.to_excel(writer, sheet_name='Revenue Data', index=False)
    ad_revenue_data_df.to_excel(writer, sheet_name='Ad Revenue Data', index=False)

print("File Excel với dữ liệu giả đã được tạo thành công.")
