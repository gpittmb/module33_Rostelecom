import os
from dotenv import load_dotenv
from faker import Faker
import string
import random
load_dotenv()

base_url = 'https://b2c.passport.rt.ru'

"""валидные данные"""
valid_name = 'Дмитрий'
valid_lastname = 'Зайцев'
valid_email = 'tagazaquila@yandex.ru'
valid_phone = os.getenv('phone')
valid_login = os.getenv('login')
valid_password_email = 'w4brb6vp01S'
valid_password_login = os.getenv('valid_password_login')
valid_password_phone = os.getenv('valid_password_phone')

"""фейковые данные"""
fake_ru = Faker('ru_RU')
fake_firstname = fake_ru.first_name()
fake_lastname = fake_ru.last_name()
fake_phone = fake_ru.phone_number()
fake = Faker()
fake_password = fake.password()
fake_login = fake.user_name()
fake_email = fake.email()
invalid_code = '777777'
invalid_phone = '+712345678901'
invalid_login = 'SkillFactoryTest'
invalid_ls = '112233445566'

def russian_chars(num):
    text = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    rand_string = ''.join(random.choice(text) for i in range(num))
    return rand_string

def english_chars(num):
    text = 'abcdefghijklmnopqrstuvwxyz'
    rand_string = ''.join(random.choice(text) for i in range(num))
    return rand_string

def number_chars(num):
    text = '0123456789'
    rand_string = ''.join(random.choice(text) for i in range(num))
    return rand_string

def chinese_chars(num):
    text = '见凸内允皿丹勻四见凸内允皿丹勻四'
    rand_string = ''.join(random.choice(text) for i in range(num))
    return rand_string

def special_chars(num):
    text = '|/!@#$%^&*()-_=+`~?"№;:[]{}'
    rand_string = ''.join(random.choice(text) for i in range(num))
    return rand_string
