import process_data as pd
import unittest

test1_data = [
    {
        "mobile-url": "https://trudvsem.ru/vacancy/card/1027739174033/6bf457e6-51d8-11e6-853e-037acc02728d",
        "description": "<p>Умение общаться по телефону и лично, доброжелательность, ответственность, стрессоустойчивость.</p>",
        "update-date": "2016-10-02 01:33:38 MSK",
        "employment": "Частичная занятость",
        "job-name": "Администратор на телефоне",
        "company": {
            "email": "on.klinik@mail.ru",
            "contact-name": "Светлана",
            "hr-agency": True,
            "phone": "+7(495)6084488",
            "name": "ООО РОЯЛ КЛИНИК"
        },
        "term": "<p>Присутствуют по результатам работы</p>",
        "addresses": {
            "address": {
                "location": "г. Москва, Кузнецкий Мост улица, 1",
                "lat": 55.760808,
                "lng": 37.615713
            }
        },
        "url": "https://trudvsem.ru/vacancy/card/1027739174033/6bf457e6-51d8-11e6-853e-037acc02728d",
        "salary": "от 27000",
        "duty": "<p>Консультирование клиентов по услугам медицинского центра и скидкам. Ориентирование клиента от метро до офиса.</p>",
        "creation-date": "2016-10-02 00:00:00 MSK",
        "requirement": {
            "qualification": "<p>Неполный рабочий день (несколько часов в день) утро/вечер. Стабильные выплаты каждые 2 недели. Работа по договору. Фиксированный оклад 15 000 +бонусы.Дружный коллектив.</p>",
            "education": "Среднее"
        },
        "currency": "«руб.»",
        "schedule": "Неполный рабочий день",
        "category": {
            "industry": "Работы, не требующие квалификации"
        }
    }]

test2_data = ["Программист","администратор","программист python","ПРОГРАММИСТ","НЕПРОГРАММИСТ","программист крутой"]

class TestMyModule(unittest.TestCase):
    def test_f1(self):
        self.assertEqual(pd.f1(test1_data),["Администратор на телефоне"])
    def test_f2(self):
        self.assertEqual(pd.f2(test2_data),["Программист","программист python","ПРОГРАММИСТ","программист крутой"])
    def test_f3(self):
        self.assertEqual(pd.f3(["1","2","3","4"]),["1 с опытом Python","2 с опытом Python","3 с опытом Python","4 с опытом Python"])
    


if __name__ == '__main__':
    unittest.main()


