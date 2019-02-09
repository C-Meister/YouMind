# -*- coding: utf-8 -*-
from functools import partial
import pafy
import urllib
import pyperclip
import time
import nativemessaging
from pprint import pprint as pp
import simplejson as json
from time import sleep
from pathlib import Path
import threading
from multiprocessing import Pool,Array,Manager
import sched
import os
class youtube():

    NOT_YOUTUBE = 0
    WATCH = 1
    PLAYLIST = 2
    WATCH_AND_PLAYLIST = 3
    CHANNEL = 4

    USER = 5
    OTHERS = 6

    API_KEY = ""
    DOWNLOAD_PATH = ""

    LAST_UPLOAD_URL = None
    SUBSCRIBED_ID = None
    SUBSCRIBED_forUser = None

    def __init__(self, key, path=None):
        self.API_KEY = key
        self.DOWNLOAD_PATH = path
        f=open("subscribed.txt","r")
        url=f.readline()
        f.close()
        f=open("lastuploaded.txt","r")
        self.LAST_UPLOAD_URL = f.readline()
        f.close()
        self.subscribe(url)

    def subscribe(self, url):
        urltype= self.get_urltype(url)
        flag = False
        if urltype == self.CHANNEL:
            id = url[url.find("channel/")+len("channel/"):].split('/')[0]
            
            self.SUBSCRIBED_forUser = False
            if self.SUBSCRIBED_ID != id:
                #새로운 구독
                self.LAST_UPLOAD_URL =""
                self.SUBSCRIBED_ID = id
                flag= True

        elif urltype == self.USER:
            id = url[url.find("channel/")+len("user/"):].split('/')[0]
            self.SUBSCRIBED_forUser = True    
            if self.SUBSCRIBED_ID != id:
                #새로운 구독
                self.LAST_UPLOAD_URL =""
                self.SUBSCRIBED_ID = id
                flag=True

        if flag is True:
            #쓰레드시작
            t = threading.Thread(target=self.repeater,daemon=True)
            
            t.start()
            
            
    def repeater(self):
        while True: 
            self.isUploaded()
            time.sleep(60)

    def change_path(self,path):
        self.DOWNLOAD_PATH = path

    def get_urltype(self, url):
        splited = url.split('www.youtube.com/')
        if len(splited) != 2:
            return self.NOT_YOUTUBE
        else:
            sub_url = splited[1]
            if sub_url.find("playlist") == 0:
                return self.PLAYLIST
            elif sub_url.find("watch") == 0:
                if sub_url.find("&list=") == -1:
                    return self.WATCH
                else:
                    return self.WATCH_AND_PLAYLIST
            elif sub_url.find("user/") == 0:
                return self.USER
            elif sub_url.find("channel/") == 0:
                return self.CHANNEL
            else:
                return self.OTHERS

    def get_videos(self, url):
        urltype = self.get_urltype(url)
        print("urltype:", urltype)
        # try:
        if urltype == self.NOT_YOUTUBE:
            return None
        elif urltype == self.WATCH:
            return self.get_video_one(url)
        elif urltype == self.PLAYLIST:
            id = url[url.find("list=")+len("list="):].split('&')[0]
            return self.get_videos_in_list(id, True)
        elif urltype == self.WATCH_AND_PLAYLIST:
            id = url[url.find("list=")+len("list="):].split('&')[0]
            return self.get_videos_in_list(id, True)

        elif urltype == self.CHANNEL:
            id = url[url.find("channel/")+len("channel/"):].split('/')[0]
            return self.get_videos_in_channel(id)
        elif urltype == self.USER:
            id = url[url.find("channel/")+len("user/"):].split('/')[0]
            return self.get_videos_in_channel(id, True)

        elif urltype == self.OTHERS:
            return None

        # except:
        #     return None
        
    def isUploaded(self):
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + \
            'key={}&part=snippet,id&order=date&maxResults=1'.format(
                self.API_KEY)
        first_url += '&channelId=' + \
            self.SUBSCRIBED_ID if self.SUBSCRIBED_forUser is False else '&forUsername=' + self.SUBSCRIBED_ID
        url = first_url
        # print("API URL : ",url)
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)
        current_url  = base_video_url+resp['items'][0]['id']['videoId']
        if self.LAST_UPLOAD_URL == "":
            print("FIRST :",current_url)
            self.LAST_UPLOAD_URL = current_url
            f=open("lastuploaded.txt","w")
            f.write(self.LAST_UPLOAD_URL)
            f.close()
        elif self.LAST_UPLOAD_URL != current_url:
            print("UPDATED :", current_url)
            self.LAST_UPLOAD_URL = base_video_url+resp['items'][0]['id']['videoId']
            f=open("lastuploaded.txt","w")
            f.write(self.LAST_UPLOAD_URL)
            f.close()
        else:
            print("SAME :",current_url)
        


    def get_videos_in_channel(self, channel_id, forUsername=False):

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + \
            'key={}&part=snippet,id&order=date&maxResults=50'.format(
                self.API_KEY)
        first_url += '&channelId=' + \
            channel_id if forUsername is False else '&forUsername=' + channel_id

        video_links = []
        url = first_url
        print("API URL : ", url)
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    if i['snippet']['title'] != "Private video" and i['snippet']["liveBroadcastContent"] == 'none':
                        video_links.append({
                            'url': base_video_url + i['id']['videoId'],
                            'title': i['snippet']['title'],
                            'thumbnail': i['snippet']['thumbnails']['medium']['url']
                        })
            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
                sleep(0.1)
            except:
                break
        return video_links
    
    def get_videos_in_list(self, list_id, print_title=False):

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/playlistItems?'

        first_url = base_search_url + \
            'key={}&playlistId={}&part=snippet,id&order=date&maxResults=25'.format(
                self.API_KEY, list_id)

        video_links = []
        url = first_url
        print("API URL : ", url)
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                i = i['snippet']
                if i['resourceId']['kind'] == "youtube#video":
                    if i['title'] != "Private video":
                        video_links.append({
                            'url': base_video_url + i['resourceId']['videoId'],
                            'title': i['title'],
                            'thumbnail': i['thumbnails']['medium']['url']
                        })
            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except:
                break
            time.sleep(0.1)
        return video_links

    def get_possible_fn(self, title, ext):
        fn = title+"."+ext
        idx = 2
        while Path(fn).exists():
            fn = title + " ({}).".format(idx)+ext
            idx += 1
        return fn

    def download_video(self, download_dict ):
        url = download_dict['url']  
        ext_filter = download_dict['ext']
        resl_filter= download_dict['resl'] if 'resl' in download_dict else None
        cb=download_dict['cb'] if 'cb' in download_dict else None
        idx = download_dict['idx']
        print(url)
        ytube_video = pafy.new(url)
        if resl_filter is not None:
            for s in ytube_video.streams:
                ext = s.extension
                if ext == ext_filter and s.resolution == resl_filter:
                    print("249")
                    print(s.url)
                    s.download(filepath=self.get_possible_fn(self.DOWNLOAD_PATH+ytube_video.title,ext),quiet=False,callback=lambda total, dtotal, ratio, speed, left_seconds : self.barUpdate(idx,int(ratio*100)))
                    return
        ytube_best = ytube_video.getbest(preftype=ext_filter)
        ytube_best.download(filepath=self.get_possible_fn(self.DOWNLOAD_PATH+ytube_best.title,ytube_best.extension),quiet=True,callback=lambda total,dtotal,ratio,rate,eta: self.barUpdate(idx,int(ratio*100)))
        return
    def barUpdate(self,idx,per):
        self.f.append(idx+","+per)
        


    def getVideoId(self, url):
        return url[url.find("v=")+len("v="):].split('&')[0]

    def get_video_one(self, url):

        base_video_url = 'https://www.googleapis.com/youtube/v3/videos?id={}&key={}&part=snippet,contentDetails'.format(
            self.getVideoId(url), self.API_KEY)
        inp = urllib.request.urlopen(base_video_url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['kind'] == "youtube#video":
                if i['snippet']['title'] != "Private video":
                    return [{
                        "thumbnail": i['snippet']['thumbnails']['medium']['url'],
                        "title": i['snippet']['title'],
                        "url": url
                    }]
        return None


    
    def round_robin_download(self,video_list,ext, resl=None, cb=None,threadCount = 4):
        global mydata
        mydata = self.bar_list
        
        self.f= open("temp.txt","w")
        self.f.close()
        self.f= open("temp.txt","a")
        self.bar_list = []
        pool = Pool(threadCount)
        tuple_list = [{"url":video,"ext":ext,"resl":resl,"cb":cb,"idx":idx} for video,idx in zip(video_list,range(len(video_list)))]
        
        pool.map(self.download_video,tuple_list)
        self.f.close()
        print(mydata,self.li)
        pool.close()
        pool.join()
        

    def getInfo(self, url, ext_filter=None, resl_filter=None):
        print(url)

        ytube_video = pafy.new(url)
        ytube_thumbnail = ytube_video.thumb

        ytube_exts = {}
        ytube_info = {}

        if ext_filter is None and resl_filter is None:

            for s in ytube_video.streams+ytube_video.audiostreams:

                ext = s.extension # 확장자 
                ytube_ext_info = [s.url, s.get_filesize()] # url과 파일 사이즈
                ytube_ext_info_dic = {s.resolution : ytube_ext_info}


                if not ext in ytube_exts:

                    ext_list = []
                    ytube_exts[ext] = ext_list

                ytube_exts[ext].append(ytube_ext_info_dic)

            ytube_info = {
            "thumbnail" : ytube_thumbnail,
            "title" : ytube_video.title,
            "download" : ytube_exts
        }

        elif ext_filter is not None and resl_filter is not None:

            EXIST = 0

            for s in ytube_video.streams+ytube_video.audiostreams:

                ext = s.extension

                if ext == ext_filter and (s.resolution == resl_filter or s.bitrate == resl_filter):

                    ytube_ext_info = [s.url, s.get_filesize()] # url과 파일 사이즈
                    if s.bitrate == resl_filter:

                        ytube_ext_info_dic = {s.bitrate : ytube_ext_info}
                    else:
                        ytube_ext_info_dic = {s.resolution : ytube_ext_info}

                    ytube_info = {
                    "thumbnail" : ytube_thumbnail,
                    "title" : ytube_video.title,
                    "download" : ytube_ext_info_dic
                    }
                    EXIST = 1

            if EXIST == 0:
                print("best")
                ytube_best = ytube_video.getbest(preftype=ext_filter)
                if ytube_best is None:
                    ytube_best = ytube_video.getbestaudio(preftype=ext_filter)

                    ytube_ext_info = [ytube_best.url, ytube_best.get_filesize()]
                    ytube_ext_info_dic = {ytube_best.bitrate : ytube_ext_info}
                else:

                    ytube_ext_info = [ytube_best.url, ytube_best.get_filesize()]
                    ytube_ext_info_dic = {ytube_best.resolution : ytube_ext_info}


                ytube_info = {
                    "thumbnail" : ytube_thumbnail,
                    "title" : ytube_video.title,
                    "download" : ytube_ext_info_dic
                    }


        return ytube_info
                    


    def get_channel_Info(self, id, forUsername=False):
        url = "https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&key={}".format(
            self.API_KEY)
        url += "&forUsername=" + id if forUsername is True else "&id="+id
        print("url:",url)
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)
        img_url = resp['items'][0]['snippet']['thumbnails']['default']['url']
        return {"url":img_url,"title":resp['items'][0]['snippet']['title'],"subscriberCount":resp['items'][0]['statistics']['subscriberCount']}
    def zsdf(self):
        
        y.round_robin_download(y.get_videos("https://www.youtube.com/channel/UCGR-u2P38jfdOrO495kqVaw/videos?view=0&flow=grid"),"mp4","480x360")

if __name__ == '__main__':
    y = youtube("AIzaSyBTXsPgj6BuSIBgMpiEUHmZ_Acgiz04Prs","C:\\Users\\YASUO\\Videos\\")
    #pp(y.getInfo(pyperclip.paste()))

    #print(y.getInfo(pyperclip.paste(),"m4a", "128k"))

    #y.zsdf()
    y.download_video({"url":"https://www.youtube.com/watch?v=1eEcL8XjogE","ext":"mp4","resl":"1280x720"})
    
    #print(y.get_channel_Info("mnetMPD",True))
    #y.subscribe("https://www.youtube.com/channel/UCu9BCtGIEr73LXZsKmoujKw","")
    # while True:
    #     pass
