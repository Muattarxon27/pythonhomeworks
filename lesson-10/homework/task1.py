import requests

# API ma'lumotlari
API_KEY = "YOUR_API_KEY"  # O'zingizning API kalitingizni shu joyga yozing
CITY = "Tashkent"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# API so'rovi yuborish
params = {"q": CITY, "appid": API_KEY, "units": "metric"}
response = requests.get(BASE_URL, params=params)

# Ma'lumotlarni chiqarish
if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print(f"🌤 Ob-havo ma'lumoti ({CITY}):")
    print(f"🌡 Harorat: {temp}°C")
    print(f"💧 Namlik: {humidity}%")
    print(f"🌦 Holat: {weather.capitalize()}")
else:
    print("❌ Ma'lumotni yuklashda xatolik yuz berdi!")