
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
        input_username.send_keys('standard_user')
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
        
        options_browser = Options()
        self.driver = webdriver.Chrome(options = options_browser)
        
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
        
        add_to_cart = self.driver.find_elements(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
      
        for item in add_to_cart:
            item.click()
        
        cart = self.driver.find_element(By.CLASS_NAME,'shopping_cart_link')
        
        print(cart.text)
            
       
            
        



        time.sleep(2)

        
    
    
            
        
        
        
        
        

if __name__ == "__main__":
    unittest.main()
        
    
