import os
from bs4 import BeautifulSoup
from tabulate import tabulate

# HTML fayl mavjudligini tekshirish
if not os.path.exists("weather.html"):
    print("❌ Xatolik: 'weather.html' fayli topilmadi!")
    exit()

# HTML faylni yuklash
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Jadvalni topish
table = soup.find("table")
if not table:
    print("❌ Xatolik: Jadval topilmadi!")
    exit()

# Barcha qatorlarni olish
rows = table.find_all("tr")[1:]  # Sarlavha qatorini tashlab ketamiz

# Ma'lumotlarni saqlash uchun ro‘yxat
weather_data = []

# HTML dan ma'lumotlarni ajratib olish
for row in rows:
    cols = row.find_all("td")
    if len(cols) < 3:
        continue  # Agar qator to'liq bo'lmasa, uni o'tkazib yuboramiz
    day = cols[0].text.strip()
    temp_text = cols[1].text.strip().replace("°C", "")
    condition = cols[2].text.strip()
    
    # Sonni olish va xatolikni oldini olish
    try:
        temp = int(temp_text)
    except ValueError:
        print(f"⚠️ Ogohlantirish: '{day}' uchun harorat noto‘g‘ri formatda!")
        continue
    
    weather_data.append({"day": day, "temperature": temp, "condition": condition})

# Ma'lumotlarni chiroyli formatda chop etish
print("\n📅 5 kunlik ob-havo ma'lumoti:")
headers = ["Day", "Temperature (°C)", "Condition"]
table_data = [[entry["day"], entry["temperature"], entry["condition"]] for entry in weather_data]
print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Eng yuqori haroratli kunni topish
if weather_data:
    hottest_day = max(weather_data, key=lambda x: x["temperature"])
    print(f"\n🔥 Eng issiq kun: {hottest_day['day']} ({hottest_day['temperature']}°C)")

    # Quyoshli kunlarni topish
    sunny_days = [entry["day"] for entry in weather_data if entry["condition"].lower() == "sunny"]
    if sunny_days:
        print(f"\n☀️ Quyoshli kunlar: {', '.join(sunny_days)}")
    else:
        print("\n☀️ Quyoshli kun yo‘q.")

    # O‘rtacha haroratni hisoblash
    average_temp = sum(entry["temperature"] for entry in weather_data) / len(weather_data)
    print(f"\n🌡 O'rtacha harorat: {average_temp:.2f}°C")
else:
    print("\n❌ Xatolik: Hech qanday ob-havo ma'lumoti topilmadi.")
