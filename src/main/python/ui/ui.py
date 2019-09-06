# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rester.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1047, 762)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.action_frame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action_frame.sizePolicy().hasHeightForWidth())
        self.action_frame.setSizePolicy(sizePolicy)
        self.action_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.action_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.action_frame.setObjectName("action_frame")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.action_frame)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.request_type = QtWidgets.QComboBox(self.action_frame)
        self.request_type.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.request_type.sizePolicy().hasHeightForWidth())
        self.request_type.setSizePolicy(sizePolicy)
        self.request_type.setObjectName("request_type")
        self.request_type.addItem("")
        self.request_type.addItem("")
        self.gridLayout_10.addWidget(self.request_type, 0, 0, 1, 1)
        self.url = QtWidgets.QLineEdit(self.action_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.url.sizePolicy().hasHeightForWidth())
        self.url.setSizePolicy(sizePolicy)
        self.url.setObjectName("url")
        self.gridLayout_10.addWidget(self.url, 0, 1, 1, 1)
        self.send_btn = QtWidgets.QPushButton(self.action_frame)
        self.send_btn.setStyleSheet("background-color: #95a3ab;\n"
"color: white")
        self.send_btn.setObjectName("send_btn")
        self.gridLayout_10.addWidget(self.send_btn, 0, 2, 1, 1)
        self.save_btn = QtWidgets.QPushButton(self.action_frame)
        self.save_btn.setStyleSheet("background-color: #3689e6;\n"
"color: white")
        self.save_btn.setObjectName("save_btn")
        self.gridLayout_10.addWidget(self.save_btn, 0, 3, 1, 1)
        self.req_res_container_frame = QtWidgets.QFrame(self.action_frame)
        self.req_res_container_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.req_res_container_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.req_res_container_frame.setObjectName("req_res_container_frame")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.req_res_container_frame)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.splitter_2 = QtWidgets.QSplitter(self.req_res_container_frame)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.req_container_frame = QtWidgets.QFrame(self.splitter_2)
        self.req_container_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.req_container_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.req_container_frame.setLineWidth(0)
        self.req_container_frame.setObjectName("req_container_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.req_container_frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.req_container_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.params_tablist = QtWidgets.QTabWidget(self.req_container_frame)
        self.params_tablist.setObjectName("params_tablist")
        self.params_tab = QtWidgets.QWidget()
        self.params_tab.setObjectName("params_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.params_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.params_tab_title = QtWidgets.QLabel(self.params_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.params_tab_title.setFont(font)
        self.params_tab_title.setObjectName("params_tab_title")
        self.verticalLayout.addWidget(self.params_tab_title)
        self.params_table = QtWidgets.QTableWidget(self.params_tab)
        self.params_table.setRowCount(1)
        self.params_table.setProperty("horizontalHeader", "")
        self.params_table.setObjectName("params_table")
        self.params_table.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.params_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.params_table.setHorizontalHeaderItem(1, item)
        self.params_table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.params_table)
        self.params_tablist.addTab(self.params_tab, "")
        self.auth_tab = QtWidgets.QWidget()
        self.auth_tab.setObjectName("auth_tab")
        self.formLayout = QtWidgets.QFormLayout(self.auth_tab)
        self.formLayout.setObjectName("formLayout")
        self.auth_type_label = QtWidgets.QLabel(self.auth_tab)
        self.auth_type_label.setObjectName("auth_type_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.auth_type_label)
        self.token_field_label = QtWidgets.QLabel(self.auth_tab)
        self.token_field_label.setObjectName("token_field_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.token_field_label)
        self.auth_type_value = QtWidgets.QLineEdit(self.auth_tab)
        self.auth_type_value.setObjectName("auth_type_value")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.auth_type_value)
        self.auth_type = QtWidgets.QComboBox(self.auth_tab)
        self.auth_type.setObjectName("auth_type")
        self.auth_type.addItem("")
        self.auth_type.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.auth_type)
        self.params_tablist.addTab(self.auth_tab, "")
        self.header_tab = QtWidgets.QWidget()
        self.header_tab.setObjectName("header_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.header_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headers_tab_title = QtWidgets.QLabel(self.header_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.headers_tab_title.setFont(font)
        self.headers_tab_title.setObjectName("headers_tab_title")
        self.verticalLayout_2.addWidget(self.headers_tab_title)
        self.request_headers_table = QtWidgets.QTableWidget(self.header_tab)
        font = QtGui.QFont()
        font.setKerning(True)
        self.request_headers_table.setFont(font)
        self.request_headers_table.setRowCount(0)
        self.request_headers_table.setObjectName("request_headers_table")
        self.request_headers_table.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.request_headers_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.request_headers_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.request_headers_table.setHorizontalHeaderItem(2, item)
        self.request_headers_table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.request_headers_table)
        self.add_new_header_btn = QtWidgets.QPushButton(self.header_tab)
        self.add_new_header_btn.setStyleSheet("background-color: #3689e6;\n"
"color: white")
        self.add_new_header_btn.setObjectName("add_new_header_btn")
        self.verticalLayout_2.addWidget(self.add_new_header_btn)
        self.params_tablist.addTab(self.header_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.params_tablist.addTab(self.tab, "")
        self.gridLayout.addWidget(self.params_tablist, 1, 0, 1, 1)
        self.res_container_frame = QtWidgets.QFrame(self.splitter_2)
        self.res_container_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.res_container_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.res_container_frame.setObjectName("res_container_frame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.res_container_frame)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label = QtWidgets.QLabel(self.res_container_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)
        self.progress_bar = QtWidgets.QProgressBar(self.res_container_frame)
        self.progress_bar.setMaximum(0)
        self.progress_bar.setProperty("value", -1)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout_8.addWidget(self.progress_bar, 1, 0, 1, 1)
        self.response_tablist = QtWidgets.QTabWidget(self.res_container_frame)
        self.response_tablist.setObjectName("response_tablist")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pretty_view = QtWidgets.QTextBrowser(self.tab_4)
        self.pretty_view.setObjectName("pretty_view")
        self.gridLayout_11.addWidget(self.pretty_view, 0, 0, 1, 1)
        self.response_tablist.addTab(self.tab_4, "")
        self.response_raw_tab = QtWidgets.QWidget()
        self.response_raw_tab.setObjectName("response_raw_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.response_raw_tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.response_raw = QtWidgets.QTextBrowser(self.response_raw_tab)
        self.response_raw.setObjectName("response_raw")
        self.gridLayout_7.addWidget(self.response_raw, 0, 0, 1, 1)
        self.response_tablist.addTab(self.response_raw_tab, "")
        self.response_headers_tab = QtWidgets.QWidget()
        self.response_headers_tab.setObjectName("response_headers_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.response_headers_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.response_headers_table = QtWidgets.QTableWidget(self.response_headers_tab)
        self.response_headers_table.setGridStyle(QtCore.Qt.NoPen)
        self.response_headers_table.setRowCount(1)
        self.response_headers_table.setObjectName("response_headers_table")
        self.response_headers_table.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.response_headers_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.response_headers_table.setHorizontalHeaderItem(1, item)
        self.response_headers_table.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.response_headers_table, 0, 0, 1, 1)
        self.response_tablist.addTab(self.response_headers_tab, "")
        self.gridLayout_8.addWidget(self.response_tablist, 2, 0, 1, 1)
        self.gridLayout_9.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.req_res_container_frame, 1, 0, 1, 4)
        self.history_and_collection_frame = QtWidgets.QFrame(self.splitter)
        font = QtGui.QFont()
        font.setKerning(False)
        self.history_and_collection_frame.setFont(font)
        self.history_and_collection_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.history_and_collection_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.history_and_collection_frame.setObjectName("history_and_collection_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.history_and_collection_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.history_and_collection_tabs = QtWidgets.QTabWidget(self.history_and_collection_frame)
        self.history_and_collection_tabs.setObjectName("history_and_collection_tabs")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.history_list = QtWidgets.QListView(self.tab_2)
        self.history_list.setObjectName("history_list")
        self.gridLayout_5.addWidget(self.history_list, 0, 0, 1, 1)
        self.history_and_collection_tabs.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.collections_list = QtWidgets.QListView(self.tab_3)
        self.collections_list.setObjectName("collections_list")
        self.gridLayout_6.addWidget(self.collections_list, 0, 0, 1, 1)
        self.history_and_collection_tabs.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.history_and_collection_tabs, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1047, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(mainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionUndo = QtWidgets.QAction(mainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(mainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(mainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(mainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(mainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSelect_All = QtWidgets.QAction(mainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionToggle_Sidebar = QtWidgets.QAction(mainWindow)
        self.actionToggle_Sidebar.setObjectName("actionToggle_Sidebar")
        self.actionToggle_Fullscreen = QtWidgets.QAction(mainWindow)
        self.actionToggle_Fullscreen.setObjectName("actionToggle_Fullscreen")
        self.actionCheck_for_updates = QtWidgets.QAction(mainWindow)
        self.actionCheck_for_updates.setObjectName("actionCheck_for_updates")
        self.actionDocumentation = QtWidgets.QAction(mainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionSupport = QtWidgets.QAction(mainWindow)
        self.actionSupport.setObjectName("actionSupport")
        self.actionReport_Bug = QtWidgets.QAction(mainWindow)
        self.actionReport_Bug.setObjectName("actionReport_Bug")
        self.actionFAQs = QtWidgets.QAction(mainWindow)
        self.actionFAQs.setObjectName("actionFAQs")
        self.actionAbout_Rest_App = QtWidgets.QAction(mainWindow)
        self.actionAbout_Rest_App.setObjectName("actionAbout_Rest_App")
        self.actionPreferences_Settings = QtWidgets.QAction(mainWindow)
        self.actionPreferences_Settings.setObjectName("actionPreferences_Settings")
        self.actionSettings_Preferences = QtWidgets.QAction(mainWindow)
        self.actionSettings_Preferences.setObjectName("actionSettings_Preferences")
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences_Settings)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSettings_Preferences)
        self.menuView.addAction(self.actionToggle_Fullscreen)
        self.menuView.addAction(self.actionToggle_Sidebar)
        self.menuHelp.addAction(self.actionCheck_for_updates)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionFAQs)
        self.menuHelp.addAction(self.actionSupport)
        self.menuHelp.addAction(self.actionReport_Bug)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Rest_App)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainWindow)
        self.params_tablist.setCurrentIndex(2)
        self.response_tablist.setCurrentIndex(0)
        self.history_and_collection_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Rester | A Slick REST Client"))
        self.request_type.setItemText(0, _translate("mainWindow", "GET"))
        self.request_type.setItemText(1, _translate("mainWindow", "POST"))
        self.send_btn.setText(_translate("mainWindow", "Send"))
        self.save_btn.setText(_translate("mainWindow", "Save"))
        self.label_2.setText(_translate("mainWindow", "Request"))
        self.params_tab_title.setText(_translate("mainWindow", "URL Query Parameters"))
        item = self.params_table.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "Key"))
        item = self.params_table.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "Value"))
        self.params_tablist.setTabText(self.params_tablist.indexOf(self.params_tab), _translate("mainWindow", "Parameters"))
        self.auth_type_label.setText(_translate("mainWindow", "Authorization Type"))
        self.token_field_label.setText(_translate("mainWindow", "Token"))
        self.auth_type.setItemText(0, _translate("mainWindow", "No Auth"))
        self.auth_type.setItemText(1, _translate("mainWindow", "Bearer Token"))
        self.params_tablist.setTabText(self.params_tablist.indexOf(self.auth_tab), _translate("mainWindow", "Authorization"))
        self.headers_tab_title.setText(_translate("mainWindow", "Headers (0)"))
        item = self.request_headers_table.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "Actions"))
        item = self.request_headers_table.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "Key"))
        item = self.request_headers_table.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "Value"))
        self.add_new_header_btn.setText(_translate("mainWindow", "Add Header"))
        self.params_tablist.setTabText(self.params_tablist.indexOf(self.header_tab), _translate("mainWindow", "Headers"))
        self.params_tablist.setTabText(self.params_tablist.indexOf(self.tab), _translate("mainWindow", "Body"))
        self.label.setText(_translate("mainWindow", "Response"))
        self.response_tablist.setTabText(self.response_tablist.indexOf(self.tab_4), _translate("mainWindow", "Pretty View"))
        self.response_tablist.setTabText(self.response_tablist.indexOf(self.response_raw_tab), _translate("mainWindow", "Raw Request Dump"))
        item = self.response_headers_table.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "Key"))
        item = self.response_headers_table.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "Value"))
        self.response_tablist.setTabText(self.response_tablist.indexOf(self.response_headers_tab), _translate("mainWindow", "Response Headers"))
        self.history_and_collection_tabs.setTabText(self.history_and_collection_tabs.indexOf(self.tab_2), _translate("mainWindow", "History"))
        self.history_and_collection_tabs.setTabText(self.history_and_collection_tabs.indexOf(self.tab_3), _translate("mainWindow", "Collections"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuEdit.setTitle(_translate("mainWindow", "Edit"))
        self.menuView.setTitle(_translate("mainWindow", "View"))
        self.menuHelp.setTitle(_translate("mainWindow", "Help"))
        self.actionQuit.setText(_translate("mainWindow", "Quit"))
        self.actionUndo.setText(_translate("mainWindow", "Undo"))
        self.actionRedo.setText(_translate("mainWindow", "Redo"))
        self.actionCut.setText(_translate("mainWindow", "Cut"))
        self.actionCopy.setText(_translate("mainWindow", "Copy"))
        self.actionPaste.setText(_translate("mainWindow", "Paste"))
        self.actionSelect_All.setText(_translate("mainWindow", "Select All"))
        self.actionToggle_Sidebar.setText(_translate("mainWindow", "Toggle Sidebar"))
        self.actionToggle_Fullscreen.setText(_translate("mainWindow", "Toggle Full Screen"))
        self.actionCheck_for_updates.setText(_translate("mainWindow", "Check for Updates"))
        self.actionDocumentation.setText(_translate("mainWindow", "Documentation"))
        self.actionSupport.setText(_translate("mainWindow", "Support"))
        self.actionReport_Bug.setText(_translate("mainWindow", "Report Bug"))
        self.actionFAQs.setText(_translate("mainWindow", "FAQs"))
        self.actionAbout_Rest_App.setText(_translate("mainWindow", "About Rest App"))
        self.actionPreferences_Settings.setText(_translate("mainWindow", "Settings/Preferences"))
        self.actionSettings_Preferences.setText(_translate("mainWindow", "Settings/Preferences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
