from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# Функция для вычисления значения выражения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открыть браузер и перейти на страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # Нажать на кнопку
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Дождаться открытия новой вкладки
    WebDriverWait(browser, 10).until(
        EC.new_window_is_opened([browser.window_handles[0]])
    )

    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Ждём появления элемента с x
    x_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input_value"))
    )
    x = x_element.text

    # Посчитать функцию
    y = calc(x)

    # Ввести ответ
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    # Нажать Submit
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Получить текст из alert
    time.sleep(2)
    alert_text = browser.switch_to.alert.text
    print("Полученный результат:", alert_text)

finally:
    # Закрыть браузер через 10 секунд
    time.sleep(10)
    browser.quit()