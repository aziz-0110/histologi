# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(959, 700)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_3.setContentsMargins(0, 2, -1, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_9 = QtWidgets.QFrame(self.frame_12)
        self.frame_9.setMinimumSize(QtCore.QSize(600, 0))
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_load = QtWidgets.QPushButton(self.frame_9)
        self.btn_load.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_load.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_load.setFont(font)
        self.btn_load.setObjectName("btn_load")
        self.horizontalLayout_4.addWidget(self.btn_load)
        self.btn_crop = QtWidgets.QPushButton(self.frame_9)
        self.btn_crop.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_crop.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_crop.setFont(font)
        self.btn_crop.setObjectName("btn_crop")
        self.horizontalLayout_4.addWidget(self.btn_crop)
        self.btn_save = QtWidgets.QPushButton(self.frame_9)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_save.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_4.addWidget(self.btn_save)
        self.btn_clear = QtWidgets.QPushButton(self.frame_9)
        self.btn_clear.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_clear.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("")
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_4.addWidget(self.btn_clear)
        self.horizontalLayout_3.addWidget(self.frame_9)
        self.frame_19 = QtWidgets.QFrame(self.frame_12)
        self.frame_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.frame_19)
        self.comboBox.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 80))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.totalCell = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.totalCell.setFont(font)
        self.totalCell.setObjectName("totalCell")
        self.horizontalLayout.addWidget(self.totalCell)
        self.horizontalLayout_3.addWidget(self.frame_19)
        spacerItem = QtWidgets.QSpacerItem(469, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.frame_12)
        self.verticalLayout_7.addWidget(self.frame_11)
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        self.label_9.setMinimumSize(QtCore.QSize(0, 25))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"")
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtWidgets.QFrame(self.frame_8)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_7.setSpacing(8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.img_ori = QtWidgets.QLabel(self.frame_6)
        self.img_ori.setText("")
        self.img_ori.setObjectName("img_ori")
        self.verticalLayout_3.addWidget(self.img_ori)
        self.horizontalLayout_7.addWidget(self.frame_6)
        self.frame_14 = QtWidgets.QFrame(self.frame)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.frame_14)
        self.label_4.setMinimumSize(QtCore.QSize(0, 25))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_10.addWidget(self.label_4)
        self.img_dist = QtWidgets.QLabel(self.frame_14)
        self.img_dist.setText("")
        self.img_dist.setObjectName("img_dist")
        self.verticalLayout_10.addWidget(self.img_dist)
        self.horizontalLayout_7.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(self.frame)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.frame_13)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.img_canny = QtWidgets.QLabel(self.frame_13)
        self.img_canny.setText("")
        self.img_canny.setObjectName("img_canny")
        self.verticalLayout_9.addWidget(self.img_canny)
        self.horizontalLayout_7.addWidget(self.frame_13)
        self.horizontalLayout_5.addWidget(self.frame)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.frame_18 = QtWidgets.QFrame(self.frame_3)
        self.frame_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_18)
        self.label_3.setMinimumSize(QtCore.QSize(0, 25))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.frame_5 = QtWidgets.QFrame(self.frame_18)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_8.setSpacing(8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_17 = QtWidgets.QFrame(self.frame_5)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.frame_17)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_13.addWidget(self.label_6)
        self.img_count = QtWidgets.QLabel(self.frame_17)
        self.img_count.setText("")
        self.img_count.setObjectName("img_count")
        self.verticalLayout_13.addWidget(self.img_count)
        self.horizontalLayout_8.addWidget(self.frame_17)
        self.frame_16 = QtWidgets.QFrame(self.frame_5)
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_10 = QtWidgets.QFrame(self.frame_16)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.frame_10)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.img_label = QtWidgets.QLabel(self.frame_10)
        self.img_label.setText("")
        self.img_label.setObjectName("img_label")
        self.verticalLayout_8.addWidget(self.img_label)
        self.verticalLayout_12.addWidget(self.frame_10)
        self.horizontalLayout_8.addWidget(self.frame_16)
        self.frame_15 = QtWidgets.QFrame(self.frame_5)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.frame_15)
        self.label_7.setMinimumSize(QtCore.QSize(0, 25))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_11.addWidget(self.label_7)
        self.img_grafik = QtWidgets.QLabel(self.frame_15)
        self.img_grafik.setText("")
        self.img_grafik.setObjectName("img_grafik")
        self.verticalLayout_11.addWidget(self.img_grafik)
        self.horizontalLayout_8.addWidget(self.frame_15)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.frame_18)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout_7.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_load.setText(_translate("Form", "Image Processing"))
        self.btn_crop.setText(_translate("Form", "Croping Image"))
        self.btn_save.setText(_translate("Form", "Save"))
        self.btn_clear.setText(_translate("Form", "Clear"))
        self.comboBox.setItemText(0, _translate("Form", "1280 x 720"))
        self.comboBox.setItemText(1, _translate("Form", "1920 × 1080"))
        self.comboBox.setItemText(2, _translate("Form", "2560 × 1440"))
        self.totalCell.setText(_translate("Form", " Total Cell : "))
        self.label_9.setText(_translate("Form", "Image Processing"))
        self.label_2.setText(_translate("Form", "Original Image"))
        self.label_4.setText(_translate("Form", "Diameter Detection"))
        self.label_5.setText(_translate("Form", "Corner Detection"))
        self.label_3.setText(_translate("Form", "Result"))
        self.label_6.setText(_translate("Form", "Count Cell"))
        self.label.setText(_translate("Form", "Count Cell Diameter"))
        self.label_7.setText(_translate("Form", "Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
