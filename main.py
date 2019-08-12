import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel, QRadioButton, QGroupBox
from PyQt5.QtCore import Qt

class main(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        mainText = QLabel('Select Menu', self)
        mainText.setAlignment(Qt.AlignCenter)
        mainTextFont = mainText.font()
        mainTextFont.setPointSize(15)
        mainText.setFont(mainTextFont)

        btnCheckDevice = QPushButton('Device Connection Check', self)
        btnSystemAppRemove = QPushButton('System Application Removal', self)
        btnSystemAppRestore = QPushButton('System Application Restore', self)
        btnShellCmd = QPushButton('Use Shell Command', self)
        btnResolution = QPushButton('Change Screen Resolution', self)
        btnNavibar = QPushButton('Enable/Disable Navigation Bar', self)
        btnOperatorLogo = QPushButton('Remove Operator and VoLTE Logo', self)
        btnSubstratum = QPushButton('Enable Substratum', self)
        btnLogcat = QPushButton('Read Logcat', self)
        btnExit = QPushButton('EXIT', self)

        btnCheckDevice.clicked.connect(self.clickedCheckDevice)
        btnSystemAppRemove.clicked.connect(self.clickedSystemAppRemove)
        btnSystemAppRestore.clicked.connect(self.clickedSystemAppRestore)
        btnShellCmd.clicked.connect(self.clickedShellCmd)
        btnResolution.clicked.connect(self.clickedResolution)
        btnNavibar.clicked.connect(self.clickedNavibar)
        btnOperatorLogo.clicked.connect(self.clickedOperatorLogo)
        btnSubstratum.clicked.connect(self.clickedSubstratum)
        btnLogcat.clicked.connect(self.clickedLogcat)
        btnExit.clicked.connect(self.clickedExit)

        vbox = QVBoxLayout()
        vbox.addWidget(mainText)
        vbox.addWidget(btnCheckDevice)
        vbox.addWidget(btnSystemAppRemove)
        vbox.addWidget(btnSystemAppRestore)
        vbox.addWidget(btnShellCmd)
        vbox.addWidget(btnResolution)
        vbox.addWidget(btnNavibar)
        vbox.addWidget(btnOperatorLogo)
        vbox.addWidget(btnSubstratum)
        vbox.addWidget(btnLogcat)
        vbox.addWidget(btnExit)

        self.setLayout(vbox)
        self.setWindowTitle('Auto ADB for LG Devices')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

    def clickedCheckDevice(self):
        checkDevice = str(os.popen('.\\bin\\adb.exe devices -l').read()).find('product:')
        if checkDevice == -1:
            reply = QMessageBox.information(self, 'Device Connection', 'Device is not Connected. Please check Device state. Open Manual?', QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                os.system('notepad ".\\bin\\manual.txt"')
        else:
            QMessageBox.information(self, 'Device Connection', 'Device is Connected Correctly', QMessageBox.Yes, QMessageBox.Yes)

    def clickedSystemAppRemove(self):
        dlg = dialogSystemAppRemove()
        dlg.initUI(QWidget)

    def clickedSystemAppRestore(self):
        dlg = dialogSystemAppRestore()
        dlg.initUI(QWidget)

    def clickedShellCmd(self):
        pass

    def clickedResolution(self):
        pass

    def clickedNavibar(self):
        pass

    def clickedOperatorLogo(self):
        pass

    def clickedSubstratum(self):
        pass

    def clickedLogcat(self):
        pass

    def clickedExit(self):
        reply = QMessageBox.question(self, 'EXIT', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            sys.exit()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class dialogSystemAppRemove(QWidget):
    selDevice = 'G6'
    selOperator = 'SKT'

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grpDevice = QGroupBox('Device')
        grpOperator = QGroupBox('Operator')

        btnRemoveStart = QPushButton('Start Removing', self)
        btnRemoveStart.clicked.connect(self.startRemove)

        self.rbtnG6 = QRadioButton('G6', self)
        self.rbtnG7 = QRadioButton('G7 ThinQ', self)
        self.rbtnG8 = QRadioButton('G8 ThinQ', self)
        self.rbtnV30 = QRadioButton('V30 ThinQ', self)
        self.rbtnV40 = QRadioButton('V40 ThinQ', self)
        self.rbtnV50 = QRadioButton('V50 ThinQ', self)
        self.rbtnSKT = QRadioButton('SKT', self)
        self.rbtnKT = QRadioButton('KT', self)
        self.rbtnLGU = QRadioButton('LG U+', self)

        grpDeviceLayout = QVBoxLayout()
        grpOperatorLayout = QVBoxLayout()
        vbox = QVBoxLayout()

        grpDeviceLayout.addWidget(self.rbtnG6)
        grpDeviceLayout.addWidget(self.rbtnG7)
        grpDeviceLayout.addWidget(self.rbtnG8)
        grpDeviceLayout.addWidget(self.rbtnV30)
        grpDeviceLayout.addWidget(self.rbtnV40)
        grpDeviceLayout.addWidget(self.rbtnV50)

        grpOperatorLayout.addWidget(self.rbtnSKT)
        grpOperatorLayout.addWidget(self.rbtnKT)
        grpOperatorLayout.addWidget(self.rbtnLGU)

        grpDevice.setLayout(grpDeviceLayout)
        grpOperator.setLayout(grpOperatorLayout)

        vbox.addWidget(grpDevice)
        vbox.addWidget(grpOperator)
        vbox.addWidget(btnRemoveStart)

        self.setLayout(vbox)
        self.setWindowTitle('System Application Remove')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

    def startRemove(self):
        selDevice = ""
        selOperator = ""

        if self.rbtnG6.isChecked():
            selDevice = "G6"
        elif self.rbtnG7.isChecked():
            selDevice = "G7"
        elif self.rbtnG8.isChecked():
            selDevice = "G8"
        elif self.rbtnV30.isChecked():
            selDevice = "V30"
        elif self.rbtnV40.isChecked():
            selDevice = "V40"
        elif self.rbtnV50.isChecked():
            selDevice = "V50"

        if self.rbtnSKT.isChecked():
            selOperator = "SKT"
        elif self.rbtnKT.isChecked():
            selOperator = "KT"
        elif self.rbtnLGU.isChecked():
            selOperator = "LG U+"

        reply = QMessageBox.question(self, 'Selection', 'You selected %s device and %s operator. Click YES to continue removing apps.'%(selDevice, selOperator), QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            file = open(".\\bin\\system_app\\%s_%s.txt"%(selOperator, selDevice), "r")
            while True:
                line = file.readline()
                if not line: break
                os.system(".\\bin\\adb.exe shell pm uninstall --user 0 %s"%line)
            file.close()


class dialogSystemAppRestore(QWidget):
    selDevice = 'G6'
    selOperator = 'SKT'

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grpDevice = QGroupBox('Device')
        grpOperator = QGroupBox('Operator')

        btnRemoveStart = QPushButton('Start Restoring', self)
        btnRemoveStart.clicked.connect(self.startRemove)

        self.rbtnG6 = QRadioButton('G6', self)
        self.rbtnG7 = QRadioButton('G7 ThinQ', self)
        self.rbtnG8 = QRadioButton('G8 ThinQ', self)
        self.rbtnV30 = QRadioButton('V30 ThinQ', self)
        self.rbtnV40 = QRadioButton('V40 ThinQ', self)
        self.rbtnV50 = QRadioButton('V50 ThinQ', self)
        self.rbtnSKT = QRadioButton('SKT', self)
        self.rbtnKT = QRadioButton('KT', self)
        self.rbtnLGU = QRadioButton('LG U+', self)

        grpDeviceLayout = QVBoxLayout()
        grpOperatorLayout = QVBoxLayout()
        vbox = QVBoxLayout()

        grpDeviceLayout.addWidget(self.rbtnG6)
        grpDeviceLayout.addWidget(self.rbtnG7)
        grpDeviceLayout.addWidget(self.rbtnG8)
        grpDeviceLayout.addWidget(self.rbtnV30)
        grpDeviceLayout.addWidget(self.rbtnV40)
        grpDeviceLayout.addWidget(self.rbtnV50)

        grpOperatorLayout.addWidget(self.rbtnSKT)
        grpOperatorLayout.addWidget(self.rbtnKT)
        grpOperatorLayout.addWidget(self.rbtnLGU)

        grpDevice.setLayout(grpDeviceLayout)
        grpOperator.setLayout(grpOperatorLayout)

        vbox.addWidget(grpDevice)
        vbox.addWidget(grpOperator)
        vbox.addWidget(btnRemoveStart)

        self.setLayout(vbox)
        self.setWindowTitle('System Application Restore')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

    def startRemove(self):
        selDevice = ""
        selOperator = ""

        if self.rbtnG6.isChecked():
            selDevice = "G6"
        elif self.rbtnG7.isChecked():
            selDevice = "G7"
        elif self.rbtnG8.isChecked():
            selDevice = "G8"
        elif self.rbtnV30.isChecked():
            selDevice = "V30"
        elif self.rbtnV40.isChecked():
            selDevice = "V40"
        elif self.rbtnV50.isChecked():
            selDevice = "V50"

        if self.rbtnSKT.isChecked():
            selOperator = "SKT"
        elif self.rbtnKT.isChecked():
            selOperator = "KT"
        elif self.rbtnLGU.isChecked():
            selOperator = "LG U+"

        reply = QMessageBox.question(self, 'Selection',
                                     'You selected %s device and %s operator. Click YES to continue restoring apps.' % (
                                     selDevice, selOperator), QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            file = open(".\\bin\\system_app\\%s_%s.txt" % (selOperator, selDevice), "r")
            while True:
                line = file.readline()
                if not line: break
                os.system(".\\bin\\adb.exe shell cmd package install-existing %s" % line)
            file.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main()
    sys.exit(app.exec_())