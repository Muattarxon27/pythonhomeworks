# Ikki to‘plamni birlashtirish funksiyasi
def toplam_birlashtir(toplam1, toplam2):
    return toplam1.union(toplam2)  # .union() metodi ikkala to‘plamni birlashtiradi

# Misol uchun ikki to‘plam
toplam_a = {1, 2, 3, 4}
toplam_b = {3, 4, 5, 6}

# To‘plamlarni birlashtirish
yangi_toplam = toplam_birlashtir(toplam_a, toplam_b)

# Natijani chiqarish
print("Birlashtirilgan to‘plam:", yangi_toplam)

# Ikki to‘plamning kesishmasini topish funksiyasi
def toplam_kesishma(toplam1, toplam2):
    return toplam1.intersection(toplam2)  # .intersection() metodi faqat umumiy elementlarni saqlaydi

# Misol uchun ikki to‘plam
toplam_a = {1, 2, 3, 4}
toplam_b = {3, 4, 5, 6}

# To‘plamlarning kesishmasini topish
yangi_toplam = toplam_kesishma(toplam_a, toplam_b)

# Natijani chiqarish
print("Kesishma to‘plam:", yangi_toplam)
# Ikki to‘plamning farqini topish funksiyasi
def toplam_faqr(toplam1, toplam2):
    return toplam1.difference(toplam2)  # .difference() metodi faqat 1-to‘plamda bor, lekin 2-to‘plamda yo‘q elementlarni saqlaydi

# Misol uchun ikki to‘plam
toplam_a = {1, 2, 3, 4, 5}
toplam_b = {3, 4, 6, 7}

# Farqni topish
yangi_toplam = toplam_faqr(toplam_a, toplam_b)

# Natijani chiqarish
print("Farqli elementlar to‘plami:", yangi_toplam)

# To‘plamning quyi to‘plam ekanligini tekshiruvchi funksiya
def quyi_toplammi(toplam1, toplam2):
    return toplam1.issubset(toplam2)  # .issubset() metodi toplam1, toplam2 ichida bo‘lsa True qaytaradi

# Misol uchun ikki to‘plam
toplam_a = {1, 2, 3}
toplam_b = {1, 2, 3, 4, 5}

# Tekshirish
natija = quyi_toplammi(toplam_a, toplam_b)

# Natijani chiqarish
print("toplam_a, toplam_b ning quyi to‘plami:", natija)

# To‘plam ichida element borligini tekshiruvchi funksiya
def element_bormi(toplam, element):
    return element in toplam  # Agar element toplam ichida bo‘lsa, True qaytaradi

# Misol uchun to‘plam
toplam = {1, 2, 3, 4, 5}

# Tekshirish
element = 3
natija = element_bormi(toplam, element)

# Natijani chiqarish
print(f"{element} to‘plam ichida bormi?:", natija)

# To‘plam uzunligini aniqlovchi funksiya
def toplam_uzunligi(toplam):
    return len(toplam)  # len() metodi to‘plamdagi elementlar sonini qaytaradi

# Misol uchun to‘plam
toplam = {1, 2, 3, 4, 5}

# Uzunligini aniqlash
natija = toplam_uzunligi(toplam)

# Natijani chiqarish
print("To‘plamdagi unikal elementlar soni:", natija)

# Ro‘yxatni to‘plamga o‘tkazuvchi funksiya
def royxatdan_toplam(royxat):
    return set(royxat)  # set() funksiyasi faqat unikal elementlarni qoldiradi

# Misol uchun ro‘yxat
royxat = [1, 2, 2, 3, 4, 4, 5, 5, 5]

# To‘plamga aylantirish
natija = royxatdan_toplam(royxat)

# Natijani chiqarish
print("Unikal elementlardan iborat to‘plam:", natija)
# To‘plamdan elementni olib tashlash funksiyasi
def elementni_ochir(toplam, element):
    toplam.discard(element)  # discard() funksiyasi element bo‘lsa o‘chiradi, bo‘lmasa xatolik chiqarmaydi
    return toplam  # Yangilangan to‘plamni qaytaradi

# Misol uchun to‘plam
toplam = {1, 2, 3, 4, 5}

# O‘chirish uchun element
element = 3

# Elementni olib tashlash
natija = elementni_ochir(toplam, element)

# Natijani chiqarish
print("Yangilangan to‘plam:", natija)

# To‘plamni tozalash funksiyasi
def toplamni_tozalash(toplam):
    toplam.clear()  # clear() metodi barcha elementlarni o‘chiradi
    return toplam  # Bo‘sh to‘plamni qaytaradi

# Misol uchun to‘plam
toplam = {1, 2, 3, 4, 5}

# To‘plamni tozalash
natija = toplamni_tozalash(toplam)

# Natijani chiqarish
print("Tozalangan to‘plam:", natija)

# To‘plam bo‘sh yoki yo‘qligini tekshiruvchi funksiya
def toplam_boshmi(toplam):
    return len(toplam) == 0  # Agar uzunligi 0 bo‘lsa, bo‘sh hisoblanadi

# Misollar uchun to‘plamlar
toplam1 = {1, 2, 3}
toplam2 = set()  # Bo‘sh to‘plam

# Natijalarni chiqarish
print("toplam1 bo‘shmi?", toplam_boshmi(toplam1))  # False
print("toplam2 bo‘shmi?", toplam_boshmi(toplam2))  # True
# Simmetrik farqni hisoblash funksiyasi
def simmetrik_farq(toplam1, toplam2):
    return toplam1 ^ toplam2  # ^ operatori simmetrik farqni topish uchun ishlatiladi

# Misol uchun ikkita to‘plam
toplam1 = {1, 2, 3, 4}
toplam2 = {3, 4, 5, 6}

# Simmetrik farqni topish
natija = simmetrik_farq(toplam1, toplam2)

# Natijani chiqarish
print("Simmetrik farq:", natija)


# To‘plamga element qo‘shish funksiyasi
def element_qosh(toplam, element):
    toplam.add(element)  # .add() metodi elementni qo‘shadi
    return toplam

# Misol uchun to‘plam va yangi element
toplam = {1, 2, 3}
yangi_element = 4

# Element qo‘shish
natija = element_qosh(toplam, yangi_element)

# Natijani chiqarish
print("Yangi to‘plam:", natija)

# To‘plamdan elementni olib tashlash funksiyasi
def element_ol(toplam):
    if toplam:  # To‘plam bo‘sh emasligini tekshiramiz
        return toplam.pop()  # .pop() tasodifiy elementni o‘chiradi va qaytaradi
    else:
        return "To‘plam bo‘sh, hech narsa olib bo‘lmaydi!"

# Misol uchun to‘plam
toplam = {1, 2, 3, 4, 5}

# Tasodifiy elementni olib tashlash
ochirilgan_element = element_ol(toplam)

# Natijani chiqarish
print("Olib tashlangan element:", ochirilgan_element)
print("Yangi toplam:", toplam)
# To‘plamdagi eng katta elementni topish funksiyasi
def eng_katta_element(toplam):
    if toplam:  # To‘plam bo‘sh emasligini tekshiramiz
        return max(toplam)  # max() eng katta elementni qaytaradi
    else:
        return "To‘plam bo‘sh, eng katta element yo‘q!"

# Misol uchun to‘plam
toplam = {10, 25, 8, 14, 30}

# Eng katta elementni topish
natija = eng_katta_element(toplam)

# Natijani chiqarish
print("Eng katta element:", natija)
# To‘plamdagi eng kichik elementni topish funksiyasi
def eng_kichik_element(toplam):
    if toplam:  # To‘plam bo‘sh emasligini tekshiramiz
        return min(toplam)  # min() eng kichik elementni qaytaradi
    else:
        return "To‘plam bo‘sh, eng kichik element yo‘q!"

# Misol uchun to‘plam
toplam = {10, 25, 8, 14, 30}

# Eng kichik elementni topish
natija = eng_kichik_element(toplam)

# Natijani chiqarish
print("Eng kichik element:", natija)

# To‘plamdagi faqat juft sonlarni tanlab olish funksiyasi
def faqat_juft_sonlar(toplam):
    return {x for x in toplam if x % 2 == 0}  # Juft sonlarni yangi to‘plamga yig‘amiz

# Misol uchun to‘plam
toplam = {10, 25, 8, 14, 30, 17, 9}

# Juft sonlarni ajratib olish
natija = faqat_juft_sonlar(toplam)

# Natijani chiqarish
print("Juft sonlar to‘plami:", natija)

# To‘plamdagi faqat toq sonlarni tanlab olish funksiyasi
def faqat_toq_sonlar(toplam):
    return {x for x in toplam if x % 2 != 0}  # Toq sonlarni yangi to‘plamga yig‘amiz

# Misol uchun to‘plam
toplam = {10, 25, 8, 14, 30, 17, 9}

# Toq sonlarni ajratib olish
natija = faqat_toq_sonlar(toplam)

# Natijani chiqarish
print("Toq sonlar to‘plami:", natija)

# Berilgan oraliqdagi sonlardan to‘plam yaratish funksiyasi
def oraliq_toplam(bosh, oxirgi):
    return set(range(bosh, oxirgi + 1))  # Toplam yaratamiz

# Misol: 1 dan 10 gacha bo‘lgan sonlardan iborat to‘plam
natija = oraliq_toplam(1, 10)

# Natijani chiqarish
print("Hosil bo'lgan to'plam:", natija)

# Ikki ro‘yxatni birlashtirib, takroriy elementlarni olib tashlash funksiyasi
def birlashtir_va_unikal(qator1, qator2):
    return set(qator1) | set(qator2)  # To‘plamlar birlashuvi orqali unikal elementlarni olish

# Misol: Ikkita ro‘yxat
list1 = [1, 2, 3, 4, 5, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

# Funksiyani chaqirish
natija = birlashtir_va_unikal(list1, list2)

# Natijani chiqarish
print("Birlashtirilgan va unikal elementlardan iborat toplam:", natija)

# Ikki to‘plamning o‘zaro kesishmasligini tekshirish funksiyasi
def disjoint_tekshir(toplam1, toplam2):
    return toplam1.isdisjoint(toplam2)  # Agar umumiy element bo‘lmasa, True qaytaradi

# Misol: Ikkita to‘plam
toplam1 = {1, 2, 3, 4}
toplam2 = {5, 6, 7, 8}

# Funksiyani chaqirish
natija = disjoint_tekshir(toplam1, toplam2)

# Natijani chiqarish
print("To‘plamlar kesishmaydi:", natija)

# Ro‘yxatdan dublikatlarni olib tashlash funksiyasi
def dublikatlarni_olib_tashla(royxat):
    return list(set(royxat))  # Ro‘yxatni to‘plamga o‘tkazib, yana ro‘yxatga aylantiramiz

# Misol: Dublikatlari bor ro‘yxat
royxat = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]

# Funksiyani chaqirish
yangi_royxat = dublikatlarni_olib_tashla(royxat)

# Natijani chiqarish
print("Dublikatlarsiz ro‘yxat:", yangi_royxat)

# Ro‘yxatdagi noyob elementlar sonini aniqlovchi funksiya
def unikal_elementlar_soni(royxat):
    return len(set(royxat))  # Ro‘yxatni to‘plamga o‘tkazib, uzunligini qaytaramiz

# Misol: Dublikatlari bor ro‘yxat
royxat = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]

# Funksiyani chaqirish
natija = unikal_elementlar_soni(royxat)

# Natijani chiqarish
print("Noyob elementlar soni:", natija)

import random  # Tasodifiy sonlar generatsiya qilish uchun modul

# Tasodifiy to‘plam yaratish funksiyasi
def tasodifiy_toplam(yigindi, min_son, max_son):
    return set(random.randint(min_son, max_son) for _ in range(yigindi))

# Misol: 5 ta tasodifiy sonni 1 dan 100 gacha bo‘lgan oraliqda yaratish
natija = tasodifiy_toplam(5, 1, 100)

# Natijani chiqarish
print("Tasodifiy to‘plam:", natija)

