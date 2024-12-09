from PyQt5.QtWidgets import QApplication
from gui import GUI

def main():
    app = QApplication([])
    window = GUI()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()





