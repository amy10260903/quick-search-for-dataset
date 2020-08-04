# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'audio_ui_v3.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QWidget, QListWidget, QLabel, QPushButton, QLineEdit, QTreeView, QFileSystemModel, QComboBox
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from .style import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        ### Main window ###
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 490)
        MainWindow.setStyleSheet(style_background)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ### List widget ###
        '''
        # List for audio files
        self.list_audio = QListWidget(self.centralwidget)
        self.list_audio.setGeometry(QRect(30, 60, 300, 351))
        self.list_audio.setFont(font_content)
        self.list_audio.setStyleSheet(style_list)
        self.list_audio.setObjectName("list_audio")
        self.list_audio.verticalScrollBar().setStyleSheet(style_slidebar)
        '''

        # List for locations
        self.list_location = QListWidget(self.centralwidget)
        self.list_location.setGeometry(QRect(370, 60, 300, 120))
        self.list_location.setStyleSheet(style_list)
        self.list_location.setObjectName("list_location")
        self.list_location.verticalScrollBar().setStyleSheet(style_slidebar)

        # List for sound source
        self.list_soundsource = QListWidget(self.centralwidget)
        self.list_soundsource.setGeometry(QRect(370, 215, 300, 130))
        self.list_soundsource.setStyleSheet(style_list)
        self.list_soundsource.setObjectName("list_soundsource")
        self.list_soundsource.verticalScrollBar().setStyleSheet(style_slidebar)
        

        ### Label ###
        # Title for audio list
        self.label_audio = QLabel(self.centralwidget)
        self.label_audio.setGeometry(QRect(30, 20, 300, 40))
        self.label_audio.setFont(font_title)
        self.label_audio.setObjectName("label_audio")

        # Title for location list
        self.label_location = QLabel(self.centralwidget)
        self.label_location.setGeometry(QRect(370, 20, 300, 40))
        self.label_location.setFont(font_title)
        self.label_location.setObjectName("label_location")

        # Title for sound source list
        self.label_soundsource = QLabel(self.centralwidget)
        self.label_soundsource.setGeometry(QRect(370, 190, 300, 30))
        self.label_soundsource.setFont(font_title)
        self.label_soundsource.setObjectName("label_soundsource")

        # Title for root path
        self.label_root = QLabel(self.centralwidget)
        self.label_root.setGeometry(QRect(30, 428, 80, 40))
        self.label_root.setFont(font_title)
        self.label_root.setObjectName("label_root")

        # Title for description
        self.label_description = QLabel(self.centralwidget)
        self.label_description.setGeometry(QRect(370, 350, 300, 40))
        self.label_description.setFont(font_title)
        self.label_description.setObjectName("label_description")

        # Title for timestamp
        self.label_timestamp = QLabel(self.centralwidget)
        self.label_timestamp.setGeometry(QRect(370, 380, 300, 40))
        self.label_timestamp.setFont(font_title)
        self.label_timestamp.setObjectName("label_timestamp")


        ### Button ###
        # Button for saving labels
        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QRect(600, 430, 70, 34))
        self.btn_save.setStyleSheet(style_btn_pressed)
        self.btn_save.setFont(font_content)
        self.btn_save.setObjectName("btn_save")
        
        # Button for loading files
        self.btn_load = QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QRect(520, 430, 70, 34))
        self.btn_load.setStyleSheet(style_btn_pressed)
        self.btn_load.setFont(font_content)
        self.btn_load.setObjectName("btn_load")


        ### ComboBox ###
        self.combo_location = QComboBox(self.centralwidget)
        self.combo_location.setGeometry(QRect(450, 29, 220, 24))
        self.combo_location.setStyleSheet(style_combobox)


        ### TextBox ###
        self.textbox_root = QLineEdit(self.centralwidget)
        self.textbox_root.setGeometry(QRect(110, 432, 360, 30))
        self.textbox_root.setStyleSheet(style_blank+style_round_box)

        self.textbox_description = QLineEdit(self.centralwidget)
        self.textbox_description.setGeometry(QRect(460, 358, 210, 24))
        self.textbox_description.setStyleSheet(style_blank+style_round_box)

        self.textbox_timestamp = QLineEdit(self.centralwidget)
        self.textbox_timestamp.setGeometry(QRect(460, 388, 210, 24))
        self.textbox_timestamp.setStyleSheet(style_blank+style_round_box)

        ### SpinBox ###
        '''
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QRect(470, 40, 43, 26))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QRect(530, 40, 43, 26))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(QRect(518, 30, 30, 40))
        self.label_4.setFont(font_title)
        self.label_4.setObjectName("label_4")
        self.spinBox_2.raise_()
        self.spinBox.raise_()
        '''

        ### List Dir/file with TreeView ###
        self.model_dataset = QFileSystemModel()
        #self.model.setRootPath(dir_path)
        self.tree_dataset =  QTreeView(self.centralwidget)
        self.tree_dataset.setModel(self.model_dataset)
        #self.tree.setRootIndex(self.model.index(dir_path))
        self.tree_dataset.hideColumn(1)
        self.tree_dataset.hideColumn(2)
        self.tree_dataset.hideColumn(3)
        self.tree_dataset.setGeometry(QRect(30, 60, 300, 351))
        self.tree_dataset.setStyleSheet(style_list)
        self.tree_dataset.verticalScrollBar().setStyleSheet(style_slidebar)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Labeling Tool"))

        #__sortingEnabled = self.list_audio.isSortingEnabled()
        #self.list_audio.setSortingEnabled(False)
        #self.list_audio.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.list_location.isSortingEnabled()
        self.list_location.setSortingEnabled(False)
        self.list_location.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.list_soundsource.isSortingEnabled()
        self.list_soundsource.setSortingEnabled(False)
        self.list_soundsource.setSortingEnabled(__sortingEnabled)

        self.label_audio.setText(_translate("MainWindow", "Audio Files"))
        self.label_location.setText(_translate("MainWindow", "Location"))
        self.label_soundsource.setText(_translate("MainWindow", "Sound Source"))
        self.label_root.setText(_translate("MainWindow", "Root Path"))
        self.label_description.setText(_translate("MainWindow", "Description"))
        self.label_timestamp.setText(_translate("MainWindow", "Timestamp"))
        #self.label_4.setText(_translate("MainWindow", ":"))
        
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.btn_load.setText(_translate("MainWindow", "Load"))
        

