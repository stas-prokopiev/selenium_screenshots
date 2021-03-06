import sys
from selenium_screenshots import Screenshots
from selenium_screenshots import make_screenshot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_class_screenshots():
    """"""
    # Create webdriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("window-size=1900,1080")
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), options=chrome_options)
    #####
    # Create screenshot handler
    screenshots_handler = Screenshots(driver)
    screenshots_handler = Screenshots(
        driver,
        int_screenshots_to_delete_half=4,
        int_max_length_of_filename=5,
    )
    # driver.maximize_window()
    driver.get("https://www.cian.ru/rent/flat/219885743/")
    screenshots_handler.create_screenshot(str_description='')
    screenshots_handler.create_screenshot(str_description='adsgdasg')
    screenshots_handler.delete_all_screenshots()
    assert screenshots_handler._count_screenshots_in_the_directory() == 0, \
        "ERROR: Wrong number of the screenshots"
    screenshots_handler.create_screenshot(str_description='dhsaj.23sd._')
    screenshots_handler.create_screenshot(str_description='///asdfh///')
    screenshots_handler.delete_all_screenshots()
    screenshots_handler.create_screenshot(str_description='hahaha')
    screenshots_handler.create_screenshot(str_description='hahaha')
    assert screenshots_handler._count_screenshots_in_the_directory() == 2, \
        "ERROR: Wrong number of the screenshots"
    screenshots_handler.delete_not_unique_screenshots()
    assert screenshots_handler._count_screenshots_in_the_directory() == 1, \
        "ERROR: Wrong number of the screenshots"
    screenshots_handler.create_screenshot(str_description='sadg....')
    assert screenshots_handler._count_screenshots_in_the_directory() == 2, \
        "ERROR: Wrong number of the screenshots"
    make_screenshot(driver, str_description="sg",)
    make_screenshot(driver, str_description="sg2",)






