import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)  # Хеширование пароля
        self.age = age

    def hash_password(self, password):
        # Хеширование пароля с помощью SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

    def __eq__(self, other):
        # Перегрузка метода сравнения, чтобы проверять пользователя по имени пользователя
        return self.nickname == other.nickname

    def __str__(self):
        return f"{self.nickname}"


class Video:
    def __init__(self, title, duration, adult_mode=False):
        # title - заголовок
        self.title = title
        # duration - продолжительность
        self.duration = duration
        # time_now - секунда остановки
        self.time_now = 0
        # adult_mode - ограничение по возрасту, False
        self.adult_mode = adult_mode

    def __eq__(self, other):
        # Перегрузка метода для проверки видео по заголовку
        return self.title.lower() == other.title.lower()

    def __str__(self):
        return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"


class UrTube:
    def __init__(self):
        # users - список пользователей
        self.users = []  #Список зарегистрированных пользователей
        # videos - список видео
        self.videos = []  #Список доступных видео
        # current_user - текущий пользователь
        self.current_user = None

    def log_in(self, nickname, password):
        # Проверка пользователя с указанным логином и паролем
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                # Если пользователь существует, то current_user меняется на найденного
                self.current_user = user
                print(f"Пользователь {nickname} вошёл в систему.")
                return True
        print("Ошибка входа: неверный логин или пароль.")
        return False

    # Метод register добавляет пользователя в список, если такого не существует
    def register(self, nickname, password, age):
        # Регистрация пользователя и автоматический  вход
        new_user = User(nickname, password, age)
        if new_user in self.users:
            # Если пользователь с таким же nickname существует
            print(f"Пользователь {nickname} уже существует.")
        else:
            self.users.append(new_user)
            self.current_user = new_user

    # Метод log_out используется для выхода из "аккаунта"
    def log_out(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы.")
            self.current_user = None
        else:
            print("В системе нет активного пользователя.")

    # Метод add добавляет еще не существующие видео
    # Если название существует, то ничего не происходит
    def add(self, *videos):
        for video in videos:
            # Если с таким же названием видео ещё не существует:
            if video not in self.videos:
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")
            else:
                print(f"Видео '{video.title}' уже существует.")

    # Метод get_videos принимает поисковое слово и возвращает список названий с ним
    def get_videos(self, search_term):
        # Перевод поискового запроса в нижний регистр.
        search_term_lower = search_term.lower()
        # Поисковый запрос, представленный в нижнем регистре
        # сравнивается с заголовком видео в нижнем регистре
        return [video.title for video in self.videos if search_term_lower in video.title.lower()]

    # Метод watch_video принимает название по точному совпадению
    def watch_video(self, title):
        # Воспроизводит видео, если пользователь вошёл в систему и имеет право на просмотр
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=' ', flush=True)
                    time.sleep(1)  # Имитируем просмотр по одной секунде
                print("Конец видео")
                video.time_now = 0  # Сбрасываем время остановки после полного просмотра
                return


# Код для проверки
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
# Вывод: ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))
# Вывод: ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
# Вывод: Войдите в аккаунт, чтобы смотреть видео
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
# Вывод: Вам нет 18 лет, пожалуйста покиньте страницу
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Вывод: 1 2 3 4 5 6 7 8 9 10 Конец видео

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# Вывод: Пользователь vasya_pupkin уже существует
print(ur.current_user)
# Вывод: urban_pythonist

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
# Вывод: Видео не найдено
