from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb+srv://anhchaiuem:anhchaiuem@pep.ghbx8ax.mongodb.net/?retryWrites=true&w=majority&appName=PEP')

db = client['overview']
collection = db['test']


excel_file = 'games_data.xlsx'

result = collection.delete_many({})
print(f"Đã xóa {result.deleted_count} tài liệu trong collection 'test'.")

# Đọc dữ liệu từ file Excel
game_info_df = pd.read_excel(excel_file, sheet_name='Game Info')
user_up_df = pd.read_excel(excel_file, sheet_name='User Up')
users_country_df = pd.read_excel(excel_file, sheet_name='Users_Country')
avg_dau_df = pd.read_excel(excel_file, sheet_name='Avg Daily Active User')
active_users_country_df = pd.read_excel(excel_file, sheet_name='ActiveUserCountry')
products_df = pd.read_excel(excel_file, sheet_name='Products')
session_df = pd.read_excel(excel_file, sheet_name='Session')
avgtime_day_df = pd.read_excel(excel_file, sheet_name='Avg Time Day')
retention_data_df = pd.read_excel(excel_file, sheet_name='Retention Data')
revenue_data_df = pd.read_excel(excel_file, sheet_name='Revenue Data')
ad_revenue_data_df = pd.read_excel(excel_file, sheet_name='Ad Revenue Data')

# Danh sách các game
games = game_info_df['game'].unique()

for game in games:
    game_info = game_info_df[game_info_df['game'] == game].iloc[0]
    user_up = user_up_df[user_up_df['game'] == game].iloc[0].drop('game').to_dict()
    users_country = users_country_df[users_country_df['game'] == game][['country', 'users']]
    avg_dau = avg_dau_df[avg_dau_df['game'] == game].iloc[0].drop('game').to_dict()
    active_users_country = active_users_country_df[active_users_country_df['game'] == game][['country', 'active_users']]
    products = products_df[products_df['game'] == game][['prd', 'price', 'tier', 'sales volume']].to_dict('records')
    selling_product = products_df[products_df['game'] == game]['prd'].unique().tolist()
    session = session_df[session_df['game'] == game][['day', 'session']].to_dict('records')
    avgtime_day = avgtime_day_df[avgtime_day_df['game'] == game][['day', 'avg']].to_dict('records')
    retention_data = retention_data_df[retention_data_df['game'] == game].drop('game', axis=1).to_dict('records')
    revenue_data = revenue_data_df[revenue_data_df['game'] == game].drop('game', axis=1).to_dict('records')
    ad_revenue_data = ad_revenue_data_df[ad_revenue_data_df['game'] == game].drop('game', axis=1).to_dict('records')

    users_country_dict = users_country.set_index('country')['users'].to_dict()
    active_users_country_dict = active_users_country.set_index('country')['active_users'].to_dict()

    # Chuyển đổi các giá trị số thành chuỗi
    user_up = {k: str(v) for k, v in user_up.items()}
    avg_dau = {k: str(v) for k, v in avg_dau.items()}

    data = {
        "game": game,
        "platform": game_info['platform'].split(','),
        "user_up": user_up,
        "users/country": users_country_dict,
        "avg_daily_active_user": avg_dau,
        "active_user/country": active_users_country_dict,
        "selling_product": selling_product,
        "products": products,
        "session": session,
        "avgtime/day": avgtime_day,
        "retention_data": retention_data,
        "revenue_data": revenue_data,
        "ad_revenue_data": ad_revenue_data,
        "user": str(game_info['user']),
        "today_revenue": str(game_info['today_revenue']),
        "request": str(game_info['request'])
    }

    collection.insert_one(data)

print("DONE!")
