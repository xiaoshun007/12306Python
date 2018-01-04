# -*- coding: utf-8 -*-
"""
@author: ssf
"""
from splinter.browser import Browser
from configparser import ConfigParser
from time import sleep
import traceback
import time, sys

class huoche(object):
    """docstring for huoche"""
    driver_name=''
    executable_path=''
    #用户名，密码
    #username = u"xxx@qq.com"
    #passwd = u"xxx"
    # cookies值得自己去找, 下面两个分别是武汉, 襄阳
    #starts = u"%u6B66%u6C49%2CWHN"
    #ends = u"%u8944%u9633%2CXFN"
    # 时间格式2018-01-19
    #dtime = u"2018-01-11"
    # 车次，选择第几趟，0则从上之下依次点击
    #order = 0
    ###乘客名
    #users = [u"xxx"]
    ##席位
    #xb = u"二等座"
    #pz=u"成人票"
	
    ## 车次类型
    #train_types = ["D", "G"]
    ## 发车时间：时间格式 12:00--18:00
    #start_time = u"12:00--18:00"

    """网址"""
    #ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    #login_url = "https://kyfw.12306.cn/otn/login/init"
    #initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
    #buy="https://kyfw.12306.cn/otn/confirmPassenger/initDc"
	
    def readConfig(self, config_file='config.ini'):
        path = r"/Users/san/githubDownload/12306Python/" + config_file
        cp = ConfigParser()
        try:
            cp.read(path)
        except IOError as e:
            print(u'打开配置文件"%s"失败啦, 请先创建或者拷贝一份配置文件config.ini' % (config_file))
            raw_input('Press any key to continue')
            sys.exit()
        # 登录名
        self.username = cp.get("login", "username")
        # 密码
        self.password = cp.get("login", "password")
        # 始发站
        self.starts = cp.get("cookieInfo", "starts")
        # 终点站
        self.ends = cp.get("cookieInfo", "ends")
        # 乘车时间
        self.dtime = cp.get("cookieInfo", "dtime")
        # 车次
        self.dtime = cp.get("cookieInfo", "dtime")
        # 乘客名
        self.users = cp.get("userInfo", "users")
        # 车次类型
        self.train_types = cp.get("trainInfo", "train_types")
        # 发车时间
        self.start_time = cp.get("trainInfo", "start_time")
        # 网址
        self.ticket_url = cp.get("urlInfo", "ticket_url")
        self.login_url = cp.get("urlInfo", "login_url")
        self.initmy_url = cp.get("urlInfo", "initmy_url")
        self.buy = cp.get("urlInfo", "buy")       

    def __init__(self):
        self.driver_name='chrome'
        self.executable_path='/usr/local/bin/chromedriver'
        #self.executable_path=r'C:\Users\sanshunfeng\Downloads\chromedriver.exe'
        # 读取配置文件，获得初始化参数
        self.readConfig();

    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill("loginUserDTO.user_name", self.username)
        # sleep(1)
        self.driver.fill("userDTO.password", self.passwd)
        print(u"等待验证码，自行输入...")
        while True:
            if self.driver.url != self.initmy_url:
                sleep(1)
            else:
                break
                
    def preStart(self):
        # 选择车次类型
        for type in self.train_types:
            print(u'--------->选择车次类型', type)
            # 车次类型选择
            train_type_dict = {'T': u'T-特快',                # 特快
                                'G': u'GC-高铁/城际',         # 高铁
                                'D': u'D-动车',               # 动车
                                'Z': u'Z-直达'}               # 直达
            if type == 'T' or type == 'G' or type == 'D' or type == 'Z':
                self.driver.find_by_text(train_type_dict[type]).click()
            else:
                print(u"车次类型异常或未选择!(train_type=%s)" % type)
		
        # 选择发车时间
        print(u'--------->选择发车时间', self.start_time)
        self.driver.find_option_by_text(self.start_time).first.click()
		
    def start(self):
        self.driver=Browser(driver_name=self.driver_name,executable_path=self.executable_path)
        self.driver.driver.set_window_size(1400, 1000)
        self.login()
        # sleep(1)
        self.driver.visit(self.ticket_url)
        try:
            print(u"购票页面开始...")
            # sleep(1)
            # 加载查询信息
            self.driver.cookies.add({"_jc_save_fromStation": self.starts})
            self.driver.cookies.add({"_jc_save_toStation": self.ends})
            self.driver.cookies.add({"_jc_save_fromDate": self.dtime})

            self.driver.reload()

            count=0
            if self.order!=0:
                while self.driver.url==self.ticket_url:
                    #self.driver.find_option_by_text("06:00--12:00").first.click()
                    #self.driver.find_by_text(u"GC-高铁/城际").click()
                    #self.driver.find_by_text(u"D-动车").click()
                    self.preStart()
                    sleep(0.05)
                    self.driver.find_by_text(u"查询").click()
                    count += 1
                    print(u"循环点击查询... 第 %s 次" % count)
                    # sleep(1)
                    try:
                        self.driver.find_by_text(u"预订")[self.order - 1].click()
                    except Exception as e:
                        print(e)
                        print(u"还没开始预订")
                        continue
            else:
                while self.driver.url == self.ticket_url:
                    #self.driver.find_option_by_text("06:00--12:00").first.click()
                    #self.driver.find_by_text(u"GC-高铁/城际").click()
                    #self.driver.find_by_text(u"D-动车").click()
                    self.preStart()
                    sleep(0.05)
                    self.driver.find_by_text(u"查询").click()
                    count += 1
                    print(u"循环点击查询... 第 %s 次" % count)
                    # sleep(0.8)
                    try:
                        for i in self.driver.find_by_text(u"预订"):
                            i.click()
                            sleep(0.5)
                    except Exception as e:
                        print(e)
                        print(u"还没开始预订 %s" %count)
                        continue
            print(u"开始预订...")
            # sleep(3)
            # self.driver.reload()
            sleep(1)
            print(u'开始选择用户...')
            for user in self.users:
                self.driver.find_by_text(user).last.click()

            print(u"提交订单...")
            sleep(1)
            # self.driver.find_by_text(self.pz).click()
            # self.driver.find_by_id('').select(self.pz)
            # # sleep(1)
            # self.driver.find_by_text(self.xb).click()
            # sleep(1)
            self.driver.find_by_id('submitOrder_id').click()
            # print u"开始选座..."
            # self.driver.find_by_id('1D').last.click()
            # self.driver.find_by_id('1F').last.click()

            sleep(1)
            print(u"确认选座...")
            self.driver.find_by_id('qr_submit_id').click()

        except Exception as e:
            print(e)

if __name__ == '__main__':
    huoche=huoche()
    huoche.start()
