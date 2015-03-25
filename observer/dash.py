import sys
from PyQt4 import QtCore, QtGui, uic
import bicycle
import caloriemeter
import speedometer

qtCreatorFile = 'dashui.ui'

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.bttn_update.clicked.connect(self.update)
        self.bicycle = bicycle.Bicycle()
        self.caloriemeter = caloriemeter.CalorieMeter(self.bicycle)
        self.speedometer = speedometer.Speedometer(self.bicycle)

    def update(self):
        rpms = self.txtedit_rpm.toPlainText()
        self.bicycle.rpms = int(rpms)
        self.txtedit_calories.setText(str(self.caloriemeter.calories))
        self.txtedit_speed.setText(str(self.speedometer.speed))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

