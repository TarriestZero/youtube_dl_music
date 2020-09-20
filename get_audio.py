import pafy
import youtube_dl
from pydub import AudioSegment
import sys
import os


def get_audio_from_url(url):    # Достаем аудио из ютуба
    song = ''
    if url[len(url)-1] == '\n':
        song = pafy.new(url[:len(url)-1]).getbestaudio()
    else:
        song = pafy.new(url).getbestaudio()
    song.download()
    return song.filename


def convert(name):  # Конвертируем и экспортируем
    music = AudioSegment.from_file(name)
    music.export('songs/' + name[:(len(name)-4)] + 'mp3', format="mp3")


def file_worker():  # чтение из файла url
    handler = open('queue.txt','r+')
    buf = handler.readlines()
    handler.seek(0) # Перемещаем указатель на 0 символ
    return buf, handler


def del_in_file(buf, del_line, handler): # Перезапись файла
    for line in buf:
        if line != del_line:
            handler.write(line)
    handler.truncate()
    handler.seek(0)


if __name__ == "__main__":
    buf, filee = file_worker()
    counter = 0
    for line in buf:
        name = get_audio_from_url(line)
        convert(name)

        # далее удаление
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), name)
        os.remove(path)
        del_in_file(buf, line, filee)
        buf[counter] = ''
        counter += 1
    filee.close()
        
        



# Добавить установку в директорию