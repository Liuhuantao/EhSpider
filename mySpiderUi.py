# 条件导入
try:
    from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
    from spiderUi_6 import Ui_MainWindow
except:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from spiderUi_2 import Ui_MainWindow

from EhSpider import ehSpider
from uaInfo import uaList
import sys, random, requests

class mySpiderUi(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        mySpiderUi.init(self)

    def init(self):
        self.label_3.hide()
        self.pushButton.clicked.connect(self.check)
    
    def check(self):
        if (self.linkInputBox.text() == ''):
            QMessageBox.warning(self, '警告', '请先输入链接！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            self.crawling(self.linkInputBox.text())

    def crawling(self, url):
        mySpider = ehSpider(url)
        mySpider.run
        

class ehSpiderForUi(ehSpider):
    def getHtml(self, url, mode = ''):
        header = {
            'Cookie': 'ipb_member_id=7039661;ipb_pass_hash=5200483cb32744ae4753b35279696c26;igneous=1ea1b762b',
            'User-Agent': random.choice(uaList)}
        request = requests.get(url = url, headers = header, timeout = 15)
        # 检查cookie是否正确或是否有里站权限
        try:
            if (request.cookies['igneous'] == 'mystery'):
                QMessageBox.warning('警告', '请求失败，未成功登录，请检查你的cookies是否正确或是否有里站权限！', QMessageBox.OK | QMessageBox.No, QMessageBox.OK)
                sys.exit()
        except KeyError:
            pass
        # 检查链接地址是否正确
        if (request.status_code == 404):
            QMessageBox.critical('错误', '404 not found, 请检查你输入的链接是否正确！', QMessageBox.OK | QMessageBox.No, QMessageBox.OK)
            sys.exit()
        if (mode == 'b'):
            return request.content
        else:
            return request.text

def main():
    #创建QApplication类的实例
    app = QApplication(sys.argv)
    window = mySpiderUi()
    window.show()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()