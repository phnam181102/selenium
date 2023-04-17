import os
import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AuthenticationModule(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # set a 10 second timeout for all driver commands
        self.driver.implicitly_wait(10)

        # create the result_images folder if it doesn't exist
        if not os.path.exists('result_images'):
            os.makedirs('result_images')

    def tearDown(self):
        self.driver.quit()

    def test_user_cannot_login_with_wrong_password(self):
        self.driver.get('https://demo-unsen.myshopify.com')
        pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
        pw_input.send_keys('4')
        enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
        enter_btn.click()

        self.driver.get('https://demo-unsen.myshopify.com/account/login')

        # Enter email
        email_element = self.driver.find_element("name", 'customer[email]')
        email_element.send_keys('example@gmail.com')

        # create the folder for this test case's screenshots
        test_case_name = self.id().split('.')[-1]
        folder_name = os.path.join('result_images', self.__class__.__name__, test_case_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # save the screenshot of step 1
        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)

        # Enter wrong password
        password_element = self.driver.find_element("name", 'customer[password]')
        password_element.send_keys('wrong_password')

        # save the screenshot of step 2
        step2_image_path = os.path.join(folder_name, 'step2.png')
        self.driver.save_screenshot(step2_image_path)

        # Click on login button
        login_btn_element = self.driver.find_element("xpath", '//*[@id="customer_login"]/div[3]/button')
        login_btn_element.click()


        # Check the error message
        error_message_element = self.driver.find_element("xpath", '//*[@id="customer_login"]/div[1]/ul/li')
        expected_error_message = 'Incorrect email or password.'
        self.assertEqual(expected_error_message, error_message_element.text)


        # save the screenshot of step 3
        step3_image_path = os.path.join(folder_name, 'step3.png')
        self.driver.save_screenshot(step3_image_path)

    def test_user_cannot_login_with_blank_password(self):
        self.driver.get('https://demo-unsen.myshopify.com')
        pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
        pw_input.send_keys('4')
        enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
        enter_btn.click()
        self.driver.get('https://demo-unsen.myshopify.com/account/login')

        # Enter email
        email_element = self.driver.find_element("name", 'customer[email]')
        email_element.send_keys('example@gmail.com')

        # create the folder for this test case's screenshots
        test_case_name = self.id().split('.')[-1]
        folder_name = os.path.join('result_images', self.__class__.__name__, test_case_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # save the screenshot of step 1
        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)

        # Enter blank password
        password_element = self.driver.find_element("name", 'customer[password]')
        password_element.send_keys('')

        # save the screenshot of step 2
        step2_image_path = os.path.join(folder_name, 'step2.png')
        self.driver.save_screenshot(step2_image_path)

        # Click on login button
        login_btn_element = self.driver.find_element("xpath", '//*[@id="customer_login"]/div[3]/button')
        login_btn_element.click()


        # Check the error message
        error_message_element = self.driver.find_element("xpath", '//*[@id="customer_login"]/div[1]/ul/li')
        expected_error_message = 'Incorrect email or password.'
        self.assertEqual(expected_error_message, error_message_element.text)


        # save the screenshot of step 3
        step3_image_path = os.path.join(folder_name, 'step3.png')
        self.driver.save_screenshot(step3_image_path)

    def test_user_can_login_with_valid_credentials(self):
        self.driver.get('https://demo-unsen.myshopify.com')
        pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
        pw_input.send_keys('4')
        enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
        enter_btn.click()
        self.driver.get('https://demo-unsen.myshopify.com/account/login')

        # Enter email
        email_element = self.driver.find_element("name", 'customer[email]')
        email_element.send_keys('lji59738@nezid.com')

        # create the folder for this test case's screenshots
        test_case_name = self.id().split('.')[-1]
        folder_name = os.path.join('result_images', self.__class__.__name__, test_case_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # save the screenshot of step 1
        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)

        # Enter valid password
        password_element = self.driver.find_element("name", 'customer[password]')
        password_element.send_keys('abc.12345')

        # save the screenshot of step 2
        step2_image_path = os.path.join(folder_name, 'step2.png')
        self.driver.save_screenshot(step2_image_path)

        # Click on login button
        login_btn_element = self.driver.find_element("xpath", '//*[@id="customer_login"]/div[3]/button')
        login_btn_element.click()


        # Check the dashboard page is loaded
        current_url = self.driver.current_url
        expected_url = 'https://demo-unsen.myshopify.com/account'
        self.assertEqual(expected_url, current_url)


        # save the screenshot of step 3
        step3_image_path = os.path.join(folder_name, 'step3.png')
        self.driver.save_screenshot(step3_image_path)

    def test_user_cannot_register_with_invalid_email(self):
        self.driver.get('https://demo-unsen.myshopify.com')
        pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
        pw_input.send_keys('4')
        enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
        enter_btn.click()
        self.driver.get('https://demo-unsen.myshopify.com/account/register')

        # Enter first name
        first_name_element = self.driver.find_element("name", 'customer[first_name]')
        first_name_element.send_keys('Nam')

        # Enter last name
        last_name_element = self.driver.find_element("name", 'customer[last_name]')
        last_name_element.send_keys('Phan')

        # Enter invalid email
        email_element = self.driver.find_element("name", 'customer[email]')
        email_element.send_keys('example.com')

        # Enter password
        password_element = self.driver.find_element("name", 'customer[password]')
        password_element.send_keys('password123')

        test_case_name = self.id().split('.')[-1]
        folder_name = os.path.join('result_images', self.__class__.__name__, test_case_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # save the screenshot of step 1
        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)

        # Click on register button
        register_btn_element = self.driver.find_element("xpath", '//*[@id="create_customer"]/div[5]/button')
        register_btn_element.click()


        # Check the error message
        error_message_element = self.driver.find_element("xpath", '//*[@id="create_customer"]/ul/li/a')
        expected_error_message = 'Email is invalid'
        self.assertEqual(expected_error_message, error_message_element.text)

        # save the screenshot of the error message
        screenshot_path = os.path.join(folder_name, 'invalid_email.png')
        self.driver.save_screenshot(screenshot_path)

    def test_user_can_register_with_valid_credentials(self):
        self.driver.get('https://demo-unsen.myshopify.com')
        pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
        pw_input.send_keys('4')
        enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
        enter_btn.click()

        # Copy mail ảo
        self.driver.get("https://10minutemail.net")
        copy_btn = self.driver.find_element('xpath', '//*[@id="copy-button"]')
        copy_btn.click()
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + Keys.TAB)

        self.driver.get('https://demo-unsen.myshopify.com/account/register')

        # Enter first name
        first_name_element = self.driver.find_element("name", 'customer[first_name]')
        first_name_element.send_keys('Nam')

        # Enter last name
        last_name_element = self.driver.find_element("name", 'customer[last_name]')
        last_name_element.send_keys('Phan')


        # Enter valid email
        email_element = self.driver.find_element("name", 'customer[email]')
        email_element.send_keys(Keys.CONTROL + 'V')

        # Enter password
        password_element = self.driver.find_element("name", 'customer[password]')
        password_element.send_keys('password123')

        test_case_name = self.id().split('.')[-1]
        folder_name = os.path.join('result_images', self.__class__.__name__, test_case_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # save the screenshot of step 1
        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)


        # Click on register button
        register_btn_element = self.driver.find_element("xpath", '//*[@id="create_customer"]/div[5]/button')
        register_btn_element.click()


        # Check that registration was successful
        current_url = self.driver.current_url
        expected_url = 'https://demo-unsen.myshopify.com/'
        self.assertEqual(expected_url, current_url)

        # save the screenshot of the success message
        screenshot_path = os.path.join(folder_name, 'success.png')
        self.driver.save_screenshot(screenshot_path)

    def test_user_cannot_register_with_existing_email(self):
        self.driver.get('https://demo-unsen.myshopify.com')
        pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
        pw_input.send_keys('4')
        enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
        enter_btn.click()
        self.driver.get('https://demo-unsen.myshopify.com/account/register')

        # Enter first name
        first_name_element = self.driver.find_element("name", 'customer[first_name]')
        first_name_element.send_keys('Nam')

        # Enter last name
        last_name_element = self.driver.find_element("name", 'customer[last_name]')
        last_name_element.send_keys('Phan')

        # Enter existing email
        email_element = self.driver.find_element("name", 'customer[email]')
        email_element.send_keys('lji59738@nezid.com')

        # Enter password
        password_element = self.driver.find_element("name", 'customer[password]')
        password_element.send_keys('password123')

        test_case_name = self.id().split('.')[-1]
        folder_name = os.path.join('result_images', self.__class__.__name__, test_case_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # save the screenshot of step 1
        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)

        # Click on register button
        register_btn_element = self.driver.find_element("xpath", '//*[@id="create_customer"]/div[5]/button')
        register_btn_element.click()


        # Check the error message
        error_message_element = self.driver.find_element("xpath", '//*[@id="create_customer"]/ul/li')
        expected_error_message = 'This email address is already associated with an account. If this account is yours, you can reset your password'
        self.assertEqual(expected_error_message, error_message_element.text)

        # save the screenshot of the error message
        screenshot_path = os.path.join(folder_name, 'existing_email.png')
        self.driver.save_screenshot(screenshot_path)

class ShoppingCartModule(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # set a 10 second timeout for all driver commands
        self.driver.implicitly_wait(10)

        # create the result_images folder if it doesn't exist
        if not os.path.exists('result_images'):
            os.makedirs('result_images')

    def tearDown(self):
        self.driver.quit()

    def test_shopping_cart_displays_correct_product_information(self):
        self.driver.get('https://demo-unsen.myshopify.com')
        pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
        pw_input.send_keys('4')
        enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
        enter_btn.click()
        self.driver.get('https://demo-unsen.myshopify.com/account/login')

        # Enter email
        email_element = self.driver.find_element("name", 'customer[email]')
        email_element.send_keys('lji59738@nezid.com')

        # create the folder for this test case's screenshots
        test_case_name = self.id().split('.')[-1]
        folder_name = os.path.join('result_images', self.__class__.__name__,test_case_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)


        # Enter valid password
        password_element = self.driver.find_element("name", 'customer[password]')
        password_element.send_keys('abc.12345')


        # Click on login button
        login_btn_element = self.driver.find_element("xpath", '//*[@id="customer_login"]/div[3]/button')
        login_btn_element.click()

        self.driver.get('https://demo-unsen.myshopify.com/collections/women/products/polka-dot-tie-front-top')
        product_info_image_path = os.path.join(folder_name, 'product_info.png')
        self.driver.save_screenshot(product_info_image_path)

        origin_name = self.driver.find_element(By.CLASS_NAME, "t4s-product__title")
        origin_price = self.driver.find_element(By.CLASS_NAME, "t4s-product-price")

        add_to_cart_btn = self.driver.find_element(By.CLASS_NAME, "t4s-product-form__submit")
        add_to_cart_btn.click()

        time.sleep(1)

        cart_name = self.driver.find_element(By.CLASS_NAME, "t4s-mini_cart__title")
        cart_price = self.driver.find_element(By.CLASS_NAME, "t4s-cart_price")

        self.assertEqual(origin_name.text, cart_name.text)
        self.assertEqual(origin_price.text, cart_price.text)

        result_image_path = os.path.join(folder_name, 'result.png')
        self.driver.save_screenshot(result_image_path)