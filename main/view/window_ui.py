
from PyQt5 import QtCore, QtGui, QtWidgets

class IForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(500, 300))

        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(560, 160, 91, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        font = QtGui.QFont()
        font.setPointSize(12)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonSelect = QtWidgets.QPushButton(Form)
        self.buttonSelect.setGeometry(QtCore.QRect(200, 260, 89, 23))
        self.buttonSelect.setObjectName("buttonSelect")
    
    
        self.textK = QtWidgets.QLineEdit(Form)#K
        self.textK.setObjectName("textK")
        self.textK.setGeometry(QtCore.QRect(100, 40, 50, 20))


        self.textNMax = QtWidgets.QLineEdit(Form)#NMAX
        self.textNMax.setObjectName("textNMax")
        self.textNMax.setGeometry(QtCore.QRect(100, 80, 50, 20))

        self.textM = QtWidgets.QLineEdit(Form)
        self.textM.setObjectName("textM")
        self.textM.setGeometry(QtCore.QRect(100, 120, 50, 20))

        self.textTMax = QtWidgets.QLineEdit(Form)
        self.textTMax.setObjectName("textTMax")
        self.textTMax.setGeometry(QtCore.QRect(100, 160, 50, 20))

        self.text0 = QtWidgets.QLineEdit(Form)
        self.text0.setObjectName("text0")
        self.text0.setGeometry(QtCore.QRect(100, 200, 50, 20))

        self.textcodP = QtWidgets.QLineEdit(Form)
        self.textcodP.setObjectName("textcodP")
        self.textcodP.setGeometry(QtCore.QRect(100, 240, 50, 20))


        self.k = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.k.setFont(font)
        self.k.setObjectName("k")
        self.k.setGeometry(QtCore.QRect(80, 0, 10, 95))

        self.nMax = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nMax.setFont(font)
        self.nMax.setObjectName("nMax")
        self.nMax.setGeometry(QtCore.QRect(55, 0, 38, 180))

        self.m = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.m.setFont(font)
        self.m.setObjectName("m")
        self.m.setGeometry(QtCore.QRect(75, 0, 38, 265))

        self.tMax = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tMax.setFont(font)
        self.tMax.setObjectName("tMax")
        self.tMax.setGeometry(QtCore.QRect(55, 0, 38, 338))

        self.t0 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.t0.setFont(font)
        self.t0.setObjectName("t0")
        self.t0.setGeometry(QtCore.QRect(75, 0, 38, 423))

        self.codP = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.codP.setFont(font)
        self.codP.setObjectName("codP")
        self.codP.setGeometry(QtCore.QRect(53, 0, 43, 500))
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Geneticos"))
        self.buttonSelect.setText(_translate("Form", "Ejecutar"))
        self.nMax.setText(_translate("Form", "NMAX: "))
        self.k.setText(_translate("Form", "K: "))
        self.m.setText(_translate("Form", "M: "))
        self.tMax.setText(_translate("Form", "TMAX: "))
        self.t0.setText(_translate("Form", "T0: "))
        self.codP.setText(_translate("Form", "CONDP: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QFormDialog()
    ui = IForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

