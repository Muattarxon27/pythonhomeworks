import sqlite3

# 1-Vazifa: roster.db yaratish
conn = sqlite3.connect('roster.db')
cursor = conn.cursor()

# Roster jadvalini yaratish
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# Ma'lumotlarni qo'shish
cursor.executemany('''
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
''', [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

# Ma'lumotni yangilash
cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

# So‘rov: Bajoran bo‘lgan shaxslar
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
print(cursor.fetchall())

# 100 yoshdan kattalarni o‘chirish
cursor.execute("DELETE FROM Roster WHERE Age > 100")

# Rank ustunini qo‘shish
cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")

# Rank ustunini to‘ldirish
cursor.executemany("UPDATE Roster SET Rank = ? WHERE Name = ?", [
    ('Captain', 'Benjamin Sisko'),
    ('Lieutenant', 'Ezri Dax'),
    ('Major', 'Kira Nerys')
])

# Yosh bo‘yicha kamayish tartibida chiqarish
cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
print(cursor.fetchall())

conn.commit()
conn.close()

# 2-Vazifa: library.db yaratish
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Books jadvalini yaratish
cursor.execute('''
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
''')

# Ma'lumotlarni qo'shish
cursor.executemany('''
INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)
''', [
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
])

# Ma'lumotni yangilash
cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")

# So‘rov: Dystopian janrli kitoblar
cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
print(cursor.fetchall())

# 1950 yildan oldin chiqqanlarni o‘chirish
cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")

# Rating ustunini qo‘shish
cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")

# Rating ustunini to‘ldirish
cursor.executemany("UPDATE Books SET Rating = ? WHERE Title = ?", [
    (4.8, 'To Kill a Mockingbird'),
    (4.7, '1984'),
    (4.5, 'The Great Gatsby')
])

# Yili bo‘yicha oshish tartibida chiqarish
cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
print(cursor.fetchall())

conn.commit()
conn.close()
