import pafy
import urllib
import pyperclip
from pprint import pprint as pp
import simplejson as json
from time import sleep
from pathlib import Path
class youtube():

    NOT_YOUTUBE = 0
    WATCH = 1
    PLAYLIST = 2
    WATCH_AND_PLAYLIST = 3
    CHANNEL = 4
    OTHERS = 5

    API_KEY =""
    DOWNLOAD_PATH = ""

    def __init__(self, key, path=None):
        self.API_KEY = key
        self.DOWNLOAD_PATH = path
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
            elif sub_url.find("watch") ==0 :
                if sub_url.find("&list=") == -1:
                    return self.WATCH
                else:
                    return self.WATCH_AND_PLAYLIST
            elif sub_url.find("channel/") == 0:
                return self.CHANNEL
            else:
                return self.OTHERS

    def get_videos(self, url):
        urltype = self.get_urltype(url)
        # try:
        if urltype == self.NOT_YOUTUBE:
            return None
        elif urltype == self.WATCH:
            return url
        elif urltype == self.PLAYLIST:
            id = url[url.find("list=")+len("list="):].split('&')[0]
            return self.get_videos_in_list(id,True)
        elif urltype == self.WATCH_AND_PLAYLIST:
            id = url[url.find("list=")+len("list="):].split('&')[0]
            return self.get_videos_in_list(id,True)

        elif urltype == self.CHANNEL:
            id =url[url.find("channel/")+len("channel/"):].split('/')[0]
            return self.get_videos_in_channel(id,True)


        elif urltype == self.OTHERS:
            return None

        # except:
        #     return None
    
    def get_videos_in_channel(self,channel_id,forUsername=False,print_title=False):

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url+'key={}&part=snippet,id&order=date&maxResults=25'.format(self.API_KEY)
        first_url += '&channelId='+ channel_id if forUsername is False else '&forUsername=' + channel_id

        video_links = []
        url = first_url
        print("API URL : ",url)
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    if i['snippet']['title']!="Private video" and i['snippet']["liveBroadcastContent"] == 'none':
                        video_links.append(base_video_url + i['id']['videoId'])
                
            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
                sleep(0.1)
            except:
                break
        return video_links

    def get_videos_in_list(self,list_id, print_title=False):

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/playlistItems?'

        first_url = base_search_url+'key={}&playlistId={}&part=snippet,id&order=date&maxResults=25'.format(self.API_KEY, list_id)
        
        video_links = []
        url = first_url
        print("API URL : ",url)
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                i = i['snippet']
                if i['resourceId']['kind'] == "youtube#video":
                    if i['title']!="Private video":
                        video_links.append(base_video_url + i['resourceId']['videoId'])
            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
                sleep(0.1)
            except:
                break
        return video_links
    def get_possible_fn(self,title, ext):
        fn= title+"."+ext
        idx = 2
        while Path(fn).exists():
            fn= title +" ({}).".format(idx)+ext
            idx+=1
        return fn

    def download_video(self, url, ext_filter=None, resl_filter=None, cb=None):
        print(url)

        ytube_video = pafy.new(url)
        if ext_filter is not None and resl_filter is not None:
            for s in ytube_video.streams:
                ext = s.extension
                if ext == ext_filter and s.resolution == resl_filter:
                    s.download(filepath=self.get_possible_fn(self.DOWNLOAD_PATH+ytube_video.title,ext),callback=cb)
                    return

            ytube_best = ytube_video.getbest(preftype=ext_filter)
            ytube_best.download(filepath=self.get_possible_fn(self.DOWNLOAD_PATH+ytube_best.title,ytube_best.extension),callback=cb)
            return
        return

    def round_robin_download(self,url_list,threadCount = 4):
        pass
        

    def get_channel_picture_url(self, id, forUsername=False):
        url ="https://www.googleapis.com/youtube/v3/channels?part=snippet&fields=items%2Fsnippet%2Fthumbnails%2Fdefault&key={}".format(self.API_KEY)
        url += "&forUsername="+ id if forUsername is True else "&id="+id
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)
        img_url= resp['items'][0]['snippet']['thumbnails']['default']['url']
        return img_url
    


y = youtube("AIzaSyCZsObQQAM1CWOzhjM6Ezevhr3mq9ueoag","C:\\Users\\YASUO\\Videos\\")
#pp(y.getInfo(pyperclip.paste()))
#print(y.getInfos(pyperclip.paste(),"mp4","1280x720"))
#print(y.get_videos_in_channel("bjummma",True))
y.download_video("https://www.youtube.com/watch?v=NZvqWmBJLP8",ext_filter="mp4",resl_filter="1280x720")
#print(y.get_channel_picture_url("mnetMPD",True))