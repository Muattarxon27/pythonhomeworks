def tekshirish(foydalanuvchi_nomi, parol):
    if not foydalanuvchi_nomi:
        print("Foydalanuvchi nomi bo'sh bo'lishi mumkin emas.")
        return
    if not parol:
        print("Parol bo'sh bo'lishi mumkin emas.")
        return
    print("Kirish muvaffaqiyatli!")

# Foydalanuvchi ma'lumotlarini olish
foydalanuvchi_nomi = input("Foydalanuvchi nomini kiriting: ")
parol = input("Parolni kiriting: ")

# Ma'lumotlarni tekshirish
tekshirish(foydalanuvchi_nomi, parol)
def tekshirish(foydalanuvchi_nomi, parol):
    if not foydalanuvchi_nomi:
        print("Foydalanuvchi nomi bo'sh bo'lishi mumkin emas.")
        return
    if not parol:
        print("Parol bo'sh bo'lishi mumkin emas.")
        return
    print("Kirish muvaffaqiyatli!")

# Foydalanuvchi ma'lumotlarini olish
foydalanuvchi_nomi = input("Foydalanuvchi nomini kiriting: ")
parol = input("Parolni kiriting: ")

# Ma'lumotlarni tekshirish
tekshirish(foydalanuvchi_nomi, parol)
def son_tekshirish(son):
    if son > 0 and son % 2 == 0:
        print("Berilgan son musbat va juft.")
    else:
        print("Berilgan son musbat juft emas yoki manfiy.")

# Foydalanuvchidan son kiritishni so'rash
son = int(input("Son kiriting: "))
son_tekshirish(son)
def uchta_son_tekshirish(son1, son2, son3):
    if son1 != son2 and son1 != son3 and son2 != son3:
        print("Barcha uchta son bir-biridan farq qiladi.")
    else:
        print("Ba'zi sonlar bir-biriga teng.")

# Foydalanuvchidan uchta son kiritishni so'rash
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))
uchta_son_tekshirish(son1, son2, son3)
def matn_uzunlik_tekshirish(matn1, matn2):
    if len(matn1) == len(matn2):
        print("Berilgan ikkita matn uzunligi teng.")
    else:
        print("Berilgan ikkita matn uzunligi har xil.")

# Foydalanuvchidan ikkita matn kiritishni so'rash
matn1 = input("Birinchi matnni kiriting: ")
matn2 = input("Ikkinchi matnni kiriting: ")
matn_uzunlik_tekshirish(matn1, matn2)
# Sonning 3 va 5 ga bo‘linishini tekshirish
def bolinuvchanlik_tekshirish(son):
    if son % 3 == 0 and son % 5 == 0:
        print("Berilgan son 3 va 5 ga bo‘linadi.")
    else:
        print("Berilgan son 3 va 5 ga bo‘linmaydi.")

# Foydalanuvchidan son kiritishni so‘rash
son = int(input("Son kiriting: "))
bolinuvchanlik_tekshirish(son)
# Ikkita son yig‘indisini tekshirish
def yigindi_tekshirish(son1, son2):
    if son1 + son2 > 50.8:
        print("Berilgan ikkita son yig‘indisi 50.8 dan katta.")
    else:
        print("Berilgan ikkita son yig‘indisi 50.8 dan kichik yoki teng.")

# Foydalanuvchidan ikkita son kiritishni so‘rash
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
yigindi_tekshirish(son1, son2)
# Sonning 10 va 20 oralig‘ida ekanligini tekshirish
def oraliq_tekshirish(son):
    if 10 <= son <= 20:
        print("Berilgan son 10 va 20 orasida joylashgan.")
    else:
        print("Berilgan son 10 va 20 orasida emas.")

# Foydalanuvchidan son kiritishni so‘rash
son = int(input("Son kiriting: "))
oraliq_tekshirish(son)