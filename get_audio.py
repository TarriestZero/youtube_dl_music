import pafy
import youtube_dl
from pydub import AudioSegment
import sys
import os


def get_audio_from_url(url):    # Достаем аудио из ютуба
    song = pafy.new(url).getbestaudio()
    song.download()
    return song.filename


def convert(name):  # Конвертируем и экспортируем
    music = AudioSegment.from_file(name)
    music.export('songs/' + name[:(len(name)-4)] + 'mp3', format="mp3")


if __name__ == "__main__":
    name = get_audio_from_url(sys.argv[1])
    convert(name)
    # далее удаление
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), name)
    os.remove(path)


# Добавить установку в директорию