import nonogram
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *

if not os.path.isdir('./output'):
    os.mkdir('./output')


class NonogramGUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        groupbox = QGroupBox('Menu')
        RunBtn = QPushButton('Run')
        vbox = QGridLayout()
        vbox.addWidget(RunBtn, 0, 0)
        groupbox.setLayout(vbox)

        RunBtn.clicked.connect(lambda: nonogram.run(int(xLine.text()), int(yLine.text()), nameLine.text()))

        xygroupbox = QGroupBox('Properties')
        xLabel = QLabel('X:')
        yLabel = QLabel('Y:')
        nameLabel = QLabel('filename:')
        xLine = QLineEdit()
        yLine = QLineEdit()
        nameLine = QLineEdit()
        auhbox1 = QHBoxLayout()
        auhbox1.addWidget(xLabel)
        auhbox1.addWidget(xLine)

        auhbox2 = QHBoxLayout()
        auhbox2.addWidget(yLabel)
        auhbox2.addWidget(yLine)

        auhbox3 = QHBoxLayout()
        auhbox3.addWidget(nameLabel)
        auhbox3.addWidget(nameLine)

        auvbox = QVBoxLayout()
        auvbox.addLayout(auhbox1)
        auvbox.addLayout(auhbox2)
        auvbox.addLayout(auhbox3)
        xygroupbox.setLayout(auvbox)

        grid = QGridLayout()
        grid.addWidget(xygroupbox, 0, 0)
        grid.addWidget(groupbox, 1, 0)
        self.setLayout(grid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = QStackedWidget()
    main = NonogramGUI()
    gui.addWidget(main)
    gui.setWindowTitle('nonogram-generator')
    gui.resize(600, 400)
    gui.setWindowIcon(QIcon('./src/nonogram_generator-logo.png'))
    gui.show()
    app.exec_()
