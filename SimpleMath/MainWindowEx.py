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