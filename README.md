# 12306Python
py12306 是一个 Python 3.x 版的12306.cn订票程序。

## 功能介绍
```
唯一需要手动操作的是：等待浏览器页面跳出后输入验证码点击登录
目前支持的功能：
    1、支持配置出发地、目的地、乘车日
    2、支持配置车次类型（动车、高铁等）
    3、支持配置出发时间
    4、需要手动输入登录验证码
    5、支持配置预定车次的选择顺序（order字段，暂时只支持配置成0，车次选择算法待优化）
    6、预定、购票自动完成	
   
还不支持的功能：
    1、chromedriver不支持可配置
    2、不支持车次选择
    3、不支持席别选择
```

## Usage
### 1、修改配置（参照Config说明）
```
    特别说明：
        cookie获得方法：
            1、打开页面：https://kyfw.12306.cn/otn/leftTicket/init
            2、填入查询条件：出发地、目的地、出发日，点查询
            3、F12 查看请求：https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2018-01-11&leftTicketDTO.from_station=WHN&leftTicketDTO.to_station=XFN&purpose_codes=ADULT
                获得的Cookie如下：
                    JSESSIONID=86D8CDAF7827575F7F77408C1FA56636;
                    tk=WpRNTJ3H2eQMrACKjRfMy_z3ZAxCj7xmM0QWqzc_WUXzOt4nxh4240;
                    RAIL_EXPIRATION=1515236695924;
                    RAIL_DEVICEID=heRJ8B6tdNNQB407baLsk3K9txtAM5lxdBJfRuILqA9q4-J8V4r77saj_RthYKmUXuutlUeZpV0YXDBi9eWWoPfILlcLSjiP4EyG-gcGbdbDn2L4lvGIit2loz4XQQifHRbPK9XDguMkGdYJvs-_lmPVjojXQQsB;
                    _jc_save_fromStation=%u6B66%u6C49%2CWHN;
                    _jc_save_toStation=%u8944%u9633%2CXFN;
                    _jc_save_fromDate=2018-01-11;
                    _jc_save_toDate=2018-01-04;
                    _jc_save_wfdc_flag=dc;
                    route=6f50b51faa11b987e576cdb301e545c4;
                    BIGipServerotn=267387402.50210.0000;
                    BIGipServerpool_passport=334299658.50215.0000;
                    current_captcha_type=Z;
                    acw_tc=AQAAAD874WWPEAgAERWK2y+f03HYaK5h
```
### 2、运行
```
直接运行:
python 12306Python.py
```
### 3、输入验证码
```
等待跳出浏览器页面，输入验证码，点击登录
```
### 4、完成支付
```
等待自动完成选票、提交订单，支付订单
```

## 环境说明
### Python版本 3.X
### 依赖包
```
pip install splinter
pip install configparser
```
### chromedriver
```
1、下载chromedrive驱动：https://chromedriver.storage.googleapis.com/index.html?path=2.34/
2、修改配置（Python抢火车票.py 方法 __init__() 中 self.executable_path=r'C:\Users\xxx\Downloads\chromedriver.exe'），executable_path为自身的chromedriver路径
```

## Config说明

最简单的方法是修改 config.ini， 然后填写自己的乘车信息， 这些配置都可以在运行期间进行修改。

```
; config.ini
; 配置信息：请依照注释修改必选项

## 登陆账号和密码
[login]
### username：12306登录用户名，必选参数
username=xxx@qq.com
### password：12306登录密码，必选参数
password=xxx

## cookie信息，出发站，目的站
## cookies值得自己去找, 下面两个分别是武汉, 襄阳
[cookieInfo]
### starts：对应搜索框出发地，必选参数，通过抓取查询请求获得cookie值
starts=%%u6B66%%u6C49%%2CWHN
### ends：对应搜索框目的地，必选参数，通过抓取查询请求获得cookie值
ends=%%u8944%%u9633%%2CXFN
### dtime：对应搜索框出发日，必选参数，时间格式：年-月-日，例如 2018-01-19
## 时间格式2018-01-19
dtime=2018-01-11

## order：车次，选择第几趟，0则从上至下依次点击，必选参数，有效值如下：
#### 0->从上至下点击
[orderItem]
order=0

## users：乘客姓名，必选参数，中文姓名，支持多个乘客，用英文逗号隔开，例如：张三,李四
[userInfo]
users = xxx

## 车次类型：
[trainInfo]
### train_types：车次类型，可选参数，默认全部车次，支持多个值，用英文逗号隔开，有效值如下：
#### T->特快
#### G->高铁
#### D->动车
#### Z->直达
train_types = D,G

### start_time：发车时间，可选参数，默认值“00:00--24:00”
### 时间格式 "12:00--18:00"（需要带英文格式的双引号），有效值如下：
##### “00:00--24:00”->00:00--24:00
##### “00:00--06:00”->00:00--06:00
##### “06:00--12:00”->06:00--12:00
##### “12:00--18:00”->12:00--18:00
##### “18:00--24:00”->18:00--24:00
start_time = "12:00--18:00"

## 网址，必选参数
## 此部分不需改动
[urlInfo]
ticket_url = https://kyfw.12306.cn/otn/leftTicket/init
login_url = https://kyfw.12306.cn/otn/login/init
initmy_url = https://kyfw.12306.cn/otn/index/initMy12306
buy = https://kyfw.12306.cn/otn/confirmPassenger/initDc
```

## TODO
```
1、支持控制台命令
2、支持邮件提醒
3、支持席别选择
4、转换为可执行文件，去除Python强依赖
5、。。。
```

LICENSE

GNU General Public License, version 2
