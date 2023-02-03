import youtube_dl


# youtube-dl --write-auto-sub --write-sub --sub-lang en --sub-format srv3 --convert-subs=srt --skip-download "https://www.youtube.com/watch?v=1LV1K69885E" -o ./downloads/subs

YT_URL = 'https://www.youtube.com/watch?v=1LV1K69885E'
YTDL_OPTS = {
    'outtmpl': './downloads/%(channel_id)s_%(id)s.%(ext)s',
    'writeautomaticsub': True,
    'writesubtitles': True,
    # 'subtitleslangs': ['en'],
    # 'subtitlesformat': 'srv3',
    'skip_download': True
}


def extract_subtitle(
    url: str, sub_lang: str = 'en', sub_format: str = 'srv3'
) -> None:
    if not url:
        raise ValueError('Invalid url')

    YTDL_OPTS['subtitleslangs'] = [sub_lang]
    YTDL_OPTS['subtitlesformat'] = sub_format

    with youtube_dl.YoutubeDL(YTDL_OPTS) as ydl:
        ydl.download([url])


def main():
    extract_subtitle(YT_URL)


if __name__ == '__main__':
    main()
