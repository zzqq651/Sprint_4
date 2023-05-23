from dataclasses import dataclass
from page_object.locators import MainPageLocators


@dataclass
class User:
    enter_button: list
    station: str
    name: str
    last_name: str
    address_to_take: str
    phone_number: str
    date: str
    index: int
    color_index: int
    message: str


user_1 = User(MainPageLocators.button_order_up,
                  "Клубная", "Иван", "Иванов",
                  "Москва, ул Карла, 11 кв 11", "89998887766",
                  "10.02.2023", 3, 1, "Тест")


user_2 = User(MainPageLocators.button_order_down,
                  "Пушкина", "Петр", "Петров",
                  "Москва, ул Маркса, 8 кв 12", "89123456789",
                  "11.04.2023", 4, 0, "Тест")


class Urls:
    dzen_url = ('https://dzen.ru/?yredirect=true')
    samokat_url = ('https://qa-scooter.praktikum-services.ru/')


class DataExample:
    dictionary_question_and_answers = {"Сколько это стоит? И как оплатить?": "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
                      "Хочу сразу несколько самокатов! Так можно?": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
                      "Как рассчитывается время аренды?": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
                      "Можно ли заказать самокат прямо на сегодня?": "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
                      "Можно ли продлить заказ или вернуть самокат раньше?": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
                      "Вы привозите зарядку вместе с самокатом?": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
                      "Можно ли отменить заказ?": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
                      "Я жизу за МКАДом, привезёте?": "Да, обязательно. Всем самокатов! И Москве, и Московской области."}