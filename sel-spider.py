from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))


#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#options = Options()
#options.binary_location = "/usr/bin/chromium-browser"

#driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=options)