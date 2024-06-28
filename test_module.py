import unittest
from main import Student


class StudentTest(unittest.TestCase):

    def test_walk(self):
        self.alex = Student(name='Александр')
        self.alex.distance = 0
        for i in range(10): self.alex.walk()
        self.assertEqual(self.alex.distance, 500, f'Дистанции не равны [дистанция человека {self.alex.name}а] != 500')

    def test_run(self):
        self.maxim = Student(name='Максим')
        self.maxim.distance = 0
        for i in range(10): self.maxim.run()
        self.assertEqual(self.maxim.distance, 1000,
                         f'Дистанции не равны [дистанция человека {self.maxim.name}а] != 1000')

    def test_Compar(self):
        self.alex = Student(name='Александр')
        self.alex.distance = 0
        self.maxim = Student(name='Максим')
        self.maxim.distance = 0
        for i in range(10):
            self.alex.walk()
            self.maxim.run()
        self.assertGreater(self.maxim.distance, self.alex.distance,
                           f'{self.maxim.name} должен преодолеть дистанцию больше, чем {self.alex.name}')


if __name__ == '__main__':
    unittest.main()
