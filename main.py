import sqlite3

from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow, QApplication

from add_pokup import Ui_Dialog_Add_Pokup
from add_post import Ui_Dialog_Add_Post
from add_product import Ui_Dialog_Add_Product
from add_stocks import Ui_Dialog_Add_Stocks
from del_pokup import Ui_Dialog_Del_Pokup
from del_post import Ui_Dialog_Del_Post
from del_product import Ui_Dialog_Del_Product
from del_stocks import Ui_Dialog_Del_Stocks
from mainwindow import Ui_MainWindow
from pokup import Ui_Dialog_Pokup
from post import Ui_Dialog_Post
from product import Ui_Dialog_Product
from stocks import Ui_Dialog_Stocks

db = sqlite3.connect('бд.db')
cursor = db.cursor()


class WinDelStocks(QDialog, Ui_Dialog_Del_Stocks):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class WinAddStocks(QDialog, Ui_Dialog_Add_Stocks):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



class WinDelProduct(QDialog, Ui_Dialog_Del_Product):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class WinAddProduct(QDialog, Ui_Dialog_Add_Product):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.accept)


class WinDelPokup(QDialog, Ui_Dialog_Del_Pokup):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class WinAddPokup(QDialog, Ui_Dialog_Add_Pokup):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class WinDelPost(QDialog, Ui_Dialog_Del_Post):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class WinAddPost(QDialog, Ui_Dialog_Add_Post):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class WindowProduct(QDialog, Ui_Dialog_Product):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_table_product()
        self.btn_add_product.clicked.connect(self.open_add_product)
        self.btn_del_product.clicked.connect(self.open_del_product)

    def open_add_product(self):
        self.add_prod = WinAddProduct()
        if self.add_prod.exec() == 1:
            text_from_form = self.add_prod.lineEdit_2.text()
            cursor.execute('INSERT INTO Товары (Наименование, Стоимость) VALUES (?,?)', ('test', '10'))
            db.commit()
        self.load_table_product()

    def open_del_product(self):
        self.del_product = WinDelProduct()
        self.del_product.show()

    def load_len_product(self):
        cursor.execute(f'SELECT Наименование, `Поставщики`.`ФИО`, `Покупатели`.`ФИО`, id_склада, Стоимость, `Товары`.`Статус` FROM `Товары`, `Поставщики`, `Покупатели`, `Склады` WHERE `Товары`.`id_поставщика` = `Поставщики`.`id` and `Товары`.`id_покупателя` = `Покупатели`.`id` and `Товары`.`id_склада` = `Склады`.`id`')
        g = cursor.fetchall()
        return g

    def load_table_product(self):
        sqlquery = f'SELECT Наименование, `Поставщики`.`ФИО`, `Покупатели`.`ФИО`, id_склада, Стоимость, `Товары`.`Статус`  FROM `Товары`, `Поставщики`, `Покупатели`, `Склады` WHERE `Товары`.`id_поставщика` = `Поставщики`.`id` and `Товары`.`id_покупателя` = `Покупатели`.`id` and `Товары`.`id_склада` = `Склады`.`id`'
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(self.load_len_product()))
        tablerow = 0
        for row in cursor.execute(sqlquery):
            self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 4, QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QTableWidgetItem(row[5]))
            tablerow += 1
        self.update()


class WindowPokup(QDialog, Ui_Dialog_Pokup):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_table_pokup()
        self.btn_add_pokup.clicked.connect(self.open_add_pokup)
        self.btn_del_pokup.clicked.connect(self.open_del_pokup)

    def open_add_pokup(self):
        self.add_pokup = WinAddPokup()
        self.add_pokup.show()

    def open_del_pokup(self):
        self.del_pokup = WinDelPokup()
        self.del_pokup.show()

    def load_len_pokup(self):
        cursor.execute(f'SELECT  ФИО, Адрес, Номер, Адрес_доставки, Дата_доставки, Наименование FROM `Покупатели`, `Товары` WHERE `Покупатели`.`id_товара` = `Товары`.`id`')
        g = cursor.fetchall()
        return g

    def load_table_pokup(self):
        sqlquery = f'SELECT ФИО, Адрес, Номер, Адрес_доставки, Дата_доставки, Наименование FROM `Покупатели`, `Товары` WHERE `Покупатели`.`id_товара` = `Товары`.`id`'
        self.tableWidget.setRowCount(len(self.load_len_pokup()))
        tablerow = 0
        for row in cursor.execute(sqlquery):
            self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QTableWidgetItem(row[5]))
            tablerow += 1



class WindowStocks(QDialog, Ui_Dialog_Stocks):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_table_stocks()
        self.btn_add_stocks.clicked.connect(self.open_add_stocks)
        self.btn_del_stocks.clicked.connect(self.open_del_stocks)

    def open_add_stocks(self):
        self.add_stocks = WinAddStocks()
        self.add_stocks.show()

    def open_del_stocks(self):
        self.del_stocks = WinDelStocks()
        self.del_stocks.show()

    def load_len_stocks(self):
       cursor.execute(f'SELECT Адрес, Вместимость, Статус, Загруженность FROM `Склады`')
       g = cursor.fetchall()
       return g

    def load_table_stocks(self):
        sqlquery = f'SELECT Адрес, Вместимость, Статус, Загруженность FROM `Склады`'
        self.tableWidget.setRowCount(len(self.load_len_stocks()))
        tablerow = 0
        for row in cursor.execute(sqlquery):
            self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
            tablerow += 1



class WindowPost(QDialog, Ui_Dialog_Post):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_table_stocks()
        self.btn_add_post.clicked.connect(self.open_add_post)
        self.btn_del_post.clicked.connect(self.open_del_post)


    def open_del_post(self):
        self.del_post = WinDelPost()
        self.del_post.show()

    def open_add_post(self):
        self.add_post = WinAddPost()
        self.add_post.show()

    def load_len_post(self):
        cursor.execute(f'SELECT ФИО, Номер, Адрес, Паспорт FROM `Поставщики`')
        g = cursor.fetchall()
        return g

    def load_table_stocks(self):
        sqlquery = f'SELECT ФИО, Номер, Адрес, Паспорт FROM `Поставщики`'
        self.tableWidget.setRowCount(len(self.load_len_post()))
        tablerow = 0
        for row in cursor.execute(sqlquery):
            self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            tablerow += 1


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_post.clicked.connect(self.open_table_post)
        self.btn_stocks.clicked.connect(self.open_table_stocks)
        self.btn_pokup.clicked.connect(self.open_table_pokup)
        self.btn_product.clicked.connect(self.open_table_product)

    def open_table_product(self):
        self.WinProduct = WindowProduct()
        self.WinProduct.show()

    def open_table_post(self):
        self.WinPost = WindowPost()
        self.WinPost.show()

    def open_table_stocks(self):
        self.WinStocks = WindowStocks()
        self.WinStocks.show()

    def open_table_pokup(self):
        self.WinPokup = WindowPokup()
        self.WinPokup.show()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
