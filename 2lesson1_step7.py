
from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://SunInJuly.github.io/execute_script.html")
i1 = browser.find_element_by_css_selector("#input_value")
i2 = i1.text
i3 = calc(i2)
i4 = browser.find_element_by_css_selector('#robotCheckbox')
browser.execute_script("return arguments[0].scrollIntoView(true);", i4)
i6 = browser.find_element_by_css_selector('#robotCheckbox')
i6.click()
i7 = browser.find_element_by_css_selector('#robotsRule')
i7.click()
i8 = browser.find_element_by_css_selector('#answer')
i8.send_keys(i3)
i7 = browser.find_element_by_css_selector("button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", i7)
i7.click()
time.sleep(20)
browser.quit()