from bs4 import BeautifulSoup

# HTML faylni yuklash
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Jadvalni topish
table = soup.find("table")

# Barcha qatorlarni olish
rows = table.find_all("tr")[1:]  # Sarlavha qatorini tashlab ketamiz

# Ma'lumotlarni saqlash uchun ro‘yxat
weather_data = []

# HTML dan ma'lumotlarni ajratib olish
for row in rows:
    cols = row.find_all("td")
    day = cols[0].text
    temp = int(cols[1].text.replace("°C", ""))  # Selsiy belgisi olib tashlanadi
    condition = cols[2].text
    weather_data.append({"day": day, "temperature": temp, "condition": condition})

# Ma'lumotlarni chop etish
print("📅 5 kunlik ob-havo ma'lumoti:")
for entry in weather_data:
    print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")

# Eng yuqori haroratli kunni topish
hottest_day = max(weather_data, key=lambda x: x["temperature"])
print(f"\n🔥 Eng issiq kun: {hottest_day['day']} ({hottest_day['temperature']}°C)")

# Quyoshli kunlarni topish
sunny_days = [entry["day"] for entry in weather_data if entry["condition"] == "Sunny"]
print(f"\n☀️ Quyoshli kunlar: {', '.join(sunny_days)}")

# O‘rtacha haroratni hisoblash
average_temp = sum(entry["temperature"] for entry in weather_data) / len(weather_data)
print(f"\n🌡 O'rtacha harorat: {average_temp:.2f}°C")
