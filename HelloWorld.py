import sys
import urllib.request
from os import listdir
from random import randint
from itertools import product
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


url = ""

countries = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antigua And Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia And Herzegovina", "Botswana", "Brazil", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo (Brazzaville)", "Congo (Kinshasa)", "Cook Islands", "Costa Rica", "D’Ivoire (Ivory Coast)", "Croatia(Hrvatska)", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands(Malvinas)", "Faroe Islands", "Fiji", "Finland", "France", "French Guiana", "French Polynesia", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Vatican City State", "Honduras", "Hong Kong, SAR", "Hungary", "Iceland", "India", "Indonesia", "Iran, Islamic Republic of", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Democratic People’s Republic of (North)", "Korea, Republic of (South)", "Kuwait", "Kyrgyzstan", "Laos (Lao PDR)", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macao (SAR China)", "Macedonia, Republic of", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia, Federated States of", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco and Western Sahara", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Palestinian Territory, Occupied", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Réunion and Mayotte", "Romania", "Russian Federation", "Rwanda", "Saint Helena and also Tristan Da Cunha", "Saint Kitts and Nevis", "Saint Lucia", "Saint Pierre and Miquelon", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "São Tomé and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "Spain", "Sri Lanka", "Sudan", "Suriname", "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic (Syria)", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela (Bolivarian Republic of)", "Viet Nam", "Virgin Islands, British", "Virgin Islands, US", "Wallis and Futuna Islands", "Yemen", "Zambia", "Zimbabwe"]


codes = ["+93", "+355", "+213", "+1", "+376", "+244", "+1", "+1", "+54", "+374", "+297", "+61", "+43", "+994", "+1", "+973", "+880", "+1", "+375", "+32", "+501", "+229", "+1", "+975", "+591", "+387", "+267", "+55", "+673", "+359", "+226", "+257", "+855", "+237", "+1", "+238", "+1", "+236", "+235", "+56", "+86", "+61", "+61", "+57", "+269", "+242", "+243", "+682", "+506", "+225", "+385", "+53", "+357", "+420", "+45", "+253", "+1", "+1", "+593", "+20", "+503", "+240", "+291", "+372", "+251", "+500", "+298", "+679", "+358", "+33", "+594", "+689", "+241", "+220", "+995", "+49", "+233", "+350", "+30", "+299", "+1", "+590", "+1", "+502", "+224", "+245", "+592", "+509", "+379", "+504", "+852", "+36", "+354", "+91", "+62", "+98", "+964", "+353", "+972", "+39", "+1", "+81", "+962", "+7", "+254", "+686", "+850", "+82", "+965", "+996", "+856", "+371", "+961", "+266", "+231", "+218", "+423", "+370", "+352", "+853", "+389", "+261", "+265", "+60", "+960", "+223", "+356", "+692", "+596", "+222", "+230", "+262", "+52", "+691", "+373", "+377", "+976", "+382", "+1", "+212", "+258", "+95", "+264", "+674", "+977", "+31", "+599", "+687", "+64", "+505", "+227", "+234", "+683", "+672", "+1", "+47", "+968", "+92", "+680", "+970", "+507", "+675", "+595", "+51", "+63", "+870", "+48", "+351", "+1", "+974", "+262", "+40", "+7", "+250", "+290", "+1", "+1", "+508", "+1", "+685", "+378", "+239", "+966", "+221", "+381", "+248", "+232", "+65", "+421", "+386", "+677", "+252", "+27", "+34", "+94", "+249", "+597", "+47", "+268", "+46", "+41", "+963", "+886", "+992", "+255", "+66", "+670", "+228", "+690", "+676", "+1", "+216", "+90", "+993", "+1", "+688", "+256", "+380", "+971", "+44", "+1", "+598", "+998", "+678", "+58", "+84", "+1", "+1", "+681", "+967", "+260", "+263"]

chosen_store = ""


class Welcome(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Welcome')

        self.init_ui()

    def init_ui(self):
        self.principalLayout = QVBoxLayout(self)

        self.title = QFrame(self)
        self.title.setFrameShape(QFrame.StyledPanel)
        self.title.setFrameShadow(QFrame.Raised)
        self.verticalLayoutU = QVBoxLayout(self.title)
        self.titleLabel = QLabel(self)
        self.titleLabel.setText("Choose Store:")
        font = self.titleLabel.font()
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.verticalLayoutU.addWidget(self.titleLabel)
        self.principalLayout.addWidget(self.title)

        self.create_store_grid()

        self.principalLayout.addWidget(self.storesFrame)
        self.center()

        self.show()

    def create_store_grid(self):
        self.storesFrame = QFrame(self)
        self.storesFrame.setFrameShape(QFrame.StyledPanel)
        self.storesFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.storesFrame)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)

        # all store logos must end with .png, skipping stores with '_'
        stores = [f.split('.png')[0] for f in listdir('logos') if not f.startswith('_')]
        hloc = list(range(3))  # how many icons in a line
        vloc = list(range(3))  # number of lines
        locations = list(product(vloc, hloc))
        btns = [[stores[i], locations[i]] for i in range(len(stores))]

        for btn in btns:
            (i, (x, y)) = btn
            icon = QIcon('logos/' + i + '.png')
            button = QPushButton(self.storesFrame)
            button.setIconSize(QSize(50, 50))
            button.setFixedSize(210, 100)
            button.setText(i)
            button.setIcon(icon)
            font = button.font()
            font.setPointSize(20)
            button.setFont(font)
            button.clicked.connect(self.load_store)
            self.gridLayout.addWidget(button, x, y)

        self.horizontalLayout.addLayout(self.gridLayout)

    def load_store(self):
        global chosen_store

        chosen_store = self.sender().text()
        self.register = Register()
        self.register.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Register(QWidget):

    def __init__(self):
        super().__init__()

        self.type = randint(1, 2)
        self.init_ui()

    def init_ui(self):
        logo = QIcon('logos/' + chosen_store + '.png')
        self.setWindowTitle('Register')
        self.setWindowIcon(logo)

        self.principalLayout = QHBoxLayout(self)

        self.rightFrame = QFrame(self)
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutL = QVBoxLayout(self.rightFrame)

        self.title = QLabel()
        self.title.setText('Welcome to ' + chosen_store.replace('&&', '&'))
        font = self.title.font()
        font.setPointSize(20)
        self.title.setFont(font)
        self.verticalLayoutL.addWidget(self.title, 1)

        self.itemList = QLabel()
        receipt = QPixmap("receipts/%s/%s.png" % (str(self.type), chosen_store))
        self.itemList.setPixmap(receipt)
        self.verticalLayoutL.addWidget(self.itemList, 5)

        self.country = 'Israel'
        combo = QComboBox(self)
        combo.addItems(countries)
        combo.setCurrentIndex(countries.index(self.country))
        combo.activated[str].connect(self.on_activated)
        font = combo.font()
        font.setPointSize(13)
        combo.setFont(font)
        combo.adjustSize()

        self.principalLayout.addWidget(self.rightFrame, 3)

        self.phoneNumberFrame = QFrame(self)
        self.phoneNumberFrame.setFrameShape(QFrame.StyledPanel)
        self.phoneNumberFrame.setFrameShadow(QFrame.Raised)
        self.labelVerticalLayout = QHBoxLayout(self.phoneNumberFrame)

        self.areaCodeLabel = QLabel(self)
        self.areaCodeLabel.setText(codes[countries.index('Israel')])
        font = self.areaCodeLabel.font()
        font.setPointSize(20)
        self.areaCodeLabel.setFont(font)
        self.labelVerticalLayout.addWidget(self.areaCodeLabel)

        self.numberLine = QLineEdit(self)
        self.numberLine.setReadOnly(True)
        font = self.numberLine.font()
        font.setPointSize(20)
        self.numberLine.setFont(font)


        self.verticalLayoutR = QVBoxLayout()
        self.verticalLayoutR.addWidget(combo)
        self.labelVerticalLayout.addWidget(self.numberLine)
        self.verticalLayoutR.addWidget(self.phoneNumberFrame)

        self.create_number_grid()

        self.verticalLayoutR.addWidget(self.numpadFrame)

        self.sendFrame = QFrame(self)
        self.sendFrame.setFrameShape(QFrame.StyledPanel)
        self.sendFrame.setFrameShadow(QFrame.Raised)
        self.sendVerticalLayout = QVBoxLayout(self.sendFrame)
        self.sendBtn = QPushButton('Send Receipt', self.sendFrame)
        self.sendBtn.clicked.connect(self.get_full_num)
        font = self.sendBtn.font()
        font.setPointSize(20)
        self.sendBtn.setFont(font)
        self.sendVerticalLayout.addWidget(self.sendBtn)
        self.verticalLayoutR.addWidget(self.sendFrame)

        self.principalLayout.addLayout(self.verticalLayoutR, 1)

        self.adjustSize()
        self.center()

    def on_activated(self, text):
        self.country = text
        code = codes[countries.index(self.country)]
        self.areaCodeLabel.setText(code)
        self.areaCodeLabel.adjustSize()

    def create_number_grid(self):
        self.numpadFrame = QFrame(self)
        self.numpadFrame.setFrameShape(QFrame.StyledPanel)
        self.numpadFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.numpadFrame)
        spacerItemLeft = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItemLeft)
        self.verticalLayout = QVBoxLayout()
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)

        hloc = list(range(3))
        vloc = list(range(4))
        locations = list(product(vloc, hloc))
        values = list(range(1, 10))
        values.extend(['CE', 0, 'C'])
        btns = [[values[i], locations[i]] for i in range(len(values))]

        for btn in btns:
            (i, (x, y)) = btn
            button = QPushButton(self.numpadFrame)
            button.setFixedSize(60, 60)
            button.setText(str(i))
            font = button.font()
            font.setPointSize(20)
            button.setFont(font)
            button.clicked.connect(self.add_num)
            self.gridLayout.addWidget(button, x, y)

        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItemRight = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItemRight)

    def add_num(self):
        text = self.sender().text()
        if text == "C":
            self.numberLine.clear()
        elif text == "CE":
            self.numberLine.backspace()
        else:
            self.numberLine.setText(self.numberLine.text() + text)

    def get_full_num(self):
        code = self.areaCodeLabel.text()
        number = self.numberLine.text()[1:] if self.numberLine.text().startswith("0") else self.numberLine.text()

        msg = "Sending receipt to:\nnumber: 0%s\nfrom: %s" % (number, self.country)

        result = QMessageBox.question(self, "Confirm number", msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if result == QMessageBox.Yes:
            full_url = url + "/NewReceipt/%s%s/%s/%s" % (code, number, chosen_store.replace("&&", "&"), self.type)
            print(full_url)
            try:
                urllib.request.urlopen(full_url).read()
            except Exception as ex:
                print(ex)
            self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Welcome()
    sys.exit(app.exec_())