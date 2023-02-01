import json

import youtube_dl


def _dict_to_json(data):
    return json.dumps(data, indent=4, ensure_ascii=False)


def save_to_json(filename, data):
    with open(f'{filename}.json', 'w') as file:
        file.write(_dict_to_json(data))


ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    yt_info = ydl.extract_info(
        'https://www.youtube.com/watch?v=wBL3P1XcQrU',
        download=False
    )
    save_to_json('ytl-info', yt_info)
