from fileinput import filename
from sre_parse import SPECIAL_CHARS
from tkinter.tix import InputOnly
from tokenize import Special
from unicodedata import name
from pytube import YouTube
from pytube.cli import on_progress
import os
from time import sleep
import sys

print("YouTube url")
name = input(":")
yt_url = name


def youtube_download(file_url):
    yt = YouTube(file_url, on_progress_callback=on_progress)  # YouTube 객체 생성

    video_streams = yt.streams
    print(video_streams)  # streams 처리 전체 정보
    print("")
    print(f'==================================================================')
    print(f'* 제작자\t: {yt.author}')
    print(f'* 채널 ID\t: {yt.channel_id}')
    print(f'* 채널 URL\t: {yt.channel_url}')
    print(f'==================================================================')
    print(f'* 영상 ID\t: {yt.video_id}')
    print(f'* 영상 URL\t: {yt.watch_url}')
    print(f'* 썸네일 URL\t: {yt.thumbnail_url}')
    print(f'* 나이 제한\t: {yt.age_restricted}')
    print(f'* 영상 제목\t: {yt.title}')
    print(
        f'* 영상 길이\t: {str(yt.length // 60).zfill(2)}:{str(yt.length % 60).zfill(2)} / {yt.length} 초.')
    print(f'* 영상 조회수\t: {yt.views}')
    print(f'==================================================================')

    """incoding 처리"""
    video_streams = yt.streams.filter(file_extension='mp4').get_by_itag(22)
    print(video_streams)

    """저장 폴더 생성"""
    if not os.path.exists('youtube_download'):
        os.mkdir("youtube_download")
        print(" ")
        print("폴더를 생성합니다.")
        sleep(5)
    else:
        pass

    title = yt.title

    Special_char = '\/:*?"<>|.'
    for c in Special_char:
        if c in title:
            title = title.replace(c, '')
    print(title)
    print(" ")
    yes_no = input("동영상을 저장하시겠습니까? (Y/N)  ")

    if yes_no == "y" or yes_no == "Y":
        video_streams.download(filename=title + '.mp4',
                               output_path='youtube_download')
    if yes_no == "n" or yes_no == "N":
        print(" ")
        print("5초 뒤 프로그램을 종료합니다.")
        sleep(5)
        sys.exit(0)

    print('영상 다운로드 완료')


youtube_download(yt_url)
