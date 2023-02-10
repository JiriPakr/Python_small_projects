from PyQt6.QtWidgets import *
import source as nn
import pathlib


def train():
    global classifier
    cur_path = path.toPlainText()
    bin_acur.setText("Working...")
    bin_acur.repaint()
    classifier, acurracy = nn.train(cur_path.__str__() + "\\train.csv")
    bin_acur.setText("Binary accuracy: " + acurracy.__str__())
def test():
    global classifier
    cur_path = path.toPlainText()
    bin_acur.setText("Working...")
    bin_acur.repaint()
    acurracy = nn.test(classifier, cur_path.__str__() + "\\valid.csv")
    bin_acur.setText("Test binary accuracy: " + acurracy.__str__())

#GUI init
cur_path = pathlib.Path().resolve()
app = QApplication([])
window = QWidget()
window.resize(500, 300)
window.setWindowTitle('KNN classifier')
layout = QVBoxLayout()

trainbtn = QPushButton('Train')
trainbtn.clicked.connect(train)
layout.addWidget(trainbtn)

testbtn = QPushButton('Test')
testbtn.clicked.connect(test)
layout.addWidget(testbtn)

bin_acur = QTextBrowser(window)
bin_acur.setText("Binary accuracy")
layout.addWidget(bin_acur)

path = QTextEdit(window)
path.setText(cur_path.__str__())
layout.addWidget(path)

window.setLayout(layout)
window.show()
app.exec()