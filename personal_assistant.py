import json
import csv
from datetime import datetime

class Note:
    def __init__(self, note_id, title, content, timestamp=None):
        self.id = note_id
        self.title = title
        self.content = content
        self.timestamp = timestamp or datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):
        return vars(self)


class Task:
    def __init__(self, task_id, title, description, done=False, priority="Средний", due_date=None):
        self.id = task_id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

    def to_dict(self):
        return vars(self)


class Contact:
    def __init__(self, contact_id, name, phone, email):
        self.id = contact_id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return vars(self)


class FinanceRecord:
    def __init__(self, record_id, amount, category, date, description):
        self.id = record_id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        return vars(self)


class PersonalAssistant:
    def export_notes_to_csv(self):
        if not self.notes:
            raise ValueError("Нет данных для экспорта. Список заметок пуст.")

        filename = "notes.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.notes[0].keys())
            writer.writeheader()
            writer.writerows(self.notes)
        print(f"Заметки экспортированы в файл {filename}.")

    def import_notes_from_csv(self):
        filename = "notes.csv"
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.notes = [row for row in reader]
            self.save_data(self.notes_file, self.notes)
            print(f"Заметки импортированы из файла {filename}.")
        except FileNotFoundError:
            print("Файл не найден.")

    def export_tasks_to_csv(self):
        if not self.tasks:
            raise ValueError("Нет данных для экспорта. Список задач пуст.")

        filename = "tasks.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.tasks[0].keys())
            writer.writeheader()
            writer.writerows(self.tasks)
        print(f"Задачи экспортированы в файл {filename}.")

    def import_tasks_from_csv(self):
        filename = "tasks.csv"
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.tasks = [row for row in reader]
            self.save_data(self.tasks_file, self.tasks)
            print(f"Задачи импортированы из файла {filename}.")
        except FileNotFoundError:
            print("Файл не найден.")

    def export_contacts_to_csv(self):
        if not self.contacts:
            raise ValueError("Нет данных для экспорта. Список контактов пуст.")

        filename = "contacts.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.contacts[0].keys())
            writer.writeheader()
            writer.writerows(self.contacts)
        print(f"Контакты экспортированы в файл {filename}.")

    def import_contacts_from_csv(self):
        filename = "contacts.csv"
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.contacts = [row for row in reader]
            self.save_data(self.contacts_file, self.contacts)
            print(f"Контакты импортированы из файла {filename}.")
        except FileNotFoundError:
            print("Файл не найден.")

    def export_finances_to_csv(self):
        if not self.finances:
            raise ValueError("Нет данных для экспорта. Список финансовых записей пуст.")

        filename = "finance_records.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.finances[0].keys())
            writer.writeheader()
            writer.writerows(self.finances)
        print(f"Финансовые записи экспортированы в файл {filename}.")

    def import_finances_from_csv(self):
        filename = "finance_records.csv"
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.finances = [row for row in reader]
            self.save_data(self.finance_file, self.finances)
            print(f"Финансовые записи импортированы из файла {filename}.")
        except FileNotFoundError:
            print("Файл не найден.")

    def __init__(self):
        self.notes_file = "notes.json"
        self.tasks_file = "tasks.json"
        self.contacts_file = "contacts.json"
        self.finance_file = "finance.json"
        self.notes = self.load_data(self.notes_file)
        self.tasks = self.load_data(self.tasks_file)
        self.contacts = self.load_data(self.contacts_file)
        self.finances = self.load_data(self.finance_file)

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self, filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def main_menu(self):
        while True:
            print("\nДобро пожаловать в Персональный помощник!")
            print("1. Управление заметками")
            print("2. Управление задачами")
            print("3. Управление контактами")
            print("4. Управление финансовыми записями")
            print("5. Калькулятор")
            print("6. Выход")

            choice = input("Выберите действие: ")
            if choice == "1":
                self.notes_menu()
            elif choice == "2":
                self.tasks_menu()
            elif choice == "3":
                self.contacts_menu()
            elif choice == "4":
                self.finance_menu()
            elif choice == "5":
                self.calculator()
            elif choice == "6":
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def notes_menu(self):
        while True:
            print("\nУправление заметками:")
            print("1. Создать заметку")
            print("2. Просмотреть список заметок")
            print("3. Просмотреть заметку")
            print("4. Редактировать заметку")
            print("5. Удалить заметку")
            print("6. Экспортировать заметки в CSV")
            print("7. Импортировать заметки из CSV")
            print("8. Назад")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.create_note()
            elif choice == "2":
                self.list_notes()
            elif choice == "3":
                self.view_note()
            elif choice == "4":
                self.edit_note()
            elif choice == "5":
                self.delete_note()
            elif choice == "6":
                try:
                    self.export_notes_to_csv()
                except ValueError as e:
                    print(e)
            elif choice == "7":
                self.import_notes_from_csv()
            elif choice == "8":
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def create_note(self):
        title = input("Введите заголовок заметки: ")
        content = input("Введите содержимое заметки: ")
        note_id = len(self.notes) + 1
        new_note = Note(note_id, title, content)
        self.notes.append(new_note.to_dict())
        self.save_data(self.notes_file, self.notes)
        print("Заметка успешно создана.")

    def list_notes(self):
        print("\nСписок заметок:")
        for note in self.notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")

    def view_note(self):
        note_id = int(input("Введите ID заметки для просмотра: "))
        note = next((n for n in self.notes if n['id'] == note_id), None)
        if note:
            print(f"Заголовок: {note['title']}")
            print(f"Содержимое: {note['content']}")
            print(f"Дата: {note['timestamp']}")
        else:
            print("Заметка не найдена.")

    def edit_note(self):
        note_id = int(input("Введите ID заметки для редактирования: "))
        note = next((n for n in self.notes if n['id'] == note_id), None)
        if note:
            note['title'] = input(f"Введите новый заголовок (текущий: {note['title']}): ")
            note['content'] = input(f"Введите новое содержимое (текущее: {note['content']}): ")
            note['timestamp'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.save_data(self.notes_file, self.notes)
            print("Заметка успешно обновлена.")
        else:
            print("Заметка не найдена.")

    def delete_note(self):
        note_id = int(input("Введите ID заметки для удаления: "))
        self.notes = [n for n in self.notes if n['id'] != note_id]
        self.save_data(self.notes_file, self.notes)
        print("Заметка успешно удалена.")

    def tasks_menu(self):
        print("\nУправление задачами — в разработке.")

    def contacts_menu(self):
        print("\nУправление контактами — в разработке.")

    def finance_menu(self):
        print("\nУправление финансовыми записями — в разработке.")

    def calculator(self):
        print("\nКалькулятор — в разработке.")

    def tasks_menu(self):
        while True:
            print("\nУправление задачами:")
            print("1. Добавить задачу")
            print("2. Просмотреть задачи")
            print("3. Отметить задачу как выполненную")
            print("4. Удалить задачу")
            print("5. Экспортировать задачи в CSV")
            print("6. Импортировать задачи из CSV")
            print("7. Назад")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.create_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.mark_task_done()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                try:
                    self.export_tasks_to_csv()
                except ValueError as e:
                    print(e)
            elif choice == "6":
                self.import_tasks_from_csv()
            elif choice == "7":
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def create_task(self):
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        priority = input("Введите приоритет (Высокий, Средний, Низкий): ")
        due_date = input("Введите срок выполнения (в формате DD-MM-YYYY): ")
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title, description, False, priority, due_date)
        self.tasks.append(new_task.to_dict())
        self.save_data(self.tasks_file, self.tasks)
        print("Задача успешно добавлена.")

    def list_tasks(self):
        print("\nСписок задач:")
        for task in self.tasks:
            status = "Выполнено" if task['done'] else "Не выполнено"
            print(f"ID: {task['id']}, Название: {task['title']}, Статус: {status}, Приоритет: {task['priority']}, Срок: {task['due_date']}")

    def mark_task_done(self):
        task_id = int(input("Введите ID задачи для отметки как выполненной: "))
        task = next((t for t in self.tasks if t['id'] == task_id), None)
        if task:
            task['done'] = True
            self.save_data(self.tasks_file, self.tasks)
            print("Задача отмечена как выполненная.")
        else:
            print("Задача не найдена.")

    def delete_task(self):
        task_id = int(input("Введите ID задачи для удаления: "))
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        self.save_data(self.tasks_file, self.tasks)
        print("Задача успешно удалена.")

    def contacts_menu(self):
        while True:
            print("\nУправление контактами:")
            print("1. Добавить контакт")
            print("2. Просмотреть контакты")
            print("3. Удалить контакт")
            print("4. Экспортировать контакты в CSV")
            print("5. Импортировать контакты из CSV")
            print("6. Назад")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.list_contacts()
            elif choice == "3":
                self.delete_contact()
            elif choice == "4":
                try:
                    self.export_contacts_to_csv()
                except ValueError as e:
                    print(e)
            elif choice == "5":
                self.import_contacts_from_csv()
            elif choice == "6":
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def add_contact(self):
        name = input("Введите имя контакта: ")
        phone = input("Введите номер телефона: ")
        email = input("Введите адрес электронной почты: ")
        contact_id = len(self.contacts) + 1
        new_contact = Contact(contact_id, name, phone, email)
        self.contacts.append(new_contact.to_dict())
        self.save_data(self.contacts_file, self.contacts)
        print("Контакт успешно добавлен.")

    def list_contacts(self):
        print("\nСписок контактов:")
        for contact in self.contacts:
            print(f"ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, Email: {contact['email']}")

    def delete_contact(self):
        contact_id = int(input("Введите ID контакта для удаления: "))
        self.contacts = [c for c in self.contacts if c['id'] != contact_id]
        self.save_data(self.contacts_file, self.contacts)
        print("Контакт успешно удален.")

    def finance_menu(self):
        while True:
            print("\nУправление финансовыми записями:")
            print("1. Добавить запись")
            print("2. Просмотреть записи")
            print("3. Экспортировать в CSV")
            print("4. Импортировать из CSV")
            print("5. Назад")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_finance_record()
            elif choice == "2":
                self.list_finance_records()
            elif choice == "3":
                try:
                    self.export_finances_to_csv()
                except ValueError as e:
                    print(e)
            elif choice == "4":
                self.import_finances_from_csv()
            elif choice == "5":
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def add_finance_record(self):
        amount = float(input("Введите сумму: "))
        category = input("Введите категорию (доход/расход): ")
        date = input("Введите дату (в формате DD-MM-YYYY): ")
        description = input("Введите описание: ")
        record_id = len(self.finances) + 1
        new_record = FinanceRecord(record_id, amount, category, date, description)
        self.finances.append(new_record.to_dict())
        self.save_data(self.finance_file, self.finances)
        print("Финансовая запись добавлена.")

    def list_finance_records(self):
        print("\nСписок финансовых записей:")
        for record in self.finances:
            print(f"ID: {record['id']}, Сумма: {record['amount']}, Категория: {record['category']}, Дата: {record['date']}, Описание: {record['description']}")

    def export_finances_to_csv(self):
        filename = "finance_records.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.finances[0].keys())
            writer.writeheader()
            writer.writerows(self.finances)
        print(f"Финансовые записи экспортированы в файл {filename}.")

    def calculator(self):
        print("\nКалькулятор:")
        expression = input("Введите математическое выражение (например, 2+2): ")
        try:
            result = eval(expression)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    app = PersonalAssistant()
    app.main_menu()