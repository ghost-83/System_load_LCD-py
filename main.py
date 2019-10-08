#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, threading, serial, psutil, time, configparser
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QIcon

signal_ui = False  # Создаем глобальную перененную для завершение цикла в порлельном потоке


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        global qbtn, qbtn_Stop, qlbl, thre  # Создаем глобальные переменные для доступа к ним из любой функции класса
        self.initUI()

    def initUI(self):
        self.move(300, 300)  # Задаем отступы от краев экрана
        self.setFixedSize(200, 70)  # Задаем статический не изменяемый размер окна
        self.setWindowTitle('Монитор PC')  # Пишем имя окна
        self.setWindowIcon(QIcon('MyIcon.ico'))  # Зодаем эконку окна
        self.qbtn = QPushButton('Старт', self)  # Создаем кнопку Старт
        self.qbtn.move(10, 20)  # Задаем отступы от края окна
        self.qbtn_Stop = QPushButton('Стоп', self)
        self.qbtn_Stop.move(110, 20)
        self.qbtn_Stop.setEnabled(False)  # Делае кнопку Стоп не активной
        self.qlbl = QLabel('Готов', self)  # Создаем этикетку
        self.qlbl.move(10, 50)  # Задаем положение этикетки в окне
        self.qlbl.resize(180, 20)  # Задарем размер этикетки

        self.qbtn.clicked.connect(self.buttonClicked)  # Связываем кнопки с функциями
        self.qbtn_Stop.clicked.connect(self.buttonOnClicked)  # при нажатии на кнопку будет вызвана заданная функция
        self.show()  # Отображаем окно

    def buttonClicked(self):
        global signal_ui  # Сообщаем что данная переменная к которой мы будем обращаться глобальная
        signal_ui = True  # Меняем значение глобальной переменной
        self.qbtn.setEnabled(False)  # Делаем кнопку Старт не активной,
        self.qbtn_Stop.setEnabled(True)  # а кнотку стоп активной
        self.thre = threading.Thread(target=self.PriemChikl,
                                     name=self.PriemChikl)  # Создаем поралельный поток с в которой будет выполняться функция PriemChikl с именм PriemChikl
        self.thre.start()  # Запускаем поралельный поток
        self.qlbl.setText('Запущен')  # Пишем в этикетку что поток запущен

    def buttonOnClicked(self):
        global signal_ui
        signal_ui = False
        self.thre.join()  # Ожидаем завершение потока
        self.qbtn.setEnabled(True)
        self.qbtn_Stop.setEnabled(False)
        self.qlbl.setText('Готов')

    def PriemChikl(self):

        global signal_ui
        data = [0, 0]
        com = serial.Serial(conf.get("setings", "port"), int(conf.get("setings", "baudrate")))

        while (signal_ui):  # Запускаем цикл для проверки поступаемого сигнала и сиуляции нажатия кнопки
            # gives a single float value
            data[0] = int(psutil.cpu_percent())
            # gives an object with many fields
            data[1] = int(psutil.virtual_memory().percent)
            com.write(bytes(data))
            time.sleep(1)

if __name__ == '__main__':  # Проверяем что произведен запуск именно данного файла
    conf = configparser.ConfigParser()
    conf.read("config.ini")
    app = QApplication(sys.argv)  # Запускаем перехват событий
    ex = MyWidget()  # Создаем окно
    sys.exit(app.exec())  # При нажатии на крестик завершаем программу