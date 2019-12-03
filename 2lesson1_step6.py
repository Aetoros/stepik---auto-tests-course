import math
from math import log
from math import sin

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")
i1 = browser.find_element_by_css_selector("#treasure")
i11 = i1.get_attribute("valuex")

i3 = calc(i11)

i5 = browser.find_element_by_css_selector("#answer")
i5.send_keys(i3)
i6 = browser.find_element_by_css_selector("#robotCheckbox")
i6.click()
i6 = browser.find_element_by_css_selector("#robotsRule")
i6.click()
i7 = browser.find_element_by_css_selector(".btn-default")
i7.click()
time.sleep(20)
browser.quit()

