# EhSpider v0.2 by Entity 303
import requests, sys, os, random, time, logging, gettext
from lxml import etree
from datetime import datetime
from uaInfo import uaList

class ehSpider(object):
    # 定义常用变量
    def __init__(self, url, imgMode, imgRange, urlMode):
        self.url = url
        self.imgMode = imgMode
        self.imgRange = imgRange
        self.urlMode = urlMode
    
    #获取响应内容函数
    def getHtml(self, url, mode = '', params = ''):
        header = {
            'Cookie': 'ipb_member_id=7039661;ipb_pass_hash=5200483cb32744ae4753b35279696c26;igneous=1ea1b762b',
            'User-Agent': random.choice(uaList)}
        try:
            request = requests.get(url = url, headers = header, timeout = 25, params = params)
        except requests.exceptions.ConnectionError:
            print('请求失败，发生了一个连接错误，请重试！')
            logger.critical('A ConnectionError occurred,Please check the log for details!', exc_info = True)
            sys.exit()
        # 检查cookie是否正确或是否有里站权限
        try:
            if (request.cookies['igneous'] == 'mystery'):
                print('请求失败，未成功登录，请检查你的cookies是否正确或是否有里站权限！')
                sys.exit()
        except KeyError:
            pass
        # 检查链接地址是否正确
        if (request.status_code == 404):
            print('404 not found, 请检查你输入的链接是否正确！')
            sys.exit()
        if (mode == 'b'):
            return request.content
        else:
            return request.text
        '''
        retry = 0
        while retry <= 3:
            try:
                request = requests.get(url = url, headers = header, timeout = 15)
            # 超时异常
            except requests.exceptions.Timeout as e:
                retry += 1
                if (retry > 3):
                    print('重试失败，原因：请求超时，请检查您的网络！')
                    sys.exit()
                print('请求超时，重试中...({0} / 3)'.format(retry))
                time.sleep(2)
            else:
                if (retry >= 1):
                    print('重试成功！')
                if (mode == 'b'):
                    return request.content
                else:
                    return request.text
        '''

    # 解析一开始页面
    def parseHtml(self, html, state):
        text = etree.HTML(html)
        try:
            # 爬取全部
            if (state == 'all'):
                # 表站和里站的代码稍微有点不一样，所以要判断
                if (self.urlMode == 1):
                    firstUrl = text.xpath("//body/div[@id = 'gdt']/div[1]/a/@href")[0]
                else:
                    firstUrl = text.xpath("//body/div[@id = 'gdt']/div[1]/div/a/@href")[0]
                totalNumber = int(text.xpath("//body/div[@class = 'gtb']/p/text()")[0].split(' ')[-2])
                galleryName = text.xpath("//h1[@id = 'gn']/text()")[0]
            # 爬取部分
            else:
                # 计算第一张图片的索引
                firstUrlIndex = self.imgRange[0] % 21
                # 如果是 0 就加 1
                if not (firstUrlIndex):
                    firstUrlIndex += 1
                if (self.urlMode == 1):
                    firstUrl = (text.xpath(("//body/div[@id = 'gdt']/div[{0}]/a/@href").format(firstUrlIndex)))[0]
                else:
                    firstUrl = (text.xpath(("//body/div[@id = 'gdt']/div[{0}]/div/a/@href").format(firstUrlIndex)))[0]
                totalNumber = self.imgRange[1] - self.imgRange[0] + 1
                galleryName = text.xpath("//h1[@id = 'gn']/text()")[0]

            return firstUrl, totalNumber, galleryName
        # 检查IP是否被封禁
        except IndexError:
            if (html.split(' ')[0] == 'Your'):
                print('解析失败，您的IP地址被暂时封禁，这可能是由于您访问的次数过多或超过最大限制，请尝试以下解决办法：\n1.更换IP地址\n2.更换账号\n3.等待{0}'.format(html.split('expires in')[-1]))
                sys.exit()     

    # 爬取图片
    def getPictures(self, firstUrl, totalNumber, galleryName):
        nowUrl = firstUrl
        galleryName = '[Spd]' + galleryName
        # 遍历去掉特殊字符
        character = '\/:*?"<>|'
        for s in character:
            if s in galleryName:
                galleryName = galleryName.replace(s, ' ')
        galleryPath = './' + galleryName
        if not (os.path.exists(galleryPath)):
            os.makedirs(galleryPath)
        # 循环爬取每一张图片
        for i in range(1, totalNumber + 1):
            print("爬取第{0}张图片中...({1} / {2})".format(i, i, totalNumber))
            html = self.getHtml(nowUrl)
            pictureUrl, nextUrl, pictureName = self.parsePictureHtml(html)
            picture = self.getHtml(pictureUrl, 'b')
            print('保存中...')
            self.writePicture(galleryPath + '/' + '[Spd]' + '[' + galleryName + ']' + ' ' + pictureName, 'wb', picture)
            nowUrl = nextUrl
            time.sleep(1)

    # 解析每一张图片页面
    def parsePictureHtml(self, html):
        text = etree.HTML(html)
        # 判断图片质量
        # 原图
        if (self.imgMode == 1):
            try:
                pictureUrl = text.xpath("//div[@id = 'i7']/a/@href")[0]
            except IndexError:
                pictureUrl = text.xpath("//img[@id = 'img']/@src")[0]
        # 非原图
        else:
            pictureUrl = text.xpath("//img[@id = 'img']/@src")[0]
        
        nextUrl = text.xpath("//div[@id = 'i3']/a/@href")[0]
        pictureName = text.xpath("//div[@id = 'i2']/div[last()]/text()")[0].split(' ')[0]
        return pictureUrl, nextUrl, pictureName

    # 保存数据
    def writePicture(self, filename, mode, file):
        with open(filename, mode) as f:
            f.write(file)

    # 计算范围
    def calculateRange(self):
        # 范围为空时
        if (self.imgRange == ['']):
            return None, 'all'
        # 范围不为空时
        else:
            range = {'p': self.imgRange[0] // 21}
            return range, 'part'

    # 主函数
    def run(self):
        range, state = self.calculateRange()
        if isinstance(range, type(None)):
            print('请求中...')
            html = self.getHtml(self.url)
        else:
            print('请求中...')
            html = self.getHtml(self.url, params = range)
        firstUrl, totalNumber, galleryName = self.parseHtml(html, state)
        self.getPictures(firstUrl, totalNumber, galleryName)
        

# 初始化日志系统
def log():
    # 判断当前目录下是否存在 ./log 文件夹，如果没有就递归创建该文件夹
    if not (os.path.exists('./log')):
        os.makedirs('./log')
    global logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler(filename = './log/{}.log'.format(str(datetime.now()).replace(':', '.')), encoding = 'utf-8')
    logger.addHandler(fileHandler)
    formatter = logging.Formatter('[%(levelname)s][%(asctime)s] %(message)s')
    fileHandler.setFormatter(formatter)

def main():
    log()
    logger.info('The program start running!')
    # 输入要爬取的图册的链接
    url = input('请输入要爬取的图册的网址：')
    logger.info('Entered gallery url: {0}'.format(url))
    # 检查链接是否是E站链接
    try:
        if (url.split('/')[2] == 'exhentai.org'):
            # 里站
            urlMode = 1
        elif (url.split('/')[2] == 'e-hentai.org'):
            # 表站
            urlMode = 2
        else:
            print('你输入的不是Exhentai的链接或E-hentai的链接，请检查你输入的链接，然后重试！')
            logger.warning('Program exited abnormally.')
            sys.exit()
    # 数组越界
    except IndexError:
        print('你输入的不是Exhentai的链接或E-hentai的链接，请检查你输入的链接，然后重试！')
        logger.critical('An IndexError occurred,This may be because you entered the wrong URL!', exc_info = True)
        logger.warning('Program exited abnormally.')
        sys.exit()

    try:
        # 输入要保存的图片质量
        imgMode = int(input('请选择你想保存的图片质量：\n1.原图（质量高，体积大，消耗GP点数多）；2.非原图（推荐）（质量中，体积小，不消耗GP点数）\n'))
        # 判断输入是否正确
        if (imgMode == 1):
            logger.info('Chosen saved picture quality:1(Original image)')
        elif (imgMode == 2):
            logger.info('Chosen saved picture quality:2(Non-original image)')
        else:
            print('输入有误，请检查图片质量，然后重试！')
            logger.error('Image mode input error!')
            logger.warning('Program exited abnormally.')
            sys.exit()
    # 输入了非数字字符导致异常
    except ValueError:
        print('输入有误，请检查图片质量，然后重试！')
        logger.error('Image mode input error!')
        logger.critical('A ValueError occurred,This may be because a non-numeric character was entered!', exc_info = True)
        sys.exit()

    # 输入图片范围
    imgRange = input('请输入你想爬取的图片范围（...-...）（下载所有留空即可）：').split('-')
    # 注意！下面的检查无法保证 imgRange 一定是正确的
    # 判断 imgRange 是否不为空
    if (imgRange != ['']):
        # 判断是否输入有误
        if (len(imgRange) != 2):
            print('输入有误，请检查图片范围，然后重试！')
            logger.error('Image range input error!')
            logger.warning('Program exited abnormally.')
            sys.exit()
        # 输入正确时
        else:
            # 转换为 int 类型
            try:
                imgRange[0] = int(imgRange[0])
                imgRange[1] = int(imgRange[1])
            # 输入了非数字字符导致异常
            except ValueError:
                print('输入有误，请检查图片范围，然后重试！')
                logger.error('Image range input error!')
                logger.critical('A ValueError occurred,This may be because a non-numeric character was entered!', exc_info = True)
                sys.exit()
            # 前面的数大于后面的数
            if (imgRange[0] > imgRange[1]):
                print('输入有误，请检查图片范围，然后重试！')
                logger.error('Image range input error(the first number is bigger than the second)!')
                sys.exit()
            # 前面的数小于等于0或后面的数小于等于0
            elif (imgRange <= 0 or imgRange[1] <= 0):
                print('输入有误，请检查图片范围，然后重试！')
                logger.error('Image range input error(the first number ≤ 0 or the second number ≤ 0)!')
                sys.exit()

    # 实例化爬虫类
    mySpider = ehSpider(url, imgMode, imgRange, urlMode)
    start = time.time()
    mySpider.run()
    end = time.time()
    print('爬取完成！用时 %.2f 秒' % (end - start))

# 程序入口
if __name__ == "__main__":
    try:
        main()
    except:
        print('程序意外退出，请查看日志！')
        logger.critical('Unexpected program exit', exc_info = True)
        sys.exit()


#https://e-hentai.org/g/2461038/4968c1ffa6/