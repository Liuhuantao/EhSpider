# ehentaiSpider v0.1 by Entity 303
import requests, sys
from lxml import etree
from uaInfo import uaList
import random, time

class exhentaiSpider(object):
    # 定义常用变量
    def __init__(self, url):
        self.url = url
    
    #获取响应内容函数
    def getHtml(self, url, mode = ''):
        header = {
            'Cookie': 'ipb_member_id=7039661;ipb_pass_hash=5200483cb32744ae4753b35279696c26;igneous=1ea1b762b',
            'User-Agent': random.choice(uaList)}
        request = requests.get(url = url, headers = header, timeout = 15)
        # 检查cookie是否正确或是否有里站权限
        try:
            if (request.cookies['igneous'] == 'mystery'):
                print('请求失败，未成功登录，请检查你的cookies或是否有里站权限！')
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
    def parseHtml(self, html):
        text = etree.HTML(html)
        try:
            firstUrl = text.xpath("//body/div[@id = 'gdt']/div[1]/a/@href")[0]
            totalNumber = int(text.xpath("//body/div[@class = 'gtb']/p/text()")[0].split(' ')[-2])
        # 检查IP是否被封禁
        except IndexError:
            if (text.xpath("//body/text()")[0].split(' ')[0] == 'Your'):
                print('解析失败，您的IP地址被暂时封禁，这可能是由于您访问的次数过多或超过最大限制，请尝试以下解决办法：\n1.更换IP地址\n2.更换账号\n3.等待{0}'.format(text.xpath("//body/text()")[0].split('expires in')[-1]))

        return firstUrl, totalNumber

    # 爬取图片
    def getPictures(self, firstUrl, totalNumber):
        nowUrl = firstUrl
        # 循环爬取每一张图片
        for i in range(1, totalNumber + 1):
            print("爬取第{0}张图片中...({1} / {2})".format(i, i, totalNumber))
            html = self.getHtml(nowUrl)
            pictureUrl, nextUrl, pictureName = self.parsePictureHtml(html)
            picture = self.getHtml(pictureUrl, 'b')
            self.writePicture('./' + pictureName, 'wb', picture)
            nowUrl = nextUrl

    # 解析每一张图片页面
    def parsePictureHtml(self, html):
        text = etree.HTML(html)
        pictureUrl = text.xpath("//div[@id = 'i3']/a/img/@src")[0]
        nextUrl = text.xpath("//div[@id = 'i3']/a/@href")[0]
        pictureName = text.xpath("//div[@id = 'i2']/div[last()]/text()")[0].split(' ')[0]
        return pictureUrl, nextUrl, pictureName

    # 保存数据
    def writePicture(self, filename, mode, file):
        with open(filename, mode) as f:
            f.write(file)

    # 主函数
    def run(self):
        print('请求中...')
        html = self.getHtml(self.url)
        print()
        firstUrl, totalNumber = self.parseHtml(html)
        self.getPictures(firstUrl, totalNumber)

if __name__ == "__main__":
    # 程序入口
    url = input('请输入要爬取的图册的网址：')
    mySpider = exhentaiSpider(url)
    start = time.time()
    mySpider.run()
    end = time.time()
    print('爬取完成！用时 %.2f 秒' % (end - start))