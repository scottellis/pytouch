#!/usr/bin/env python

from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel,
        QPushButton, QVBoxLayout, QWidget)

from PyQt5.QtCore import QSignalMapper

class TouchWin(QWidget):

    def __init__(self):
        super(TouchWin, self).__init__()

        mainLayout = QVBoxLayout()
        
        self.label = QLabel('#')
        self.label.setStyleSheet('color: red;')
        self.btns = []
        self.signalMapper = QSignalMapper(self)
        self.signalMapper.mapped.connect(self.btnClicked)

        for i in range(0, 8):
            self.btns.append(QPushButton('{:d}'.format(i+1)))
            self.btns[i].setFixedSize(60, 40)
            self.signalMapper.setMapping(self.btns[i], i+1)
            self.btns[i].clicked.connect(self.signalMapper.map) 

        self.exitBtn = QPushButton('Exit')
        self.exitBtn.setFixedSize(72, 40)
        self.exitBtn.clicked.connect(self.close)

        btnLayout = QHBoxLayout()
        btnLayout.addWidget(self.btns[0])
        btnLayout.addStretch()
        btnLayout.addWidget(self.btns[1])
        btnLayout.addStretch()
        btnLayout.addWidget(self.btns[2])
        mainLayout.addLayout(btnLayout)
        mainLayout.addStretch()

        btnLayout = QHBoxLayout()
        btnLayout.addWidget(self.btns[3])
        btnLayout.addStretch()
        btnLayout.addWidget(self.exitBtn)
        btnLayout.addStretch()
        btnLayout.addWidget(self.btns[4])
        mainLayout.addLayout(btnLayout)

        lblLayout = QHBoxLayout()
        lblLayout.addStretch()
        lblLayout.addWidget(self.label)
        lblLayout.addStretch()
        mainLayout.addSpacing(10)
        mainLayout.addLayout(lblLayout)
        mainLayout.addStretch()

        btnLayout = QHBoxLayout()
        btnLayout.addWidget(self.btns[5])
        btnLayout.addStretch()
        btnLayout.addWidget(self.btns[6])
        btnLayout.addStretch()
        btnLayout.addWidget(self.btns[7])
        mainLayout.addLayout(btnLayout)

        self.setLayout(mainLayout)

    def btnClicked(self, button):
        self.label.setText('{:d}'.format(button))


if __name__ == '__main__':
    
    import sys
    
    app = QApplication(sys.argv)

    btnStyle = """
        QPushButton { 
            background-color: rgb(86, 104, 118);
            color: white;
            border-width: 2px;
            border-radius: 10px;
        }
        QPushButton:pressed {
            background-color: rgb(136, 154, 168);
            color: red;
            border-width: 2px;
            border-radius: 10px;
        }
        """        

    app.setStyleSheet(btnStyle)

    win = TouchWin()
    win.show()

    sys.exit(app.exec_())
