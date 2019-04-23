# ===== unittest =====
Тестирование

Unit test - изолировано проверяет работу какого отдельного компонента системы(класс, функция)
Integration test - проверяет взаимодействие между компонентами

Для чего:
- тесты помогают ускорить процесс дебагинга, поиска ошибок, поддержки
- тесты помогают структурировать свои знания о проекте
- обязательны в больших проектах

Когда тестировать:
- если чтото может сломаться это должно быть тестировано(модель, отображение итд)
- каждый тест должен тестировать одну функцию
- тесты должны быть простыми и независимыми друг от друга
- нужно производить тестирование каждый раз когда хоешь чтото запушить или после пула
- тесты должны быть быстрыми

Структура:
- структура тестов должна вписываться в структуру проекта
- если тестов много нужно создать отдельную папку(test_models, test_views)
- обычно файл называют tests.py или test_smth.py



import unittest as ut

class TestName(ut.TestCase):
    def setUp(self):  # instructions before test
        pass

    def test_smth(self):  # test case
       self.assertEqual()

    def tearDown(self):  # instructions after test
        pass

# -= test functions =-
assertEqual(a, b)  # a == b
assertNotEqual(a, b)  # a != b
assertTrue(x)  # bool(x) is True
assertFalse(x)  # bool(x) is False
assertIs(a, b)   # a is b
assertIsNot(a, b)   # a is not b
assertIsNone(x)  # x is None
assertIsNotNone(x)  # x is not None
assertIn(a, b)   # a in b
assertNotIn(a, b)   # a not in b
assertIsInstance(a, b)  # isinstance(a, b)
assertNotIsInstance(a, b)   # not isinstance(a, b)
assertRaises(exc, fun, *args, **kwds)  # fun(*args, **kwds) порождает исключение exc
assertRaisesRegex(exc, r, fun, *args, **kwds)  # fun(*args, **kwds) порождает исключение exc и сообщение соответствует регулярному выражению r
assertWarns(warn, fun, *args, **kwds)  # fun(*args, **kwds) порождает предупреждение
assertWarnsRegex(warn, r, fun, *args, **kwds)  # fun(*args, **kwds) порождает предупреждение и сообщение соответствует регулярному выражению r
assertAlmostEqual(a, b)  # round(a-b, 7) == 0
assertNotAlmostEqual(a, b)  # round(a-b, 7) != 0
assertGreater(a, b)  # a > b
assertGreaterEqual(a, b)  # a >= b
assertLess(a, b)  # a < b
assertLessEqual(a, b)  # a <= b
assertRegex(s, r)  # r.search(s)
assertNotRegex(s, r)  # not r.search(s)
assertCountEqual(a, b)  # a и b содержат те же элементы в одинаковых количествах, но порядок не важен

# -= command line usage =-

# can run whole test module, class or even methods
# python -m unittest -v test_module1 test_module2  # -v(flag) to get more details
# python -m unittest test_module.TestClass
# python -m unittest test_module.TestClass.test_method
