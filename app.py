from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Авторизация в Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Открываем таблицу (замени на название своего файла)
sheet = client.open("Название_Твоей_Таблицы").sheet1

@app.route('/get_schedule', methods=['POST'])
def get_schedule():
    data = request.json
    course_name = data.get("course")

    # Ищем курс в таблице
    records = sheet.get_all_records()
    for row in records:
        if row["з"] == course_name:
            return jsonify({"schedule": row["Расписание курса"]})

    return jsonify({"error": "Ошибка"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
