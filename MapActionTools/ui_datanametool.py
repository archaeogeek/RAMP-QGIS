# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_datanametool.ui'
#
# Created: Tue Oct 16 20:09:00 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DataNameTool(object):
    def setupUi(self, DataNameTool):
        DataNameTool.setObjectName(_fromUtf8("DataNameTool"))
        DataNameTool.resize(493, 601)
        self.label_4 = QtGui.QLabel(DataNameTool)
        self.label_4.setGeometry(QtCore.QRect(180, 10, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox_2 = QtGui.QGroupBox(DataNameTool)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 40, 471, 521))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(70, 80, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(70, 10, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setLineWidth(1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(80, 430, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 451, 301))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 160, 75, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 130, 75, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 75, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 100, 75, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 70, 75, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.cboGeoExtent = QtGui.QComboBox(self.groupBox)
        self.cboGeoExtent.setGeometry(QtCore.QRect(100, 40, 200, 22))
        self.cboGeoExtent.setObjectName(_fromUtf8("cboGeoExtent"))
        self.cboScale = QtGui.QComboBox(self.groupBox)
        self.cboScale.setGeometry(QtCore.QRect(100, 160, 200, 22))
        self.cboScale.setObjectName(_fromUtf8("cboScale"))
        self.cboDataType = QtGui.QComboBox(self.groupBox)
        self.cboDataType.setGeometry(QtCore.QRect(100, 130, 200, 22))
        self.cboDataType.setObjectName(_fromUtf8("cboDataType"))
        self.cboDataTheme = QtGui.QComboBox(self.groupBox)
        self.cboDataTheme.setGeometry(QtCore.QRect(100, 100, 200, 22))
        self.cboDataTheme.setObjectName(_fromUtf8("cboDataTheme"))
        self.cboSource = QtGui.QComboBox(self.groupBox)
        self.cboSource.setGeometry(QtCore.QRect(100, 190, 200, 22))
        self.cboSource.setObjectName(_fromUtf8("cboSource"))
        self.cboPermission = QtGui.QComboBox(self.groupBox)
        self.cboPermission.setGeometry(QtCore.QRect(100, 220, 200, 22))
        self.cboPermission.setObjectName(_fromUtf8("cboPermission"))
        self.label_19 = QtGui.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(10, 190, 75, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(10, 250, 75, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(10, 220, 75, 20))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(10, 280, 121, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.txtFreeText = QtGui.QLineEdit(self.groupBox)
        self.txtFreeText.setGeometry(QtCore.QRect(100, 250, 200, 20))
        self.txtFreeText.setObjectName(_fromUtf8("txtFreeText"))
        self.cboDataCategory = QtGui.QComboBox(self.groupBox)
        self.cboDataCategory.setGeometry(QtCore.QRect(100, 70, 200, 22))
        self.cboDataCategory.setObjectName(_fromUtf8("cboDataCategory"))
        self.txtGeoExtent = QtGui.QLineEdit(self.groupBox)
        self.txtGeoExtent.setEnabled(False)
        self.txtGeoExtent.setGeometry(QtCore.QRect(330, 40, 110, 20))
        self.txtGeoExtent.setObjectName(_fromUtf8("txtGeoExtent"))
        self.chkGeoExtent = QtGui.QCheckBox(self.groupBox)
        self.chkGeoExtent.setEnabled(True)
        self.chkGeoExtent.setGeometry(QtCore.QRect(310, 40, 16, 17))
        self.chkGeoExtent.setText(_fromUtf8(""))
        self.chkGeoExtent.setObjectName(_fromUtf8("chkGeoExtent"))
        self.chkDataCategory = QtGui.QCheckBox(self.groupBox)
        self.chkDataCategory.setEnabled(True)
        self.chkDataCategory.setGeometry(QtCore.QRect(310, 70, 21, 17))
        self.chkDataCategory.setText(_fromUtf8(""))
        self.chkDataCategory.setObjectName(_fromUtf8("chkDataCategory"))
        self.chkDataTheme = QtGui.QCheckBox(self.groupBox)
        self.chkDataTheme.setGeometry(QtCore.QRect(310, 100, 21, 17))
        self.chkDataTheme.setText(_fromUtf8(""))
        self.chkDataTheme.setObjectName(_fromUtf8("chkDataTheme"))
        self.chkDataType = QtGui.QCheckBox(self.groupBox)
        self.chkDataType.setGeometry(QtCore.QRect(310, 130, 21, 17))
        self.chkDataType.setText(_fromUtf8(""))
        self.chkDataType.setObjectName(_fromUtf8("chkDataType"))
        self.chkScale = QtGui.QCheckBox(self.groupBox)
        self.chkScale.setGeometry(QtCore.QRect(310, 160, 21, 17))
        self.chkScale.setText(_fromUtf8(""))
        self.chkScale.setObjectName(_fromUtf8("chkScale"))
        self.chkSource = QtGui.QCheckBox(self.groupBox)
        self.chkSource.setGeometry(QtCore.QRect(310, 190, 21, 17))
        self.chkSource.setText(_fromUtf8(""))
        self.chkSource.setObjectName(_fromUtf8("chkSource"))
        self.chkPermission = QtGui.QCheckBox(self.groupBox)
        self.chkPermission.setGeometry(QtCore.QRect(310, 220, 16, 17))
        self.chkPermission.setText(_fromUtf8(""))
        self.chkPermission.setObjectName(_fromUtf8("chkPermission"))
        self.txtDataTheme = QtGui.QLineEdit(self.groupBox)
        self.txtDataTheme.setEnabled(False)
        self.txtDataTheme.setGeometry(QtCore.QRect(330, 100, 110, 20))
        self.txtDataTheme.setObjectName(_fromUtf8("txtDataTheme"))
        self.txtDataType = QtGui.QLineEdit(self.groupBox)
        self.txtDataType.setEnabled(False)
        self.txtDataType.setGeometry(QtCore.QRect(330, 130, 110, 20))
        self.txtDataType.setObjectName(_fromUtf8("txtDataType"))
        self.txtDataCategory = QtGui.QLineEdit(self.groupBox)
        self.txtDataCategory.setEnabled(False)
        self.txtDataCategory.setGeometry(QtCore.QRect(330, 70, 110, 20))
        self.txtDataCategory.setObjectName(_fromUtf8("txtDataCategory"))
        self.txtScale = QtGui.QLineEdit(self.groupBox)
        self.txtScale.setEnabled(False)
        self.txtScale.setGeometry(QtCore.QRect(330, 160, 110, 20))
        self.txtScale.setObjectName(_fromUtf8("txtScale"))
        self.txtSource = QtGui.QLineEdit(self.groupBox)
        self.txtSource.setEnabled(False)
        self.txtSource.setGeometry(QtCore.QRect(330, 190, 110, 20))
        self.txtSource.setObjectName(_fromUtf8("txtSource"))
        self.txtPermission = QtGui.QLineEdit(self.groupBox)
        self.txtPermission.setEnabled(False)
        self.txtPermission.setGeometry(QtCore.QRect(330, 220, 110, 20))
        self.txtPermission.setObjectName(_fromUtf8("txtPermission"))
        self.label_23 = QtGui.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(180, 10, 51, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(370, 10, 41, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.groupBox)
        self.label_25.setGeometry(QtCore.QRect(10, 10, 71, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.btnCheckName = QtGui.QPushButton(self.groupBox)
        self.btnCheckName.setGeometry(QtCore.QRect(370, 270, 75, 23))
        self.btnCheckName.setObjectName(_fromUtf8("btnCheckName"))
        self.btnPermissionLookup = QtGui.QPushButton(self.groupBox)
        self.btnPermissionLookup.setGeometry(QtCore.QRect(82, 223, 16, 16))
        self.btnPermissionLookup.setObjectName(_fromUtf8("btnPermissionLookup"))
        self.txtDirectory = QtGui.QLineEdit(self.groupBox_2)
        self.txtDirectory.setGeometry(QtCore.QRect(20, 460, 291, 20))
        self.txtDirectory.setObjectName(_fromUtf8("txtDirectory"))
        self.btnGetDirectory = QtGui.QPushButton(self.groupBox_2)
        self.btnGetDirectory.setGeometry(QtCore.QRect(320, 460, 81, 23))
        self.btnGetDirectory.setObjectName(_fromUtf8("btnGetDirectory"))
        self.chkAddMapLayer = QtGui.QCheckBox(self.groupBox_2)
        self.chkAddMapLayer.setGeometry(QtCore.QRect(20, 490, 16, 17))
        self.chkAddMapLayer.setText(_fromUtf8(""))
        self.chkAddMapLayer.setChecked(True)
        self.chkAddMapLayer.setObjectName(_fromUtf8("chkAddMapLayer"))
        self.label_26 = QtGui.QLabel(self.groupBox_2)
        self.label_26.setGeometry(QtCore.QRect(40, 490, 121, 20))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_18 = QtGui.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(20, 430, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_34 = QtGui.QLabel(self.groupBox_2)
        self.label_34.setGeometry(QtCore.QRect(10, 10, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.label_35 = QtGui.QLabel(self.groupBox_2)
        self.label_35.setGeometry(QtCore.QRect(10, 80, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.cboTocLayers = QtGui.QComboBox(self.groupBox_2)
        self.cboTocLayers.setGeometry(QtCore.QRect(10, 44, 211, 22))
        self.cboTocLayers.setObjectName(_fromUtf8("cboTocLayers"))
        self.btnSaveShapefile = QtGui.QPushButton(DataNameTool)
        self.btnSaveShapefile.setGeometry(QtCore.QRect(380, 570, 75, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnSaveShapefile.setFont(font)
        self.btnSaveShapefile.setObjectName(_fromUtf8("btnSaveShapefile"))
        self.btnCancel = QtGui.QPushButton(DataNameTool)
        self.btnCancel.setGeometry(QtCore.QRect(300, 570, 75, 23))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))

        self.retranslateUi(DataNameTool)
        QtCore.QMetaObject.connectSlotsByName(DataNameTool)

    def retranslateUi(self, DataNameTool):
        DataNameTool.setWindowTitle(QtGui.QApplication.translate("DataNameTool", "MapAction Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DataNameTool", "Data Name Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DataNameTool", " Rename the layer by selecting parameter values", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DataNameTool", "Select a vector layer from Table of Content to rename", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DataNameTool", "Choose a directory to save the new file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("DataNameTool", "Scale*", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("DataNameTool", "Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("DataNameTool", "Geoextent", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("DataNameTool", "Data Theme", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("DataNameTool", "Data Category", None, QtGui.QApplication.UnicodeUTF8))
        self.cboPermission.setToolTip(QtGui.QApplication.translate("DataNameTool", "<html><head/><body><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("DataNameTool", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("DataNameTool", "Free Text*", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("DataNameTool", "Permission*", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("DataNameTool", "* Optional parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.chkGeoExtent.setToolTip(QtGui.QApplication.translate("DataNameTool", "Click to add a new parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.chkDataCategory.setToolTip(QtGui.QApplication.translate("DataNameTool", "Click to add a new parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.chkDataTheme.setToolTip(QtGui.QApplication.translate("DataNameTool", "Click to add a new parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.chkDataType.setToolTip(QtGui.QApplication.translate("DataNameTool", "Click to add a new parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.chkScale.setToolTip(QtGui.QApplication.translate("DataNameTool", "Click to add a new parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSource.setToolTip(QtGui.QApplication.translate("DataNameTool", "Click to add a new parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.chkPermission.setToolTip(QtGui.QApplication.translate("DataNameTool", "Click to add a new parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("DataNameTool", "Existing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("DataNameTool", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("DataNameTool", "Parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCheckName.setToolTip(QtGui.QApplication.translate("DataNameTool", "<html><head/><body><p>Click to check the layer name with the current parameter settings.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCheckName.setText(QtGui.QApplication.translate("DataNameTool", "Validate", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPermissionLookup.setToolTip(QtGui.QApplication.translate("DataNameTool", "<html><head/><body><p><span style=\" font-weight:600;\">hh</span> Both the data and any derived products may only be distributed amogst the humanitarian community. Neither data nor derived products may be distributed amongst general public.</p><p><span style=\" font-weight:600;\">hp</span> This data may be distributed amogst the humanitarian community. Derived products can be freely distributed</p><p><span style=\" font-weight:600;\">mh</span> The dataset may not be given to anyone outside MapAction. Derived maps may only be distributed amogst the humanitarian community.</p><p><span style=\" font-weight:600;\">mm</span> This dataset is for MapAction internal use only. (It is unlikely that this code wil every be used).</p><p><span style=\" font-weight:600;\">mp</span> The dataset may not be given to anyone outside MapAction. Only derived maps can be freely distributed. (This is typical for a comercial dataset, given to MA free of charge)</p><p><span style=\" font-weight:600;\">pp</span> This dataset is avaiable in the public domain. Derived products can be freely distributed</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPermissionLookup.setText(QtGui.QApplication.translate("DataNameTool", "i", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGetDirectory.setText(QtGui.QApplication.translate("DataNameTool", "Get Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.chkAddMapLayer.setToolTip(QtGui.QApplication.translate("DataNameTool", "Click to add a new parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("DataNameTool", "Add new layer to map?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("DataNameTool", "Step 3.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("DataNameTool", "Step 1.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("DataNameTool", "Step 2.", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSaveShapefile.setText(QtGui.QApplication.translate("DataNameTool", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("DataNameTool", "Cancel", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DataNameTool = QtGui.QDialog()
    ui = Ui_DataNameTool()
    ui.setupUi(DataNameTool)
    DataNameTool.show()
    sys.exit(app.exec_())
