import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


    def __hash__(self):
        return hash(self.password)

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = []
        self.videos = []
        self.current_user = current_user


    def register(self, nickname, password, age):
        if nickname not in self.users:
            self.users.append(nickname)
        else:
            print(f'Пользователь {nickname} уже существует')


    def log_in(self, nickname, password):


    def log_out(self, current_user):


    def add(self, title):
        if title not in self.videos:
            self.videos.append(title)


    def get_videos(self):
        search_word = input('Введите название видео, которое Вы хотите найти: ')
        if search_word in self.videos:


    def watch_video(self, title):


if __name__ == 'main':
