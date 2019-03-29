from selenium import webdriver

# create an instance of the webdrive in this case Firefox
browser = webdriver.Firefox()
# open the website
browser.get('http://0.0.0.0:5000')

# lets find the input fields
username = browser.find_element_by_name('name')
password = browser.find_element_by_name('password')

# fill in the input fields
username.send_keys('admin')
password.send_keys('admin')

# lets submit the form
# note: you can find elements by tag_name, id, name
login_attempt = browser.find_element_by_tag_name('button')
# submit the form
login_attempt.submit()
