阅文作家助手
===========================
![](https://img.shields.io/badge/Python-3-green.svg) ![](https://img.shields.io/badge/requests-2.22.0-green.svg)
### 阅文作家专区 - <https://write.qq.com/>
帮助遗失原稿的作家从后台批量下载自己的稿子

    
****
## :dolphin:前言
在水群的时候，听说有作者像读者求助，原稿丢了，想要盗版网站可下的那种全本txt。  
当时我就震惊了。。。

## :dolphin:使用前须知
有两个参数需要改一下：
```
	UserID --> https://write.qq.com/portal/booknovels/chaptertmp/CBID/ 后面的那一串数字
	Cookie --> pgv_pvi=x; eas_sid=xx; pgv_pvid=xxx; RK=xxxx; ptcz=... 总之很长就是了。你懂的
```

## :dolphin:运行环境
Version: Python3
## :dolphin:安装依赖库
```
pip3 install -r requirements.txt
```
## :dolphin:运行结果
大致将保存成一下结构：
```
data
|
|------作品相关
|		|---------相关1.txt
|		|---------相关2.txt
|
|------第一卷 xxx
|		|---------第一章 xxx.txt
|		|---------第二章 xxx.txt
|
|	...
|
|------草稿
|		|---------草稿1.txt
|		|---------草稿2.txt
|
|	...
```

## :dolphin:LICENSE
本项目基于SATA协议，同时使用者可以考虑收藏或推荐[**以混沌之名**](https://book.qidian.com/info/1017574231)(有人说巨毒，所以不给也无所谓😳
