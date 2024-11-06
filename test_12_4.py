import logging
import rt_with_exceptions
import unittest

class RunnerTest(unittest.TestCase):
    # настройте basicConfig на следующие параметры:
    # Уровень - INFO
    # Режим - запись с заменой('w')
    # Название файла - runner_tests.log
    # Кодировка - UTF-8
    # Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
    def setUp(self):
        logging.basicConfig(level=logging.INFO,
                            filemode='w',
                            filename='runner_tests.log',
                            encoding='utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')

#     Дополните метод тестирования test_walk:
#     Оберните основной код конструкцией try-except.
#     При создании объекта Runner передавайте отрицательное значение в speed.
#     В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
#     В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
    def test_wolk(self):
        try:
            run_wolk = rt_with_exceptions.Runner('Wolk', -5)
            for _ in range(10):
                run_wolk.walk()
            logging.info('"test_walk" выполнен успешно', exc_info=True)
            self.assertEqual(run_wolk.distance, 50)
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

#test_run:
    # Оберните основной код конструкцией try-except.
    # При создании объекта Runner передавайте что-то кроме строки в name.
    # В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
    # В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".
    def test_run(self):
        try:
            run_run = rt_with_exceptions.Runner(10, 10)
            for _ in range(10):
                run_run.run()
            logging.info('"test_run" выполнен успешно', exc_info=True)
            self.assertEqual(run_run.distance, 200)
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        run_wolk = rt_with_exceptions.Runner('Wolk')
        run_run = rt_with_exceptions.Runner('Run')

        for _ in range(10):
            run_wolk.walk()
            run_wolk.run()

        for _ in range(9):
            run_run.walk()
            run_run.run()

        self.assertNotEqual(run_wolk.distance, run_run.distance)

if __name__ == '__main__':
    unittest.main()



