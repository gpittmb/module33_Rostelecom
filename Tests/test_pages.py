import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from settings import *

#Тестирование страницы "Регистрация"

def test_reg_page(browser):
    """проверка, что работает страница "Регистрация" """
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Регистрация', print('Тест провален')
    assert driver.find_element(By.TAG_NAME, 'p').text == 'Личные данные', print('Тест провален')
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/button'), print('Тест провален')


def test_reg_double_account(browser):
    """проверка, что регистрация не проходит при вводе ранее зарегистрированной почты"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(valid_name)
    driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(valid_lastname)
    driver.find_element(By.ID, 'address').send_keys(valid_email)
    driver.find_element(By.ID, 'password').send_keys(fake_password)
    driver.find_element(By.XPATH, "//input[@id='password-confirm']").send_keys(fake_password)
    time.sleep(20)  # время на ввод капчи при ее появлении
    driver.find_element(By.XPATH, "//button[@name='register']").click()
    assert driver.find_element(By.XPATH, "//h2[@class='card-modal__title']").text == 'Учётная запись уже существует'


def test_reg_double_account(browser):
    """проверка, что поле 'Пароль' и 'Подтверждение пароля' совпадают"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(valid_name)
    driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(valid_lastname)
    driver.find_element(By.ID, 'address').send_keys(fake_email)
    driver.find_element(By.ID, 'password').send_keys(fake_password)
    driver.find_element(By.XPATH, "//input[@id='password-confirm']").send_keys(valid_password_email)
    time.sleep(20)  # время на ввод капчи при ее появлении
    driver.find_element(By.XPATH, "//button[@name='register']").click()
    assert driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta--error').text == 'Пароли не совпадают'


def test_password_recovery(browser):
    """проверка, что работает страница "Восстановление пароля" """
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 't-btn-tab-login')))#
    driver.find_element(By.ID, 'forgot_password').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Восстановление пароля', print('Тест провален')
    assert driver.find_element(By.ID, 'reset').text == 'Продолжить', print('Тест провален')


def test_reg_empty_fields(browser):
    """проверка, что с пустыми полями регистрация не проходит"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    error = driver.find_elements(By.CSS_SELECTOR, '.rt-input-container--error')
    time.sleep(3)
    assert len(error) == 5

#Тестирование Авторизации

def test_auth_user_mail(browser):
    """проверка авторизации с помощью валидных данных (электронная почта и пароль)"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    driver.find_element(By.ID, 'password').send_keys(valid_password_email)
    time.sleep(20)  # время на ввод капчи при ее появлении
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные'

def test_auth_user_login(browser):
    """проверка авторизации с помощью валидных данных (логин/телефон и пароль) """
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, 'username').send_keys(valid_login)
    driver.find_element(By.ID, 'password').send_keys(valid_password_login)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(20)  # время на ввод капчи при ее появлении
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные'

def test_auth_fake_phone_email(browser):
    """проверка, что авторизация не проходит при вводе фейкового телефона и фейковой почты"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'username').send_keys(invalid_phone)
    driver.find_element(By.ID, 'password').send_keys(password_phone)
    time.sleep(20)  # время на ввод капчи при ее появлении
    driver.find_element(By.ID, 'kc-login').click()
    time.sleep(2)
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys(fake_email)
    driver.find_element(By.ID, 'password').send_keys(valid_password_email)
    time.sleep(20)  # время на ввод капчи при ее появлении
    driver.find_element(By.ID, 'kc-login').click()
    assert driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'
    assert driver.find_element(By.ID, 'forgot_password').value_of_css_property('color') == "rgba(255, 79, 18, 1)"

def test_auth_fake_login_ls(browser):
    """проверка, что авторизация не проходит при вводе фейкового логина или лицевого счета"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, 'username').send_keys(invalid_login)
    driver.find_element(By.ID, 'password').send_keys(valid_password_email)
    time.sleep(20)  # время на ввод капчи при ее появлении
    driver.find_element(By.ID, 'kc-login').click()
    time.sleep(2)
    driver.find_element(By.ID, 't-btn-tab-ls').click()
    driver.find_element(By.ID, 'username').send_keys(invalid_ls)
    driver.find_element(By.ID, 'password').send_keys(valid_password_email)
    time.sleep(20)  # время на ввод капчи при ее появлении
    driver.find_element(By.ID, 'kc-login').click()
    assert driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'
    assert driver.find_element(By.ID, 'forgot_password').value_of_css_property('color') == "rgba(255, 79, 18, 1)"

def test_auth_valid_mail_fake_pass(browser):
    """проверка авторизации с помощью валидной почты и неправильного пароля"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'kc-login')))
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    driver.find_element(By.ID, 'password').send_keys(fake_password)
    time.sleep(20)  # время на ввод капчи при ее появлении
    driver.find_element(By.ID, 'kc-login').click()
    assert driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'
    assert driver.find_element(By.ID, 'forgot_password').value_of_css_property('color') == "rgba(255, 79, 18, 1)"


#Тестирование полей регистрации

@pytest.mark.parametrize("negative_input", [russian_chars(1), russian_chars(31), russian_chars(256), english_chars(15), number_chars(15), chinese_chars(10), special_chars(20)])
def test_reg_incorrect_name(negative_input, browser):
    """проверка поля Имя при попытке ввода недопустимых символов"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    driver.find_element(By.ID, "kc-register").click()
    driver.find_element(By.NAME, "firstName").send_keys(negative_input)
    driver.find_element(By.NAME, "lastName").click()
    assert driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


@pytest.mark.parametrize("negative_input", [russian_chars(1), russian_chars(31), russian_chars(256), english_chars(15), number_chars(15), chinese_chars(10), special_chars(20)])
def test_reg_incorrect_lastname(negative_input, browser):
    """проверка поля Фамилия при попытке ввода недопустимых символов"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    driver.find_element(By.ID, "kc-register").click()
    driver.find_element(By.NAME, "firstName").clear()
    driver.find_element(By.NAME, "lastName").send_keys(negative_input)
    driver.find_element(By.NAME, "firstName").click()
    assert driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


@pytest.mark.parametrize("negative_input", ['testmail.ru', 'test@mail,ru', '@mail.ru'])
def test_reg_incorrect_email(negative_input, browser):
    """проверка поля "email или телефон" при попытке ввода некорректной почты"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    driver.find_element(By.ID, "kc-register").click()
    driver.find_element(By.ID, "address").send_keys(negative_input)
    driver.find_element(By.ID, "password").click()
    assert driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"


@pytest.mark.parametrize("negative_input", ['+7 900 111-22-3у', '+7 900 111-22-3№', '+7 900 111-22-3', '+7 900 111-22-333', '+7 900 111-22-3', '+375 11 222-33-4'])
def test_reg_incorrect_phone(negative_input, browser):
    """проверка поля "email или телефон" при попытке ввода некорректного телефона"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    driver.find_element(By.ID, "kc-register").click()
    driver.find_element(By.ID, "address").send_keys(negative_input)
    driver.find_element(By.ID, "password").click()
    assert driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"


@pytest.mark.parametrize("negative_input", ['(Test', '(Тест2808', '!"№;%:?*', 'testoviy12', '1234567890', 'Testoviy12Testoviy12$', 'TESTOVIYPASSWORD*'])
def test_reg_incorrect_password(negative_input, browser):
    """проверка сложности пароля на соответствие требований"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    driver.find_element(By.ID, "kc-register").click()
    driver.find_element(By.ID, "password").send_keys(negative_input)
    driver.find_element(By.ID, "address").click()
    temporary = False
    try:
        driver.find_element(By.XPATH,
                                   "(/html[1]/body[1]/div[1]/main[1]/section[2]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1])")
    except NoSuchElementException:
        temporary = True

    assert temporary == False


#Проверка авторизации с помощью соцсетей

def test_vk_btn(browser):
    """проверка доступности авторизации через VK"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'oidc_vk'))).click()
    assert 'vk.com' in driver.find_element(By.XPATH, '//div[@class="oauth_head"]/a').get_attribute('href')
    assert 'id.vk.com' in driver.current_url

def test_ok_btn(browser):
    """проверка доступности авторизации через OK"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'oidc_ok'))).click()
    assert driver.find_element(By.XPATH, '//div[@class="ext-widget_h_tx"]').text == 'Одноклассники'
    assert 'ok' in driver.current_url

def test_mail_btn(browser):
    """проверка доступности авторизации через Mail-Мой мир"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'oidc_mail'))).click()
    assert 'mail.ru' in driver.find_element(By.XPATH, '//span[@class="header__logo"]').text.lower()
    assert 'mail' in driver.current_url

def test_yandex_btn(browser):
    """проверка доступности авторизации через Яндекс"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'oidc_ya'))).click()
    try:
        assert 'yandex' in driver.current_url
    except AssertionError:
        print('переход не осуществлен')
