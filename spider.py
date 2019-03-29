from selenium import webdriver

# create an instance of the webdrive in this case Firefox
browser = webdriver.Firefox()
# open the website
url = '''https://www.zse.co.zw/index.php?option=com_content&view=article&id=135&itemid=249'''
admin_url = '''https://www.zse.co.zw/administrator'''
browser.get(url)

username = browser.find_element_by_name('username')
password = browser.find_element_by_name('password')

username.send_keys('admin')
password.send_keys('admin')

login_attempt = browser.find_element_by_name('Submit')
login_attempt.submit()


