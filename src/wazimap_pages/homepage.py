from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


# Class for Wazimap homepage
class WazimapHomepage:
    # Constructor for the homepage
    def __init__(self, driver):
        # Chrome driver
        self.driver = driver
        # Web Elements locators
        self._data_mapper_element_xpath = "//div[@class='panel-toggle data-mapper-panel__open']"
        self._demographic_menu_xpath = "//div[@class='data-category__h1_title']//div[@class='truncate'][contains("\
                                       "text(),'Demographics')] "
        self._age_item_xpath = "//div[@class='data-category__h2_trigger']//div[@class='truncate'][contains(text(),"\
                               "'Age')] "
        self._youth_population_xpath = "//div[@class='truncate'][contains(text(),'Youth population')]"
        self._youths_xpath = "//div[@class='truncate'][contains(text(),'Youths')]"
        self._nonYouth_xpath = "//div[contains(text(),'Non youth')]"

    # Click Data Mapper SVG icon
    def click_data_mapper(self):
        data_mapper_element_xpath = self.driver.find_elements_by_xpath(self._data_mapper_element_xpath)[1]
        ActionChains(self.driver).move_to_element(data_mapper_element_xpath).click(data_mapper_element_xpath).perform()
        pass

    # Click on Demographic Menu
    def click_demographic_menu(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located
                                             ((By.XPATH, self._demographic_menu_xpath)))
        demographic = self.driver.find_element_by_xpath(self._demographic_menu_xpath)
        ActionChains(self.driver).move_to_element(demographic).click(demographic).perform()
        pass

    # Click on Age Item
    def click_age_item(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located
                                             ((By.XPATH, self._age_item_xpath)))
        age_click = self.driver.find_element_by_xpath(self._age_item_xpath)
        ActionChains(self.driver).move_to_element(age_click).click(age_click).perform()
        pass

    # Click on Youth Population
    def click_youth_population_item(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located
                                             ((By.XPATH, self._youth_population_xpath)))
        youth_population = self.driver.find_element_by_xpath(self._youth_population_xpath)
        ActionChains(self.driver).move_to_element(youth_population).click(youth_population).perform()
        pass

    # Below 2 Test cases for any improvements
    def click_youth(self):
        youths = self.driver.find_element_by_xpath(self._youths_xpath)
        ActionChains(self.driver).move_to_element(youths).click(youths).perform()

        pass

    def click_non_youth(self):
        youths = self.driver.find_element_by_xpath(self._nonYouth_xpath)
        ActionChains(self.driver).move_to_element(youths).click(youths).perform()
        pass
