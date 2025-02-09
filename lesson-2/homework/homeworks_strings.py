name=input("Ismingizni yozing:  ")
k=int(input("tug'ilgan yilingizni  yozing:  "))
print(f"{name} {k} yilda tug'ilgan.")

# Matndan avtomobil nomlarini topish
def extract_car_names(txt):
    car_brands = ["Maserati", "BMW", "Audi", "Toyota", "Tesla", "Ford", "Honda"]
    from itertools import permutations
    possible_words = {''.join(p) for p in permutations(txt)}
    found_brands = [brand for brand in car_brands if brand in possible_words]
    return found_brands

# Foydalanuvchidan matn kiritishni so‘rash
txt = input("Matnni kiriting: ")
cars = extract_car_names(txt)
print("Topilgan avtomobil brendlari:", cars)

txt=input("Biror matn kiriting:")
print(len(txt))
print(txt.upper())
print(txt.lower())

s=input("biror satr kiriting")
if s==s[::-1]:
    print("bu satr palindrom.")
else:
    print("bu satr palindrom emas.")

s=input("Biror matnni kiriting").lower()
vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
vowel_count=0
consonant_count=0
for char in s:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1
        print("unli harflar soni: ", vowel_count)
        print("undosh harflar soni:", consonant_count)


main_string=input("Asosiy matnni kiriting")
sub_string=input("qidirilayotgan matnni kiriting")
if sub_string in main_string:
    print("Ha, bu matn asosiy matn ichida bor")
else:
    print("yo'q, bu matn asosiy matnda yo'q")

sentence=input("Biror matn kiriting")
old_world=input("qaysi so'zni almashtirmoqchisiz?")
new_world=input("yangi so'zni kiriting:")
updated_sentence=sentence.replace(old_world, new_world)
print("yangi gap:", updated_sentence)
text=input("matnni kiriting")
if len(text) > 0:
    print("birinchi belgi:", text[0])
    print("oxirgi belgi:", text[-1])
else:
    print("siz bo'sh matn kiritdingiz")
    s=input("Biror matni kiriting")
reversed_s=s[::-1]
print("Teskari matn:", reversed_s)

s=input("Matnni kiriting")
print(len(s))

s=input("matnni kiriting")
contains_digit=any(char.isdigit()for char in s)
if contains_digit:
    print("Matnda raqam mavjud.")
else:
    print("Matnda hech qanday raqam yo'q.")

words=input("So'zlarni vergul biln ajratib yozing")
if ',' in words:
    words=words.split(',')
else:
    words=words.split()
words=[word.strip() for word in words]
separator=input("So'zlarni qanday belgi bilan ajratishni xohlaysiz?")
joined_string=separator.join(words)
print("yakuniy matn:", joined_string)
words=input("So'zlarni vergul biln ajratib yozing")
if ',' in words:
    words=words.split(',')
else:
    words=words.split()
words=[word.strip() for word in words]
separator=input("So'zlarni qanday belgi bilan ajratishni xohlaysiz?")
joined_string=separator.join(words)
print("yakuniy matn:", joined_string)

string1=input("birinchi matnni kiriting:")
string2=input("ikkinchi matnni kiriting:")
if string1==string2:
    print("bmatnlar teng")
else:
    print("Matnlar teng emas")
    sentence=input("jumla kiriting: ")
acronym="".join(world[0].upper()for world in sentence.split())
print("Akronim:", acronym)

text=input("Matnni kiriting: ")
char_to_remove=input("Olib tashlanadigan belgini kiriting: ")
char_to_remove=char_to_remove[0]
new_text=text.replace(char_to_remove, "")
print("Natijani: ", new_text)
text=input("Matnni kiriting: ")
symbol=input("Almashtirish belgisini kiriting: ")
vowels="aeiouAEIOU"
new_text="".join(symbol if char in vowels else char for char in text)
print("Natija: ", new_text)

text=input("Matnni kiriting: ")
start_word=input("Qaysi so'z bilan boshlanishini tekshiramiz ")
end_word=input("Qaysi so'z bilan tugashini tekshiramiz ")
if text.startswith(start_word) and text.endswith(end_word):
    print("Matn aynan shu so'z bilan boshlanadi va tugaydi!")
else:
    print("Matn bu so'z bilan boshlanmaydi va tugamaydi.")
    