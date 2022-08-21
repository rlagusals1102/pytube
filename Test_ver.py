import os
import sys
import pytube
from pytube import YouTube
from pytube.cli import on_progress
from time import sleep
import tkinter as tk
from tkinter import messagebox


'''pip3 install pytube 설치'''


def youtube_download(file_url):
    yt = YouTube(file_url, on_progress_callback=on_progress)


name = input("유튜브 주소를 입력하세요.")
url = name

yt = pytube.YouTube(url, on_progress_callback=on_progress)
video_streams = yt.streams.filter(file_extension='mp4').get_by_itag(22)

print(" ")
print(" ")
print("<-----설명----->")
print("제목 : ", yt.title)
print("길이 : ", yt.length)
print("게시자 : ", yt.author)
print("게시날짜 : ", yt.publish_date)
print("조회수 : ", yt.views)
print("키워드 : ", yt.keywords)
print(" ")
print(" ")

yes_no = input("동영상을 저장하시겠습니까? (Y/N)  ")
if yes_no == "y" or yes_no == "Y":

    if not os.path.exists('youtube_download'):
      os.mkdir('youtube_download')
    else:
        pass
    title = yt.title
    special_char = '/:*?"<>|.'

    for c in special_char:
        if c in title:
            title = title.replacr(c, '')
    print(title)

    video_streams.download(filename=title + '.mp4',
                           output_path='youtube_download')


if yes_no == "n" or yes_no == "N":
    print(" ")
    print("5초 뒤 프로그램을 종료합니다.")
    sleep(5)
    sys.exit(0)
