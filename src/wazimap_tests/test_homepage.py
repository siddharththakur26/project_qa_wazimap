# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os
import HtmlTestRunner
from src.wazimap_pages.homepage import WazimapHomepage


# Test class for testing Wazimap Homepage
class TestHomepage(unittest.TestCase):
    # Initial Setup
    @classmethod
    def setUp(cls):
        # create a new Chrome session
        option = webdriver.ChromeOptions()
        option.add_argument(" — incognito")
        chrome_dir = '' + os.getcwd() + '/chromedriver'
        cls.driver = webdriver.Chrome(executable_path = chrome_dir, options = option)
        # Webpage address
        url = 'https://wazimap-ng.africa/'
        # navigate to the application home page
        cls.driver.get(url)
        # Wait till the homepage elements are located.
        WebDriverWait(cls.driver, 10).until(expected_conditions.visibility_of_element_located\
                                                ((By.XPATH, "//div[@class='point-mapper-content narrow-scroll']")))

    # test for the visibility of Data Mapper
    def test_data_mapper_opens(self):
        driver = self.driver
        # Instance of Wazimap Homepage
        homepage = WazimapHomepage(driver)
        # Click the Data Mapper
        homepage.click_data_mapper()
        # Find the Description of data mapper
        _data_mapper_content_xpath = driver.find_element_by_xpath\
            ("//div[contains(text(),'Explore data categories available for this locatio')]").\
            get_attribute('textContent')

        content_to_match =\
            "Explore data categories available for this location. Click or tap a sub-indicator to show it on the map."
        # Wait till the Data Mapper Header is displayed
        _data_mapper_header_xpath = WebDriverWait(driver, 2).until(expected_conditions.invisibility_of_element
                                                                   ((By.XPATH, "//div[@class='data-mapper']")))

        self.assertTrue(_data_mapper_header_xpath, 'Data Mapper is not displayed')
        self.assertEqual(_data_mapper_content_xpath, content_to_match,
                         'Data Mapper description is either not matched or found.')

    # test for the menu items under the Demographic Item visibility
    def test_demographic_menu_age_item_visible(self):
        driver = self.driver
        homepage = WazimapHomepage(driver)
        homepage.click_data_mapper()
        # wait till Demographic is displayed
        _demographic_header_xpath = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH,
                                                               "//div[@class='data-category__h1_title']//div["
                                                               "@class='truncate'][contains(text(),'Demographics')]")))
        self.assertTrue(_demographic_header_xpath.is_displayed(), 'Demographic Menu is not displayed')
        # check for all the menu sub items of Demographic item
        homepage.click_demographic_menu()
        is_age = driver.find_element_by_xpath\
            ("//div[@class='data-category__h2_trigger']//div[@class='truncate'][contains(text(),'Age')]")\
            .is_displayed()
        is_gender = driver.find_element_by_xpath\
            ("//div[@class='data-category__h2_trigger']//div[@class='truncate'][contains(text(),'Gender')]")\
            .is_displayed()
        is_race = driver.find_element_by_xpath\
            ("//div[@class='data-category__h2_trigger']//div[@class='truncate'][contains(text(),'Race')]")\
            .is_displayed()
        is_region = driver.find_element_by_xpath\
            ("//div[@class='data-category__h2_trigger']//div[@class='truncate'][contains(text(),'Region of Birth')]")\
            .is_displayed()
        is_citizenship = driver.find_element_by_xpath\
            ("//div[@class='data-category__h2_trigger']//div[@class='truncate'][contains(text(),'Citizenship')]")\
            .is_displayed()
        is_language = driver.find_element_by_xpath\
            ("//div[@class='data-category__h2_trigger']//div[@class='truncate'][contains(text(),'Language')]")\
            .is_displayed()
        self.assertTrue(is_age, 'Age Item is not displayed.')
        self.assertTrue(is_race, 'Race Item is not displayed.')
        self.assertTrue(is_gender, 'Gender Item is not displayed.')
        self.assertTrue(is_region, 'Region Item is not displayed.')
        self.assertTrue(is_citizenship, 'Citizenship Item is not displayed.')
        self.assertTrue(is_language, 'Language Item is not displayed.')

    # test for visibility of Youth Population under Age item
    def test_youth_population_item_visbile(self):
        driver = self.driver
        homepage = WazimapHomepage(driver)
        homepage.click_data_mapper()
        # click the Demographic Item under Data Mapper
        homepage.click_demographic_menu()
        # click the Age sub item under Demographic Item
        homepage.click_age_item()
        # Boolean for the visibility of Youth population under the Age item
        is_youth_population_item = driver.find_element_by_xpath\
            ("//div[@class='truncate'][contains(text(),'Youth population')]").is_displayed()
        self.assertTrue(is_youth_population_item, 'Youth Population is not displayed')

    # test for visibility of Youth and Non Youth Population under Age item
    def test_youths_and_non_youths_subitem_visbile(self):
        driver = self.driver
        homepage = WazimapHomepage(driver)
        homepage.click_data_mapper()
        homepage.click_demographic_menu()
        homepage.click_age_item()
        # Click on Youth Population sub item under Age
        homepage.click_youth_population_item()
        # True if Youths are visible else False
        is_youth = driver.find_element_by_xpath\
            ("//div[@class='truncate'][contains(text(),'Youths')]").is_displayed()
        self.assertTrue(is_youth, 'Youth is not displayed')
        # True if Non Youths are visible else False
        is_non_youth = driver.find_element_by_xpath\
            ("//div[contains(text(),'Non youth')]").is_displayed()
        self.assertTrue(is_non_youth, 'Non Youth is not displayed')

    # close the chrome driver and browser
    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.close()
        cls.driver.quit()


if __name__=='__main__':
    dir_path = os.getcwd()
    unittest.main(verbosity = 2, testRunner = HtmlTestRunner.HTMLTestRunner(output = dir_path))
