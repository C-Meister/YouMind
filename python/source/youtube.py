# -*- coding: utf-8 -*-

import pafy
import urllib
import pyperclip
import time
from pprint import pprint as pp
import simplejson as json


class youtube():

    NOT_YOUTUBE = 0
    WATCH = 1
    PLAYLIST = 2
    WATCH_AND_PLAYLIST = 3
    CHANNEL = 4

    USER = 5
    OTHERS = 6

    API_KEY = ""

    def __init__(self, key):
        self.API_KEY = key

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
                            'thumbnail': i['snippet']['thumbnails']['default']['url']
                        })
            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
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
                            'thumbnail': i['thumbnails']['default']['url']
                        })
            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except:
                break
            time.sleep(0.1)
        return video_links

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
                        "thumbnail": i['snippet']['thumbnails']['default']['url'],
                        "title": i['snippet']['title'],
                        "url": url
                    }]
        return None

    def getInfo(self, url, ext_filter=None, resl_filter=None):
        print(url)

        ytube_video = pafy.new(url)
        ytube_thumbnail = ytube_video.thumb
        ytube_duration = ytube_video.duration

        ytube_exts = {}
        ytube_info = {}

        if ext_filter is None and resl_filter is None:

            for s in ytube_video.streams:

                ext = s.extension  # 확장자
                ytube_ext_info = [s.url, s.get_filesize()]  # url과 파일 사이즈
                ytube_ext_info_dic = {s.resolution: ytube_ext_info}

                if not ext in ytube_exts:

                    ext_list = []
                    ytube_exts[ext] = ext_list

                ytube_exts[ext].append(ytube_ext_info_dic)

            ytube_info = {
                "thumbnail": ytube_thumbnail,
                "title": ytube_video.title,
                "download": ytube_exts,
                "duration": ytube_duration
            }

        elif ext_filter is not None and resl_filter is not None:

            EXIST = 0

            for s in ytube_video.streams:

                ext = s.extension

                if ext == ext_filter and s.resolution == resl_filter:

                    ytube_ext_info = [s.url, s.get_filesize()]  # url과 파일 사이즈
                    ytube_ext_info_dic = {s.resolution: ytube_ext_info}

                    ytube_info = {
                        "thumbnail": ytube_thumbnail,
                        "title": ytube_video.title,
                        "download": ytube_ext_info_dic,
                        "duration": ytube_duration
                    }
                    EXIST = 1

            if EXIST == 0:

                ytube_best = ytube_video.getbest(preftype=ext_filter)

                ytube_ext_info = [ytube_best.url, ytube_best.get_filesize()]
                ytube_ext_info_dic = {ytube_best.resolution: ytube_ext_info}

                ytube_info = {
                    "thumbnail": ytube_thumbnail,
                    "title": ytube_video.title,
                    "download": ytube_ext_info_dic,
                    "duration": ytube_duration
                }

        return ytube_info

    def getInfos(self, url, ext, resl):

        urlList = self.get_videos(url)
        if urlList is None:
            return None
        elif not isinstance(urlList, list):
            self.getVideoinfo(url)

        # InfoList = []
        # print(urlList)
        pyperclip.copy(str(urlList))
        # for url in urlList:
        #     # InfoList.append(self.getInfo(url, ext, resl))
        #     self.getVideoinfo(url)
        #     time.sleep(0.01)
        # return InfoList

        # return InfoList

    def get_channel_picture_url(self, id, forUsername=False):
        url = "https://www.googleapis.com/youtube/v3/channels?part=snippet&fields=items%2Fsnippet%2Fthumbnails%2Fdefault&key={}".format(
            self.API_KEY)
        url += "&forUsername=" + id if forUsername is True else "&id="+id
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)
        img_url = resp['items'][0]['snippet']['thumbnails']['default']['url']
        return img_url


y = youtube("AIzaSyCmksLiLUv1yrxdnF1bPHt0x_O8wxwlGoE")

# pp(y.getInfo(pyperclip.paste()))
print(y.getInfos(pyperclip.paste(), "mp4", "1280x720"))
# print(y.get_videos_in_channel("bjummma",True))
# print(y.get_channel_picture_url("mnetMPD",True))
