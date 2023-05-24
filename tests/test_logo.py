import allure
from page_object.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from page_object.locators import MainPageLocators
from selenium.webdriver.common.by import By
from data import Urls as u


class TestNavigitationLogo:
    @allure.title("Проверка навигации с помощью кнопки логотипа 'Самоката'")
    def test_click_on_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_order()
        main_page.click_on_logo_scooter()
        main_page.checking_tabs()
        element = driver.find_element(By.XPATH, ".//button[@class='App_CookieButton__3cvqF' and text()='да все привыкли']").text

        assert driver.current_url == u.samokat_url and element == 'да все привыкли', 'Навигация на главную страницу «Самоката».'


    @allure.title("Проверка навигации с помощью кнопки логотипа 'Яндекса'")
    def test_click_on_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_logo_yandex()
        main_page.checking_tabs()
        element = driver.find_element(By.XPATH, ".//div[@class='card-news-header__title-2F' and @aria-label='Новости на тему']").text

        assert driver.current_url == u.dzen_url and element == "Сейчас в СМИ", 'В новом окне должна открыться главная страница Яндекса(Дзен).'