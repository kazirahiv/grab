from fastapi import FastAPI, HTTPException
import re
import os
from os import rename
from pydantic import BaseModel
import requests
from pathlib import Path
import time
from glob import glob
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Data(BaseModel):
    url: str
    onlyAudio: bool


download_directory = '/home/'


@app.post('/api/prepare')
def prepare(data: Data):
    return DownloadByURL(data.url, data.onlyAudio)


def DownloadByURL(url, onlyAudio=False):
    print(url)
    downloadDirectory = '/home/'
    formattedLink = url.replace("&t*", "")
    downloadCommand = "youtube-dl --extract-audio --audio-format mp3 --output \"%(title)s.%(ext)s\" " + \
        formattedLink
    videoName = os.popen(
        "youtube-dl --get-filename --output \"%(title)s.%(ext)s\" " + url).read()
    videoName = videoName.rsplit('.', 1)
    videoName.pop(videoName.index(videoName[-1]))
    videoName = ''.join(videoName)
    videoName = videoName + ".mp3"
    if not onlyAudio:
        downloadCommand = "youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' --output \"%(title)s.%(ext)s\" " + \
            formattedLink
        videoName = videoName.replace(".mp3", ".mp4").replace('\n', '')
    downloadCommand = re.sub("&t.*", "", downloadCommand)  # Clearing time bits

    os.chdir(downloadDirectory)
    os.system(downloadCommand)
    filePath = downloadDirectory+videoName
    if os.path.exists(filePath):
        return {'downloaded': True, 'fileName': videoName, 'filePath': filePath}
    else:
        return {'downloaded': True, 'fileName': videoName, 'filePath': filePath}


@app.get("/api/download")
async def download(path: str):
    if os.path.exists(path):
        return FileResponse(path)
    return HTTPException(status_code=404, detail="File not found")


@app.get("/api/searchvideo")
def video_search(search: str):
    print(search)
    videos = []
    try:
        search_response = youtube.search().list(
            q=search, part='snippet', maxResults=10).execute()
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                title = search_result["snippet"]["title"]
                thumbnail = search_result["snippet"]["thumbnails"]["high"]["url"]
                link = search_result["id"]["videoId"]
                videos.append(
                    dict(title=title, link=link, thumbnail=thumbnail))
    except Exception as e:
        print(e)
        return(videos)
    return(videos)
