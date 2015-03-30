import sys
import messagesuser 
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "ui.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.input_user =  messagesuser.User()
        self.user1 = messagesuser.User()
        self.user2 = messagesuser.User()

        self.input_user.add_observer(self.user1)
        self.input_user.add_observer(self.user2)

        self.pushButton.clicked.connect(self.update)

    def update(self):
        msg = self.txtedit_input.toPlainText()
        self.txtedit_input.clear()
        self.input_user.post_message(msg)

        # Should be listeners attached to Qt text browsers.
        self.txtbrowser_one.append(self.user1.observed_messages[-1])
        self.txtbrowser_two.append(self.user1.observed_messages[-1])

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

