import unittest  #  модуль для тестирования
import pickle  #  модуль для сериализации объектов
import os  #  модуль для работы с файловой системой

from Main import *

class TestFlowerShop(unittest.TestCase):

    '''
    def test_flower_default(self):  # Тест для проверки значений по умолчанию у цветка
        flower = Flower()  # Создаем экземпляр цветка
        self.assertEqual(flower.name, "Незнакомый цветок")  # Проверяем имя
        self.assertEqual(flower.color, "неизвестный")  # Проверяем цвет
        self.assertEqual(flower.price, 0)  # Проверяем цену

    def test_flower_str(self):  # Тест для проверки строкового представления цветка
        flower = Flower("Лилия", "белый", 150)  # Создаем экземпляр цветка с заданными параметрами
        self.assertIn("Flower(ID:", str(flower))  # Проверяем наличие ID в строковом представлении
        self.assertIn("Name: Лилия", str(flower))  # Проверяем наличие имени в строковом представлении

    def test_bouquet_str(self):  # Тест для проверки строкового представления букета
        bouquet = Bouquet()  # Создаем экземпляр букета
        flower1 = Flower("Роза", "красный", 100)  # Создаем цветок
        flower2 = Flower("Тюльпан", "желтый", 80)  # Создаем другой цветок
        bouquet.add_flower(flower1)  # Добавляем первый цветок в букет
        bouquet.add_flower(flower2)  # Добавляем второй цветок в букет
        self.assertIn("Total Price: 180", str(bouquet))  # Проверяем наличие общей цены в строковом представлении

    def test_flower_destruction(self):  # Тест для проверки удаления цветка
        flower = Flower("Лилия", "белый", 150)  # Создаем экземпляр цветка
        del flower  # Удаляем цветок
        # Проверяем, что не возникает исключений при удалении.

    def test_transaction_history(self):  # Тест для проверки истории транзакций цветка
        flower = Flower("Лилия", "белый", 150)  # Создаем экземпляр цветка
        flower.set_name("Роза")  # Изменяем имя цветка
        self.assertEqual(len(flower.transaction_history), 1)  # Проверяем количество транзакций
        self.assertEqual(flower.transaction_history[0][1], "set_name")  # Проверяем тип операции

    def test_serialization(self):  # Тест для проверки сериализации и десериализации букета
        bouquet = Bouquet()  # Создаем экземпляр букета
        flower1 = Flower("Роза", "красный", 100)  # Создаем цветок
        bouquet.add_flower(flower1)  # Добавляем цветок в букет
        # Сериализация
        with open('bouquet.pkl', 'wb') as f:  # Открываем файл для записи
            pickle.dump(bouquet, f)  # Сериализуем букет
        # Десериализация
        with open('bouquet.pkl', 'rb') as f:  # Открываем файл для чтения
            loaded_bouquet = pickle.load(f)  # Десериализуем букет
        self.assertEqual(len(loaded_bouquet.flowers), 1)  # Проверяем количество цветов в загруженном букете
        self.assertEqual(loaded_bouquet.flowers[0].name, "Роза")  # Проверяем имя загруженного цветка

    def tearDown(self):  # Метод, выполняемый после каждого теста
        # Удаляем файл после тестирования сериализации
        if os.path.exists('bouquet.pkl'):  # Проверяем существование файла
            os.remove('bouquet.pkl')  # Удаляем файл

    def test_rose_creation(self):
        rose = Rose("красный", 100, 5)
        self.assertEqual(rose.name, "Роза")
        self.assertEqual(rose.thorn_length, 5)

    def test_tulip_description(self):
        tulip = Tulip("желтый", 50, 6)
        # Обновлённое ожидание с учетом количества лепестков
        self.assertEqual(tulip.get_description(), "Тюльпан - желтый, цена: 50, количество лепестков: 6")

    def test_set_price(self):
        tulip = Tulip("розовый", 60, 5)
        tulip.set_price(-10)  # Вывод сообщения о некорректной цене
        self.assertEqual(tulip.price, 60)  # Цена не должна измениться

        tulip.set_price(70)
        self.assertEqual(tulip.price, 70)  # Проверяем, что цена изменилась
        '''

    def test_price_exception(self):
        flower = Flower()
        with self.assertRaises(PriceException):
            flower.price = -10  # Установка отрицательной цены должна вызвать исключение

    def test_name_exception(self):
        flower = Flower()
        with self.assertRaises(NameException):
            flower.set_name("")  # Установка пустого имени должна вызвать исключение

    def test_add_flower_to_bouquet(self):
        bouquet = Bouquet()
        flower = Flower(name="Тюльпан", color="желтый", price=20)
        bouquet.add_flower(flower)

        self.assertEqual(len(bouquet.get_flowers()), 1)  # Проверяем, что цветок добавился

    def setUp(self):
        self.rose1 = Rose("красный", 100, 5)
        self.rose2 = Rose("белый", 120, 3)
        self.tulip1 = Tulip("жёлтый", 80, 6)

    def test_addition(self):
        mixed_flower = self.rose1 + self.rose2
        self.assertEqual(mixed_flower.price, 220)
        self.assertEqual(mixed_flower.name, "Смешанный")

    def test_subtraction(self):
        difference_flower = self.rose2 - self.rose1
        self.assertEqual(difference_flower.price, 20)
        self.assertEqual(difference_flower.name, "Разница")

    def test_multiplication(self):
        multiplied_flower = self.rose1 * 2
        self.assertEqual(multiplied_flower.price, 200)
        self.assertEqual(multiplied_flower.name, "Умноженный")

    def test_division(self):
        divided_flower = self.rose2 / 2
        self.assertEqual(divided_flower.price, 60)
        self.assertEqual(divided_flower.name, "Поделённый")

    def test_bouquet_price(self):
        bouquet = Bouquet()
        bouquet.add_flower(self.rose1)
        bouquet.add_flower(self.tulip1)
        self.assertEqual(bouquet.total_price(), 180)

class TestFlowerShop(unittest.TestCase):
    def setUp(self):
        self.shop = FlowerShop()
        self.flower1 = Flower("Роза", "красный", 100)
        self.flower2 = Flower("Тюльпан", "желтый", 70)
        self.shop.add_flower(self.flower1)
        self.shop.add_flower(self.flower2)

    def test_add_flower(self):
        self.assertEqual(len(self.shop.flowers), 2)

    def test_modify_flower(self):
        self.shop.modify_flower(self.flower1.id, name="Пион")
        self.assertEqual(self.flower1.name, "Пион")

    def test_delete_flower(self):
        self.shop.delete_flower(self.flower2.id)
        self.assertEqual(len(self.shop.flowers), 1)

    def test_view_flowers(self):
        self.assertTrue(len(self.shop.flowers) > 0)

if __name__ == "__main__":
    unittest.main()  # Запускаем тесты