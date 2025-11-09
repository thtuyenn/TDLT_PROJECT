from SimpleMath.MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.sutupSignalsAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def sutupSignalsAndSlot(self):
        self.pushButtonadd.clicked.connect(self.process_sum)
        self.pushButtonmulti.clicked.connect(self.process_X)
        self.pushButtonminus.clicked.connect(self.process_minus)
        self.pushButtondivide.clicked.connect(self.process_divide)

    def process_sum(self):
        a = float(self.lineEditA.text())
        b = float(self.lineEditB.text())
        result = "{0}+{1}={2}".format(a, b, a + b)
        self.lineEditResult.setText(result)

    def process_X(self):
        a = float(self.lineEditA.text())
        b = float(self.lineEditB.text())
        result = "{0}*{1}={2}".format(a, b, a * b)
        self.lineEditResult.setText(result)