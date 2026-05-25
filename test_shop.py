import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys




class Test_autorization(unittest.TestCase):
    
    def setUp(self):
        
        options_browser = Options()
        self.driver = webdriver.Chrome(options = options_browser)
        self.driver.get('https://www.saucedemo.com/')

        
    def tearDown(self):
        self.driver.quit()
    
    
    def test_username(self):
        
        input_username = self.driver.find_element(By.ID, "user-name")
        input_username.send_keys(t'standard_user')
        value_input = input_username.get_attribute("value")
        
        input_password = self.driver.find_element(By.ID, 'password')
        input_password.send_keys('secret_sauce')
        value_input_password = input_password.get_attribute("value")        
        
        btn_login = self.driver.find_element(By.ID, 'login-button')
        
        btn_login.click()
        
        # оэидаемый и фактический URL
        
        expected_url = 'https://www.saucedemo.com/inventory.html'
        actual_url = self.driver.current_url
        
        self.assertEqual(actual_url, expected_url)
        
       
        
        time.sleep(5)


    def test_login_invalid_password(self):
        
        input_username = self.driver.find_element(By.ID, "user-name")
        input_username.send_keys('standard_user')
        value_input = input_username.get_attribute("value")
        
        input_password = self.driver.find_element(By.ID, 'password')
        input_password.send_keys('wrong_password')
        value_input_password = input_password.get_attribute("value")        
        
        btn_login = self.driver.find_element(By.ID, 'login-button')
        btn_login.click()  
        # Проверка того, что мы остались на прежней странице и никуда не перешли 
        expected_url = 'https://www.saucedemo.com/'
        actual_url = self.driver.current_url
        self.assertEqual(actual_url, expected_url)
        # Поиск ошибки и название ошибки
        error = self.driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
        self.assertTrue(error.is_displayed())
        self.assertEqual(error.text, 'Epic sadface: Username and password do not match any user in this service' )
         
        time.sleep(2)
        
    def test_login_with_enter(self):
        
        input_username = self.driver.find_element(By.ID, "user-name")
        input_username.send_keys('standard_user')
        value_input = input_username.get_attribute("value")
        
        input_password = self.driver.find_element(By.ID, 'password')
        input_password.send_keys('secret_sauce')
        value_input_password = input_password.get_attribute("value")
                
        input_password.send_keys(Keys.ENTER)
        
        expected_url = 'https://www.saucedemo.com/inventory.html'
        actual_url = self.driver.current_url
        self.assertEqual(actual_url, expected_url)
        
        self.driver.get('https://www.saucedemo.com/inventory.html')
        all_items = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name ')
        
        if len(all_items) > 0:
            is_visible = all_items[0].is_displayed()
            self.assertTrue(is_visible)
   
        
        
        time.sleep(2)
                  
        
        
class TestProducts(unittest.TestCase):
    
    def setUp(self):
        
        options = Options()

        prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
}

        options.add_experimental_option("prefs", prefs)

        options.add_argument("--disable-notifications")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-features=PasswordLeakDetection")
        self.driver = webdriver.Chrome(options = options)
        
        self.driver.get('https://www.saucedemo.com/')
        
        input_username = self.driver.find_element(By.ID, "user-name")
        input_username.send_keys('standard_user')
        value_input = input_username.get_attribute("value")
        
        input_password = self.driver.find_element(By.ID, 'password')
        input_password.send_keys('secret_sauce')
        value_input_password = input_password.get_attribute("value")        
        
        btn_login = self.driver.find_element(By.ID, 'login-button')
        
        btn_login.click()
        
    def tearDown(self):
        self.driver.quit()
        
    def test_all_products(self):
        
        all_items = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name ')
        
        if len(all_items) > 0:
            is_visible = all_items[0].is_displayed()
            self.assertTrue(is_visible)
        else:
            self.fail('ни одного товара не найдено')
            
        self.assertTrue(len(all_items) >0 )
        
        items = []
        for item in all_items:
            items.append(item.text)
        print(items)
        
        
    def test_add_to_cart(self):
        # Находим все кнопки добавления товара в корзину
        buttons = self.driver.find_elements(By.CSS_SELECTOR, '.btn.btn_primary.btn_small.btn_inventory')
        
        # определяем кол-во найденных кнопок      
        count_buttons = (len(buttons))
        
        # определяем сколько кнопок было нажато 
        clicked_count = 0
        
        # проходимся циклом по всем кнопкам и нажимаем на каждую кнопку
        for item in buttons:
            item.click()
            clicked_count += 1

            
           
        time.sleep(2)

        # находим  кол-во товаров в корзине
        cart = self.driver.find_elements(By.CLASS_NAME,'shopping_cart_badge')
        
        # В переменной cart хранится объект класса WebElement. Для того чтобы  достать  значение применяем .text 
        value = cart[0].text
        
        # делаем из значения число 
        number_of_value = int(value)
         
        # сравниваем число показывающее кол-во товаров в корзине с числом 6   
        self.assertEqual(number_of_value,6)
        
        # сравниваем число показывающее сколько кнопок было нажато с числом указывающим сколько товаров находится в корзине 
        self.assertEqual(clicked_count,number_of_value)
        
        time.sleep(2)

        
    # def test_data_product(self):
        
    #     all_items =  self.driver.find_elements(By.CLASS_NAME,'inventory_item_description')
        
    #     collected_data = []
        
    #     for item in all_items:
            
    #         name = item.find_element(By.CLASS_NAME,'inventory_item_name ').text
    #         price = item.find_element(By.CLASS_NAME,'inventory_item_price').text 

    #         collected_data.append ({
                
    #             'name' :name,
    #             'price':price
            
    #         })
            
    #         print(f"товар: {name}, стоит {price}")

    
            
        
        
        
        
        

if __name__ == "__main__":
    unittest.main()
        
    
# python -m unittest + название файла который нажо запустить + . название класса + . функция 
#  python -m unittest -v  