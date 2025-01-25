import uuid
import pickle
import datetime
import time
from functools import wraps

# Декоратор для измерения времени выполнения метода
def execution_time_tracker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения {func.__name__}: {end_time - start_time:.4f} секунд")
        return result
    return wrapper

# Декоратор для подсчёта вызовов метода
def call_count_tracker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Вызов метода {func.__name__}: {wrapper.calls} раз")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

# Исключение для цветочной ошибки
class FlowerException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

# Исключение для неверной цены
class PriceException(FlowerException):
    pass

# Исключение для неверного имени цветка
class NameException(FlowerException):
    pass

# Класс, представляющий цветок
class Flower:
    def __init__(self, name="Незнакомый цветок", color="неизвестный", price=0):
        self.id = uuid.uuid4()  # Генерация уникального ID для каждого цветка
        self.__name = name  # Имя цветка
        self.__color = color  # Цвет цветка
        self.price = price  # Цена цветка
        self.__transaction_history = []  # История транзакций
        self._call_counts = {}  # Инициализация _call_counts для всех экземпляров

    def __str__(self):
        return f"Flower(ID: {self.id}, Name: {self.__name}, Color: {self.__color}, Price: {self.__price})"

    @execution_time_tracker# Декоратор для отслеживания времени выполнения метода
    @call_count_tracker# Декоратор для отслеживания количества вызовов метода
    def set_name(self, name):
        if not name:
            raise NameException("Имя не может быть пустым!") # Проверка на пустое имя
        old_name = self.__name# Сохраняем старое имя для истории
        self.__name = name # Устанавливаем новое имя
        self.__transaction_history.append((datetime.datetime.now(), "set_name", old_name, name)) # Логи изменений имени

    @execution_time_tracker
    @call_count_tracker
    def get_description(self):
        return f"{self.__name} - {self.__color}, цена: {self.price}"# Возвращаем описание цветка

    # Состояния, используя свойства
    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise PriceException("Цена должна быть положительной!")
        self.__price = new_price

    # Метод для получения описания цветка
    def get_description(self):
        return f"{self.__name} - {self.__color}, цена: {self.__price}"

    def set_name(self, name):
        if not name:
            raise NameException("Имя не может быть пустым!")
        old_name = self.__name
        self.__name = name
        self.__transaction_history.append((datetime.datetime.now(), "set_name", old_name, name))

    def __del__(self):
        print(f"Цветок {self.__name} удаляется.")

    def __add__(self, other):
        if isinstance(other, Flower):
            return Flower("Смешанный", "разный", self.price + other.price)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Flower):
            return Flower("Разница", "разный", self.price - other.price)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Flower("Умноженный", self.color, self.price * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)) and other != 0:
            return Flower("Поделённый", self.color, self.price / other)
        return NotImplemented

class FlowerShop:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def modify_flower(self, flower_id, name=None, color=None, price=None):
        for flower in self.flowers:
            if flower.id == flower_id:
                if name:
                    flower.set_name(name)
                if color:
                    flower.__color = color
                if price is not None:
                    flower.price = price
                return
        print("Цветок не найден.")

    def delete_flower(self, flower_id):
        self.flowers = [flower for flower in self.flowers if flower.id != flower_id]

    def view_flowers(self):
        for flower in self.flowers:
            print(flower)

# Класс, представляющий розу
class Rose(Flower):
    def __init__(self, color, price, thorn_length):
        super().__init__("Роза", color, price)  # Вызываем конструктор родителя
        self.__thorn_length = thorn_length  # Длина шипов

    @execution_time_tracker
    @call_count_tracker
    def get_description(self):
        return super().get_description() + f", длина шипов: {self.__thorn_length} см"


# Класс, представляющий тюльпан
class Tulip(Flower):
    def __init__(self, color, price, petal_count):
        super().__init__("Тюльпан", color, price)  # Вызываем конструктор родителя
        self.__petal_count = petal_count  # Количество лепестков

    @execution_time_tracker # Декоратор для отслеживания времени выполнения метода
    @call_count_tracker# Декоратор для отслеживания количества вызовов метода
    def get_description(self):
        return f"{self.name} - {self.color}, цена: {self.price}, количество лепестков: {self.__petal_count}"# Возвращаем строку с описанием тюльпана


# Класс, представляющий букет
class Bouquet:
    def __init__(self):
        self.__flowers = []  # Список для хранения цветов в букете
        self.__transaction_history = []  # История транзакций
        self._call_counts = {}  # Инициализация _call_counts для всех экземпляров

    @execution_time_tracker
    @call_count_tracker
    def add_flower(self, flower):
        self.__flowers.append(flower) # Добавляем цветок в список
        self.__transaction_history.append((datetime.datetime.now(), "add_flower", None, flower)) # Логируем операцию добавления

    def get_flowers(self):
        return self.__flowers # Возвращаем список цветков в букете

    @execution_time_tracker
    @call_count_tracker
    def total_price(self):
        return sum(flower.price for flower in self.__flowers)  # Суммируем цены всех цветов

    def __str__(self):
        flowers_str = ', '.join(str(flower) for flower in self.__flowers)  # Преобразуем каждый цветок в строку
        return f"Bouquet(Flowers: [{flowers_str}], Total Price: {self.total_price()})" # Возвращаем строку с информацией о букете

    def serialize(self):
        with open('bouquet.pkl', 'wb') as f:
            pickle.dump(self, f)# Сохраняем состояние букета в файл

    @staticmethod
    def deserialize():
        with open('bouquet.pkl', 'rb') as f:
            return pickle.load(f) # Загружаем состояние букета из файла

    def __del__(self):
        print("Букет удаляется.") # Выводим сообщение при удалении объекта букета



# Тестирование декораторов
def test_decorators():
    rose = Rose("красный", 100, 5)
    tulip = Tulip("жёлтый", 80, 6)

    print(rose.get_description())
    print(tulip.get_description())

    # Тестируем добавление в букет
    bouquet = Bouquet()
    bouquet.add_flower(rose)
    bouquet.add_flower(tulip)
    print(f"Общая цена букета: {bouquet.total_price()}")# Выводим общую цену букета

    # Проверяем вызовы
    print(f"Количество вызовов set_name: {rose._call_counts.get('set_name', 0)}") # Выводим количество вызовов метода set_name для розы
    print(f"Количество вызовов get_description: {rose._call_counts.get('get_description', 0)}")# Количество вызовов метода get_description для розы
    print(f"Количество вызовов add_flower: {bouquet._call_counts.get('add_flower', 0)}")# Количество вызовов метода add_flower для букета
    print(f"Количество вызовов total_price: {bouquet._call_counts.get('total_price', 0)}")# Количество вызовов метода total_price для букета


if __name__ == "__main__":
    default_flower = Flower()  # Создание цветка по умолчанию
    print(default_flower)  # Печать объекта цветка
    rose = Rose("красный", 100, 5)  # Создание цветка розы с параметрами
    print(rose)  # Вывод розы
    bouquet = Bouquet()  # Создание нового букета
    bouquet.add_flower(rose)  # Добавление розы в букет
    bouquet.add_flower(default_flower)
    print(bouquet)  # Вывод букета с его цветами и общей ценой
    test_decorators()