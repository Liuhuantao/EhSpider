# 逻辑文件，包含ui交互控制以及爬虫部分
'''
代码千万条
注释第一条
代码不规范
亲人两行泪
笑死
'''

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

# 主窗口
class mySpiderUi(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        mySpiderUi.init(self)

    # 初始化窗口
    def init(self):
        # 隐藏状态标签
        self.status.hide()
        self.spinBox.clear()
        self.spinBox_2.clear()
        # 设置 “终止爬取” 按钮不可用
        self.stopCrawling.setEnabled(False)
        # 设置 “打开文件夹” 按钮不可用
        self.openFolder.setEnabled(False)
        # 将 “开始爬取” 绑定至 check 函数
        self.startCrawling.clicked.connect(self.check)
    
    # 检查用户输入，如无误就开始爬取
    def check(self):
        # 检查链接框的输入
        try:
            if (self.linkInputBox.text() == ''):
                QMessageBox.warning(self, '警告', '请正确的输入链接！', QMessageBox.Yes, QMessageBox.Yes)
                return
            else:
                if (self.linkInputBox.text().split('/')[2] == 'exhentai.org'):
                    # 里站
                    urlMode = 1
                elif (self.linkInputBox.text().split('/')[2] == 'e-hentai.org'):
                    # 表站
                    urlMode = 2
                else:
                    QMessageBox.warning(self, '警告', '你输入的不是Exhentai的链接或E-hentai的链接！', QMessageBox.Yes, QMessageBox.Yes)
                    return
        # 数组越界
        except IndexError:
            QMessageBox.warning(self, '警告', '你输入的不是Exhentai的链接或E-hentai的链接！', QMessageBox.Yes, QMessageBox.Yes)
            return

        # 检查爬取范围的输入
        if (self.spinBox.value() == 0 and self.spinBox_2.value() == 0):
            imgRange = ['']
        else:
            # 前面的数大于后面的数
            if (self.spinBox.value() > self.spinBox_2.value()):
                QMessageBox.warning(self, '警告', '范围输入有误（前面的数大于后面的数）！', QMessageBox.Yes, QMessageBox.Yes)
                return
            # 前面的数等于0
            elif (self.spinBox.value() == 0):
                QMessageBox.warning(self, '警告', '范围输入有误（前面的数等于0）！', QMessageBox.Yes, QMessageBox.Yes)
                return
            else:
                imgRange = [self.spinBox.value(), self.spinBox_2.value()]
        
        # 判断图片质量
        # 原图
        if (self.buttonGroup.checkedButton() == self.radioButton):
            imgMode = 1
        # 非原图
        elif (self.buttonGroup.checkedButton() == self.radioButton_2):
            imgMode = 2
        # 未选择（未选择时返回 None）
        else:
            QMessageBox.warning(self, '警告', '请选择图片质量！', QMessageBox.Yes, QMessageBox.Yes)
            return

        # 没有问题则调用 crawling 方法开始爬取
        self.crawling(self.linkInputBox.text(), imgMode, imgRange, urlMode)

    def crawling(self, url, imgMode, imgRange, urlMode):
        mySpider = ehSpiderForUi(url, imgMode, imgRange, urlMode)
        self.linkInputBox.setEnabled(False)
        self.spinBox.setEnabled(False)
        self.spinBox_2.setEnabled(False)
        self.radioButton.setEnabled(False)
        self.radioButton_2.setEnabled(False)
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