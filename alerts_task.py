from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import math

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

    second_window=browser.window_handles[1]
    browser.switch_to.window(second_window)

    x = browser.find_element(By.ID, "input_value").text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()



#работа с переключением между вкладками

# new_window = browser.window_handles[1] - нашли вторую по порядку вкладку и засунули в переменную
# browser.switch_to.window(new_window) - переключились на вторую вкладку

# first_window = browser.window_handles[0] - определили первую по порядку вкладку, потом можно вернуться на нее