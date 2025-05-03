from behave import given, when, then
from process_data import f1, f2, f3

@given('I have a list of dictionaries with resume')
def step_impl(context):
    context.data = [
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

@given('I have a list of job names')
def step_impl(context):
    context.data = ["Программист","администратор","программист python","ПРОГРАММИСТ","НЕПРОГРАММИСТ","программист крутой"]

@when('I call function f1 with this list')
def step_impl(context):
    context.result = f1(context.data)

@then('I should get a sorted list of job names')
def step_impl(context):
    assert context.result == ["Администратор на телефоне"]

@when('I call function f2 with this list')
def step_impl(context):
    context.result = f2(context.data)

@then('I should get a list of job names starting with "программист"')
def step_impl(context):
    assert context.result == ["Программист","программист python","ПРОГРАММИСТ","программист крутой"]

@when('I call function f3 with this list')
def step_impl(context):
    context.result = f3(context.data)

@then('I should get a list of job names with " с опытом Python" appended')
def step_impl(context):
    assert context.result == ["Программист с опытом Python","администратор с опытом Python","программист python с опытом Python","ПРОГРАММИСТ с опытом Python","НЕПРОГРАММИСТ с опытом Python","программист крутой с опытом Python"]
