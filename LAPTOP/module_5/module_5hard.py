import hashlib   # Импорт модуля хэширования паролей
import time   # Позволяет работать с временем, включая задержки выполнения программы.


class User:   # Класс User с атрибутами
    def __init__(self, nickname, password, age): #
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):   # Создает объект хэширования с использованием алгоритма
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)  #


class Video:  # Класс Видео с атрибутами
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:  # Класс UrTube
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):  # Обработка логики входа
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return
        print("Пользователь не найден или пароль неверен.")

    def register(self, nickname, password, age): # Обработка логики РЕГИСТРАЦИИ
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user  # Вход после регистрации

    def log_out(self):
        self.current_user = None    #Логика выхода

    def add(self, *videos): # Функция добавления видео
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, keyword): # выполняет задачу фильтрации видео по ключевому слову.
        return [video.title for video in self.videos if keyword.lower() in video.title.lower()]

    def watch_video(self, title):  # содержит проверку на то, вошел ли пользователь в аккаунт
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos: # Цикл проверки возраста
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                while video.time_now < video.duration:  # Цикл воспроизведения видео
                    print(video.time_now + 1)  # Показать каждую секунду
                    time.sleep(1)
                    video.time_now += 1

                print("Конец видео")
                return

        print("Видео не найдено")


# Код для проверки
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
