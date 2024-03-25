import allure
from selenium import webdriver
from helper_module.screenshot_engine.image_processor import ImageProcessor
from config import create_screenshot_driver
from config import host_prod, host_stage


class TestSomePage(ImageProcessor):

    WINDOW_H = 1280
    WINDOW_W = 4500

    @allure.title("Проверка главной страницы в г. Абакан")
    def test_easy_func(self, driver: webdriver.Chrome):
        path = '/abakan/orders/tohome'

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
        #
        # image_prod.show()
        # image_beta.show()
        image_result.show()

        allure.attach(self.image_to_bytes(image_prod), 'prod', allure.attachment_type.PNG)
        allure.attach(self.image_to_bytes(image_beta), 'stage', allure.attachment_type.PNG)
        allure.attach(self.image_to_bytes(image_result), 'diff', allure.attachment_type.PNG)