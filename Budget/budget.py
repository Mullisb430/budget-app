import sys, os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


budgetMain = resource_path("budgetMain.ui")


class Budget(QMainWindow):
    def __init__(self):
        super(Budget, self).__init__()
        uic.loadUi(budgetMain, self)
        self.itemValue1.textChanged.connect(self.onlyNums)
        self.itemValue2.textChanged.connect(self.onlyNums)
        self.itemValue3.textChanged.connect(self.onlyNums)
        self.itemValue4.textChanged.connect(self.onlyNums)
        self.itemValue5.textChanged.connect(self.onlyNums)
        self.itemValue6.textChanged.connect(self.onlyNums)
        self.itemValue7.textChanged.connect(self.onlyNums)
        self.itemValue8.textChanged.connect(self.onlyNums)
        self.itemValue9.textChanged.connect(self.onlyNums)
        self.itemValue10.textChanged.connect(self.onlyNums)
        self.itemValue11.textChanged.connect(self.onlyNums)
        self.itemValue12.textChanged.connect(self.onlyNums)
        self.itemValue13.textChanged.connect(self.onlyNums)
        self.itemValue14.textChanged.connect(self.onlyNums)
        self.itemValue15.textChanged.connect(self.onlyNums)
        self.itemValue16.textChanged.connect(self.onlyNums)
        self.itemValue17.textChanged.connect(self.onlyNums)
        self.itemValue18.textChanged.connect(self.onlyNums)
        self.itemValue19.textChanged.connect(self.onlyNums)
        self.itemValue20.textChanged.connect(self.onlyNums)
        self.itemValue21.textChanged.connect(self.onlyNums)
        self.itemValue22.textChanged.connect(self.onlyNums)
        self.itemValue23.textChanged.connect(self.onlyNums)
        self.itemValue24.textChanged.connect(self.onlyNums)
        self.salary.textChanged.connect(self.onlyNums)
        self.itemValue1.textChanged.connect(self.calculate)
        self.itemValue2.textChanged.connect(self.calculate)
        self.itemValue3.textChanged.connect(self.calculate)
        self.itemValue4.textChanged.connect(self.calculate)
        self.itemValue5.textChanged.connect(self.calculate)
        self.itemValue6.textChanged.connect(self.calculate)
        self.itemValue7.textChanged.connect(self.calculate)
        self.itemValue8.textChanged.connect(self.calculate)
        self.itemValue9.textChanged.connect(self.calculate)
        self.itemValue10.textChanged.connect(self.calculate)
        self.itemValue11.textChanged.connect(self.calculate)
        self.itemValue12.textChanged.connect(self.calculate)
        self.itemValue13.textChanged.connect(self.calculate)
        self.itemValue14.textChanged.connect(self.calculate)
        self.itemValue15.textChanged.connect(self.calculate)
        self.itemValue16.textChanged.connect(self.calculate)
        self.itemValue17.textChanged.connect(self.calculate)
        self.itemValue18.textChanged.connect(self.calculate)
        self.itemValue19.textChanged.connect(self.calculate)
        self.itemValue20.textChanged.connect(self.calculate)
        self.itemValue21.textChanged.connect(self.calculate)
        self.itemValue22.textChanged.connect(self.calculate)
        self.itemValue23.textChanged.connect(self.calculate)
        self.itemValue24.textChanged.connect(self.calculate)
        self.salary.textChanged.connect(self.calculate)
        self.calculate()
        self.itemValue1.textChanged.connect(self.color)
        self.itemValue2.textChanged.connect(self.color)
        self.itemValue3.textChanged.connect(self.color)
        self.itemValue4.textChanged.connect(self.color)
        self.itemValue5.textChanged.connect(self.color)
        self.itemValue6.textChanged.connect(self.color)
        self.itemValue7.textChanged.connect(self.color)
        self.itemValue8.textChanged.connect(self.color)
        self.itemValue9.textChanged.connect(self.color)
        self.itemValue10.textChanged.connect(self.color)
        self.itemValue11.textChanged.connect(self.color)
        self.itemValue12.textChanged.connect(self.color)
        self.itemValue13.textChanged.connect(self.color)
        self.itemValue14.textChanged.connect(self.color)
        self.itemValue15.textChanged.connect(self.color)
        self.itemValue16.textChanged.connect(self.color)
        self.itemValue17.textChanged.connect(self.color)
        self.itemValue18.textChanged.connect(self.color)
        self.itemValue19.textChanged.connect(self.color)
        self.itemValue20.textChanged.connect(self.color)
        self.itemValue21.textChanged.connect(self.color)
        self.itemValue22.textChanged.connect(self.color)
        self.itemValue23.textChanged.connect(self.color)
        self.itemValue24.textChanged.connect(self.color)
        self.salary.textChanged.connect(self.color)
        self.color()
        self.saveButton.clicked.connect(self.file_save)
        self.file_open()
        self.loadButton.clicked.connect(self.file_open)

    def file_open(self):
            with open('saveFile.txt', 'r') as file:
                file = file.readlines()    
                self.itemName1.setText(str(file[0][0:-1]))
                self.itemName2.setText(str(file[1][0:-1]))
                self.itemName3.setText(str(file[2][0:-1]))
                self.itemName4.setText(str(file[3][0:-1]))
                self.itemName5.setText(str(file[4][0:-1]))
                self.itemName6.setText(str(file[5][0:-1]))
                self.itemName7.setText(str(file[6][0:-1]))
                self.itemName8.setText(str(file[7][0:-1]))
                self.itemName9.setText(str(file[8][0:-1]))
                self.itemName10.setText(str(file[9][0:-1]))
                self.itemName11.setText(str(file[10][0:-1]))
                self.itemName12.setText(str(file[11][0:-1]))
                self.itemName13.setText(str(file[12][0:-1]))
                self.itemName14.setText(str(file[13][0:-1]))
                self.itemName15.setText(str(file[14][0:-1]))
                self.itemName16.setText(str(file[15][0:-1]))
                self.itemName17.setText(str(file[16][0:-1]))
                self.itemName18.setText(str(file[17][0:-1]))
                self.itemName19.setText(str(file[18][0:-1]))
                self.itemName20.setText(str(file[19][0:-1]))
                self.itemName21.setText(str(file[20][0:-1]))
                self.itemName22.setText(str(file[21][0:-1]))
                self.itemName23.setText(str(file[22][0:-1]))
                self.itemName24.setText(str(file[23][0:-1]))
                self.salary.setText(str(file[24][0:-1]))
                self.itemValue1.setText(str(file[25][0:-1]))
                self.itemValue2.setText(str(file[26][0:-1]))
                self.itemValue3.setText(str(file[27][0:-1]))
                self.itemValue4.setText(str(file[28][0:-1]))
                self.itemValue5.setText(str(file[29][0:-1]))
                self.itemValue6.setText(str(file[30][0:-1]))
                self.itemValue7.setText(str(file[31][0:-1]))
                self.itemValue8.setText(str(file[32][0:-1]))
                self.itemValue9.setText(str(file[33][0:-1]))
                self.itemValue10.setText(str(file[34][0:-1]))
                self.itemValue11.setText(str(file[35][0:-1]))
                self.itemValue12.setText(str(file[36][0:-1]))
                self.itemValue13.setText(str(file[37][0:-1]))
                self.itemValue14.setText(str(file[38][0:-1]))
                self.itemValue15.setText(str(file[39][0:-1]))
                self.itemValue16.setText(str(file[40][0:-1]))
                self.itemValue17.setText(str(file[41][0:-1]))
                self.itemValue18.setText(str(file[42][0:-1]))
                self.itemValue19.setText(str(file[43][0:-1]))
                self.itemValue20.setText(str(file[44][0:-1]))
                self.itemValue21.setText(str(file[45][0:-1]))
                self.itemValue22.setText(str(file[46][0:-1]))
                self.itemValue23.setText(str(file[47][0:-1]))
                self.itemValue24.setText(str(file[48][0:-1]))
            

    def file_save(self):
                file = open('saveFile.txt', 'w')
                with file:
                    file.write(f'{self.itemName1.text()}\n')
                    file.write(f'{self.itemName2.text()}\n')
                    file.write(f'{self.itemName3.text()}\n')
                    file.write(f'{self.itemName4.text()}\n')
                    file.write(f'{self.itemName5.text()}\n')
                    file.write(f'{self.itemName6.text()}\n')
                    file.write(f'{self.itemName7.text()}\n')
                    file.write(f'{self.itemName8.text()}\n')
                    file.write(f'{self.itemName9.text()}\n')
                    file.write(f'{self.itemName10.text()}\n')
                    file.write(f'{self.itemName11.text()}\n')
                    file.write(f'{self.itemName12.text()}\n')
                    file.write(f'{self.itemName13.text()}\n')
                    file.write(f'{self.itemName14.text()}\n')
                    file.write(f'{self.itemName15.text()}\n')
                    file.write(f'{self.itemName16.text()}\n')
                    file.write(f'{self.itemName17.text()}\n')
                    file.write(f'{self.itemName18.text()}\n')
                    file.write(f'{self.itemName19.text()}\n')
                    file.write(f'{self.itemName20.text()}\n')
                    file.write(f'{self.itemName21.text()}\n')
                    file.write(f'{self.itemName22.text()}\n')
                    file.write(f'{self.itemName23.text()}\n')
                    file.write(f'{self.itemName24.text()}\n')
                    file.write(f'{self.salary.text()}\n')
                    file.write(f'{self.itemValue1.text()}\n')
                    file.write(f'{self.itemValue2.text()}\n')
                    file.write(f'{self.itemValue3.text()}\n')
                    file.write(f'{self.itemValue4.text()}\n')
                    file.write(f'{self.itemValue5.text()}\n')
                    file.write(f'{self.itemValue6.text()}\n')
                    file.write(f'{self.itemValue7.text()}\n')
                    file.write(f'{self.itemValue8.text()}\n')
                    file.write(f'{self.itemValue9.text()}\n')
                    file.write(f'{self.itemValue10.text()}\n')
                    file.write(f'{self.itemValue11.text()}\n')
                    file.write(f'{self.itemValue12.text()}\n')
                    file.write(f'{self.itemValue13.text()}\n')
                    file.write(f'{self.itemValue14.text()}\n')
                    file.write(f'{self.itemValue15.text()}\n')
                    file.write(f'{self.itemValue16.text()}\n')
                    file.write(f'{self.itemValue17.text()}\n')
                    file.write(f'{self.itemValue18.text()}\n')
                    file.write(f'{self.itemValue19.text()}\n')
                    file.write(f'{self.itemValue20.text()}\n')
                    file.write(f'{self.itemValue21.text()}\n')
                    file.write(f'{self.itemValue22.text()}\n')
                    file.write(f'{self.itemValue23.text()}\n')
                    file.write(f'{self.itemValue24.text()}\n')

    def color(self):
        if float(self.netTotal.text()) < 0:
            self.netTotal.setStyleSheet("background-color: #444;" + "color: #FF0000;")
            self.netBackground.setStyleSheet("background-color: #CC0000;")
            self.label_4.setStyleSheet("background-color: #330000;" + "color: #fff")
        elif float(self.netTotal.text()) > 0:
            self.netTotal.setStyleSheet("background-color: #444;" + "color: #00FF00;")
            self.netBackground.setStyleSheet("background-color: #00CC00;")
            self.label_4.setStyleSheet("background-color: #003300;" + "color: #fff")

    def calculate(self):
        try:
            lst = [float(self.itemValue1.text()), float(self.itemValue2.text()), float(self.itemValue3.text()), float(self.itemValue4.text()), float(self.itemValue5.text()), float(self.itemValue6.text()), float(self.itemValue7.text()), float(self.itemValue8.text()), float(self.itemValue9.text()), float(self.itemValue10.text()), float(self.itemValue11.text()), float(self.itemValue12.text()), float(self.itemValue13.text()), float(self.itemValue14.text()), float(self.itemValue15.text()), float(self.itemValue16.text()), float(self.itemValue17.text()), float(self.itemValue18.text()), float(self.itemValue19.text()), float(self.itemValue20.text()), float(self.itemValue21.text()), float(self.itemValue22.text()), float(self.itemValue23.text()), float(self.itemValue24.text())]
        except Exception:
            lst = ['0']

        try:
            self.budgetTotal.setText(str(sum(lst)))
        except Exception:
            self.budgetTotal.setText('0')

        try:
            number = float(self.salary.text()) - sum(lst)
            self.netTotal.setText(str(round(number, 2)))
        except Exception:
            self.netTotal.setText('0')

    def onlyNums(self):
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ' ']
        for letter in self.itemValue1.text():
            if letter not in numbers:
                self.itemValue1.setText(self.itemValue1.text().replace(letter, ''))

        for letter in self.itemValue2.text():
            if letter not in numbers:
                self.itemValue2.setText(self.itemValue2.text().replace(letter, ''))
        
        for letter in self.itemValue3.text():
            if letter not in numbers:
                self.itemValue3.setText(self.itemValue3.text().replace(letter, ''))
        
        for letter in self.itemValue4.text():
            if letter not in numbers:
                self.itemValue4.setText(self.itemValue4.text().replace(letter, ''))
        
        for letter in self.itemValue5.text():
            if letter not in numbers:
                self.itemValue5.setText(self.itemValue5.text().replace(letter, ''))
        
        for letter in self.itemValue6.text():
            if letter not in numbers:
                self.itemValue6.setText(self.itemValue6.text().replace(letter, ''))
        
        for letter in self.itemValue7.text():
            if letter not in numbers:
                self.itemValue7.setText(self.itemValue7.text().replace(letter, ''))
        
        for letter in self.itemValue8.text():
            if letter not in numbers:
                self.itemValue8.setText(self.itemValue8.text().replace(letter, ''))
        
        for letter in self.itemValue9.text():
            if letter not in numbers:
                self.itemValue9.setText(self.itemValue9.text().replace(letter, ''))
        
        for letter in self.itemValue10.text():
            if letter not in numbers:
                self.itemValue10.setText(self.itemValue10.text().replace(letter, ''))
        
        for letter in self.itemValue11.text():
            if letter not in numbers:
                self.itemValue11.setText(self.itemValue11.text().replace(letter, ''))
        
        for letter in self.itemValue12.text():
            if letter not in numbers:
                self.itemValue12.setText(self.itemValue12.text().replace(letter, ''))
        
        for letter in self.itemValue13.text():
            if letter not in numbers:
                self.itemValue13.setText(self.itemValue13.text().replace(letter, ''))
        
        for letter in self.itemValue14.text():
            if letter not in numbers:
                self.itemValue14.setText(self.itemValue14.text().replace(letter, ''))
        
        for letter in self.itemValue15.text():
            if letter not in numbers:
                self.itemValue15.setText(self.itemValue15.text().replace(letter, ''))
        
        for letter in self.itemValue16.text():
            if letter not in numbers:
                self.itemValue16.setText(self.itemValue16.text().replace(letter, ''))
        
        for letter in self.itemValue17.text():
            if letter not in numbers:
                self.itemValue17.setText(self.itemValue17.text().replace(letter, ''))
        
        for letter in self.itemValue18.text():
            if letter not in numbers:
                self.itemValue18.setText(self.itemValue18.text().replace(letter, ''))
        
        for letter in self.itemValue19.text():
            if letter not in numbers:
                self.itemValue19.setText(self.itemValue19.text().replace(letter, ''))
        
        for letter in self.itemValue20.text():
            if letter not in numbers:
                self.itemValue20.setText(self.itemValue20.text().replace(letter, ''))
        
        for letter in self.itemValue21.text():
            if letter not in numbers:
                self.itemValue21.setText(self.itemValue21.text().replace(letter, ''))
        
        for letter in self.itemValue22.text():
            if letter not in numbers:
                self.itemValue22.setText(self.itemValue22.text().replace(letter, ''))
        
        for letter in self.itemValue23.text():
            if letter not in numbers:
                self.itemValue23.setText(self.itemValue23.text().replace(letter, ''))
        
        for letter in self.itemValue24.text():
            if letter not in numbers:
                self.itemValue24.setText(self.itemValue24.text().replace(letter, ''))
            

app = QApplication(sys.argv)
budget = Budget()
budget.setFixedSize(771, 706)
budget.show()
app.exec_()