import math
import time
from selenium import webdriver


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")
i1 = browser.find_element_by_css_selector("#num1")
i11 = i1.text
i2 = browser.find_element_by_css_selector("#num2")
i12 = i2.text
i4 = str(int(i11)+int(i12))


from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(i4) 
button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(20)
browser.quit()

