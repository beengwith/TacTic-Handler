# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkin_out/ui_checkin_options.ui'
#
# Created: Wed Jan  4 14:23:20 2017
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_checkinOptionsGroupBox(object):
    def setupUi(self, checkinOptionsGroupBox):
        checkinOptionsGroupBox.setObjectName("checkinOptionsGroupBox")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(checkinOptionsGroupBox.sizePolicy().hasHeightForWidth())
        checkinOptionsGroupBox.setSizePolicy(sizePolicy)
        checkinOptionsGroupBox.setFlat(True)
        self.gridLayout = QtGui.QGridLayout(checkinOptionsGroupBox)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setContentsMargins(2, 4, 2, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(checkinOptionsGroupBox)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.saveAsDefaultsPushButton = QtGui.QPushButton(self.groupBox)
        self.saveAsDefaultsPushButton.setObjectName("saveAsDefaultsPushButton")
        self.horizontalLayout_2.addWidget(self.saveAsDefaultsPushButton)
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 2)
        self.mayaOptionsGroupBox = QtGui.QGroupBox(checkinOptionsGroupBox)
        self.mayaOptionsGroupBox.setObjectName("mayaOptionsGroupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.mayaOptionsGroupBox)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.createMayaDirsCheckBox = QtGui.QCheckBox(self.mayaOptionsGroupBox)
        self.createMayaDirsCheckBox.setChecked(True)
        self.createMayaDirsCheckBox.setObjectName("createMayaDirsCheckBox")
        self.horizontalLayout.addWidget(self.createMayaDirsCheckBox)
        self.createPlayblastCheckBox = QtGui.QCheckBox(self.mayaOptionsGroupBox)
        self.createPlayblastCheckBox.setChecked(True)
        self.createPlayblastCheckBox.setObjectName("createPlayblastCheckBox")
        self.horizontalLayout.addWidget(self.createPlayblastCheckBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.mayaOptionsGroupBox, 0, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(checkinOptionsGroupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.repositoryLabel = QtGui.QLabel(self.groupBox_2)
        self.repositoryLabel.setObjectName("repositoryLabel")
        self.horizontalLayout_3.addWidget(self.repositoryLabel)
        self.repositoryComboBox = QtGui.QComboBox(self.groupBox_2)
        self.repositoryComboBox.setObjectName("repositoryComboBox")
        self.horizontalLayout_3.addWidget(self.repositoryComboBox)
        self.checkinMethodLabel = QtGui.QLabel(self.groupBox_2)
        self.checkinMethodLabel.setObjectName("checkinMethodLabel")
        self.horizontalLayout_3.addWidget(self.checkinMethodLabel)
        self.checkinMethodComboBox = QtGui.QComboBox(self.groupBox_2)
        self.checkinMethodComboBox.setObjectName("checkinMethodComboBox")
        self.checkinMethodComboBox.addItem("")
        self.checkinMethodComboBox.addItem("")
        self.checkinMethodComboBox.addItem("")
        self.checkinMethodComboBox.addItem("")
        self.checkinMethodComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.checkinMethodComboBox)
        self.updateVersionlessCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.updateVersionlessCheckBox.setChecked(True)
        self.updateVersionlessCheckBox.setObjectName("updateVersionlessCheckBox")
        self.horizontalLayout_3.addWidget(self.updateVersionlessCheckBox)
        self.askBeforeSaveCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.askBeforeSaveCheckBox.setChecked(True)
        self.askBeforeSaveCheckBox.setObjectName("askBeforeSaveCheckBox")
        self.horizontalLayout_3.addWidget(self.askBeforeSaveCheckBox)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(6, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 2)

        self.retranslateUi(checkinOptionsGroupBox)
        QtCore.QMetaObject.connectSlotsByName(checkinOptionsGroupBox)

    def retranslateUi(self, checkinOptionsGroupBox):
        checkinOptionsGroupBox.setWindowTitle(QtGui.QApplication.translate("checkinOptionsGroupBox", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        checkinOptionsGroupBox.setTitle(QtGui.QApplication.translate("checkinOptionsGroupBox", "Checkin Options:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("checkinOptionsGroupBox", "Misc:", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAsDefaultsPushButton.setText(QtGui.QApplication.translate("checkinOptionsGroupBox", "Apply to All Tabs", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("checkinOptionsGroupBox", "Edit Filenaming", None, QtGui.QApplication.UnicodeUTF8))
        self.mayaOptionsGroupBox.setTitle(QtGui.QApplication.translate("checkinOptionsGroupBox", "Maya quick options:", None, QtGui.QApplication.UnicodeUTF8))
        self.createMayaDirsCheckBox.setText(QtGui.QApplication.translate("checkinOptionsGroupBox", "Create Maya Dirs (worspace.mel)", None, QtGui.QApplication.UnicodeUTF8))
        self.createPlayblastCheckBox.setText(QtGui.QApplication.translate("checkinOptionsGroupBox", "Create screenshot (playblast)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("checkinOptionsGroupBox", "Saving options:", None, QtGui.QApplication.UnicodeUTF8))
        self.repositoryLabel.setText(QtGui.QApplication.translate("checkinOptionsGroupBox", "Repository:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkinMethodLabel.setText(QtGui.QApplication.translate("checkinOptionsGroupBox", "Method:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkinMethodComboBox.setItemText(0, QtGui.QApplication.translate("checkinOptionsGroupBox", "Preallocate", None, QtGui.QApplication.UnicodeUTF8))
        self.checkinMethodComboBox.setItemText(1, QtGui.QApplication.translate("checkinOptionsGroupBox", "In-Place", None, QtGui.QApplication.UnicodeUTF8))
        self.checkinMethodComboBox.setItemText(2, QtGui.QApplication.translate("checkinOptionsGroupBox", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.checkinMethodComboBox.setItemText(3, QtGui.QApplication.translate("checkinOptionsGroupBox", "Move", None, QtGui.QApplication.UnicodeUTF8))
        self.checkinMethodComboBox.setItemText(4, QtGui.QApplication.translate("checkinOptionsGroupBox", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.updateVersionlessCheckBox.setText(QtGui.QApplication.translate("checkinOptionsGroupBox", "Update versionless", None, QtGui.QApplication.UnicodeUTF8))
        self.askBeforeSaveCheckBox.setText(QtGui.QApplication.translate("checkinOptionsGroupBox", "Ask before save", None, QtGui.QApplication.UnicodeUTF8))
