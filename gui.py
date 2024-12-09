import sys
import re

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QFileDialog, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from ai_model import AIModel


class GUI(QWidget):
    __ai_model = AIModel()
    __img_label = None
    __name_label = None
    __select_button = None

    def __init__(self):
        super().__init__()
        self.__img_label = QLabel()
        self.__name_label = QLabel('Select image file: jpg, jpeg, png, gif, bmp, tiff, tif')
        self.__select_button = QPushButton('Select Image')
        self.init_gui()

    def init_gui(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Simple Ai App')

        layout = QVBoxLayout()

        self.__img_label.setAlignment(Qt.AlignCenter)

        self.__name_label.setFixedHeight(15)
        self.__name_label.setAlignment(Qt.AlignCenter)
        self.__name_label.setFont(QFont('Arial', 15))

        self.__select_button.clicked.connect(self.select_image)

        layout.addWidget(self.__img_label)
        layout.addWidget(self.__name_label)
        layout.addWidget(self.__select_button)
        self.setLayout(layout)

    def load_image(self, file_path):
        pixmap = QPixmap(file_path)
        if pixmap.width() > 600 or pixmap.height() > 800:
            self.__img_label.setPixmap(pixmap.scaled(QSize(int(pixmap.width()*0.25), int(pixmap.height()*0.25))))
        else:
            self.__img_label.setPixmap(pixmap)
        self.__name_label.setText(self.__ai_model.recognize_image(file_path))

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select image file: jpg, jpeg, png, gif, bmp, tiff, tif')
        if file_path:
            img_extensions = re.compile(r'.(jpg|jpeg|png|gif|bmp|tiff|tif)$', re.IGNORECASE)
            if img_extensions.search(file_path):
                self.load_image(file_path)
