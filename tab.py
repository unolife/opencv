from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

def main():

    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))

    mw = QtGui.QMainWindow()
    mw.setWindowTitle('Camera GUI')

    tabs = QtGui.QTabWidget()

    # Create tabs
    tab1 = QtGui.QWidget()

    ml = QtGui.QGridLayout()
    tab1.setLayout(ml)
    mw.setCentralWidget(tab1)
    mw.showMaximized()

    tab2 = QtGui.QWidget()

    # Resize width and height
    # tabs.resize(250, 150)
    screen_width = QtGui.QApplication.desktop().screenGeometry().width()
    screen_height = QtGui.QApplication.desktop().screenGeometry().height()
    tabs.resize(screen_width, screen_height)

    # Set layout of first tab
    # vBoxlayout1       = QtGui.QVBoxLayout()
    # pushButton1 = QtGui.QPushButton("Add camera code here")
    # vBoxlayout1.addWidget(pushButton1)
    # tab1.setLayout(vBoxlayout1)

    vBoxlayout2 = QtGui.QVBoxLayout()
    pushButton2 = QtGui.QPushButton("Add Load Cell code here")
    vBoxlayout2.addWidget(pushButton2)
    tab2.setLayout(vBoxlayout2)

    # Add tabs
    tabs.addTab(tab1,"Camera")
    tabs.addTab(tab2,"Load Cell")

    # Set title and show
    tabs.setWindowTitle('Prototype of SmartShelf')
    tabs.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
                                      