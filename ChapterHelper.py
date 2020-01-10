# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'NiceLee'


'''
项目: 阅文作者小帮手
如果作者本地的稿子已经丢失，这个时候从阅文后台一章一章手动复制到本地会很麻烦，此时，小助手可以派上用场
UserID --> https://write.qq.com/portal/booknovels/chaptertmp/CBID/ 后面的那一串数字
Cookie --> pgv_pvi=x; eas_sid=xx; pgv_pvid=xxx; RK=xxxx; ptcz=... 总之很长就是了。你懂的
'''

import requests
import json
import os

UserID = '1234567'
Cookie = 'pgv_pvi=...; eas_sid=...'
Headers = {
    'Referer': 'https://write.qq.com/portal/booknovels/chaptertmp/CBID/%s' % UserID,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': Cookie
}

# 草稿章节列表
DraftChaptersUrl = "https://write.qq.com/Contentv3/Chapter/getDraftChapters/CBID/%s" % UserID
# 已发布章节列表
VolumeChaptersUrl = "https://write.qq.com/Contentv3/Chapter/getVolumeChapters/CBID/%s" % UserID

# 创建文件夹(如果不存在)
def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        
def getHttpJson(url, headers):
    http_result = requests.get(url, timeout=10, headers=headers)
    json_data = json.loads(http_result.text)
    return json_data

# 获取已发布章节列表
def getVolumeChapters():
    json_data = getHttpJson(VolumeChaptersUrl, Headers)
    return json_data['result']['volumes']

# 获取草稿章节列表
def getDraftChapters():
    json_data = getHttpJson(DraftChaptersUrl, Headers)
    return json_data['result']['chapters']

# 获取指定id章节内容
def getChapterContent(CCID):
    url = 'https://write.qq.com/Contentv3/Chapter/getChapter/CBID/%s/CCID/%s' % (UserID, CCID)
    json_data = getHttpJson(url, Headers)
    return json_data['result']['chapter']['content']
    
# 保存传入的章节
def saveChapters(volume_title, chapters, isOverwite = True):
    mkdir('data/' + volume_title)
    for chapter in chapters:  # 遍历章节
        CCID = chapter['CCID']
        chapter_title = chapter['chaptertitle']
        file_name = 'data/%s/%s.txt'%(volume_title, chapter_title)
        print('\t', chapter_title)
        if not isOverwite:
            if os.path.exists(file_name):
                print('\t--本地已经存在该章节 ')
                continue
        chapter_content = getChapterContent(CCID)
        with open(file_name , 'w' , encoding='utf-8') as file_obj:
            file_obj.write(chapter_content)

def saveVolumeChapters(volumes, isOverwite = True):
    mkdir('data')
    for volume in volumes:  # 遍历分卷
        saveChapters(volume['showtitle'], volume['chapters'], isOverwite)
 
if __name__ == '__main__':        
    volumes = getVolumeChapters()
    saveVolumeChapters(volumes, isOverwite = False)
    
    drafts = getDraftChapters()
    saveChapters('草稿',  drafts, isOverwite = False)