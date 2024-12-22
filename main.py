import os
from PyQt5 import QtWidgets, QtCore
import random
import string


def get_password(len):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = list(string.ascii_lowercase)
    boolean = [True, False]

    password = ''

    for i in range(len):
        symbol = random.choice(boolean)

        fa

    return password


def update_file_list():
    files = [f for f in os.listdir('saves') if f.endswith('.txt')]
    file_list.clear()
    file_list.addItems(files)


def display_file_content():
    select_file = file_list.currentItem()
    if select_file:
        with open(f'saves/{select_file.text()}', 'r') as file:
            content = file.read()
        output_browser.setText(content)


def update_slider_label():
    slider_label.setText(f'Довжина паролю {slider.value()}')


def create_password():
    service_name = service_input.text()
    login = login_input.text()
    len_password = slider.value()

    password = get_password(len_password)

    if not service_name or not login:
        output_browser.setText('Заповніть всі поля')
        return

    filename = f'{service_name.replace(" ", "_")}_{login.replace(" ", "_")}.txt'

    with open(f'saves/{filename}', 'w') as file:
        file.write(f'service name: {service_name}\nlogin: {login}\npassword: {password}')

    update_file_list()

    output_browser.setText(f'Пароль створено для {service_name}, {login}, {password}')




# Створення основного вікна
app = QtWidgets.QApplication([])
dialog = QtWidgets.QDialog()
dialog.setWindowTitle("Менеджер паролів")
dialog.resize(600, 400)

# Поля для введення сервісу та логіна
service_label = QtWidgets.QLabel("Назва сервісу", dialog)
service_label.setGeometry(350, 40, 70, 85)

service_input = QtWidgets.QLineEdit(dialog)
service_input.setGeometry(440, 70, 120, 25)

slider_label = QtWidgets.QLabel("Довжина пораля: 10", dialog)
slider_label.setGeometry(350, 230, 200, 20)

login_label = QtWidgets.QLabel("Логін", dialog)
login_label.setGeometry(375, 120, 50, 20)
slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, dialog)
slider.setGeometry(320, 250, 160, 20)
slider.setMinimum(5)
slider.setMaximum(32)
slider.setValue(10)
slider.valueChanged.connect(update_slider_label)


login_input = QtWidgets.QLineEdit(dialog)
login_input.setGeometry(440, 120, 120, 25)

# Кнопка для створення пароля
create_button = QtWidgets.QPushButton("Створити пароль", dialog)
create_button.setGeometry(370, 190, 160, 50)
create_button.clicked.connect(create_password)

# Список текстових файлів
file_list = QtWidgets.QListWidget(dialog)
file_list.setGeometry(10, 10, 260, 370)
file_list.itemClicked.connect(display_file_content)

# Текстовий браузер для виведення результатів
output_browser = QtWidgets.QTextBrowser(dialog)
output_browser.setGeometry(290, 280, 290, 100)

# Оновлення списку файлів при запуску
update_file_list()

dialog.show()
app.exec_()