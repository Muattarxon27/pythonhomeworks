# Ikki to‘plamning birlashmasini hisoblovchi funksiya
def toplam_birlashma(toplam1, toplam2):
    return toplam1 | toplam2  # '|' operatori to‘plam birlashmasini hosil qiladi

# Misol uchun to‘plamlar
toplam_a = {1, 2, 3, 4}
toplam_b = {3, 4, 5, 6}

# Birlashma hosil qilish
natija = toplam_birlashma(toplam_a, toplam_b)

# Natijani chiqarish
print("To‘plamlarning birlashmasi:", natija)
# Ikki to‘plamning kesishmasini hisoblovchi funksiya
def toplam_kesishma(toplam1, toplam2):
    return toplam1 & toplam2  # '&' operatori to‘plam kesishmasini hosil qiladi

# Misol uchun to‘plamlar
toplam_a = {1, 2, 3, 4}
toplam_b = {3, 4, 5, 6}

# Kesishma hosil qilish
natija = toplam_kesishma(toplam_a, toplam_b)

# Natijani chiqarish
print("To‘plamlarning kesishmasi:", natija)
# Ikki to‘plamning farqini hisoblovchi funksiya
def toplam_farqi(toplam1, toplam2):
    return toplam1 - toplam2  # '-' operatori farqni hosil qiladi

# Misol uchun to‘plamlar
toplam_a = {1, 2, 3, 4, 5}
toplam_b = {3, 4, 6, 7}

# Farq hosil qilish
natija = toplam_farqi(toplam_a, toplam_b)

# Natijani chiqarish
print("To‘plamlarning farqi (A - B):", natija)
# To‘plamning quyi to‘plam ekanligini tekshiruvchi funksiya
def toplam_quyi(toplam1, toplam2):
    return toplam1.issubset(toplam2)  # .issubset() metodi quyi to‘plamni tekshiradi

# Misol uchun to‘plamlar
toplam_a = {1, 2, 3}
toplam_b = {1, 2, 3, 4, 5}

# Tekshirish
natija = toplam_quyi(toplam_a, toplam_b)

# Natijani chiqarish
print("A to‘plami B ning quyi to‘plami:", natija)

# Elementning to‘plam ichida borligini tekshiruvchi funksiya
def elementni_tekshir(toplam, element):
    return element in toplam  # 'in' operatori element mavjudligini tekshiradi

# Misol uchun to‘plam
toplam = {1, 2, 3, 4, 5}

# Tekshirilayotgan element
element = 3

# Tekshirish
natija = elementni_tekshir(toplam, element)

# Natijani chiqarish
print(f"{element} to‘plam ichida bormi? {natija}")

# To‘plam uzunligini (elementlar sonini) aniqlovchi funksiya
def toplam_uzunligi(toplam):
    return len(toplam)  # len() funksiyasi to‘plam elementlari sonini qaytaradi

# Misol uchun to‘plam
toplam = {1, 2, 3, 4, 5}

# Uzunlikni aniqlash
natija = toplam_uzunligi(toplam)

# Natijani chiqarish
print("To‘plamdagi unikal elementlar soni:", natija)
# Ro‘yxatni to‘plamga o‘girish funksiyasi
def royxatni_toplamga_aylantir(royxat):
    return set(royxat)  # set() funksiyasi takrorlanmalarni olib tashlaydi

# Misol uchun ro‘yxat
royxat = [1, 2, 3, 4, 5, 2, 3, 1]

# To‘plamga aylantirish
natija = royxatni_toplamga_aylantir(royxat)

# Natijani chiqarish
print("Ro‘yxatning unikal elementlardan iborat to‘plami:", natija)
# To‘plamdan elementni o‘chiruvchi funksiya
def elementni_ochir(toplam, element):
    toplam.discard(element)  # discard() elementi o‘chiradi, agar u mavjud bo‘lsa
    return toplam  # Yangilangan to‘plamni qaytaradi

# Misol uchun to‘plam
toplam = {1, 2, 3, 4, 5}

# O‘chiriladigan element
element = 3

# Elementni o‘chirish
natija = elementni_ochir(toplam, element)

# Natijani chiqarish
print("Yangilangan to‘plam:", natija)
# To‘plamni bo‘shatish funksiyasi
def toplamni_boshat(toplam):
    toplam.clear()  # clear() metodi to‘plamni tozalaydi
    return toplam  # Bo‘sh to‘plamni qaytaradi

# Misol uchun to‘plam
toplam = {1, 2, 3, 4, 5}

# To‘plamni bo‘shatish
natija = toplamni_boshat(toplam)

# Natijani chiqarish
print("Bo‘shatilgan to‘plam:", natija)

# To‘plam bo‘shligini tekshiruvchi funksiya
def toplam_boshmi(toplam):
    return len(toplam) == 0  # Agar uzunlik 0 bo‘lsa, True qaytaradi

# Misol uchun to‘plamlar
toplam1 = {1, 2, 3}
toplam2 = set()  # Bo‘sh to‘plam

# Tekshirish
print("To‘plam1 bo‘shmi?", toplam_boshmi(toplam1))  # False
print("To‘plam2 bo‘shmi?", toplam_boshmi(toplam2))  # True

# Simmetrik farqni topuvchi funksiya
def simmetrik_farq(toplam1, toplam2):
    return toplam1 ^ toplam2  # ^ operatori simmetrik farqni hisoblaydi

# Misol uchun ikkita to‘plam
toplam1 = {1, 2, 3, 4, 5}
toplam2 = {4, 5, 6, 7, 8}

# Simmetrik farqni topish
natija = simmetrik_farq(toplam1, toplam2)

# Natijani chiqarish
print("Simmetrik farq:", natija)
# To‘plamga element qo‘shuvchi funksiya
def element_qosh(toplam, element):
    toplam.add(element)  # add() metodi elementni qo‘shadi
    return toplam  # Yangilangan to‘plamni qaytaradi

# Misol uchun to‘plam
toplam = {1, 2, 3, 4, 5}

# Qo‘shiladigan element
element = 6

# Elementni qo‘shish
natija = element_qosh(toplam, element)

# Natijani chiqarish
print("Yangilangan to‘plam:", natija)
# To‘plamdan element olib tashlovchi funksiya
def element_ol(toplam):
    if toplam:  # Agar to‘plam bo‘sh bo‘lmasa
        return toplam.pop()  # pop() metodi tasodifiy elementni olib tashlaydi va qaytaradi
    else:
        return None  # Agar to‘plam bo‘sh bo‘lsa, None qaytaradi

# Misol uchun to‘plam
toplam = {1, 2, 3, 4, 5}

# Tasodifiy elementni olib tashlash
olingan_element = element_ol(toplam)

# Natijalarni chiqarish
print("Olingan element:", olingan_element)
print("Yangilangan to‘plam:", toplam)
# To‘plamdagi eng katta elementni topuvchi funksiya
def eng_katta_element(toplam):
    if toplam:  # Agar to‘plam bo‘sh bo‘lmasa
        return max(toplam)  # max() eng katta elementni qaytaradi
    else:
        return None  # Agar to‘plam bo‘sh bo‘lsa, None qaytaradi

# Misol uchun to‘plam
toplam = {3, 7, 2, 9, 5}

# Eng katta elementni topish
natija = eng_katta_element(toplam)

# Natijani chiqarish
print("Eng katta element:", natija)
# To‘plamdagi eng kichik elementni topuvchi funksiya
def eng_kichik_element(toplam):
    if toplam:  # Agar to‘plam bo‘sh bo‘lmasa
        return min(toplam)  # min() eng kichik elementni qaytaradi
    else:
        return None  # Agar to‘plam bo‘sh bo‘lsa, None qaytaradi

# Misol uchun to‘plam
toplam = {3, 7, 2, 9, 5}

# Eng kichik elementni topish
natija = eng_kichik_element(toplam)

# Natijani chiqarish
print("Eng kichik element:", natija)
# To‘plamdan faqat juft sonlarni ajratib oluvchi funksiya
def faqat_juft_sonlar(toplam):
    return {x for x in toplam if x % 2 == 0}  # Juft sonlarni tanlaymiz

# Misol uchun to‘plam
toplam = {3, 7, 2, 9, 4, 6, 8, 5}

# Yangi to‘plamni yaratish
juft_sonlar_toplami = faqat_juft_sonlar(toplam)

# Natijani chiqarish
print("Juft sonlar to‘plami:", juft_sonlar_toplami)
# To‘plamdan faqat toq sonlarni ajratib oluvchi funksiya
def faqat_toq_sonlar(toplam):
    return {x for x in toplam if x % 2 != 0}  # Toq sonlarni tanlaymiz

# Misol uchun to‘plam
toplam = {3, 7, 2, 9, 4, 6, 8, 5}

# Yangi to‘plamni yaratish
toq_sonlar_toplami = faqat_toq_sonlar(toplam)

# Natijani chiqarish
print("Toq sonlar to‘plami:", toq_sonlar_toplami)

# Berilgan diapazondagi sonlar to‘plamini yaratish funksiyasi
def diapazon_toplami(boshlanish, tugash):
    return set(range(boshlanish, tugash + 1))  # To‘plam yaratish

# Misol uchun diapazon
boshlanish = 1
tugash = 10

# Yangi to‘plamni yaratish
sonlar_toplami = diapazon_toplami(boshlanish, tugash)

# Natijani chiqarish
print("Diapazon bo‘yicha to‘plam:", sonlar_toplami)
# Ikkita ro‘yxatni birlashtirib, takrorlarni olib tashlaydigan funksiya
def birlashtir_va_yakuniy_toplam(royxat1, royxat2):
    return set(royxat1) | set(royxat2)  # To‘plamlar birlashuvi (union)

# Misol uchun ikkita ro‘yxat
royxat1 = [1, 2, 3, 4, 5, 5, 6]
royxat2 = [4, 5, 6, 7, 8, 9, 9]

# Yangi to‘plamni yaratish
yakuniy_toplam = birlashtir_va_yakuniy_toplam(royxat1, royxat2)

# Natijani chiqarish
print("Takrorlarsiz yangi to‘plam:", yakuniy_toplam)

# Ikkita ro‘yxatni birlashtirib, takrorlarni olib tashlaydigan funksiya
def birlashtir_va_yakuniy_toplam(royxat1, royxat2):
    return set(royxat1) | set(royxat2)  # To‘plamlar birlashuvi (union)

# Misol uchun ikkita ro‘yxat
royxat1 = [1, 2, 3, 4, 5, 5, 6]
royxat2 = [4, 5, 6, 7, 8, 9, 9]

# Yangi to‘plamni yaratish
yakuniy_toplam = birlashtir_va_yakuniy_toplam(royxat1, royxat2)

# Natijani chiqarish
print("Takrorlarsiz yangi to‘plam:", yakuniy_toplam)

# Ikki to‘plamning disjoint (kesishmaydigan) ekanligini tekshiradigan funksiya
def disjoint_tekshir(set1, set2):
    return set1.isdisjoint(set2)  # Agar umumiy element bo‘lmasa, True qaytaradi

# Misol uchun ikki to‘plam
toplam1 = {1, 2, 3, 4}
toplam2 = {5, 6, 7, 8}

# Tekshirish
natija = disjoint_tekshir(toplam1, toplam2)

# Natijani chiqarish
print("Toplamlar kesishmaydi:", natija)
# Ro‘yxatdan takroriy elementlarni olib tashlaydigan funksiya
def takrorlarni_olib_tashla(royxat):
    return list(set(royxat))  # To‘plam orqali unikal elementlarni saqlab, qayta ro‘yxatga aylantiramiz

# Misol uchun ro‘yxat
royxat = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# Yangi ro‘yxatni yaratish
yangi_royxat = takrorlarni_olib_tashla(royxat)

# Natijani chiqarish
print("Takrorlarsiz ro‘yxat:", yangi_royxat)

def takrorlarni_olib_tashla_tartib(royxat):
    return list(dict.fromkeys(royxat))

# Misol
royxat = [4, 2, 4, 3, 1, 2]
print(takrorlarni_olib_tashla_tartib(royxat))  # Natija: [4, 2, 3, 1]

# Ro‘yxatda nechta unikal element borligini hisoblaydigan funksiya
def unikal_elementlar_soni(royxat):
    return len(set(royxat))  # To‘plam faqat unikal elementlarni saqlaydi, len() esa sonini qaytaradi

# Misol uchun ro‘yxat
royxat = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# Unikal elementlar sonini topish
soni = unikal_elementlar_soni(royxat)

# Natijani chiqarish
print("Unikal elementlar soni:", soni)
import random  # Tasodifiy sonlar yaratish uchun kutubxona

# Tasodifiy to‘plam yaratish funksiyasi
def tasodifiy_toplam_yarat(soni, boshi, oxir):
    return set(random.randint(boshi, oxir) for _ in range(soni))

# Misol uchun tasodifiy to‘plam yaratamiz
tasodifiy_toplam = tasodifiy_toplam_yarat(5, 1, 20)  # 1 dan 20 gacha bo‘lgan 5 ta son

# Natijani chiqarish
print("Tasodifiy toplam:", tasodifiy_toplam)
