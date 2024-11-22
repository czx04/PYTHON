# đang bị lỗi k nhận file @@ dash lỏ

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
from pymongo import MongoClient
import base64
import io

# Kết nối tới MongoDB
def get_mongo_client():
    mongo_uri = 'mongodb+srv://anhchaiuem:anhchaiuem@pep.ghbx8ax.mongodb.net/?retryWrites=true&w=majority&appName=PEP'
    return MongoClient(mongo_uri)
def upload_layout():
    return html.Div([
        html.H1("Tải lên File Excel và Nhập vào MongoDB"),
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Kéo và thả hoặc ',
                html.A('chọn file')
            ]),
            style={
                'width': '50%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '20px auto'
            },
            multiple=False
        ),
        html.Div(id='output-data-upload')
    ], style={'textAlign': 'center'})

def parse_contents(contents, filename):
    print(f"Bắt đầu xử lý file: {filename}")
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        # Đọc tất cả các sheet từ file Excel
        excel_file = io.BytesIO(decoded)
        excel_data = pd.read_excel(excel_file, sheet_name=None)

        # In ra danh sách các sheet để kiểm tra
        print(f"Các sheet có trong file: {list(excel_data.keys())}")

        # Kiểm tra xem các sheet cần thiết có tồn tại không
        required_sheets = ['Game Info', 'User Up', 'Users_Country', 'Avg Daily Active User',
                           'ActiveUserCountry', 'Products', 'Session', 'Avg Time Day',
                           'Retention Data', 'Revenue Data', 'Ad Revenue Data']

        for sheet in required_sheets:
            if sheet not in excel_data:
                raise ValueError(f"Sheet '{sheet}' không tồn tại trong file Excel.")

        # Lấy dữ liệu từ từng sheet
        game_info_df = excel_data['Game Info']
        user_up_df = excel_data['User Up']
        users_country_df = excel_data['Users_Country']
        avg_dau_df = excel_data['Avg Daily Active User']
        active_users_country_df = excel_data['ActiveUserCountry']
        products_df = excel_data['Products']
        session_df = excel_data['Session']
        avgtime_day_df = excel_data['Avg Time Day']
        retention_data_df = excel_data['Retention Data']
        revenue_data_df = excel_data['Revenue Data']
        ad_revenue_data_df = excel_data['Ad Revenue Data']

        # Danh sách các game
        games = game_info_df['game'].unique()
        print(f"Danh sách các game: {games}")

        # Kết nối tới MongoDB
        client = get_mongo_client()
        db = client['overview']
        collection = db['test']

        # Xử lý và nhập dữ liệu vào MongoDB
        for game in games:
            print(f"Đang xử lý game: {game}")
            # Lọc dữ liệu cho game hiện tại
            game_info = game_info_df[game_info_df['game'] == game].iloc[0]
            user_up = user_up_df[user_up_df['game'] == game].iloc[0].drop('game').to_dict()
            users_country = users_country_df[users_country_df['game'] == game][['country', 'users']]
            avg_dau = avg_dau_df[avg_dau_df['game'] == game].iloc[0].drop('game').to_dict()
            active_users_country = active_users_country_df[active_users_country_df['game'] == game][['country', 'active_users']]
            products = products_df[products_df['game'] == game][['prd', 'price', 'tier', 'sales_volume']].to_dict('records')
            selling_product = products_df[products_df['game'] == game]['prd'].unique().tolist()
            session = session_df[session_df['game'] == game][['day', 'session']].to_dict('records')
            avgtime_day = avgtime_day_df[avgtime_day_df['game'] == game][['day', 'avg']].to_dict('records')
            retention_data = retention_data_df[retention_data_df['game'] == game].drop('game', axis=1).to_dict('records')
            revenue_data = revenue_data_df[revenue_data_df['game'] == game].drop('game', axis=1).to_dict('records')
            ad_revenue_data = ad_revenue_data_df[ad_revenue_data_df['game'] == game].drop('game', axis=1).to_dict('records')

            # Chuyển đổi users_country và active_users_country thành dictionary
            users_country_dict = users_country.set_index('country')['users'].to_dict()
            active_users_country_dict = active_users_country.set_index('country')['active_users'].to_dict()

            # Chuyển đổi các giá trị số thành chuỗi (nếu cần thiết)
            user_up = {k: str(v) for k, v in user_up.items()}
            avg_dau = {k: str(v) for k, v in avg_dau.items()}

            # Tạo document để nhập vào MongoDB
            data = {
                "game": game,
                "platform": str(game_info['platform']).split(','),
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

            # Nhập dữ liệu vào MongoDB
            collection.insert_one(data)
            print(f"Đã nhập dữ liệu cho game: {game}")

        # Đóng kết nối MongoDB
        client.close()

        return html.Div([
            html.H5(f"File '{filename}' đã được xử lý và dữ liệu đã được nhập vào MongoDB thành công."),
        ])
    except Exception as e:
        print(f"Lỗi khi xử lý file {filename}: {e}")
        return html.Div([
            html.H5(f"Có lỗi xảy ra khi xử lý file '{filename}': {str(e)}")
        ])

def register_callbacks(app):
    @app.callback(Output('output-data-upload', 'children'),
                  Input('upload-data-upload', 'contents'),
                  State('upload-data-upload', 'filename'),
                  prevent_initial_call=True)
    def update_output(contents, filename):
        if contents is not None:
            print("Callback update_output được gọi")
            print(f"Đã nhận được file: {filename}")
            return parse_contents(contents, filename)
        else:
            print("Không có nội dung file")
            return html.Div([
                html.H5("Không có file nào được tải lên.")
            ])
