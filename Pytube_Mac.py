from fileinput import filename
from sre_parse import SPECIAL_CHARS
from tkinter.tix import InputOnly
from tokenize import Special
from unicodedata import name
from pytube import YouTube
from pytube.cli import on_progress
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


name = input("YouTube url : ")
yt_url = name


def youtube_download(file_url):
    yt = YouTube(file_url, on_progress_callback=on_progress)  # YouTube 객체 생성

    video_streams = yt.streams
    print(video_streams)  # streams 처리 전체 정보

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
    print(f'* 영상 키워드\t: {yt.keywords}\n')
    print(f'* 영상 설명\n\n{yt.description}')
    print(f'==================================================================')

    """incoding 처리"""
    video_streams = yt.streams.filter(file_extension='mp4').get_by_itag(22)
    print(video_streams)

    """저장 폴더 생성"""
    if not os.path.exists('youtube_download'):
        os.mkdir("youtube_download")
    else:
        pass

    title = yt.title

    Special_char = '\/:*?"<>|.'
    for c in Special_char:
        if c in title:
            title = title.replace(c, '')
    print(title)

    video_streams.download(filename=title + '.mp4',
                           output_path='youtube_download')

    print('영상 다운로드 완료')
    os.system("pause")

youtube_download(yt_url)
