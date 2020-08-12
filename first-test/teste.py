from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"C:\chromeselenium\chromedriver.exe")

browser.get("https://chartos.herokuapp.com")
 
a_funcionarios = browser.find_element_by_xpath("/html/body/nav/div/ul/li[@class='nav-item']").click()

print("era pra ter feito.")
print(a_funcionarios)
