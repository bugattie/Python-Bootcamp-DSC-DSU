from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from getpass import getpass

driver = webdriver.Chrome()


def login():
    email = ''
    pw = input('')

    fb_email = driver.find_element_by_id("m_login_email")
    password = driver.find_element_by_id("m_login_password")
    login_button = driver.find_element_by_css_selector('#u_0_4 button')

    fb_email.send_keys(email)
    password.send_keys(pw)
    login_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div._2pii div a"))).click()


def like(target_url):
    like_button = driver.find_element_by_id('u_0_s')
    like_button.click()


def comment(target_url, review):
    para = review.split(".")
    for i in para:
        commt_area = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.mentions textarea#composerInput")))
        commt_area.send_keys(i)

        post_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-sigil="touchable composer-submit"]')))
        post_button.click()


def share(cap, target_url):
    share_button = driver.find_element_by_css_selector(
        'a[data-sigil="share-popup"]').click()

    write_post = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, "share-with-message-button"))).click()

    post_msg = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'textarea#share_msg_input')))
    post_msg.send_keys(cap)

    post_button = driver.find_element_by_css_selector(
        'div#modalDialogHeaderButtons button#share_submit').click()


def main():
    base_url = 'https://m.facebook.com/'
    target_url = 'https://m.facebook.com/DeveloperStudentClubDHASuffaUniversity/photos/a.1451042185216529/2839108256409908/'
    comment_text = 'Thankyou DSC-DSU for giving us an opportunity to learn a top-rated skill. Enjoyed the course. Well managed course, well explanation. I learned python basics, file handling, exception handling, web scraping, web automation.'
    caption = "This is just one example to automate like, comment and share a facebook posts that I learned from PythonBootcamp2020 organized by DSC@DSU. #DSCDSU #DeveloperStudentClubs #DSCPakistan #Python #Bot"

    driver.get(base_url)
    login()
    like(target_url)
    comment(target_url, comment_text)
    share(caption, target_url)


if __name__ == '__main__':
    main()
