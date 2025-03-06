import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Seleniumni sozlash
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Brauzerni fon rejimida ochish
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Demoblaze saytini ochish
driver.get("https://www.demoblaze.com")
time.sleep(3)  # Sahifa yuklanishi uchun kutish

# Laptops bo‘limiga o'tish
laptop_section = driver.find_element(By.LINK_TEXT, "Laptops")
laptop_section.click()
time.sleep(3)

# Ma'lumotlarni yig'ish uchun bo'sh ro‘yxat
laptops = []

# Sahifalarni ko‘rib chiqish
while True:
    time.sleep(3)  # Sahifa yuklanishini kutish
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # Har bir laptop kartasini topish
    items = soup.find_all("div", class_="card-block")
    
    for item in items:
        name = item.find("h4", class_="card-title").text.strip()
        price = item.find("h5").text.strip()
        description = item.find("p", class_="card-text").text.strip()
        
        laptops.append({
            "name": name,
            "price": price,
            "description": description
        })

    # "Next" tugmachasini bosish
    try:
        next_button = driver.find_element(By.LINK_TEXT, "Next")
        next_button.click()
    except:
        break  # Agar "Next" tugmachasi bo‘lmasa, siklni to‘xtatish

# JSON faylga saqlash
with open("laptops.json", "w", encoding="utf-8") as file:
    json.dump(laptops, file, indent=4, ensure_ascii=False)

# Brauzerni yopish
driver.quit()

print("✅ Ma'lumotlar 'laptops.json' fayliga saqlandi!")
