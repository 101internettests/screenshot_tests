import allure
from selenium import webdriver
from helper_module.screenshot_engine.image_processor import ImageProcessor
from config import create_screenshot_driver
from config import host_prod, host_stage


class TestSomePage(ImageProcessor):

    WINDOW_H = 1280
    WINDOW_W = 4500

    @allure.title("Проверка главной страницы в г. Екатеринбург")
    def test_mainpage_ekaterinburg(self, driver: webdriver.Chrome):
        path = '/ekaterinburg/'
        driver.get(host_stage + path)
        driver.set_window_size(self.WINDOW_H, self.WINDOW_W)
        second_driver = create_screenshot_driver()
        second_driver.get(host_prod + path)
        second_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)
        screenshot_prod_bytes = driver.get_screenshot_as_png()
        screenshot_beta_bytes = second_driver.get_screenshot_as_png()
        image_prod = self.load_image_from_bytes(screenshot_prod_bytes)
        image_beta = self.load_image_from_bytes(screenshot_beta_bytes)
        get_result = self.check_images_difference(image_prod, image_beta)
        image_result = self.load_image_from_bytes(get_result[1])
        # image_prod.show()
        # image_beta.show()
        # image_result.show()
        allure.attach(self.image_to_bytes(image_prod), 'prod', allure.attachment_type.PNG)
        allure.attach(self.image_to_bytes(image_beta), 'stage', allure.attachment_type.PNG)
        allure.attach(self.image_to_bytes(image_result), 'diff', allure.attachment_type.PNG)

    @allure.title("Проверка страницы поиска домашнего интернета в г. Екатеринбург")
    def test_orders_tohome_ekaterinburg(self, driver: webdriver.Chrome):
        path = '/ekaterinburg/orders/tohome/'
        driver.get(host_stage + path)
        driver.set_window_size(self.WINDOW_H, self.WINDOW_W)
        second_driver = create_screenshot_driver()
        second_driver.get(host_prod + path)
        second_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)
        screenshot_prod_bytes = driver.get_screenshot_as_png()
        screenshot_beta_bytes = second_driver.get_screenshot_as_png()
        image_prod = self.load_image_from_bytes(screenshot_prod_bytes)
        image_beta = self.load_image_from_bytes(screenshot_beta_bytes)
        get_result = self.check_images_difference(image_prod, image_beta)
        image_result = self.load_image_from_bytes(get_result[1])
        # image_prod.show()
        # image_beta.show()
        # image_result.show()
        allure.attach(self.image_to_bytes(image_prod), 'prod', allure.attachment_type.PNG)
        allure.attach(self.image_to_bytes(image_beta), 'stage', allure.attachment_type.PNG)
        allure.attach(self.image_to_bytes(image_result), 'diff', allure.attachment_type.PNG)

    @allure.title("Проверка страницы провайдеров в г. Екатеринбург")
    def test_providers_ekaterinburg(self, driver: webdriver.Chrome):
        path = '/ekaterinburg/providers'
        driver.get(host_stage + path)
        driver.set_window_size(self.WINDOW_H, self.WINDOW_W)
        second_driver = create_screenshot_driver()
        second_driver.get(host_prod + path)
        second_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)
        screenshot_prod_bytes = driver.get_screenshot_as_png()
        screenshot_beta_bytes = second_driver.get_screenshot_as_png()
        image_prod = self.load_image_from_bytes(screenshot_prod_bytes)
        image_beta = self.load_image_from_bytes(screenshot_beta_bytes)
        get_result = self.check_images_difference(image_prod, image_beta)
        image_result = self.load_image_from_bytes(get_result[1])
        # image_prod.show()
        # image_beta.show()
        # image_result.show()
        allure.attach(self.image_to_bytes(image_prod), 'prod', allure.attachment_type.PNG)
        allure.attach(self.image_to_bytes(image_beta), 'stage', allure.attachment_type.PNG)
        allure.attach(self.image_to_bytes(image_result), 'diff', allure.attachment_type.PNG)

    @allure.title("Проверка страницы рейтинга в г. Екатеринбург")
    def test_rating_ekaterinburg(self, driver: webdriver.Chrome):
        path = '/ekaterinburg/rating'
        driver.get(host_stage + path)
        driver.set_window_size(self.WINDOW_H, self.WINDOW_W)
        second_driver = create_screenshot_driver()
        second_driver.get(host_prod + path)
        second_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)
        screenshot_prod_bytes = driver.get_screenshot_as_png()
        screenshot_beta_bytes = second_driver.get_screenshot_as_png()
        image_prod = self.load_image_from_bytes(screenshot_prod_bytes)
        image_beta = self.load_image_from_bytes(screenshot_beta_bytes)
        get_result = self.check_images_difference(image_prod, image_beta)
        image_result = self.load_image_from_bytes(get_result[1])
        # image_prod.show()
        # image_beta.show()
        # image_result.show()
        allure.attach(self.image_to_bytes(image_prod), 'prod', allure.attachment_type.PNG)
        allure.attach(self.image_to_bytes(image_beta), 'stage', allure.attachment_type.PNG)
        allure.attach(self.image_to_bytes(image_result), 'diff', allure.attachment_type.PNG)

    @allure.title("Проверка страницы интернета в офис в г. Екатеринбург")
    def test_orders_office_ekaterinburg(self, driver: webdriver.Chrome):
        path = '/ekaterinburg/orders/office'
        driver.get(host_stage + path)
        driver.set_window_size(self.WINDOW_H, self.WINDOW_W)
        second_driver = create_screenshot_driver()
        second_driver.get(host_prod + path)
        second_driver.set_window_size(self.WINDOW_H, self.WINDOW_W)
        screenshot_prod_bytes = driver.get_screenshot_as_png()
        screenshot_beta_bytes = second_driver.get_screenshot_as_png()
        image_prod = self.load_image_from_bytes(screenshot_prod_bytes)
        image_beta = self.load_image_from_bytes(screenshot_beta_bytes)
        get_result = self.check_images_difference(image_prod, image_beta)
        image_result = self.load_image_from_bytes(get_result[1])
        # image_prod.show()
        # image_beta.show()
        # image_result.show()
        allure.attach(self.image_to_bytes(image_prod), 'prod', allure.attachment_type.PNG)
        allure.attach(self.image_to_bytes(image_beta), 'stage', allure.attachment_type.PNG)
        allure.attach(self.image_to_bytes(image_result), 'diff', allure.attachment_type.PNG)