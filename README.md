# 12306Python

![](https://img.shields.io/badge/language-python-blue.svg) ![](https://img.shields.io/badge/hack12306-v1.0.3-519dd9.svg)

hack12306.py 是一个 Python 3.x 版的[12306.cn](http://www.12306.cn/mormhweb/)自动订票程序。利用[splinter](https://splinter.readthedocs.io/en/latest/index.html)（一个开源的用来通过python自动化测试web的工具），让电脑自动操作网页。

## [English version](https://github.com/xiaoshun007/12306Python/blob/master/README_EN.md)


## 码云地址
### [hack12306](https://gitee.com/xiaoshun/12306Python)

## 说明
```
    |-- README.md：说明
    |-- config.ini：登录名、密码等的配置文件
    |-- hack12306.py：主程序
    |-- city_code.txt：城市中文名称与三字码对应文件
    |-- resoures：存放的一些资源信息
            |-- images
                    |-- 流程图.jpg
```

## 设计
![image](https://github.com/xiaoshun007/12306Python/blob/master/resources/images/流程图.jpg)

## 功能介绍
```
    hack12306.py 是一个 Python 3.x 版的12306.cn订票程序。执行程序，等待浏览器页面跳出后输入验证码点击登录，即可完成自动购票。

支持的功能：
    1、支持配置出发地、目的地、乘车日
    2、支持配置车次类型（动车、高铁等）
    3、支持配置出发时间
    4、需要手动输入登录验证码
    5、支持配置预定车次的选择顺序（使用order字段配置，数字0：从上至下选择；数字x（1、2、3、4...）：车次从上到下的序号，配置2表示列表中的第二个车次）
    6、支持预定、购票自动完成	
    7、支持配置文件路径指定
    8、支持席别指定
    9、支持是否允许分配无座
   
还不支持的功能：
    1、邮件提醒
```

## Usage
### 1、加入待购票乘车人信息到登录账号
```
    乘客姓名需要提前加入到登录的12306账号的联系人中，为了程序自动选择乘客姓名
```

### 2、修改配置（参照Config说明）
```
直接修改 hack12306.py 当前目录下的config.ini 或者 拷贝一份 config.ini 到任意目录，在执行时指定绝对路径

    特别说明：
        1、[cookieInfo]中starts和ends为中文名称
```
### 3、运行
```
方式一：直接运行（配置文件使用hack12306.py相同目录下的config.ini）
	python hack12306.py

方式二：指定config.ini路径（配置文件使用指定的config.ini）
	python hack12306.py -c /Users/xxx/config.ini

	参数说明：
		'-c', '--config', '可选参数, 指定配置文件, 默认使用当前目录 config.ini'

方式三：下载可执行文件执行
    1、下载可执行程序
    2、配置config.ini，放在可执行程序同级目录
    3、双击运行程序

```

### 可执行程序下载地址
[下载 hack12306 可执行程序](https://github.com/xiaoshun007/12306Python/releases)
```
可执行文件说明：
    1、本程序的可执行文件都是通过 pyinstaller 转换的，如果不能时候，请pull最新代码，重新转换
        pyinstaller -onefile <scriptName>
    2、下载后解压，按照上文【3、运行】-> 方式三 步骤执行
```

### 4、输入验证码
```
等待跳出浏览器页面，输入验证码，点击登录
```
### 5、完成支付
```
等待自动完成选票、提交订单，完成后自行支付订单
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
1、查看chrome版本号：帮助->关于Google Chrome，在打开的设置页面中间可以看到Chrome的当前版本，例如：当前Chrome版本63，下载v2.34版本的chromedriver
2、下载chromedrive驱动：https://chromedriver.storage.googleapis.com/index.html
3、注意浏览器chrome与chromedriver的对应版本（我的chrome是63+，因此选择2.34的chromedriver）
4、参照下方的对应关系表下载
```

#### chromedriver与chrome的对应关系表
```
chromedriver版本  支持的Chrome版本
    v2.34           v61-63
    v2.33           v60-62
    v2.32           v59-61
    v2.31           v58-60
    v2.30           v58-60
    v2.29           v56-58
    v2.28           v55-57
    v2.27           v54-56
    v2.26           v53-55
    v2.25           v53-55
    v2.24           v52-54
    v2.23           v51-53
    v2.22           v49-52
    v2.21           v46-50
    v2.20           v43-48
    v2.19           v43-47
    v2.18           v43-46
    v2.17           v42-43
    v2.13           v42-45
    v2.15           v40-43
    v2.14           v39-42
    v2.13           v38-41
    v2.12           v36-40
    v2.11           v36-40
    v2.10           v33-36
    v2.9            v31-34
    v2.8            v30-33
    v2.7            v30-33
    v2.6            v29-32
    v2.5            v29-32
    v2.4            v29-32
```

## Config说明

最简单的方法是修改 config.ini， 然后填写自己的乘车信息， 这些配置都可以在运行期间进行修改。

```
; config.ini
; 配置信息：请依照注释修改必选项，非必选项可以删除等号后的值

## 登陆账号和密码
[login]
### username：12306登录用户名，必选参数
username=xxx@qq.com
### password：12306登录密码，必选参数
password=xxx

## cookie信息，出发站，目的站
[cookieInfo]
### starts：对应搜索框出发地，必选参数，请输入中文名称，例如：武汉
starts=武汉
### ends：对应搜索框目的地，必选参数，请输入中文名称，例如：南京
ends=南京
### dtime：对应搜索框出发日，必选参数，时间格式：年-月-日，例如 2018-01-19
## 时间格式2018-01-19
dtime=2018-01-11

## order：车次，选择第几趟，0则从上至下依次点击，必选参数，如果要特定车次，需要先找到车次在列表中的次序，有效值如下：
#### 0->从上至下点击
#### 1->第一个车次
#### 2->第二个车次
[orderItem]
order=2

## users：乘客姓名，必选参数，中文姓名，支持多个乘客，用英文逗号隔开，例如：张三,李四
### 乘客姓名需要提前加入到登录的12306账号的联系人中，为了程序自动选择乘客姓名
[userInfo]
users = xxx

## 车次类型：
[trainInfo]
### train_types：车次类型，可选参数，默认全部车次，支持多个值，用英文逗号隔开，特别需求的在此指定值，不指定请删除等号后的值，默认是车次不勾选，有效值如下：
#### T->特快
#### G->高铁
#### D->动车
#### Z->直达
#### K->快车
train_types = D,G

### start_time：发车时间，可选参数，不指定请删除等号后的值，默认值“00:00--24:00”
### 时间格式 12:00--18:00，有效值如下：
##### 00:00--24:00->00:00--24:00
##### 00:00--06:00->00:00--06:00
##### 06:00--12:00->06:00--12:00
##### 12:00--18:00->12:00--18:00
##### 18:00--24:00->18:00--24:00
start_time = 12:00--18:00

[confirmInfo]
## 席别
### seat_type：席别，可选参数，不指定请删除等号后的值，默认按照12306预定到的车次的席别，有效值如下：
#### 硬座
#### 硬卧
#### 软卧
#### 一等软座
#### 二等软座
#### 商务座
#### 一等座
#### 二等座
#### 混编硬座
#### 特等座
seat_type = 二等座

## 网址，必选参数
## 此部分不需改动
[urlInfo]
ticket_url = https://kyfw.12306.cn/otn/leftTicket/init
login_url = https://kyfw.12306.cn/otn/login/init
initmy_url = https://kyfw.12306.cn/otn/index/initMy12306
buy = https://kyfw.12306.cn/otn/confirmPassenger/initDc

## 路径信息
[pathInfo]
### driver_name: 浏览器名称，必选参数
driver_name = chrome
### executable_path: 浏览器驱动路径，必选参数
### windows路径例如：C:\Users\sanshunfeng\Downloads\chromedriver.exe
executable_path = C:\Users\sanshunfeng\Downloads\chromedriver.exe



```

## 一些说明
```
    1、本程序是让电脑自动操作浏览器，将一些手动点击的动作自动化完成，机器操作总比手动点击要快一点，能争取一点时间是一点时间
    2、如果在运行中遇到找不到元素等错误，如object has no attribute 'click'，这是因为程序点击时页面还没加载出来，请将程序中sleep的时间稍微加大一些
    3、遇到上述错误程序退出，重新运行一遍
    4、由于使用splinter包，通过加载浏览器驱动，获取浏览器渲染之后的响应内容，由于需要加载浏览器，效率上有待商榷，但是模拟程度更高
```

## TODO
```
1、支持邮件提醒
2、。。。
```

LICENSE

