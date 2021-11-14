import sys

from PyQt5 import QtWidgets

from utils import create_new_user, get_firs_user_by_type, get_all_users_by_type

import main
import admin
import card
import users


class Main(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)

        self.admin = Admin()
        self.card = Card()
        self.user_list = UsersList()

        self.ui.admin_button.clicked.connect(self.open_admin)
        self.ui.employee_button.clicked.connect(self.open_employee_card)
        self.ui.child_button.clicked.connect(self.open_child_card)
        self.ui.employes_button.clicked.connect(self.open_employes)
        self.ui.children_button.clicked.connect(self.open_childrens)

    def open_admin(self):
        self.destroy()
        self.admin.show()

    def open_employee_card(self):
        self.destroy()
        self.card.update_info('employee')
        self.card.show()

    def open_child_card(self):
        self.destroy()
        self.card.update_info('child')
        self.card.show()

    def open_employes(self):
        self.destroy()
        self.user_list.update_info('employee')
        self.user_list.show()

    def open_childrens(self):
        self.destroy()
        self.user_list.update_info('child')
        self.user_list.show()


class Admin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = admin.Ui_MainWindow()
        self.ui.setupUi(self)

        # QString
        self.name = self.ui.name.text
        self.surname = self.ui.surname.text
        self.patronomic = self.ui.patronomic.text
        self.years = self.ui.years.text
        self.data_start = self.ui.data_start.text

        # QCombo
        self.who_combo = self.ui.who_combo
        self.type_combo = self.ui.type_combo
        self.group_combo = self.ui.group_combo

        # Adding choices
        self.update_combo_boxes()

        self.ui.add_button.clicked.connect(self.create_user)

    def create_user(self) -> None:
        data = self.get_values()

        if not data['status']:
            print(data['exception'])
            return

        del data['status']

        create_new_user(data)

    def update_combo_boxes(self) -> None:
        who_combo = self.who_combo
        who_combo.addItem('Добавить сотрудника')
        who_combo.addItem('Добавить ребенка')

        type_combo = self.type_combo
        type_combo.addItem('Старшая')
        type_combo.addItem('Средняя')
        type_combo.addItem('Ясельная')

        group_combo = self.group_combo
        group_combo.addItem('18')
        group_combo.addItem('19')
        group_combo.addItem('20')
        group_combo.addItem('21')

    def get_values(self) -> dict:
        try:
            return {
                'status': True,
                'user_type': self.get_combo_text(self.who_combo),
                'group_type': self.get_combo_text(self.type_combo),
                'group': self.get_combo_text(self.group_combo),
                'name': self.name(),
                'surname': self.surname(),
                'patronomic': self.patronomic(),
                'years': int(self.years()),
                'date_joined': self.data_start(),
            }
        except Exception as e:
            return {'status': False, 'exception': e}

    @staticmethod
    def get_combo_text(combo) -> str:
        if combo.currentIndex() != -1:
            return combo.currentText()
        else:
            raise ValueError(f'Wrong index on {combo.objectName()}')


class Card(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = card.Ui_MainWindow()
        self.ui.setupUi(self)

        self.name = self.ui.name
        self.surname = self.ui.surname
        self.patronomic = self.ui.patronomic
        self.year = self.ui.year
        self.timetable = self.ui.timetable

    def update_info(self, user_type: str):
        data = get_firs_user_by_type(user_type)

        if user_type == 'employee':
            self.setWindowTitle('Карта сотрудника')
        else:
            self.setWindowTitle('Карта ребенка')

        if not data:
            data = {
                "user_type": user_type,
                "group_type": "Тип группы",
                "group": "Номер группы",
                "name": "Имя",
                "surname": "Фамилия",
                "patronomic": "Отчество",
                "years": "Количество лет",
                "date_joined": "Дата регистрации",
                "timetable": [
                    {
                        'year': 2021,
                        'month': 1,
                        'day': 1,
                        'time_start': '09:00',
                        'time_end': '15:00'
                    },
                    {
                        'year': 2021,
                        'month': 1,
                        'day': 2,
                        'time_start': '09:00',
                        'time_end': '16:00'
                    },
                    {
                        'year': 2021,
                        'month': 1,
                        'day': 3,
                        'time_start': '08:30',
                        'time_end': '16:30'
                    }
                ]
            }

        self.name.setText(data['name'])
        self.surname.setText(data['surname'])
        self.patronomic.setText(data['patronomic'])
        self.year.setText(str(data['years']))

        for row_num, row_data in enumerate(data['timetable']):
            self.timetable.insertRow(row_num)
            for column_num, column_key in enumerate(row_data.keys()):
                self.timetable.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(str(row_data[column_key])))


class UsersList(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = users.Ui_MainWindow()
        self.ui.setupUi(self)

        self.table = self.ui.table

    def update_info(self, user_type: str):
        users_with_current_type = get_all_users_by_type(user_type)

        if user_type == 'employee':
            self.setWindowTitle('Сотрудники')
        else:
            self.setWindowTitle('Дети')

        for row in range(len(users_with_current_type)):
            self.table.insertRow(row)

        for row, user in enumerate(users_with_current_type):
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(user['num'])))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(user['name'])))
            self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(user['surname'])))
            self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(user['patronomic'])))
            self.table.setItem(row, 4, QtWidgets.QTableWidgetItem(str(user['group_type'])))
            self.table.setItem(row, 5, QtWidgets.QTableWidgetItem(str(user['group'])))
            self.table.setItem(row, 6, QtWidgets.QTableWidgetItem(str(user['years'])))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = Main()
    myapp.show()
    sys.exit(app.exec_())
