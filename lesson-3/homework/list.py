def sum_of_elements(numbers):
    return sum(numbers)

# Example usage
numbers = [1, 2, 3, 4, 5]  # You can change this list
total = sum_of_elements(numbers)

# Print result
print("Sum of elements:", total)

def eng_katta_element(sonlar):
    return max(sonlar)

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 47]  # Istalgan sonlarni kiritish mumkin
eng_katta = eng_katta_element(sonlar)

# Natijani chiqarish
print("Eng katta element:", eng_katta)
def eng_kichik_element(sonlar):
    return min(sonlar)

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 47]  # Istalgan sonlarni kiritish mumkin
eng_kichik = eng_kichik_element(sonlar)

# Natijani chiqarish
print("Eng kichik element:", eng_kichik)

def elementni_tekshirish(sonlar, element):
    return element in sonlar

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 47]  # Istalgan sonlarni kiritish mumkin
element = 25  # Qidirilayotgan elementni shu yerda o‘zgartirish mumkin

# Natijani chiqarish
if elementni_tekshirish(sonlar, element):
    print(f"{element} ro‘yxatda bor.")
else:
    print(f"{element} ro‘yxatda yo‘q.")
    
def birinchi_element(sonlar):
    if len(sonlar) > 0:
        return sonlar[0]
    else:
        return "Ro‘yxat bo‘sh!"

# Misol uchun ro‘yxatlar
sonlar = [10, 25, 3, 99, 47]  # Istalgan sonlarni kiritish mumkin
# sonlar = []  # Bo‘sh ro‘yxatni tekshirish uchun shu qatordan foydalaning

# Natijani chiqarish
print("Birinchi element:", birinchi_element(sonlar))

def uchta_birinchi_element(sonlar):
    return sonlar[:3]  # Ro‘yxatning 0-dan 3-gacha bo‘lgan qismini ajratib oladi

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 47]  # Istalgan sonlarni kiritish mumkin

# Natijani chiqarish
yangi_royxat = uchta_birinchi_element(sonlar)
print("Yangi ro‘yxat (birinchi 3 ta element):", yangi_royxat)

def teskari_royxat(sonlar):
    return sonlar[::-1]  # Ro‘yxatni teskari o‘giradi

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 47]  # Istalgan sonlarni kiritish mumkin

# Natijani chiqarish
teskari = teskari_royxat(sonlar)
print("Teskari ro‘yxat:", teskari)

# Ro‘yxatni tartiblangan holda qaytaruvchi funksiya
def tartiblangan_royxat(sonlar):
    return sorted(sonlar)  # Ro‘yxatni o‘sish tartibida saralaydi

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 47]  # Istalgan sonlarni kiritish mumkin

# Natijani chiqarish
yangi_royxat = tartiblangan_royxat(sonlar)
print("Tartiblangan ro‘yxat:", yangi_royxat)

def noyob_elementlar(sonlar):
    return list(set(sonlar))  # Ro‘yxatni to‘plam (set) ga aylantirib, takrorlarni olib tashlaydi

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 47, 25, 10, 3]  # Takroriy elementlar bor

# Natijani chiqarish
yangi_royxat = noyob_elementlar(sonlar)
print("Takrorlanmas elementlar ro‘yxati:", yangi_royxat)

def element_qoshish(sonlar, indeks, element):
    sonlar.insert(indeks, element)  # Berilgan indeksga element qo‘shish
    return sonlar

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 47]  # Asosiy ro‘yxat
indeks = 2  # Element qo‘shish kerak bo‘lgan joy
yangi_element = 50  # Qo‘shiladigan element

# Natijani chiqarish
yangi_royxat = element_qoshish(sonlar, indeks, yangi_element)
print("Yangi ro‘yxat:", yangi_royxat)

def element_indeksi(sonlar, element):
    if element in sonlar:
        return sonlar.index(element)  # Elementning indeksini qaytaradi
    else:
        return "Element ro‘yxatda yo‘q!"

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 47, 25, 3]  # Asosiy ro‘yxat
qidirilayotgan_element = 25 # Indeksi topiladigan element

# Natijani chiqarish
indeks = element_indeksi(sonlar, qidirilayotgan_element)
print(f"{qidirilayotgan_element} elementining indeksi:", indeks)

# Ro‘yxat bo‘sh yoki yo‘qligini tekshiruvchi funksiya
def royxat_boshmi(sonlar):
    return len(sonlar) == 0  # Ro‘yxat uzunligi 0 ga teng bo‘lsa, True qaytaradi

# Misol uchun ro‘yxatlar
sonlar1 = [10, 25, 3]  # To‘ldirilgan ro‘yxat
sonlar2 = []  # Bo‘sh ro‘yxat

# Natijani chiqarish
print("Ro‘yxat 1 bo‘shmi?", royxat_boshmi(sonlar1))  # False qaytaradi
print("Ro‘yxat 2 bo‘shmi?", royxat_boshmi(sonlar2))  # True qaytaradi

# Ro‘yxatda nechta juft son borligini hisoblovchi funksiya
def juft_sonlar_soni(sonlar):
    return sum(1 for son in sonlar if son % 2 == 0)  # Har bir juft son uchun 1 qo‘shib boradi

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 48, 50, 12]  # Juft va toq sonlar bor

# Natijani chiqarish
juftlar_soni = juft_sonlar_soni(sonlar)
print("Ro‘yxatda", juftlar_soni, "ta juft son bor.")
# Ro‘yxatda nechta toq son borligini hisoblovchi funksiya
def toq_sonlar_soni(sonlar):
    return sum(1 for son in sonlar if son % 2 != 0)  # Har bir toq son uchun 1 qo‘shib boradi

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 48, 50, 12]  # Juft va toq sonlar bor

# Natijani chiqarish
toq_sonlar = toq_sonlar_soni(sonlar)
print("Ro‘yxatda", toq_sonlar, "ta toq son bor.")

# Ikkita ro‘yxatni birlashtiruvchi funksiya
def royxat_birlash(royxat1, royxat2):
    return royxat1 + royxat2  # Ro‘yxatlarni qo‘shish orqali birlashtiradi

# Misol uchun ro‘yxatlar
royxat1 = [1, 2, 3]
royxat2 = [4, 5, 6]

# Natijani chiqarish
yangi_royxat = royxat_birlash(royxat1, royxat2)
print("Birlashgan ro‘yxat:", yangi_royxat)


# Ro‘yxatda subro‘yxat mavjudligini tekshiruvchi funksiya
def subroyxat_bormi(royxat, subroyxat):
    n, m = len(royxat), len(subroyxat)
    
    # Agar subro‘yxat uzunligi asosiy ro‘yxatdan katta bo‘lsa, mavjud emas
    if m > n:
        return False  

    # Har bir indeksdan boshlab subro‘yxatni tekshiramiz
    for i in range(n - m + 1):
        if royxat[i:i + m] == subroyxat:
            return True  # Agar mos keladigan qism topilsa, True qaytariladi
            
    return False  # Agar hech qanday moslik topilmasa, False qaytariladi

# Misol uchun ro‘yxatlar
asosiy_royxat = [1, 2, 3, 4, 5, 6, 7, 8]
kichik_royxat = [3, 4, 5]

# Natijani chiqarish
natija = subroyxat_bormi(asosiy_royxat, kichik_royxat)
print("Subro‘yxat mavjudmi?", natija)
# Ro‘yxatda birinchi uchragan elementni almashtiruvchi funksiya
def element_almashtirish(royxat, eski_element, yangi_element):
    if eski_element in royxat:  # Agar element ro‘yxatda bo‘lsa
        indeks = royxat.index(eski_element)  # Uning indeksini topamiz
        royxat[indeks] = yangi_element  # O‘sha indeksdagi elementni almashtiramiz
    return royxat  # Yangilangan ro‘yxatni qaytaramiz

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 47, 25, 3]  
eski = 25  # Almashtiriladigan element
yangi = 50  # Yangi qo‘yiladigan element

# Natijani chiqarish
yangi_royxat = element_almashtirish(sonlar, eski, yangi)
print("Yangi ro‘yxat:", yangi_royxat)

# Ro‘yxatdan ikkinchi eng katta elementni topuvchi funksiya
def ikkinchi_katta(royxat):
    noyob_sonlar = list(set(royxat))  # Takrorlangan elementlarni olib tashlaymiz
    if len(noyob_sonlar) < 2:
        return "Ro‘yxatda ikkinchi eng katta element yo‘q!"
    
    noyob_sonlar.sort(reverse=True)  # Kamayish tartibida saralash
    return noyob_sonlar[1]  # Ikkinchi eng katta elementni qaytarish

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 47, 25, 3]

# Natijani chiqarish
natija = ikkinchi_katta(sonlar)
print("Ikkinchi eng katta element:", natija)

# Ro‘yxatdan ikkinchi eng kichik elementni topuvchi funksiya
def ikkinchi_kichik(royxat):
    noyob_sonlar = list(set(royxat))  # Takrorlangan elementlarni olib tashlaymiz
    if len(noyob_sonlar) < 2:
        return "Ro‘yxatda ikkinchi eng kichik element yo‘q!"
    
    noyob_sonlar.sort()  # O‘sish tartibida saralash
    return noyob_sonlar[1]  # Ikkinchi eng kichik elementni qaytarish

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 47, 25, 3]

# Natijani chiqarish
natija = ikkinchi_kichik(sonlar)
print("Ikkinchi eng kichik element:", natija)
# Juft sonlarni ajratib oluvchi funksiya
def faqat_juft_sonlar(royxat):
    return [son for son in royxat if son % 2 == 0]  # Faqat juft sonlarni oladi

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 48, 50, 12]

# Natijani chiqarish
juft_sonlar = faqat_juft_sonlar(sonlar)
print("Juft sonlar:", juft_sonlar)

# Toq sonlarni ajratib oluvchi funksiya
def faqat_toq_sonlar(royxat):
    return [son for son in royxat if son % 2 != 0]  # Faqat toq sonlarni oladi

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 48, 50, 12]

# Natijani chiqarish
toq_sonlar = faqat_toq_sonlar(sonlar)
print("Toq sonlar:", toq_sonlar)

# Ro‘yxat uzunligini aniqlovchi funksiya
def royxat_uzunligi(royxat):
    return len(royxat)  # len() funksiyasi orqali elementlar sonini qaytaramiz

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 48, 50, 12]

# Natijani chiqarish
uzunlik = royxat_uzunligi(sonlar)
print("Ro‘yxat uzunligi:", uzunlik)


# Ro‘yxatdan nusxa olish funksiyasi
def royxat_nusxasi(royxat):
    return royxat.copy()  # .copy() usuli ro‘yxatning yangi nusxasini qaytaradi

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 48, 50, 12]

# Ro‘yxat nusxasini yaratish
yangi_royxat = royxat_nusxasi(sonlar)

# Natijani chiqarish
print("Asl ro‘yxat:", sonlar)
print("Nusxa ro‘yxat:", yangi_royxat)

# Ro‘yxatning o‘rtasidagi element(lar)ni topuvchi funksiya
def ortadagi_element(royxat):
    uzunlik = len(royxat)  # Ro‘yxat uzunligini aniqlaymiz
    if uzunlik == 0:
        return "Ro‘yxat bo‘sh!"  # Agar ro‘yxat bo‘sh bo‘lsa, xabar qaytaramiz
    
    indeks = uzunlik // 2  # O‘rta indeksni hisoblaymiz

    if uzunlik % 2 == 1:  # Agar ro‘yxat uzunligi toq bo‘lsa
        return royxat[indeks]  # Bitta o‘rta elementni qaytaramiz
    else:  # Agar ro‘yxat uzunligi juft bo‘lsa
        return [royxat[indeks - 1], royxat[indeks]]  # Ikki o‘rta elementni qaytaramiz

# Misol uchun ro‘yxatlar
royxat1 = [10, 25, 3, 99, 48]  # Toq uzunlik
royxat2 = [10, 25, 3, 99, 48, 50]  # Juft uzunlik

# Natijani chiqarish
print("Toq uzunlikdagi ro‘yxat o‘rta elementi:", ortadagi_element(royxat1))
print("Juft uzunlikdagi ro‘yxat o‘rta elementlari:", ortadagi_element(royxat2))

# Subro‘yxatdan (sublist) eng katta elementni topuvchi funksiya
def subroyxat_eng_katta(royxat, boshlanish, tugash):
    subroyxat = royxat[boshlanish:tugash]  # Berilgan indekslar bo‘yicha subro‘yxat yaratamiz
    if not subroyxat:
        return "Subro‘yxat bo‘sh!"  # Agar subro‘yxat bo‘sh bo‘lsa, xabar chiqaramiz
    return max(subroyxat)  # Subro‘yxatdagi eng katta elementni qaytaramiz

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 48, 50, 12]

# Subro‘yxatdan eng katta elementni topish (indekslar: 1 dan 5 gacha)
natija = subroyxat_eng_katta(sonlar, 1, 5)

# Natijani chiqarish
print("Subro‘yxatdagi eng katta element:", natija)
# Subro‘yxatdan (sublist) eng kichik elementni topuvchi funksiya
def subroyxat_eng_kichik(royxat, boshlanish, tugash):
    subroyxat = royxat[boshlanish:tugash]  # Berilgan indekslar bo‘yicha subro‘yxat yaratamiz
    if not subroyxat:
        return "Subro‘yxat bo‘sh!"  # Agar subro‘yxat bo‘sh bo‘lsa, xabar chiqaramiz
    return min(subroyxat)  # Subro‘yxatdagi eng kichik elementni qaytaramiz

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 48, 50, 12]

# Subro‘yxatdan eng kichik elementni topish (indekslar: 1 dan 5 gacha)
natija = subroyxat_eng_kichik(sonlar, 1, 5)

# Natijani chiqarish
print("Subro‘yxatdagi eng kichik element:", natija)


# Ro‘yxatdan indeks bo‘yicha elementni olib tashlovchi funksiya
def indeks_boyicha_olib_tashlash(royxat, indeks):
    if 0 <= indeks < len(royxat):  # Indeks ro‘yxat chegarasida ekanligini tekshiramiz
        del royxat[indeks]  # Indeksdagi elementni olib tashlaymiz
        return royxat  # Yangilangan ro‘yxatni qaytaramiz
    else:
        return "Xatolik: Indeks ro'yxat chegarasidan tashqarida!"  # Xato xabari

# Misol uchun ro‘yxat
sonlar = [10, 25, 3, 99, 48, 50, 12]

# Indeks bo‘yicha elementni olib tashlash (masalan, 3-indeks)
natija = indeks_boyicha_olib_tashlash(sonlar, 3)

# Natijani chiqarish
print("Yangilangan ro'yxat:", natija)

# Ro‘yxat tartiblanganligini tekshiruvchi funksiya
def royxat_tartiblanganmi(royxat):
    return royxat == sorted(royxat)  # Agar ro‘yxat tartiblangan bo‘lsa, True qaytaradi

# Misol uchun ro‘yxatlar
royxat1 = [1, 2, 3, 4, 5]  # Tartiblangan ro‘yxat
royxat2 = [10, 5, 3, 8, 2]  # Tartiblanmagan ro‘yxat

# Natijalarni chiqarish
print("royxat1 tartiblanganmi?", royxat_tartiblanganmi(royxat1))  # True
print("royxat2 tartiblanganmi?", royxat_tartiblanganmi(royxat2))  # False

# Ro‘yxat elementlarini ko‘paytiruvchi funksiya
def elementlarni_takrorlash(royxat, takror_soni):
    if takror_soni <= 0:
        return "Xatolik: Takrorlash soni musbat bo‘lishi kerak!"  # Xato xabari
    return [element for element in royxat for _ in range(takror_soni)]  # Har bir elementni takrorlaymiz

# Misol uchun ro‘yxat
sonlar = [1, 2, 3]

# Har bir elementni 3 marta takrorlash
natija = elementlarni_takrorlash(sonlar, 3)

# Natijani chiqarish
print("Yangilangan ro‘yxat:", natija)
# Ikki ro‘yxatni birlashtirib, tartiblaydigan funksiya
def birlashtir_va_tartibla(royxat1, royxat2):
    yangi_royxat = royxat1 + royxat2  # Ro‘yxatlarni birlashtiramiz
    return sorted(yangi_royxat)  # Yangi ro‘yxatni tartiblaymiz

# Misol uchun ro‘yxatlar
royxat1 = [5, 2, 8]
royxat2 = [3, 7, 1, 4]

# Ro‘yxatlarni birlashtirish va tartiblash
natija = birlashtir_va_tartibla(royxat1, royxat2)

# Natijani chiqarish
print("Birlashtirilgan va tartiblangan ro‘yxat:", natija)

# Berilgan elementning barcha indekslarini topuvchi funksiya
def barcha_indekslarni_top(royxat, element):
    indekslar = [i for i, x in enumerate(royxat) if x == element]  # Element mos kelgan indekslarni topamiz
    return indekslar if indekslar else "Element ro‘yxatda yo‘q!"  # Agar topilmasa, xabar chiqaramiz

# Misol uchun ro‘yxat
sonlar = [3, 7, 2, 7, 9, 7, 5]

# Elementni qidirish
element = 7
natija = barcha_indekslarni_top(sonlar, element)

# Natijani chiqarish
print(f"{element} elementi joylashgan indekslar:", natija)

# Ro‘yxatni o‘ngga aylantiruvchi funksiya
def royxatni_aylantirish(royxat, qadam):
    if not royxat:  
        return "Xatolik: Ro‘yxat bo‘sh!"  # Agar ro‘yxat bo‘sh bo‘lsa, xabar qaytaramiz
    qadam = qadam % len(royxat)  # Ro‘yxat uzunligidan oshib ketmasligi uchun
    return royxat[-qadam:] + royxat[:-qadam]  # Oxirgi elementlarni boshiga qo‘shamiz

# Misol uchun ro‘yxat
sonlar = [1, 2, 3, 4, 5]

# Ro‘yxatni o‘ngga 2 qadamga aylantirish
natija = royxatni_aylantirish(sonlar, 2)

# Natijani chiqarish
print("Aylantirilgan ro‘yxat:", natija)
# Berilgan oraliqdagi sonlardan ro‘yxat yaratish funksiyasi
def oraliq_royxat(boshlanish, tugash, qadam=1):
    return list(range(boshlanish, tugash + 1, qadam))  # Ro‘yxat yaratamiz

# Misol uchun oraliq
natija = oraliq_royxat(1, 10)

# Natijani chiqarish
print("Yaratilgan ro‘yxat:", natija)
# Musbat sonlar yig‘indisini hisoblovchi funksiya
def musbat_sonlar_yigindisi(royxat):
    return sum(son for son in royxat if son > 0)  # Musbat sonlarni qo‘shamiz

# Misol uchun ro‘yxat
sonlar = [3, -7, 5, -2, 8, -1]

# Musbat sonlar yig‘indisini hisoblash
natija = musbat_sonlar_yigindisi(sonlar)

# Natijani chiqarish
print("Musbat sonlar yig‘indisi:", natija)
# Manfiy sonlar yig‘indisini hisoblovchi funksiya
def manfiy_sonlar_yigindisi(royxat):
    return sum(son for son in royxat if son < 0)  # Faqat manfiy sonlarni qo‘shamiz

# Misol uchun ro‘yxat
sonlar = [3, -7, 5, -2, 8, -1]

# Manfiy sonlar yig‘indisini hisoblash
natija = manfiy_sonlar_yigindisi(sonlar)

# Natijani chiqarish
print("Manfiy sonlar yig‘indisi:", natija)
# Ro‘yxat palindrom ekanligini tekshiruvchi funksiya
def palindromni_tekshir(royxat):
    return royxat == royxat[::-1]  # Ro‘yxatni teskari qilib solishtiramiz

# Misol uchun ro‘yxatlar
royxat1 = [1, 2, 3, 2, 1]  # Palindrom
royxat2 = [1, 2, 3, 4, 5]  # Palindrom emas

# Natijalarni chiqarish
print("royxat1 palindrommi?", palindromni_tekshir(royxat1))  # True
print("royxat2 palindrommi?", palindromni_tekshir(royxat2))  # False
# Berilgan ro‘yxatdan subro‘yxatlar yaratish funksiyasi
def ichki_royxat_yaratish(royxat, uzunlik):
    return [royxat[i:i + uzunlik] for i in range(0, len(royxat), uzunlik)]

# Misol uchun ro‘yxat
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Har 3 ta elementdan iborat subro‘yxatlar yaratish
natija = ichki_royxat_yaratish(sonlar, 3)

# Natijani chiqarish
print("Yangi ro‘yxat:", natija)
# Ro‘yxatdan takrorlanmagan elementlarni chiqarish funksiyasi
def unikal_elementlar(royxat):
    yangi_royxat = []
    for element in royxat:
        if element not in yangi_royxat:  # Agar oldin qo‘shilmagan bo‘lsa, qo‘shamiz
            yangi_royxat.append(element)
    return yangi_royxat

# Misol uchun ro‘yxat
sonlar = [1, 2, 3, 2, 4, 1, 5, 3, 6]

# Unikal elementlarni chiqarish
natija = unikal_elementlar(sonlar)

# Natijani chiqarish
print("Takrorlanmagan elementlar:", natija)
