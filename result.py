# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import q


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # self.again = QtWidgets.QPushButton(self.centralwidget)
        # self.again.setGeometry(QtCore.QRect(490, 400, 255, 51))
        # self.again.setObjectName("again")
        # self.again.clicked.connect(self.again_f)

        self.show = QtWidgets.QPushButton(self.centralwidget)
        self.show.setGeometry(QtCore.QRect(490, 400, 500, 100))
        self.show.setObjectName("show")
        self.show.clicked.connect(self.res)

        self.result = QtWidgets.QLabel(MainWindow)
        self.result.setGeometry(QtCore.QRect(10, 0, 255, 51))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(24)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.result.setWordWrap(True)

        self.result_desc = QtWidgets.QLabel(MainWindow)
        self.result_desc.setGeometry(QtCore.QRect(100, 60, 800, 400))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(16)
        self.result_desc.setFont(font)
        self.result_desc.setObjectName("result_desc")
        self.result.setWordWrap(True)

        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_E():
        return q.E
    E = get_E()

    def get_E():
        return q.E
    E = get_E()

    def res(MainWindow):
        if E > 12 and q.N > 14:
            self.result.setText(_translate("MainWindow", "Ви - холерик"))
            self.result_desc.setText(_translate("MainWindow", "Дії холерика поривчасті. Він відрізняється підвищеною збудженістю та великою емоційністю. Прояв цього типу темпераменту в значній мірі залежить від спрямованості особистості. У людей із громадськими інтересами він фокусується в ініціативності, енергійності, принциповості. Там, де немає багатства духовного життя, холеричний темперамент проявляється негативно (роздратованість, афективність)."))


        if E > 12 and N < 14:
            self.result.setText(_translate("MainWindow", "Ви - сангвінік"))
            self.result_desc.setText(_translate("MainWindow", "Сангвінік швидко пристосовується до нових умов, швидко знаходить спільну розмову з людьми, комунікативний. Почуття швидко виникають і зникають. У людини цього типу яскрава міміка. Відсутність чіткої мети, не включеність сангвініка у творчу діяльність поступово формується в поверховість і нестабільність."))

        if E < 12 and N > 14:
            self.result.setText(_translate("MainWindow", "Ви - меланхолік"))
            self.result_desc.setText(_translate("MainWindow", "Реакція меланхоліка здебільшого відповідає силі подразника. Особливо потужне в людини цього типу темпераменту зовнішнє гальмування. Йому тяжко на чомусь зосередитись. Сильні подразники здебільшого викликають довготривалу реакцію гальмування. У стійких та стабільних умовах життя меланхолік характеризується змістовністю й глибиною думок. У негативних зовнішніх умовах меланхолік може стати замкнутим, боягузливим, неспокійним."))


        if E < 12 and N <14:
            self.result.setText(_translate("MainWindow", "Ви - флегматик"))
            self.result_desc.setText(_translate("MainWindow", "У флегматика нові форми поведінки виробляються повільно, але вони стійкі. Здебільшого флегматик спокійний, рівномірний, рідко виходить із себе, не схильних до афектів. Залежно від умов середовища життєдіяльності в нього можуть сформуватися позитивні риси (витримка, глибина думки і т. ін.) або ж яскраві негативні риси характеру (в’ялість, лінь, нестійкість, низькі вольові якості)."))

    # def again_f():
    #     subprocess.run(["python", "a.py"])
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.again.setText(_translate("MainWindow", "пройти знову"))
        self.show.setText(_translate("MainWindow", "показати результати"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
