from unittest import TestCase
from Lion import Lion

import unittest

class Lion_test(TestCase):
    def setUp(self):
        self.test_subject = "охотник"
        self.test_row = {("охотник", "сытый"): ("Лев убегает. Проголодался.", "голодный")}
        self.test_state = "сытый"
        
        self.Lion = Lion(self.test_row, self.test_state)


    def test_init(self):
        self.assertEqual(self.Lion.state_table, self.test_row, "ошибка инициализации таблицы")
        self.assertEqual(self.Lion.state, self.test_state, "ошибка инициализации состояния")

    def test_action(self):
        self.return_action = self.Lion.action(self.test_subject)
        self.assertEqual(self.return_action, self.test_row[self.test_subject, self.test_state][0], "возвращено неверное значение")
        self.assertEqual(self.Lion.state, self.test_row[self.test_subject, self.test_state][1], "не изменилось состояние Льва")

    def test_negative(self):
        self.assertRaises(Exception, self.Lion.action, "йцукен")



if __name__ == '__main__':
    unittest.main()
