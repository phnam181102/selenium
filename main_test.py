import os
import time
import unittest
from selenium import webdriver
from selenium.common import NoAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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

    def test_wrong_password_login(self):
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
        time.sleep(1)
        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)

        # Enter wrong password
        password_element = self.driver.find_element("name", 'customer[password]')
        password_element.send_keys('wrong_password')

        # save the screenshot of step 2
        time.sleep(1)
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
        time.sleep(1)
        step3_image_path = os.path.join(folder_name, 'step3.png')
        self.driver.save_screenshot(step3_image_path)

    def test_unregistered_email_login(self):
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
        time.sleep(1)
        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)

        # Enter blank password
        password_element = self.driver.find_element("name", 'customer[password]')
        password_element.send_keys('')

        # save the screenshot of step 2
        time.sleep(1)
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
        time.sleep(1)
        step3_image_path = os.path.join(folder_name, 'step3.png')
        self.driver.save_screenshot(step3_image_path)

    def test_blank_fields_login(self):
        self.driver.get('https://demo-unsen.myshopify.com')
        pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
        pw_input.send_keys('4')
        enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
        enter_btn.click()
        self.driver.get('https://demo-unsen.myshopify.com/account/login')

        # create the folder for this test case's screenshots
        test_case_name = self.id().split('.')[-1]
        folder_name = os.path.join('result_images', self.__class__.__name__, test_case_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # save the screenshot
        time.sleep(1)
        step2_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step2_image_path)


        # Click on login button
        login_btn_element = self.driver.find_element("xpath", '//*[@id="customer_login"]/div[3]/button')
        login_btn_element.click()

        time.sleep(2)

        # Check the error message
        error_message_element = self.driver.find_element("xpath", '//*[@id="customer_login"]/div[1]/ul/li')
        expected_error_message = 'Incorrect email or password.'
        self.assertEqual(expected_error_message, error_message_element.text)


        # save the screenshot of step 3
        time.sleep(1)
        step3_image_path = os.path.join(folder_name, 'result.png')
        self.driver.save_screenshot(step3_image_path)

    def test_valid_credentials_login(self):
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
        time.sleep(1)
        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)

        # Enter valid password
        password_element = self.driver.find_element("name", 'customer[password]')
        password_element.send_keys('abc.12345')

        # save the screenshot of step 2
        time.sleep(1)
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
        time.sleep(1)
        step3_image_path = os.path.join(folder_name, 'step3.png')
        self.driver.save_screenshot(step3_image_path)

    def test_invalid_email_registration(self):
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
        time.sleep(1)
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

    def test_blank_fields_registration(self):
        self.driver.get('https://demo-unsen.myshopify.com')
        pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
        pw_input.send_keys('4')
        enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
        enter_btn.click()
        self.driver.get('https://demo-unsen.myshopify.com/account/register')

        test_case_name = self.id().split('.')[-1]
        folder_name = os.path.join('result_images', self.__class__.__name__, test_case_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # save the screenshot of step 1
        time.sleep(1)
        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)

        # Click on register button
        register_btn_element = self.driver.find_element("xpath", '//*[@id="create_customer"]/div[5]/button')
        register_btn_element.click()

        time.sleep(2)

        # Check the error password
        error_password_element = self.driver.find_element("xpath", '//*[@id="create_customer"]/ul/li[1]/a')
        expected_error_pw_message = "Password can't be blank"
        self.assertEqual(expected_error_pw_message, error_password_element.text)

        # Check the error email
        error_email_element = self.driver.find_element("xpath", '//*[@id="create_customer"]/ul/li[2]/a')
        expected_error_email_message = "Email can't be blank"
        self.assertEqual(expected_error_email_message, error_email_element.text)

        # save the screenshot of the error message
        time.sleep(1)
        screenshot_path = os.path.join(folder_name, 'result.png')
        self.driver.save_screenshot(screenshot_path)

    def test_valid_credentials_registration(self):
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
        time.sleep(1)
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
        time.sleep(1)
        screenshot_path = os.path.join(folder_name, 'success.png')
        self.driver.save_screenshot(screenshot_path)

    def test_existing_email_registration(self):
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
        time.sleep(1)
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
        time.sleep(1)
        screenshot_path = os.path.join(folder_name, 'existing_email.png')
        self.driver.save_screenshot(screenshot_path)

    def test_reset_password_unregistered_email(self):
        self.driver.get('https://demo-unsen.myshopify.com')
        pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
        pw_input.send_keys('4')
        enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
        enter_btn.click()
        self.driver.get('https://demo-unsen.myshopify.com/account/login#recover')

        # Enter email
        first_name_element = self.driver.find_element("xpath", '//*[@id="RecoverEmail"]')
        first_name_element.send_keys('example@gmail.com')

        test_case_name = self.id().split('.')[-1]
        folder_name = os.path.join('result_images', self.__class__.__name__, test_case_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # save the screenshot of step 1
        time.sleep(1)
        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)

        # Click on reset password button
        reset_pw_btn = self.driver.find_element("xpath", '//*[@id="recover"]/form/div[2]/button')
        reset_pw_btn.click()

        time.sleep(2)

        # Check the error message
        error_message_element = self.driver.find_element("xpath", '//*[@id="RecoverEmail-email-error"]')
        expected_error_message = 'No account found with that email.'
        self.assertEqual(expected_error_message, error_message_element.text)

        # save the screenshot of the error message
        screenshot_path = os.path.join(folder_name, 'result.png')
        self.driver.save_screenshot(screenshot_path)

    def test_reset_password_blank_email(self):
        self.driver.get('https://demo-unsen.myshopify.com')
        pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
        pw_input.send_keys('4')
        enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
        enter_btn.click()
        self.driver.get('https://demo-unsen.myshopify.com/account/login#recover')

        test_case_name = self.id().split('.')[-1]
        folder_name = os.path.join('result_images', self.__class__.__name__, test_case_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # save the screenshot of step 1
        time.sleep(1)
        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)

        # Click on reset password button
        reset_pw_btn = self.driver.find_element("xpath", '//*[@id="recover"]/form/div[2]/button')
        reset_pw_btn.click()

        time.sleep(2)

        # Check the error message
        error_message_element = self.driver.find_element("xpath", '//*[@id="RecoverEmail-email-error"]')
        expected_error_message = 'No account found with that email.'
        self.assertEqual(expected_error_message, error_message_element.text)

        # save the screenshot of the error message
        screenshot_path = os.path.join(folder_name, 'result.png')
        self.driver.save_screenshot(screenshot_path)

    def test_reset_password_registered_email(self):
        self.driver.get('https://demo-unsen.myshopify.com')
        pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
        pw_input.send_keys('4')
        enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
        enter_btn.click()
        self.driver.get('https://demo-unsen.myshopify.com/account/login#recover')

        # Enter email
        first_name_element = self.driver.find_element("xpath", '//*[@id="RecoverEmail"]')
        first_name_element.send_keys('lji59738@nezid.com')

        test_case_name = self.id().split('.')[-1]
        folder_name = os.path.join('result_images', self.__class__.__name__, test_case_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # save the screenshot of step 1
        time.sleep(1)
        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)

        # Click on reset password button
        reset_pw_btn = self.driver.find_element("xpath", '//*[@id="recover"]/form/div[2]/button')
        reset_pw_btn.click()

        time.sleep(2)

        # Check the message
        message_element = self.driver.find_element("xpath", '//*[@id="login"]/h3')
        expected_message = "We've sent you an email with a link to update your password."
        self.assertEqual(expected_message, message_element.text)

        # save the screenshot of the error message
        screenshot_path = os.path.join(folder_name, 'result.png')
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

    def test_correct_product_information_displayed_in_cart(self):
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
        time.sleep(1)
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

    def test_quantity_update_in_cart(self):
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

        add_to_cart_btn = self.driver.find_element(By.CLASS_NAME, "t4s-product-form__submit")
        add_to_cart_btn.click()

        time.sleep(3)

        step1_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_path)

        plus_btn = self.driver.find_element(By.XPATH, '//*[@id="t4s-tab-minicart"]/div[1]/div/div[2]/div/div/div[2]/div/div/button[2]')
        plus_btn.click()

        time.sleep(2)

        result_image_path = os.path.join(folder_name, 'result.png')
        self.driver.save_screenshot(result_image_path)

        remove_btn = self.driver.find_element(By.CLASS_NAME, "t4s-mini_cart__remove")
        remove_btn.click()

    def test_successful_product_removal_from_cart(self):
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

        add_to_cart_btn = self.driver.find_element(By.CLASS_NAME, "t4s-product-form__submit")
        add_to_cart_btn.click()

        time.sleep(3)

        step1_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_path)

        remove_btn = self.driver.find_element(By.CLASS_NAME, "t4s-mini_cart__remove")
        remove_btn.click()

        time.sleep(2)

        result_image_path = os.path.join(folder_name, 'result.png')
        self.driver.save_screenshot(result_image_path)

    def test_negative_quantity_product_addition_not_possible(self):
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

        # Enter valid password
        password_element = self.driver.find_element("name", 'customer[password]')
        password_element.send_keys('abc.12345')

        # Click on login button
        login_btn_element = self.driver.find_element("xpath", '//*[@id="customer_login"]/div[3]/button')
        login_btn_element.click()

        self.driver.get('https://demo-unsen.myshopify.com/collections/women/products/polka-dot-tie-front-top')

        quantity_input_btn = self.driver.find_element(By.CLASS_NAME, "t4s-quantity-input")
        quantity_input_btn.clear()
        quantity_input_btn.send_keys('-5')

        time.sleep(1)
        step1_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_path)

        add_to_cart_btn = self.driver.find_element(By.CLASS_NAME, "t4s-product-form__submit")
        add_to_cart_btn.click()

        time.sleep(3)

        result_image_path = os.path.join(folder_name, 'result.png')
        self.driver.save_screenshot(result_image_path)

        remove_btn = self.driver.find_element(By.CLASS_NAME, "t4s-mini_cart__remove")
        remove_btn.click()

    def test_checkout_without_agreeing_terms(self):
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

        # Enter valid password
        password_element = self.driver.find_element("name", 'customer[password]')
        password_element.send_keys('abc.12345')

        # Click on login button
        login_btn_element = self.driver.find_element("xpath", '//*[@id="customer_login"]/div[3]/button')
        login_btn_element.click()

        self.driver.get('https://demo-unsen.myshopify.com/collections/women/products/polka-dot-tie-front-top')

        add_to_cart_btn = self.driver.find_element(By.CLASS_NAME, "t4s-product-form__submit")
        add_to_cart_btn.click()

        time.sleep(2)

        step1_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_path)
        # //*[@id="t4s-tab-minicart"]/div[2]/div[4]/button

        checkout_btn = self.driver.find_element(By.XPATH, '//*[@id="t4s-tab-minicart"]/div[2]/div[4]/button')
        checkout_btn.click()

        time.sleep(2)

        result_image_path = os.path.join(folder_name, 'result.png')
        self.driver.save_screenshot(result_image_path)

        remove_btn = self.driver.find_element(By.CLASS_NAME, "t4s-mini_cart__remove")
        remove_btn.click()

class UserModule(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # set a 10 second timeout for all driver commands
        self.driver.implicitly_wait(10)

        # create the result_images folder if it doesn't exist
        if not os.path.exists('result_images'):
            os.makedirs('result_images')

    def tearDown(self):
        self.driver.quit()

    # def test_user_can_edit_address(self):
    #     self.driver.get('https://demo-unsen.myshopify.com')
    #     pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
    #     pw_input.send_keys('4')
    #     enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
    #     enter_btn.click()
    #     self.driver.get('https://demo-unsen.myshopify.com/account/login')
    #
    #     email_element = self.driver.find_element("name", 'customer[email]')
    #     email_element.send_keys('lji59738@nezid.com')
    #
    #     password_element = self.driver.find_element("name", 'customer[password]')
    #     password_element.send_keys('abc.12345')
    #
    #     # Click on login button
    #     login_btn_element = self.driver.find_element("xpath", '//*[@id="customer_login"]/div[3]/button')
    #     login_btn_element.click()
    #
    #     self.driver.get('https://demo-unsen.myshopify.com/account/addresses')
    #
    #     # create the folder for this test case's screenshots
    #     test_case_name = self.id().split('.')[-1]
    #     folder_name = os.path.join('result_images', self.__class__.__name__,test_case_name)
    #     if not os.path.exists(folder_name):
    #         os.makedirs(folder_name)
    #
    #     step1_image_path = os.path.join(folder_name, 'step1.png')
    #     self.driver.save_screenshot(step1_image_path)
    #
    #     edit_btn = self.driver.find_element("xpath", '//*[@id="EditFormButton_8340735885553"]')
    #     edit_btn.click()
    #
    #     time.sleep(1)
    #
    #     self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight/3)')
    #
    #     company_element = self.driver.find_element(By.ID, 'AddressCompany_8340735885553')
    #     company_element.send_keys('KTPM')
    #
    #     address1_element = self.driver.find_element(By.ID, 'AddressAddress1_8340735885553')
    #     address1_element.send_keys('46 Nguyen Huu Tho')
    #
    #     address2_element = self.driver.find_element(By.ID, 'AddressAddress2_8340735885553')
    #     address2_element.send_keys('ABC Homestay')
    #
    #     city_element = self.driver.find_element(By.ID, 'AddressCity_8340735885553')
    #     city_element.send_keys('Da Nang')
    #
    #     zip_element = self.driver.find_element(By.ID, 'AddressZip_8340735885553')
    #     zip_element.send_keys('70000')
    #
    #     phone_element = self.driver.find_element(By.ID, 'AddressPhone_8340735885553')
    #     phone_element.send_keys('012345678')
    #
    #     time.sleep(1)
    #     step2_image_path = os.path.join(folder_name, 'step2.png')
    #     self.driver.save_screenshot(step2_image_path)
    #
    #     update_btn = self.driver.find_element("xpath", '//*[@id="address_form_8340735885553"]/div[12]/button[1]')
    #     update_btn.click()
    #
    #     time.sleep(2)
    #     result_image_path = os.path.join(folder_name, 'result.png')
    #     self.driver.save_screenshot(result_image_path)

    def test_add_new_address(self):
        self.driver.get('https://demo-unsen.myshopify.com')
        pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
        pw_input.send_keys('4')
        enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
        enter_btn.click()
        self.driver.get('https://demo-unsen.myshopify.com/account/login')

        email_element = self.driver.find_element("name", 'customer[email]')
        email_element.send_keys('lji59738@nezid.com')

        password_element = self.driver.find_element("name", 'customer[password]')
        password_element.send_keys('abc.12345')

        # Click on login button
        login_btn_element = self.driver.find_element("xpath", '//*[@id="customer_login"]/div[3]/button')
        login_btn_element.click()

        self.driver.get('https://demo-unsen.myshopify.com/account/addresses')

        # create the folder for this test case's screenshots
        test_case_name = self.id().split('.')[-1]
        folder_name = os.path.join('result_images', self.__class__.__name__,test_case_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight/3)')

        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)

        add_new_btn = self.driver.find_element("xpath", '//*[@id="shopify-section-template--16347085046001__main"]/div/div[2]/div/button')
        add_new_btn.click()

        time.sleep(1)

        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight/3)')

        fisrt_name_element = self.driver.find_element(By.XPATH, '//*[@id="AddressFirstNameNew"]')
        fisrt_name_element.send_keys('Nam')

        last_name_element = self.driver.find_element(By.XPATH, '//*[@id="AddressLastNameNew"]')
        last_name_element.send_keys('Phan')

        company_element = self.driver.find_element(By.XPATH, '//*[@id="AddressCompanyNew"]')
        company_element.send_keys('New Company')

        address1_element = self.driver.find_element(By.XPATH, '//*[@id="AddressAddress1New"]')
        address1_element.send_keys('New Address')

        address2_element = self.driver.find_element(By.XPATH, '//*[@id="AddressAddress2New"]')
        address2_element.send_keys('ABC Homestay')

        city_element = self.driver.find_element(By.XPATH, '//*[@id="AddressCityNew"]')
        city_element.send_keys('New City')

        select_element = self.driver.find_element(By.ID ,"AddressCountryNew")
        select = Select(select_element)
        select.select_by_value("Vietnam")

        zip_element = self.driver.find_element(By.XPATH, '//*[@id="AddressZipNew"]')
        zip_element.send_keys('70000')

        phone_element = self.driver.find_element(By.XPATH, '//*[@id="AddressPhoneNew"]')
        phone_element.send_keys('012345678')

        time.sleep(1)
        step2_image_path = os.path.join(folder_name, 'step2.png')
        self.driver.save_screenshot(step2_image_path)

        add_btn = self.driver.find_element("xpath", '//*[@id="address_form_new"]/div[12]/button[1]')
        add_btn.click()

        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight/3)')

        time.sleep(2)
        result_image_path = os.path.join(folder_name, 'result.png')
        self.driver.save_screenshot(result_image_path)

class SearchModule(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # set a 10 second timeout for all driver commands
        self.driver.implicitly_wait(10)

        # create the result_images folder if it doesn't exist
        if not os.path.exists('result_images'):
            os.makedirs('result_images')

    def tearDown(self):
        self.driver.quit()

    # def test_search_product_functionality(self):
    #     self.driver.get('https://demo-unsen.myshopify.com')
    #     pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
    #     pw_input.send_keys('4')
    #     enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
    #     enter_btn.click()
    #     self.driver.get('https://demo-unsen.myshopify.com/account/login')
    #
    #     email_element = self.driver.find_element("name", 'customer[email]')
    #     email_element.send_keys('lji59738@nezid.com')
    #
    #     password_element = self.driver.find_element("name", 'customer[password]')
    #     password_element.send_keys('abc.12345')
    #
    #     # Click on login button
    #     login_btn_element = self.driver.find_element("xpath", '//*[@id="customer_login"]/div[3]/button')
    #     login_btn_element.click()
    #
    #     self.driver.get('https://demo-unsen.myshopify.com')
    #
    #     search_btn = self.driver.find_element("xpath", '//*[@id="shopify-section-header-inline"]/div/div/div/div[4]/div/div[1]/a')
    #     search_btn.click()
    #
    #     # create the folder for this test case's screenshots
    #     test_case_name = self.id().split('.')[-1]
    #     folder_name = os.path.join('result_images', self.__class__.__name__,test_case_name)
    #     if not os.path.exists(folder_name):
    #         os.makedirs(folder_name)
    #
    #     time.sleep(1)
    #     step1_image_path = os.path.join(folder_name, 'step1.png')
    #     self.driver.save_screenshot(step1_image_path)
    #
    #     search_input_element = self.driver.find_element(By.XPATH, '//*[@id="t4s-search-hidden"]/form/div/div[2]/input')
    #     search_input_element.send_keys('Aqua')
    #
    #     time.sleep(2)
    #     step2_image_path = os.path.join(folder_name, 'result.png')
    #     self.driver.save_screenshot(step2_image_path)

    def test_search_product_by_category(self):
        self.driver.get('https://demo-unsen.myshopify.com')
        pw_input = self.driver.find_element("xpath", '//*[@id="password"]')
        pw_input.send_keys('4')
        enter_btn = self.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/form/button')
        enter_btn.click()
        self.driver.get('https://demo-unsen.myshopify.com/account/login')

        email_element = self.driver.find_element("name", 'customer[email]')
        email_element.send_keys('lji59738@nezid.com')

        password_element = self.driver.find_element("name", 'customer[password]')
        password_element.send_keys('abc.12345')

        # Click on login button
        login_btn_element = self.driver.find_element("xpath", '//*[@id="customer_login"]/div[3]/button')
        login_btn_element.click()

        self.driver.get('https://demo-unsen.myshopify.com')

        search_btn = self.driver.find_element("xpath", '//*[@id="shopify-section-header-inline"]/div/div/div/div[4]/div/div[1]/a')
        search_btn.click()

        # create the folder for this test case's screenshots
        test_case_name = self.id().split('.')[-1]
        folder_name = os.path.join('result_images', self.__class__.__name__,test_case_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        time.sleep(1)
        step1_image_path = os.path.join(folder_name, 'step1.png')
        self.driver.save_screenshot(step1_image_path)

        select_element = self.driver.find_element(By.XPATH ,'//*[@id="t4s-search-hidden"]/form/div/div[1]/div/select')
        select = Select(select_element)
        select.select_by_value("Women")

        time.sleep(2)
        step2_image_path = os.path.join(folder_name, 'result.png')
        self.driver.save_screenshot(step2_image_path)