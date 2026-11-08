from collections import UserDict
from unicodedata import name

class Field: # Базовий клас для полів запису.
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field): # Клас для зберігання імені контакту. Обов'язкове поле.
    def __init__(self, name: str):
        super().__init__(name)

class Phone(Field): # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    def __init__(self, value: str):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError('Phone number must be 10 digits long.')
        super().__init__(value)
		
class Record: # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str): # Додавання телефонів.
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str): # Видалення телефонів.
        removed_phone = self.find_phone(phone)
        if removed_phone:
            self.phones.remove(removed_phone)

    def edit_phone(self, old_phone: str, new_phone: str): # Редагування телефонів.
        eddited_old_phone = self.find_phone(old_phone)
        if not eddited_old_phone:
            raise ValueError('Old phone number not found.')

        eddited_new_phone = Phone(new_phone)
        index = self.phones.index(eddited_old_phone)
        self.phones[index] = eddited_new_phone
            
    def find_phone(self, phone: str): # Пошук телефону.
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict): # Клас для зберігання та управління записами.
    def add_record(self, record): # Додавання нового запису до адресної книги.
        self.data[record.name.value] = record

    def find(self, name: str): # Пошук записів за іменем.
        return self.data.get(name) 

    def delete(self, name: str): # Видалення записів за іменем.
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())