import logging
import unittest

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)


class Runner:
    def __init__(self, name, speed):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if speed < 0:
            raise ValueError("Speed must be non-negative")
        self.name = name
        self.speed = speed


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("John", -5)
        except ValueError:
            logging.warning("Неверная скорость для Runner")
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(123, 10)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
        else:
            logging.info('"test_run" выполнен успешно')


if __name__ == '__main__':
    unittest.main()
