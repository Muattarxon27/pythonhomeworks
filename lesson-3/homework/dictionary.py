# Lug‘atdan qiymat olish funksiyasi
def qiymat_ol(lugat, kalit, standart=None):
    return lugat.get(kalit, standart)

# Misol lug‘at
talaba = {
    "ism": "Muattarxon",
    "yosh": 17,
    "universitet": "fardu universiteti"
}

# Lug‘atdan mavjud kalitni olish
print("Ism:", qiymat_ol(talaba, "ism"))  # "Muattarxon"

# Lug‘atda mavjud bo‘lmagan kalitni olish
print("Kurs:", qiymat_ol(talaba, "kurs", "1"))  # "1"

# Lug‘atda kalit bor-yo‘qligini tekshiruvchi funksiya
def kalit_tekshir(lugat, kalit):
    return kalit in lugat

# Misol lug‘at
talaba = {
    "ism": "Muattarxon",
    "yosh": 17,
    "universitet": "fardu universiteti",
    "kurs": 1
 }

# Kalit mavjudligini tekshirish
print("Kalit 'ism' mavjudmi?", kalit_tekshir(talaba, "ism"))  # True
print("Kalit 'kurs' mavjudmi?", kalit_tekshir(talaba, "kurs"))  # False

# Lug‘atdagi kalitlar sonini hisoblovchi funksiya
def kalitlar_soni(lugat):
    return len(lugat)

# Misol lug‘at
talaba = {
    "ism": "Muattarxon",
    "yosh": 17,
    "universitet": "fardu universiteti"
}

# Natija
print("Lug‘atdagi kalitlar soni:", kalitlar_soni(talaba))  # 3

# Lug‘atdagi barcha kalitlarni ro‘yxat sifatida qaytaruvchi funksiya
def barcha_kalitlar(lugat):
    return list(lugat.keys())

# Misol lug‘at
talaba = {
    "ism": "Muattarxon",
    "yosh": 17,
    "universitet": "Biladi universiteti"
}

# Natija
print("Lug‘atdagi kalitlar:", barcha_kalitlar(talaba))  
# ['ism', 'yosh', 'universitet']
# Lug‘atdagi barcha qiymatlarni ro‘yxat sifatida qaytaruvchi funksiya
def barcha_qiymatlar(lugat):
    return list(lugat.values())

# Misol lug‘at
talaba = {
    "ism": "Muattarxon",
    "yosh": 17,
    "universitet": "fardu universiteti"
}

# Natija
print("Lug‘atdagi qiymatlar:", barcha_qiymatlar(talaba))  
# ['Muattarxon', 17, 'Biladi universiteti']

# Ikki lug‘atni birlashtirib, yangi lug‘at qaytaruvchi funksiya
def birlashtir_lugatlar(lugat1, lugat2):
    yangi_lugat = {**lugat1, **lugat2}
    return yangi_lugat

# Misol lug‘atlar
lugat1 = {"ism": "Muattarxon", "yosh": 17}
lugat2 = {"universitet": "Biladi universiteti", "kurs": 1}

# Natija
birlashtirilgan = birlashtir_lugatlar(lugat1, lugat2)
print("Birlashtirilgan lug‘at:", birlashtirilgan)  

# {'ism': 'Muattarxon', 'yosh': 17, 'universitet': 'Biladi universiteti', 'kurs': 1}

# Lug‘atdan berilgan kalitni o‘chiruvchi funksiya
def ochir_lugat_kaliti(lugat, kalit):
    if kalit in lugat:
        del lugat[kalit]
        print(f"'{kalit}' kaliti o‘chirildi.")
    else:
        print(f"'{kalit}' kaliti lug‘atda yo‘q.")
    return lugat

# Misol lug‘at
lugat = {"ism": "Muattarxon", "yosh": 17, "universitet": "Biladi universiteti"}

# Kalitni o‘chirish
yangilangan_lugat = ochir_lugat_kaliti(lugat, "yosh")
print("Yangilangan lug‘at:", yangilangan_lugat)

# Natija:
# 'yosh' kaliti o‘chirildi.
# Yangilangan lug‘at: {'ism': 'Muattarxon', 'universitet': 'Biladi universiteti'}

# Lug‘atni tozalash funksiyasi
def tozalash_lugat():
    return {}

# Misol lug‘at
lugat = {"ism": "Muattarxon", "yosh": 17, "universitet": "Biladi universiteti"}

# Lug‘atni tozalash
yangi_lugat = tozalash_lugat()
print("Tozalangan lug‘at:", yangi_lugat)

# Natija:
# Tozalangan lug‘at: {}

# Lug‘at bo‘shligini tekshirish funksiyasi
def lugat_boshmi(lugat):
    return len(lugat) == 0  # Agar uzunligi 0 bo‘lsa, True qaytaradi

# Misollar
lugat1 = {}  # Bo‘sh lug‘at
lugat2 = {"ism": "Muattarxon", "yosh": 17}

# Natijalarni chiqarish
print("Lugat1 bo‘shmi?", lugat_boshmi(lugat1))  # True
print("Lugat2 bo‘shmi?", lugat_boshmi(lugat2))  # False

# Kalit-qiymat juftligini qaytaruvchi funksiya
def kalit_qiymat_jufti(lugat, kalit):
    if kalit in lugat:  # Agar kalit lug‘atda bo‘lsa
        return (kalit, lugat[kalit])  # Kalit va qiymatni juftlik sifatida qaytaradi
    else:
        return None  # Agar kalit yo‘q bo‘lsa, None qaytariladi

# Misollar
lugat = {"ism": "Muattarxon", "yosh": 17, "shahar": "Toshkent"}

# Kalit mavjud bo‘lsa
print(kalit_qiymat_jufti(lugat, "ism"))  # ('ism', 'Muattarxon')

# Kalit mavjud bo‘lmasa
print(kalit_qiymat_jufti(lugat, "kasb"))  # None

# Lug‘atda kalit bo‘yicha qiymatni yangilovchi funksiya
def qiymat_yangilash(lugat, kalit, yangi_qiymat):
    if kalit in lugat:  # Agar kalit mavjud bo‘lsa
        lugat[kalit] = yangi_qiymat  # Yangi qiymatni o‘rnatadi
        return True  # Muvaffaqiyatli yangilansa, True qaytariladi
    else:
        return False  # Agar kalit mavjud bo‘lmasa, False qaytariladi

# Misollar
lugat = {"ism": "Muattarxon", "yosh": 17, "shahar": "Toshkent"}

# Mavjud kalit uchun yangilash
print(qiymat_yangilash(lugat, "yosh", 18))  # True
print(lugat)  # {'ism': 'Muattarxon', 'yosh': 18, 'shahar': 'Toshkent'}

# Mavjud bo‘lmagan kalit uchun
print(qiymat_yangilash(lugat, "kasb", "Dasturchi"))  # False
print(lugat)  # O‘zgarmaydi

# Lug‘atda ma'lum qiymat necha marta borligini hisoblovchi funksiya
def qiymat_soni(lugat, qiymat):
    return list(lugat.values()).count(qiymat)  # Qiymatlarning sonini hisoblaydi

# Misol lug‘at
lugat = {"A": 5, "B": 3, "C": 5, "D": 7, "E": 5}

# Qiymat necha marta borligini tekshiramiz
print(qiymat_soni(lugat, 5))  # 3 marta
print(qiymat_soni(lugat, 3))  # 1 marta
print(qiymat_soni(lugat, 10))  # 0 marta

# Lug‘atni o‘rin almashtirish (kalitlarni qiymat, qiymatlarni kalit qilish)
def invert_lugat(lugat):
    return {qiymat: kalit for kalit, qiymat in lugat.items()}

# Misol lug‘at
lugat = {"A": 1, "B": 2, "C": 3}

# O‘rin almashtirilgan lug‘at
yangi_lugat = invert_lugat(lugat)
print(yangi_lugat)  # {1: 'A', 2: 'B', 3: 'C'}

# Lug‘atdagi berilgan qiymatga ega bo‘lgan barcha kalitlarni topish
def find_keys_with_value(lugat, target_value):
    return [kalit for kalit, qiymat in lugat.items() if qiymat == target_value]

# Misol lug‘at
lugat = {"A": 5, "B": 3, "C": 5, "D": 7}

# Qiymati 5 bo‘lgan barcha kalitlarni topish
natija = find_keys_with_value(lugat, 5)
print(natija)  # ['A', 'C']

# Ikkita ro‘yxatdan lug‘at yaratish
def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

# Misol ro‘yxatlar
keys = ["A", "B", "C"]
values = [10, 20, 30]

# Lug‘at yaratish
new_dict = create_dict_from_lists(keys, values)
print(new_dict)  # {'A': 10, 'B': 20, 'C': 30}

# Lug‘atda ichki lug‘atlar borligini tekshirish
def has_nested_dict(d):
    return any(isinstance(value, dict) for value in d.values())

# Misollar
dict1 = {"a": 1, "b": {"c": 2, "d": 3}, "e": 4}
dict2 = {"x": 10, "y": 20, "z": 30}

print(has_nested_dict(dict1))  # True (ichki lug‘at bor)
print(has_nested_dict(dict2))  # False (ichki lug‘at yo‘q)

# Ichki lug‘atdan qiymat olish
def get_nested_value(d, keys, default=None):
    current = d
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default  # Agar kalit topilmasa, default qiymat qaytariladi
    return current

# Misollar
nested_dict = {
    "a": {
        "b": {
            "c": 42
        }
    },
    "x": 100
}

print(get_nested_value(nested_dict, ["a", "b", "c"]))  # 42
print(get_nested_value(nested_dict, ["a", "b"]))        # {'c': 42}
print(get_nested_value(nested_dict, ["a", "z"], "Not found"))  # "Not found"
print(get_nested_value(nested_dict, ["x"]))  # 100
print(get_nested_value(nested_dict, ["y"], "No key"))  # "No key"



from collections import defaultdict

# Default qiymati 0 bo‘lgan lug‘at yaratish
default_dict = defaultdict(int)

print(default_dict["x"])  # 0 (avtomatik ravishda 0 qo‘yiladi)
print(default_dict["y"])  # 0

# Qiymat qo‘shish
default_dict["x"] += 5
print(default_dict["x"])  # 5

def count_unique_values_nested(d):
    unique_values = set()

    def extract_values(dictionary):
        for value in dictionary.values():
            if isinstance(value, dict):  # Agar qiymat lug‘at bo‘lsa, rekursiya ishlatamiz
                extract_values(value)
            else:
                unique_values.add(value)

    extract_values(d)
    return len(unique_values)

# Misol
nested_data = {
    "x": 10,
    "y": {"a": 20, "b": 30, "c": 10},
    "z": 40,
    "w": {"d": 30, "e": 50}
}

print(count_unique_values_nested(nested_data))  # Natija: 5 (qiymatlar: {10, 20, 30, 40, 50})

def sort_dict_by_key(d):
    return dict(sorted(d.items()))

# Misol
data = {
    "c": 3,
    "a": 1,
    "b": 2,
    "d": 4
}

print(sort_dict_by_key(data))
# Natija: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

# Misol
data = {
    "c": 3,
    "a": 1,
    "b": 2,
    "d": 4
}

print(sort_dict_by_value(data))
# Natija: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

def filter_dict_by_value(d, condition):
    return {k: v for k, v in d.items() if condition(v)}

# Misol
data = {
    "a": 1,
    "b": 6,
    "c": 3,
    "d": 8
}

# Qiymatlari 5 dan katta bo'lganlar
filtered_data = filter_dict_by_value(data, lambda x: x > 5)
print(filtered_data)
# Natija: {'b': 6, 'd': 8}

def check_common_keys(dict1, dict2):
    common_keys = set(dict1.keys()) & set(dict2.keys())  # Intersection of keys
    return len(common_keys) > 0

# Misol
dict1 = {
    "a": 1,
    "b": 2,
    "c": 3
}

dict2 = {
    "b": 4,
    "c": 5,
    "d": 6
}

# Umumiy kalitlar bormi?
result = check_common_keys(dict1, dict2)
print(result)  # Natija: True (b, c)

# Tuple of key-value pairs
tuple_data = (("a", 1), ("b", 2), ("c", 3))

# Convert tuple to dictionary
dict_from_tuple = dict(tuple_data)

print(dict_from_tuple)

# Tuple of key-value pairs
tuple_data = (("apple", 3), ("banana", 5), ("cherry", 2))

# Convert tuple to dictionary
fruit_count = dict(tuple_data)

print(fruit_count)

# Tuple of key-value pairs
tuple_data = (("x", 10), ("y", 20), ("z", 30))

# Convert to dictionary
dict_from_tuple = dict(tuple_data)

# Print dictionary
print(dict_from_tuple)

# Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Get the first key-value pair
first_item = list(my_dict.items())[0]

print(first_item)

