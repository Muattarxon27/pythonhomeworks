import json
import csv

# JSON fayl nomi
JSON_FILE = "tasks.json"
CSV_FILE = "tasks.csv"

# JSON dan vazifalarni yuklash
def load_tasks():
    try:
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: tasks.json fayli topilmadi.")
        return []
    except json.JSONDecodeError:
        print("Error: JSON fayl noto‘g‘ri formatda.")
        return []

# Vazifalarni ekranga chiqarish
def display_tasks(tasks):
    print("\nVazifalar Ro‘yxati:")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

# Statistikani hisoblash
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\n📊 Statistik Ma'lumotlar:")
    print(f"🔹 Umumiy vazifalar: {total_tasks}")
    print(f"✅ Bajarilgan vazifalar: {completed_tasks}")
    print(f"❌ Bajarilmagan vazifalar: {pending_tasks}")
    print(f"⭐ O‘rtacha ustuvorlik: {avg_priority:.2f}")

# JSON ma'lumotlarini CSV formatiga o'tkazish
def convert_json_to_csv(tasks):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print(f"\n✅ JSON ma'lumotlari CSV fayliga ({CSV_FILE}) saqlandi.")

# Dastur ishga tushirilishi
if __name__ == "__main__":
    tasks = load_tasks()
    display_tasks(tasks)
    calculate_stats(tasks)
    convert_json_to_csv(tasks)