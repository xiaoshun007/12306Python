# 12306Python

![](https://img.shields.io/badge/language-python-blue.svg) ![](https://img.shields.io/badge/hack12306-v1.0.3-519dd9.svg)

hack12306.py is a automatic [12306.cn](http://www.12306.cn/mormhweb/) ticket booking program by Python 3.x . This program uses [splinter](https://splinter.readthedocs.io/en/latest/index.html) (python test framework for web applications) to operate the website automatically.

## [Chinese version](https://github.com/xiaoshun007/12306Python/blob/master/README.md)

## Description
```
    |-- README.md：Description
    |-- config.ini：Config file
    |-- hack12306.py：Main program	
    |-- city_code.txt：city and code mapping file
    |-- resoures：resources
            |-- images：images
                    |-- 流程图.jpg：flow chart
```

## Design
![image](https://github.com/xiaoshun007/12306Python/blob/master/resources/images/流程图.jpg)

## Features
```
    hack12306.py is a automatic 12306.cn ticket booking program by Python 3.x. While you run it, what you need to do is wait for the browser page to jump out, enter the verification code, click the login button, then go have a cup of tea or coffee, the ticket you want will be in your pocket. Easy and hanppy!

Supported：
    1、support config departure city, destination city, start date
    2、support config train types(D, G etc.)
    3、support config departure time
    4、need to enter the verification code manually
    5、support config train order
    		(0 means the first matches from top to bottom; 2 means the second train on the list)
    6、support auto search and confirm	
    7、support config file configurable
    8、support config seat type
   
Not supported：
    1、Email
```

## Usage
### 1、The one who wants to buy tikect should to be added to the login account
```
    passenger info should be added in advance for the program to use
```

### 2、config（Config.ini）
```

```
