import re
from validate_email import validate_email
from UniBox.Classes.data_dto import DataDto


def get_valid_personal_data(data_info: DataDto) -> DataDto:
    if not correct_name(data_info.name):
        data_info.name = 'Ошибка при заполнении имени! (Длина имени не менее 3 и не более 10 символов)'

    if not correct_number(data_info.phone_number):
        data_info.phone_number = 'Ошибка при заполнении мобильного телефона! (Шаблон: 88005553535)'

    if not correct_email(data_info.email):
        data_info.email = 'Ошибка при заполнении почтового адреса! (Адрес заполнен не верно)'

    return data_info


def validate(order_info: DataDto) -> bool:
    return correct_name(order_info.name) \
           and correct_number(order_info.phone_number) \
           and correct_email(order_info.email)


def correct_name(name: str) -> bool:
    return name is not None and re.match(r'[a-zA-Zа-яА-Я]{3,10}', name) is not None


def correct_number(number: str) -> bool:
    return number is not None and re.match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', number) is not None


def correct_email(email: str) -> bool:
    return email is not None and validate_email(email) != "Invalid!"


