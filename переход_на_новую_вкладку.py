from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
  
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

   
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


    WebDriverWait(browser, 10).until(
        EC.new_window_is_opened([browser.window_handles[0]])
    )

  
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input_value"))
    )
    x = x_element.text

 
    y = calc(x)


    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)


    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

  
    time.sleep(2)
    alert_text = browser.switch_to.alert.text
    print("Полученный результат:", alert_text)

finally:
  
    time.sleep(10)
    browser.quit()
