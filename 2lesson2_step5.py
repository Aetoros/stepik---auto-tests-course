from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
i1 = browser.find_element_by_css_selector("[type='submit']")
i1.click()
window_name = browser.window_handles[1]
browser.switch_to.window(window_name)
i2 = browser.find_element_by_css_selector("#input_value")
i3 = i2.text
i4 = calc(i3)
i5 = browser.find_element_by_css_selector("#answer")
i5.send_keys(i4)
i5 = browser.find_element_by_css_selector("button.btn")
i5.click()
time.sleep(20)
browser.quit()
