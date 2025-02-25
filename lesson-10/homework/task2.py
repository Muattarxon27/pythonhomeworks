import requests
import random

# API ma'lumotlari
API_KEY = "YOUR_API_KEY"  # O'zingizning API kalitingizni shu joyga yozing
BASE_URL = "https://api.themoviedb.org/3"

# Barcha janrlarni olish
def get_genres():
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        genres = response.json()["genres"]
        return {genre["name"].lower(): genre["id"] for genre in genres}
    else:
        print("❌ Janrlarni yuklab bo‘lmadi!")
        return {}

# Berilgan janrdagi filmlarni olish
def get_movies_by_genre(genre_id):
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json()["results"]
        return movies
    else:
        print("❌ Filmlar yuklanmadi!")
        return []

# Foydalanuvchidan janr so‘rash va tasodifiy film tavsiya qilish
def recommend_movie():
    genres = get_genres()
    if not genres:
        return
    
    user_genre = input("🎬 Qaysi janrdagi filmni xohlaysiz? ").lower()

    if user_genre in genres:
        genre_id = genres[user_genre]
        movies = get_movies_by_genre(genre_id)
        
        if movies:
            random_movie = random.choice(movies)
            print("\n🎥 Sizga tavsiya qilingan film:")
            print(f"📌 Nomi: {random_movie['title']}")
            print(f"📆 Chiqarilgan yili: {random_movie['release_date']}")
            print(f"⭐ Reyting: {random_movie['vote_average']}")
            print(f"📖 Tavsif: {random_movie['overview']}\n")
        else:
            print("❌ Bu janrda film topilmadi!")
    else:
        print("❌ Bunday janr mavjud emas!")

# Dastur ishga tushiriladi
recommend_movie()