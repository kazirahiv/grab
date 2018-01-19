from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
DEVELOPER_KEY = "AIzaSyA8oSdX2G8WQSACcp9pl-WTE49GR1ybgkw"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
#search_response = youtube.search().list(q="surfing", part='snippet', maxResults=1).execute()
#videos = []
# for search_result in search_response.get("items", []):
#        if search_result["id"]["kind"] == "youtube#video":
#            title = search_result["snippet"]["title"]
#            id = search_result["id"]["videoId"]
#            videos.append(dict(title=title, id=id))
def video_search(string):
   search_response = youtube.search().list(q=string, part='snippet', maxResults=10).execute()
   videos = []
   for search_result in search_response.get("items", []):
      if search_result["id"]["kind"] == "youtube#video":
         title = search_result["snippet"]["title"]
         link = search_result["id"]["videoId"]
         videos.append(dict(title=title, link=link))
   return(videos)