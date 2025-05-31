from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, QDateTime, QTimer
from PyQt5.QtWidgets import QDesktopWidget, QCheckBox, QMessageBox, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap, QImage, QPainter
import configparser
import time
from requests.exceptions import RequestException
import qrcode
import os
from licensing.methods import Key, Helpers

RSAPubKey = "<RSAKeyValue><Modulus>vNB8qoeJTGykdnQUM4O9sK6yil4H5xxjVOuUwoEwdj1k+qjk67qwe2h2nEcuJqrrfV9HDQLCewyc2iC/IqaRzppQ3f1l+ixUsMzP4f2bheAavxQ9FP6JE7hj3YF+LMRvzpCK47YWySrjRwgJ1yCWiRvj4hKBzqa+XRULFbOxioz7SrPgGJDggkd/2S+rAXCn+zQnInSjp+7BDAac8WplMOy1EnVnLpfL4I0aOaY/cIQffFxLEYwgzWLvD153FIOfM9KeUUxAUJqqV8GhRZXHyclfkmlTsBokbZ+Bu8PlwreBfMGnmWb5FcT0jTLuhHEzYsQ5z40kzw1c9kw4rgBHFw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyI4OTQ0NTgyMyIsIm4rWWV1dDd4NTJYTUhOY2dNZ2ExTVhZb20xWTkrTkVIdGFZL2RETWMiXQ=="  # AUTHKEY WITH ACTIVATE !

class Ui_Form(object): 
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(429, 319)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setStyleSheet("background-color: rgb(100, 178, 128);")

        self.lbTitle = QtWidgets.QLabel(Form)
        self.lbTitle.setGeometry(QtCore.QRect(10, 10, 411, 51))
        self.lbTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbTitle.setStyleSheet('font: 16pt "Khmer OS Muol Pali";')
        self.lbTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTitle.setObjectName("lbTitle")

        self.gbFunction = QtWidgets.QGroupBox(Form)
        self.gbFunction.setGeometry(QtCore.QRect(10, 60, 411, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gbFunction.setFont(font)
        self.gbFunction.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gbFunction.setStyleSheet("color: rgb(255, 255, 255);")
        self.gbFunction.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gbFunction.setFlat(False)
        self.gbFunction.setObjectName("gbFunction")

        self.txtDeviceIDPC = QtWidgets.QLineEdit(self.gbFunction)
        self.txtDeviceIDPC.setGeometry(QtCore.QRect(20, 56, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.txtDeviceIDPC.setFont(font)
        self.txtDeviceIDPC.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);")
        self.txtDeviceIDPC.setObjectName("txtDeviceIDPC")
        self.txtDeviceIDPC.setEchoMode(QtWidgets.QLineEdit.Password)  # Set default as Password mode

        self.lbPC = QtWidgets.QLabel(self.gbFunction)
        self.lbPC.setGeometry(QtCore.QRect(20, 26, 131, 31))
        self.lbPC.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbPC.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbPC.setObjectName("lbPC")

        self.txtLicenseKey = QtWidgets.QLineEdit(self.gbFunction)
        self.txtLicenseKey.setGeometry(QtCore.QRect(20, 136, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.txtLicenseKey.setFont(font)
        self.txtLicenseKey.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);")
        self.txtLicenseKey.setObjectName("txtLicenseKey")
        self.txtLicenseKey.setEchoMode(QtWidgets.QLineEdit.Password)  # Set default as Password mode

        self.lbKey = QtWidgets.QLabel(self.gbFunction)
        self.lbKey.setGeometry(QtCore.QRect(20, 106, 131, 31))
        self.lbKey.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbKey.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbKey.setObjectName("lbKey")

        self.chkShowHide = QtWidgets.QCheckBox(self.gbFunction)
        self.chkShowHide.setGeometry(QtCore.QRect(20, 186, 101, 17))
        self.chkShowHide.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chkShowHide.setObjectName("chkShowHide")

        self.chkSavePassword = QtWidgets.QCheckBox(self.gbFunction)
        self.chkSavePassword.setGeometry(QtCore.QRect(90, 186, 101, 17))
        self.chkSavePassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chkSavePassword.setObjectName("chkSavePassword")
        self.chkSavePassword.setChecked(True)

        self.btnLogin = QtWidgets.QPushButton(self.gbFunction)
        self.btnLogin.setGeometry(QtCore.QRect(300, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Khmer OS Muol Light")
        font.setPointSize(10)
        self.btnLogin.setFont(font)
        self.btnLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogin.setStyleSheet("color: rgb(0, 170, 0);\nfont: 10pt \"Khmer OS Muol Light\";\nbackground-color: rgb(255, 255, 255);")
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.clicked.connect(self.checkLicense)  # Connect login button to checkLicense function

        self.btnClose = QtWidgets.QPushButton(self.gbFunction)
        self.btnClose.setGeometry(QtCore.QRect(190, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Khmer OS Muol Light")
        font.setPointSize(10)
        self.btnClose.setFont(font)
        self.btnClose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnClose.setStyleSheet("color: rgb(255, 0, 0);\nfont: 10pt \"Khmer OS Muol Light\";\nbackground-color: rgb(255, 255, 255);")
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.confirmClose)  # Connect close button to confirmClose function

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Enable dragging of the window
        self.offset = None
        Form.mousePressEvent = self.mousePressEvent
        Form.mouseMoveEvent = self.mouseMoveEvent

        # Connect the checkbox to the show/hide function
        self.chkShowHide.stateChanged.connect(self.toggleTextVisibility)

        # Check if config file exists and load data
        config = configparser.ConfigParser()
        if config.read('QR_config.ini'):
            if 'Login - QR Code Generate by Phekdey PHORN' in config and 'DeviceID' in config['Login - QR Code Generate by Phekdey PHORN']:
                self.txtDeviceIDPC.setText(config['Login - QR Code Generate by Phekdey PHORN']['DeviceID'])
            if 'Login - QR Code Generate by Phekdey PHORN' in config and 'LicenseKey' in config['Login - QR Code Generate by Phekdey PHORN']:
                self.txtLicenseKey.setText(config['Login - QR Code Generate by Phekdey PHORN']['LicenseKey'])

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbTitle.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#ffffff;\">ចូលកម្មវិធី - QR Code Generate</span></p></body></html>"))
        self.gbFunction.setTitle(_translate("Form", " សួស្ដី "))
        self.lbPC.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">លេខម៉ាស៊ីនកុំព្យូទ័រ</span></p></body></html>"))
        self.lbKey.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">សោអាជ្ញាប័ណ្ណ</span></p></body></html>"))
        self.chkShowHide.setText(_translate("Form", "បង្ហាញ"))
        self.chkSavePassword.setText(_translate("Form", "ចងចាំ"))
        self.btnLogin.setText(_translate("Form", "ចូល"))
        self.btnClose.setText(_translate("Form", "បិទ"))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            Form.move(Form.pos() + event.pos() - self.offset)

    def confirmClose(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setIcon(QtWidgets.QMessageBox.Question)
        message_box.setWindowTitle('បញ្ជាក់ការបិទ')
        message_box.setText('តើអ្នកពិតជាចង់បិទចោលកម្មវិធីមែនឬទេ?')

        yes_button = message_box.addButton('យល់ព្រម', QtWidgets.QMessageBox.YesRole)
        yes_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        no_button = message_box.addButton('បដិសេដ', QtWidgets.QMessageBox.NoRole)
        no_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        message_box.setDefaultButton(no_button)

        reply = message_box.exec_()

        if message_box.clickedButton() == yes_button:
            QtCore.QCoreApplication.instance().quit()

    def toggleTextVisibility(self):
        if self.chkShowHide.isChecked():
            self.txtDeviceIDPC.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.txtLicenseKey.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.txtDeviceIDPC.setEchoMode(QtWidgets.QLineEdit.Password)
            self.txtLicenseKey.setEchoMode(QtWidgets.QLineEdit.Password)

    def checkLicense(self):
        device_id = self.txtDeviceIDPC.text().strip()
        license_key = self.txtLicenseKey.text().strip()

        # Check if fields are empty
        if not device_id or not license_key:
            QtWidgets.QMessageBox.critical(None, "កំហុស", "សូមបំពេញទម្រង់លេខម៉ាស៊ីនកុំព្យូទ័រ | លេខសោអាជ្ញាប័ណ្ណ។")
            return

        try:
            result = Key.activate(token=auth,
                                  rsa_pub_key=RSAPubKey,
                                  product_id=26531,
                                  key=license_key,
                                  machine_code=device_id)

            if result[0] is None:
                error_message = "បរាជ័យក្នុងការបើកដំណើរការអាជ្ញាប័ណ្ណ: {0}".format(result[1])
                QtWidgets.QMessageBox.critical(None, "កំហុសអាជ្ញាប័ណ្ណ", error_message)
            elif not Helpers.IsOnRightMachine(result[0]):
                error_message = "អាជ្ញាប័ណ្ណមិនត្រូវគ្នានឹងម៉ាស៊ីននេះទេ។"
                QtWidgets.QMessageBox.critical(None, "កំហុសអាជ្ញាប័ណ្ណ", error_message)
            else:
                success_message = "អាជ្ញាប័ណ្ណត្រូវបានដំណើរការដោយជោគជ័យ !"
                QtWidgets.QMessageBox.information(None, "អាជ្ញាប័ណ្ណមានសុពលភាព", success_message)
                license_key = result[0]
                period = str(license_key.period)

                # Check if Save Password checkbox is checked
                if self.chkSavePassword.isChecked():
                    # Save login details to config file
                    config = configparser.ConfigParser()
                    config['Login - QR Code Generate by Phekdey PHORN'] = {
                        'DeviceID': device_id,
                        'LicenseKey': license_key.key,
                        'Create License Key': license_key.created,
                        'Expired License Key': license_key.expires,
                        'Allow Use This Key': license_key.max_no_of_machines,
                        'License Key No.': license_key.id,
                    }
                    # Write to config file
                    with open('QR_config.ini', 'w') as configfile:
                        config.write(configfile)

                self.login_success()

        except RequestException as e:
            QtWidgets.QMessageBox.critical(None, "Network Error", f"Could not contact the server: {e}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"An unexpected error occurred: {e}")

    def login_success(self):
        # Close the login form
        Form.close()

        # Launch the main application
        self.main_app = MainApplication()
        self.main_app.show()


class MainApplication(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.resize(612, 460)
        self.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.lbUser = QtWidgets.QLabel(self)
        self.lbUser.setGeometry(QtCore.QRect(10, 0, 291, 61))
        self.lbUser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbUser.setStyleSheet('font: 10pt "Khmer OS Muol Light";')
        self.lbUser.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbUser.setObjectName("lbUser")
        
        self.btnMinimize = QtWidgets.QPushButton(self)
        self.btnMinimize.setGeometry(QtCore.QRect(540, 20, 21, 21))
        self.btnMinimize.setFont(QtGui.QFont("MS PGothic", 12))
        self.btnMinimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMinimize.setStyleSheet("color: rgb(0, 0, 127);\nbackground-color: rgb(255, 255, 255);\nfont: 12pt 'MS PGothic';")
        self.btnMinimize.setObjectName("btnMinimize")
        self.btnMinimize.clicked.connect(self.showMinimized)
        
        self.btnInfo = QtWidgets.QPushButton(self)
        self.btnInfo.setGeometry(QtCore.QRect(500, 20, 21, 21))
        self.btnInfo.setFont(QtGui.QFont("MS PGothic", 12))
        self.btnInfo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnInfo.setStyleSheet("color: rgb(0, 0, 127);\nbackground-color: rgb(255, 255, 255);\nfont: 12pt 'MS PGothic';")
        self.btnInfo.setObjectName("btnInfo")
        self.btnInfo.clicked.connect(self.showInfo)

        self.btnLicense = QtWidgets.QPushButton(self)
        self.btnLicense.setGeometry(QtCore.QRect(460, 20, 21, 21))
        self.btnLicense.setFont(QtGui.QFont("MS PGothic", 12))
        self.btnLicense.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLicense.setStyleSheet("color: rgb(0, 0, 127);\nbackground-color: rgb(255, 255, 255);\nfont: 12pt 'MS PGothic';")
        self.btnLicense.setObjectName("btnLicense")
        self.btnLicense.clicked.connect(self.showLicense)
        
        self.btnClose = QtWidgets.QPushButton(self)
        self.btnClose.setGeometry(QtCore.QRect(580, 20, 21, 21))
        self.btnClose.setFont(QtGui.QFont("MS PGothic", 12))
        self.btnClose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnClose.setStyleSheet("color: rgb(0, 0, 127);\nbackground-color: rgb(255, 255, 255);\nfont: 12pt 'MS PGothic';")
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.confirmClose)
        
        self.lbNameApp = QtWidgets.QLabel(self)
        self.lbNameApp.setGeometry(QtCore.QRect(10, 60, 591, 61))
        self.lbNameApp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbNameApp.setStyleSheet('font: 14pt "Khmer OS Muol Light";\nbackground-color: rgb(161, 167, 255);\ncolor: blue;')
        self.lbNameApp.setAlignment(QtCore.Qt.AlignCenter)  # Align text to the center
        self.lbNameApp.setObjectName("lbNameApp")
        
        self.gbAction = QtWidgets.QGroupBox(self)
        self.gbAction.setGeometry(QtCore.QRect(10, 300, 351, 81))
        self.gbAction.setFont(QtGui.QFont("Khmer OS Fasthand", 8))
        self.gbAction.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.gbAction.setStyleSheet("color: rgb(0, 0, 0);")
        self.gbAction.setObjectName("gbAction")
        
        self.btnSave = QtWidgets.QPushButton(self.gbAction)
        self.btnSave.setGeometry(QtCore.QRect(240, 30, 90, 31))
        self.btnSave.setFont(QtGui.QFont("Khmer OS Muol Light", 8))
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSave.setStyleSheet("color: rgb(255, 0, 0);\nfont: 8pt 'Khmer OS Muol Light';\nbackground-color: rgb(255, 255, 255);")
        self.btnSave.setObjectName("btnSave")
        self.btnSave.clicked.connect(self.saveQrCode)
        
        self.btnClear = QtWidgets.QPushButton(self.gbAction)
        self.btnClear.setGeometry(QtCore.QRect(130, 30, 90, 31))
        self.btnClear.setFont(QtGui.QFont("Khmer OS Muol Light", 8))
        self.btnClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnClear.setStyleSheet("color: rgb(255, 170, 0);\nfont: 8pt 'Khmer OS Muol Light';\nbackground-color: rgb(255, 255, 255);")
        self.btnClear.setObjectName("btnClear")
        self.btnClear.clicked.connect(self.validate_clear_code)
        
        self.btnGenerate = QtWidgets.QPushButton(self.gbAction)
        self.btnGenerate.setGeometry(QtCore.QRect(20, 30, 90, 31))
        self.btnGenerate.setFont(QtGui.QFont("Khmer OS Muol Light", 8))
        self.btnGenerate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGenerate.setStyleSheet("color: rgb(0, 170, 0);\nfont: 8pt 'Khmer OS Muol Light';\nbackground-color: rgb(255, 255, 255);")
        self.btnGenerate.setObjectName("btnGenerate")
        self.btnGenerate.clicked.connect(self.generateQrCode)
        
        self.gbAddLink = QtWidgets.QGroupBox(self)
        self.gbAddLink.setGeometry(QtCore.QRect(10, 130, 591, 81))
        self.gbAddLink.setFont(QtGui.QFont("Khmer OS Fasthand", 8))
        self.gbAddLink.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.gbAddLink.setStyleSheet("color: rgb(0, 0, 0);")
        self.gbAddLink.setObjectName("gbAddLink")
        
        self.txtLinkGenerate = QtWidgets.QPlainTextEdit(self.gbAddLink)
        self.txtLinkGenerate.setGeometry(QtCore.QRect(10, 25, 571, 45))
        self.txtLinkGenerate.setFont(QtGui.QFont("Roboto", 9))
        self.txtLinkGenerate.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.txtLinkGenerate.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);\nborder-color: 1px solid rgb(0, 0, 0);")
        self.txtLinkGenerate.setObjectName("txtLinkGenerate")
        
        self.gbPreviewQRCode = QtWidgets.QGroupBox(self)
        self.gbPreviewQRCode.setGeometry(QtCore.QRect(380, 220, 221, 231))
        self.gbPreviewQRCode.setFont(QtGui.QFont("Khmer OS Fasthand", 8))
        self.gbPreviewQRCode.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.gbPreviewQRCode.setStyleSheet("color: rgb(0, 0, 0);")
        self.gbPreviewQRCode.setObjectName("gbPreviewQRCode")
        
        self.frameGenerateQrCode = QtWidgets.QFrame(self.gbPreviewQRCode)
        self.frameGenerateQrCode.setGeometry(QtCore.QRect(10, 20, 200, 200))
        self.frameGenerateQrCode.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameGenerateQrCode.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameGenerateQrCode.setObjectName("frameGenerateQrCode")
        
        self.gbAddImgQR = QtWidgets.QGroupBox(self)
        self.gbAddImgQR.setGeometry(QtCore.QRect(10, 220, 351, 80))
        self.gbAddImgQR.setFont(QtGui.QFont("Khmer OS Fasthand", 8))
        self.gbAddImgQR.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gbAddImgQR.setStyleSheet("color: rgb(0, 0, 0);")
        self.gbAddImgQR.setCheckable(True)
        self.gbAddImgQR.setObjectName("gbAddImgQR")
        self.gbAddImgQR.setChecked(False)
        
        self.txtImgQrCode = QtWidgets.QPlainTextEdit(self.gbAddImgQR)
        self.txtImgQrCode.setGeometry(QtCore.QRect(10, 25, 281, 40))
        self.txtImgQrCode.setFont(QtGui.QFont("Roboto", 9))
        self.txtImgQrCode.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.txtImgQrCode.setStyleSheet("background-color: rgb(255, 255, 255);\ncolor: rgb(0, 0, 0);\nborder-color: 1px solid rgb(0, 0, 0);")
        self.txtImgQrCode.setObjectName("txtImgQrCode")
        
        self.btnBrowseImgQR = QtWidgets.QToolButton(self.gbAddImgQR)
        self.btnBrowseImgQR.setGeometry(QtCore.QRect(294, 25, 41, 40))
        self.btnBrowseImgQR.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBrowseImgQR.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnBrowseImgQR.setObjectName("btnBrowseImgQR")
        self.btnBrowseImgQR.clicked.connect(self.browseImageFile)
        
        self.txtCurrentDateTime = QtWidgets.QLabel(self)
        self.txtCurrentDateTime.setGeometry(QtCore.QRect(10, 400, 351, 41))
        self.txtCurrentDateTime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtCurrentDateTime.setStyleSheet('color: green;')
        self.txtCurrentDateTime.setFont(QtGui.QFont("Khmer OS Fasthand", 8))
        self.txtCurrentDateTime.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.txtCurrentDateTime.setObjectName("txtCurrentDateTime")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.offset = None
        Form.mousePressEvent = self.mousePressEvent
        Form.mouseMoveEvent = self.mouseMoveEvent

        # Set up a timer to update the date and time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)  # Update every second
        self.updateDateTime()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.lbUser.setText(_translate("self", "ផន ភក្ដី | កំណែទម្រង់ ៣.០"))
        self.btnMinimize.setText(_translate("self", "-"))
        self.btnLicense.setText(_translate("self", "#"))
        self.btnInfo.setText(_translate("self", "?"))
        self.btnClose.setText(_translate("self", "X"))
        self.lbNameApp.setText(_translate("self", "កម្មវិធីបង្កើត​ QR Code"))
        self.gbAction.setTitle(_translate("self", " មុខងារ "))
        self.btnSave.setText(_translate("self", "រក្សាទុក"))
        self.btnClear.setText(_translate("self", "សម្អាត"))
        self.btnGenerate.setText(_translate("self", "បង្កើត"))
        self.gbAddLink.setTitle(_translate("self", " តំណភ្ជាប់ "))
        self.gbPreviewQRCode.setTitle(_translate("self", " លទ្ទផល "))
        self.gbAddImgQR.setTitle(_translate("self", " រូបភាព "))
        self.btnBrowseImgQR.setText(_translate("self", "..."))
        self.txtCurrentDateTime.setText(_translate("self", "date"))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)

    def updateDateTime(self):
        current_time = QDateTime.currentDateTime()
        time_str = current_time.toString('hh:mm:ss AP')
        date_str = current_time.toString('dd-MMMM-yyyy')
        
        # Splitting the time and AM/PM parts
        time_parts, am_pm = time_str.split(' ')
        
        # Converting the time and date to the desired format
        hour, minute, second = map(int, time_parts.split(':'))
        am_pm_kh = 'ព្រឹក' if am_pm == 'AM' else 'ល្ងាច'
        
        # Convert to Khmer numbers
        khmer_numbers = {0: '០', 1: '១', 2: '២', 3: '៣', 4: '៤', 5: '៥', 6: '៦', 7: '៧', 8: '៨', 9: '៩'}
        hour_kh = ''.join(khmer_numbers[int(digit)] for digit in str(hour))
        minute_kh = ''.join(khmer_numbers[int(digit)] for digit in str(minute))
        second_kh = ''.join(khmer_numbers[int(digit)] for digit in str(second))
        
        # Convert date to Khmer
        day, month, year = date_str.split('-')
        day_kh = ''.join(khmer_numbers[int(digit)] for digit in day)
        month_kh = self.convertMonthToKhmer(month)
        year_kh = ''.join(khmer_numbers[int(digit)] for digit in year)
        
        formatted_date_time = f"{am_pm_kh} | {day_kh}-{month_kh}-{year_kh} \n{hour_kh}:{minute_kh}:{second_kh}"
        self.txtCurrentDateTime.setText(formatted_date_time)

    def convertMonthToKhmer(self, month):
        khmer_months = {
            "January": "មករា",
            "February": "កុម្ភៈ",
            "March": "មីនា",
            "April": "មេសា",
            "May": "ឧសភា",
            "June": "មិថុនា",
            "July": "កក្កដា",
            "August": "សីហា",
            "September": "កញ្ញា",
            "October": "តុលា",
            "November": "វិច្ឆិកា",
            "December": "ធ្នូ"
        }
        return khmer_months.get(month, month)

    def confirmClose(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setIcon(QtWidgets.QMessageBox.Question)
        message_box.setWindowTitle('បញ្ជាក់ការបិទ')
        message_box.setText('តើអ្នកពិតជាចង់បិទចោលកម្មវិធីមែនឬទេ?')

        yes_button = message_box.addButton('យល់ព្រម', QtWidgets.QMessageBox.YesRole)
        yes_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        no_button = message_box.addButton('បដិសេដ', QtWidgets.QMessageBox.NoRole)
        no_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        message_box.setDefaultButton(no_button)

        reply = message_box.exec_()

        if message_box.clickedButton() == yes_button:
            QtCore.QCoreApplication.instance().quit()

    def showInfo(self):
        info_text = """
        <html>
            <body style='font-size: 12pt; color: white; background-color: gray;'>
                <p>កម្មវិធីឈ្មោះ: QR Code Generate</p>
                <p>សរសេរដោយ: Phekdey PHORN | ផន ភក្ដី</p>
                <p>ទំនាក់ទំនង: ០៨៩ ៧៥៥ ៧៧០</p>
                <p>ភាសាកូដៈ Python</p>
                <p>បង្កើតថ្ងៃៈ ១៦-កក្កដា-២០២៤</p>
                <p>បច្ចុប្បន្នភាពចុងក្រោយៈ ១៧-កក្កដា-២០២៤</p>
                <p>ការប្រើប្រាស់ៈ ឥតគិតថ្លៃ</p>
                <p>កំណែទម្រង់ៈ៣.០</p>
            </body>
        </html>
        """
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Info")
        msg_box.setText(info_text)
        msg_box.setStyleSheet("QLabel{min-width: 400px;}")
        return_button = msg_box.addButton("ត្រលប់", QMessageBox.AcceptRole)
        return_button.setStyleSheet("color: white;")
        return_button.setCursor(Qt.PointingHandCursor)
        msg_box.exec_()
        return_button.clicked.connect(msg_box.close)

    def showMinimized(self):
        self.showMinimized()

    def showLicense(self):
        config = configparser.ConfigParser()
        config.read('QR_config.ini')

        device_id = config.get('Login - QR Code Generate by Phekdey PHORN', 'deviceid')
        license_key = config.get('Login - QR Code Generate by Phekdey PHORN', 'licensekey')
        create_date_str = config.get('Login - QR Code Generate by Phekdey PHORN', 'create license key')
        expire_date_str = config.get('Login - QR Code Generate by Phekdey PHORN', 'expired license key')

        create_date = QDateTime.fromString(create_date_str, 'yyyy-MM-dd hh:mm:ss')
        expire_date = QDateTime.fromString(expire_date_str, 'yyyy-MM-dd hh:mm:ss')

        current_day = self.get_current_day()

        license_text = f"""
        <html>
            <body style='font-size: 12pt; color: white; background-color: gray;'>
                <p>លេខម៉ាស៊ីនកុំព្យូទ័រ: {device_id}</p>
                <p>សោអាជ្ញាបណ្ណ: {license_key}</p>
                <p>ពេលចាប់ផ្ដើម: {create_date.toString('dd-MMM-yyyy hh:mm:ss')}</p>
                <p>ពេលបញ្ចប់: {expire_date.toString('dd-MMM-yyyy hh:mm:ss')}</p>
                <p>ថ្ងៃនេះ: {current_day}</p>
            </body>
        </html>
        """

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("License")
        msg_box.setText(license_text)
        msg_box.setStyleSheet("QLabel{min-width: 800px;}")

        return_button = msg_box.addButton("ត្រលប់", QMessageBox.AcceptRole)
        return_button.setStyleSheet("color: white;")
        return_button.setCursor(Qt.PointingHandCursor)

        msg_box.exec_()
        return_button.clicked.connect(msg_box.close)

    def get_current_day(self):
        current_date = QDateTime.currentDateTime().toString('dd-MMM-yyyy hh:mm:ss')
        return current_date

    def validate_clear_code(self):
        linkGenerateQR = self.txtLinkGenerate.toPlainText().strip()
        fileImgQr = self.txtImgQrCode.toPlainText().strip()
        
        if not linkGenerateQR and not fileImgQr:
            warning_box = QMessageBox(self)
            warning_box.setWindowTitle('ការព្រមាន')
            warning_box.setText('មិនមានទិន្នន័យទេ!')
            warning_box.setStyleSheet("""
                QLabel { color: white; }
                QPushButton { color: white; background-color: rgb(50, 50, 50); }
            """)
            warning_box.setStandardButtons(QMessageBox.Ok)
            warning_box.button(QMessageBox.Ok).setText('យល់ព្រម')
            warning_box.button(QMessageBox.Ok).setCursor(Qt.PointingHandCursor)
            warning_box.exec_()
        elif linkGenerateQR or fileImgQr:
            confirmation_box = QMessageBox(self)
            confirmation_box.setWindowTitle('បញ្ជាក់ការសម្អាត')
            confirmation_box.setText('តើអ្នកពិតជាចង់សម្អាតទម្រង់វាចោលមែនទេ?')
            confirmation_box.setStyleSheet("""
                QLabel { color: white; }
                QPushButton { color: white; background-color: rgb(50, 50, 50); }
            """)
            confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirmation_box.button(QMessageBox.Yes).setText('យល់ព្រម')
            confirmation_box.button(QMessageBox.Yes).setCursor(Qt.PointingHandCursor)
            confirmation_box.button(QMessageBox.No).setText('បដិសេដ')
            confirmation_box.button(QMessageBox.No).setCursor(Qt.PointingHandCursor)
            
            reply = confirmation_box.exec_()
            if reply == QMessageBox.Yes:
                self.txtLinkGenerate.clear()
                self.txtImgQrCode.clear()
                #self.clearQrCode()

    def clearQrCode(self):
        layout = self.frameGenerateQrCode.layout()
        if layout:
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()

    def validate_get_qr_code(self):
        linkGenerateQR = self.txtLinkGenerate.toPlainText().strip()
        if not linkGenerateQR:
            message_box = QMessageBox(self)
            message_box.setWindowTitle('ការព្រមាន')
            message_box.setText('សូមបញ្ចូលតំណភ្ជាប់សម្រាប់បង្កើតជាមុនសិន!')
            message_box.setStyleSheet("""
                QLabel { color: white; }
                QPushButton { color: white; background-color: rgb(50, 50, 50); }
            """)
            message_box.exec_()
        else:
            return linkGenerateQR

    def generateQrCode(self):
        url = self.txtLinkGenerate.toPlainText().strip()
        if url:
            try:
                qr_code_dir = 'C:/QR_Code_PY/'
                if not os.path.exists(qr_code_dir):
                    os.makedirs(qr_code_dir)
                
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(url)
                qr.make(fit=True)
                
                img = qr.make_image(fill='black', back_color='white')
                
                if self.gbAddImgQR.isChecked():
                    img_path = self.txtImgQrCode.toPlainText().strip()
                    if img_path and os.path.isfile(img_path):
                        # 
                        return 0
                
                img_path = os.path.join(qr_code_dir, 'qrcode.png')
                img.save(img_path)  # Save QR code to the specified location
                
                pixmap = QPixmap(img_path)
                self.qr_pixmap = pixmap
                
                label = QtWidgets.QLabel(self.frameGenerateQrCode)
                label.setGeometry(QtCore.QRect(0, 0, 200, 200))
                label.setPixmap(pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio))
                label.setAlignment(Qt.AlignCenter)
                
                # Clear previous layout if it exists
                layout = self.frameGenerateQrCode.layout()
                if layout:
                    QtWidgets.QWidget().setLayout(layout)
                
                # Create new layout and add the label
                layout = QtWidgets.QVBoxLayout()
                layout.addWidget(label)
                self.frameGenerateQrCode.setLayout(layout)
            
            except Exception as e:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setWindowTitle('Error')
                msgBox.setText(f'An error occurred while generating the QR Code: {e}')
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
        
        else:
            self.validate_get_qr_code()
            
    def saveQrCode(self):
        # Check if the frame is empty by checking its size and contents
        if not self.frameGenerateQrCode.children():
            message_box = QMessageBox(self)
            message_box.setWindowTitle('ការព្រមាន')
            message_box.setText('សូមបង្កើត QR Code មុនពេលរក្សាទុក។')
            message_box.setStyleSheet("""
                QLabel { color: white; }
                QPushButton { color: white; background-color: rgb(50, 50, 50); }
            """)
            message_box.exec_()
            return
        
        # Create a pixmap of the frame
        pixmap = QPixmap(self.frameGenerateQrCode.size())
        self.frameGenerateQrCode.render(pixmap)
        
        # Open a file dialog to choose the save location
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(None, "រក្សាទុករូបភាព QR Code", "", "PNG Files (*.png);;JPEG Files (*.jpg);;BMP Files (*.bmp);;All Files (*)", options=options)
        
        # Save the image
        if fileName:
            pixmap.save(fileName)

    def browseImageFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(None, "សូមជ្រើសរើសរូបភាពសម្រាប់ QR Code", "", "Image Files (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if fileName:
            self.txtImgQrCode.setPlainText(fileName)


            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


