# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_layermetadatatool.ui'
#
# Created: Tue Oct 16 20:08:59 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LayerMetadataTool(object):
    def setupUi(self, LayerMetadataTool):
        LayerMetadataTool.setObjectName(_fromUtf8("LayerMetadataTool"))
        LayerMetadataTool.resize(395, 456)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LayerMetadataTool.sizePolicy().hasHeightForWidth())
        LayerMetadataTool.setSizePolicy(sizePolicy)
        LayerMetadataTool.setSizeGripEnabled(False)
        LayerMetadataTool.setModal(True)
        self.groupBox = QtGui.QGroupBox(LayerMetadataTool)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 371, 156))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cboTocLayers = QtGui.QComboBox(self.groupBox)
        self.cboTocLayers.setGeometry(QtCore.QRect(140, 20, 211, 21))
        self.cboTocLayers.setObjectName(_fromUtf8("cboTocLayers"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 101, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 141, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 95, 121, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(141, 60, 129, 19))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.chkOutputPDF = QtGui.QCheckBox(self.layoutWidget)
        self.chkOutputPDF.setChecked(True)
        self.chkOutputPDF.setObjectName(_fromUtf8("chkOutputPDF"))
        self.horizontalLayout.addWidget(self.chkOutputPDF)
        self.chkOutputXML = QtGui.QCheckBox(self.layoutWidget)
        self.chkOutputXML.setEnabled(True)
        self.chkOutputXML.setObjectName(_fromUtf8("chkOutputXML"))
        self.horizontalLayout.addWidget(self.chkOutputXML)
        self.chkOutputTXT = QtGui.QCheckBox(self.layoutWidget)
        self.chkOutputTXT.setChecked(False)
        self.chkOutputTXT.setObjectName(_fromUtf8("chkOutputTXT"))
        self.horizontalLayout.addWidget(self.chkOutputTXT)
        self.layoutWidget1 = QtGui.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(140, 95, 182, 46))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton_2 = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButton.setEnabled(False)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout.addWidget(self.radioButton)
        self.groupBox_2 = QtGui.QGroupBox(LayerMetadataTool)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 205, 371, 211))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.tabWidget = QtGui.QTabWidget(self.groupBox_2)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 331, 171))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.txtOrganisation = QtGui.QLineEdit(self.tab)
        self.txtOrganisation.setGeometry(QtCore.QRect(100, 20, 216, 20))
        self.txtOrganisation.setObjectName(_fromUtf8("txtOrganisation"))
        self.txtEmail = QtGui.QLineEdit(self.tab)
        self.txtEmail.setGeometry(QtCore.QRect(100, 80, 216, 20))
        self.txtEmail.setObjectName(_fromUtf8("txtEmail"))
        self.txtWWW = QtGui.QLineEdit(self.tab)
        self.txtWWW.setGeometry(QtCore.QRect(100, 110, 216, 20))
        self.txtWWW.setObjectName(_fromUtf8("txtWWW"))
        self.txtAuthor = QtGui.QLineEdit(self.tab)
        self.txtAuthor.setGeometry(QtCore.QRect(100, 50, 216, 20))
        self.txtAuthor.setObjectName(_fromUtf8("txtAuthor"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_4.sizePolicy().hasHeightForWidth())
        self.tab_4.setSizePolicy(sizePolicy)
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.txtDescription = QtGui.QTextEdit(self.tab_4)
        self.txtDescription.setGeometry(QtCore.QRect(10, 30, 301, 106))
        self.txtDescription.setObjectName(_fromUtf8("txtDescription"))
        self.label_6 = QtGui.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.btnUpdateFromToolbarConfig = QtGui.QToolButton(self.groupBox_2)
        self.btnUpdateFromToolbarConfig.setGeometry(QtCore.QRect(325, 15, 31, 26))
        self.btnUpdateFromToolbarConfig.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/MapActionTools/icons/import.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUpdateFromToolbarConfig.setIcon(icon)
        self.btnUpdateFromToolbarConfig.setIconSize(QtCore.QSize(20, 20))
        self.btnUpdateFromToolbarConfig.setObjectName(_fromUtf8("btnUpdateFromToolbarConfig"))
        self.label = QtGui.QLabel(LayerMetadataTool)
        self.label.setGeometry(QtCore.QRect(110, 10, 171, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.btnCreateMetadata = QtGui.QPushButton(LayerMetadataTool)
        self.btnCreateMetadata.setGeometry(QtCore.QRect(300, 425, 81, 21))
        self.btnCreateMetadata.setObjectName(_fromUtf8("btnCreateMetadata"))
        self.btnCancel = QtGui.QPushButton(LayerMetadataTool)
        self.btnCancel.setGeometry(QtCore.QRect(210, 425, 81, 21))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.pushButton = QtGui.QPushButton(LayerMetadataTool)
        self.pushButton.setGeometry(QtCore.QRect(370, 5, 21, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(LayerMetadataTool)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LayerMetadataTool)
        LayerMetadataTool.setTabOrder(self.cboTocLayers, self.radioButton)
        LayerMetadataTool.setTabOrder(self.radioButton, self.txtOrganisation)
        LayerMetadataTool.setTabOrder(self.txtOrganisation, self.txtAuthor)
        LayerMetadataTool.setTabOrder(self.txtAuthor, self.txtEmail)
        LayerMetadataTool.setTabOrder(self.txtEmail, self.txtWWW)
        LayerMetadataTool.setTabOrder(self.txtWWW, self.btnCreateMetadata)
        LayerMetadataTool.setTabOrder(self.btnCreateMetadata, self.tabWidget)
        LayerMetadataTool.setTabOrder(self.tabWidget, self.btnCancel)
        LayerMetadataTool.setTabOrder(self.btnCancel, self.txtDescription)
        LayerMetadataTool.setTabOrder(self.txtDescription, self.pushButton)

    def retranslateUi(self, LayerMetadataTool):
        LayerMetadataTool.setWindowTitle(QtGui.QApplication.translate("LayerMetadataTool", "MapAction Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("LayerMetadataTool", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("LayerMetadataTool", "1. Select layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("LayerMetadataTool", "2. Output format", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("LayerMetadataTool", "3. Metadata standard", None, QtGui.QApplication.UnicodeUTF8))
        self.chkOutputPDF.setText(QtGui.QApplication.translate("LayerMetadataTool", "pdf", None, QtGui.QApplication.UnicodeUTF8))
        self.chkOutputXML.setText(QtGui.QApplication.translate("LayerMetadataTool", "xml", None, QtGui.QApplication.UnicodeUTF8))
        self.chkOutputTXT.setText(QtGui.QApplication.translate("LayerMetadataTool", "txt", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("LayerMetadataTool", "Project ZEBRA", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("LayerMetadataTool", "MapAction Deployment", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("LayerMetadataTool", "Add information", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("LayerMetadataTool", "Organisation: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("LayerMetadataTool", "Author", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("LayerMetadataTool", "www:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("LayerMetadataTool", "Email:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("LayerMetadataTool", " About Metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("LayerMetadataTool", "Describe the layer", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("LayerMetadataTool", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.btnUpdateFromToolbarConfig.setToolTip(QtGui.QApplication.translate("LayerMetadataTool", "<html><head/><body><p>Update form with values from toolbar configuration file.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LayerMetadataTool", "Create Layer Metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCreateMetadata.setText(QtGui.QApplication.translate("LayerMetadataTool", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("LayerMetadataTool", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setToolTip(QtGui.QApplication.translate("LayerMetadataTool", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Layer Metadata Tool</span></p><p>This tool helps you creates layer metadata. Metadata is information that describes a dataset, for instance, who created it? What coordinate system is it in? Its file type and geographical extent.</p><p><span style=\" font-size:12pt;\">Instructions</span></p><p>1. Select a layer from the drop down list. This list is composed of layers in your current QGIS map Table of Content.</p><p>2. Choose what format(s) you would like the output from the options: XML, text file and PDF.</p><p>3. Choose what level of metadata you would like to create. The default is the simplified Project ZEBRA standard which will be satisfactory in most instances.</p><p>4. Add information to the fields in the form, this infomation will become part of your metadata document.</p><p>5. When you create the document it will place the output file into the directory of the layer you have selected to create metadata for with the suffix \'&lt;filename&gt;_metadata.xml\' for example.</p><p>For more information please visit <a href=\"http://www.mapaction.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">www.mapaction.org/</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("LayerMetadataTool", "i", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LayerMetadataTool = QtGui.QDialog()
    ui = Ui_LayerMetadataTool()
    ui.setupUi(LayerMetadataTool)
    LayerMetadataTool.show()
    sys.exit(app.exec_())

