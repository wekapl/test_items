import time


class TestInternetMarket(object):
    def test_find_button(self, browser):
        #
        # пример ссылки на товар
        #
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        #
        # ищем кнопки для добавления товара в корзину
        #
        button = browser.find_elements_by_xpath \
            (".//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
        #
        # вывод ошибки, если найденое количество кнопок меньше или равно 0
        #
        assert 0 < len(button), \
            "кнопка добавления товара в корзину не найдена"
        # добавить строку при проверке теста
        time.sleep(30)
        #
