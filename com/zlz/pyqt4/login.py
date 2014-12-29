# coding=utf-8
'''
Created on 2014-12-26

@author: zenglizhi
'''

from PyQt4 import QtGui, Qt, QtCore 

image = QtGui.QImage()
class Login(QtGui.QMainWindow):
    """
    """
    windowTitle = u"登陆客户端"
    version = 1.0
    
    def __init__(self, parent=None):
        """
        """
        super(Login, self).__init__(parent)
        self.setWindowTitle(self.windowTitle)
        self.setFixedSize(347, 264)
        self.setWindowIcon(QtGui.QIcon("images/login.png"))
        desktop = QtGui.QApplication.desktop()
        width = desktop.width()
        height = desktop.height()
        self.move((width - self.width()) / 2, (height - self.height()) / 2)
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint) 
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setIcon(QtGui.QIcon("images/client.png"))

        self.trayIcon.show()
        self.trayIcon.activated.connect(self.trayClick)
        self.trayMenu() 
        
        label_user = QtGui.QLabel(u"用户名：", self)
        label_user.setGeometry(QtCore.QRect(116, 135, 50, 22))
        
        label_passwd = QtGui.QLabel(u"密码：", self)
        label_passwd.setGeometry(QtCore.QRect(116, 170, 50, 22))
        
        self.lineEdit_user = QtGui.QLineEdit("", self)
        self.lineEdit_user.setGeometry(QtCore.QRect(160, 135, 150, 22))

        self.lineEdit_passwd = QtGui.QLineEdit("", self)
        self.lineEdit_passwd.setGeometry(QtCore.QRect(160, 170, 150, 22))
        self.lineEdit_passwd.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_passwd.setValidator(QtGui.QRegExpValidator(Qt.QRegExp("[A-Za-z0-9]+"), self))
        
        
        self.pushButton_login = QtGui.QPushButton(QtGui.QIcon("images/logins.png"), u"登录", self)
        self.pushButton_login.setGeometry(QtCore.QRect(250, 235, 75, 22))
        self.connect(self.pushButton_login, QtCore.SIGNAL("clicked()"), self.log_in)
        
        
        self.btn_min = labelBtn(1)  # 定义最小化按钮 ID:1
        self.btn_min.setParent(self)
        self.btn_min.setGeometry(308, 0, 27, 23)
        self.btn_min.setToolTip(u"最小化")
        self.btn_close = labelBtn(2)  # 定义关闭按钮 ID:2
        self.btn_close.setParent(self)
        self.btn_close.setGeometry(329, 0, 38, 21)
        self.btn_close.setToolTip(u"关闭")
        
        
        
    def trayClick(self, reason):
        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            self.showNormal()
        else:
            pass 
                            
    def trayMenu(self):
        #  bg = QtGui.QImage(':/images/demobg.png')
        img_open = QtGui.QIcon("images/open.png")
        img_exit = QtGui.QIcon("images/exit.png")
        self.trayIcon.setToolTip(self.windowTitle)
        self.restoreAction = QtGui.QAction(img_open, u"打开", self)
        self.restoreAction.triggered.connect(self.showNormal)
        self.quitAction = QtGui.QAction(img_exit, u"退出", self)
        self.quitAction.triggered.connect(QtGui.qApp.quit)
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon.setContextMenu(self.trayIconMenu)
    
    def log_in(self):
        dlg = QtGui.QMessageBox(self)
        dlg.information(self, u"提示", u"登陆...", QtGui.QMessageBox.Ok)     
        
    def btnHandle(self, ID):
        if ID == 1:  # 最小化
            self.hide()
            self.showMinimized()
        elif ID == 2:           
            self.trayIcon.hide()
            self.close()

    def btnEnter(self, ID):
        if ID == 1:# 鼠标进入
            self.btn_min.setPixmap(QtGui.QPixmap("images/min_f.png"))
        elif ID == 2:
            self.btn_close.setPixmap(QtGui.QPixmap("images/close_f.png"))

    def btnLeave(self, ID):
        self.btn_min.setPixmap(QtGui.QPixmap("images/min.png"))
        self.btn_close.setPixmap(QtGui.QPixmap("images/close.png"))


    def resizeEvent(self, event):
        image.load("images/background.png")
        pal = QtGui.QPalette()
        pal.setBrush(QtGui.QPalette.Window, QtGui.QBrush(image.scaled(event.size(),
                                                                      Qt.Qt.KeepAspectRatioByExpanding, Qt.Qt.SmoothTransformation)))
        self.setPalette(pal)
    
    def mousePressEvent(self, event):
        # 拖动窗口
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()


    def mouseMoveEvent(self, event):
        # 鼠标移动事件
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()   

        
class labelBtn(QtGui.QLabel):
    def __init__(self, ID):
        super(labelBtn, self).__init__()
        self.setMouseTracking(True)
        self.ID = ID

    def mouseReleaseEvent(self, event):  
        self.parent().btnHandle(self.ID)

    def enterEvent(self, event):
        self.parent().btnEnter(self.ID)

    def leaveEvent(self, event):
        self.parent().btnLeave(self.ID)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frm = Login()
    frm.show()
    sys.exit(app.exec_())


