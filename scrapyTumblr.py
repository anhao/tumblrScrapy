# -*- encoding:gbk -*-
__author__ = 'henan'
import urllib2
import json
import time
import re
import os

def getHtml(username):
    '���ݽӿڴӷ�������ȡ����ҳ��'
    #overview_url='http://'+username+'.tumblr.com/api/read/json?start=0&num=200'
    #print overview_url
    #sp_req=urllib2.Request(overview_url)
    #sp_req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
    #data=urllib2.urlopen(sp_req).read()
    #print data
    #return data
    f=open('./source/tumblr_normal.txt','r')
    return f.read()


def getResourceUrl(htmlStr):
    '��ȡ���е���Ƶ��ַ'
    videoList=[]
    imageList=[]
    data=json.loads(htmlStr[22:-1])
    for i in range(0,len(data["posts"])):
        if data["posts"][i]["type"]=="video":
            pass
            videoSourceCode = data["posts"][i]["video-player-500"]
            videoList.append(videoSourceCode)
        elif data["posts"][i]["type"]=="photo":
            image=data["posts"][i]["photo-url-500"]
            imageList.append(image)
            if data["posts"][i]["photos"]!= None:
                for j in range(0,len(data["posts"][i]["photos"])):
                    imageList.append(data["posts"][i]["photos"][j]["photo-url-500"])
    print "��Ƶ�б������ɣ�"
    print "ͼƬ�б������ɣ�"
    return (videoList,imageList)    #������Ƶ��ͼƬ�����б�

def saveUrl(saveContentList):
    '������ַ��txt�������ݿ�'
    resourceDir="./source"
    if not os.path.exists(resourceDir):
        os.makedirs(resourceDir)
        print "��ԴĿ¼������ɣ�"
    f=open("./source/video.txt",'w')
    f2=open("./source/image.txt","w")
    (video, image) = saveContentList
    for videoItem in video:
        f.write(videoItem+"\n")
    for imageItem in image:
        f2.write(imageItem+"\n")
    f.close()
    f2.close()
    print "�ļ������ϣ����������"

def parse2Html():
    '����ַƴ��Ϊ��ҳ'
    pass

def save2Local():
    '�����ݱ��浽����'
    pass

if __name__ == '__main__':
    f=getHtml('songdaping')
    c=getResourceUrl(f)
    saveUrl(c)