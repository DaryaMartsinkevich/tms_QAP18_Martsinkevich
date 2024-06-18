class Cinema:
    def __init__(self, city, name, format):
        self.city: str = city
        self.name: str = name
        self.format: str = format


class TicketOffice(Cinema):
    def __init__(self, name_of_movie, genre, hall, time, places, tickets):
        super().__init__("Гродно", "Красная звезда", "3D")
        self.name_of_movie: str = name_of_movie
        self.genre: str = genre
        self.hall: int = hall
        self.time: float = time
        self.places: int = places
        self.tickets: int = tickets

    def addition_info(self):
        print(f"Название кинотеатра: {self.name}\n"
              f"Название фильма: {self.name_of_movie}\n"
              f"Жанр: {self.genre}\n"
              f"Начало фильма: {self.time}\n"
              f"Номер зала: {self.hall}")

    def deletion_info(self):
        print(f"Сеанс фильма {self.name_of_movie} отменен, по техническим причинам.")

    def replacement_info(self, new_name_of_movie, ):
        old_name_of_movie = self.name_of_movie
        self.name_of_movie = new_name_of_movie
        print(f"Фильм {old_name_of_movie} заменен на фильм {new_name_of_movie}.\n"
              f"Начало фильма: {self.time}\n"
              f"Номер зала: {self.hall}")

    def ticket_info(self, count):
        self.tickets -= count
        self.places -= count
        print(f"Осталось билетов: {self.tickets}\n"
              f"Свободных мест: {self.places}\n")

    def new_info(self, new_movie, genre, time, hall):
        self.name_of_movie = new_movie
        self.genre = genre
        self.time = time
        self.hall = hall
        print(f"Добавлен новый фильм: {new_movie}\n"
              f"Жанр: {self.genre}\n"
              f"Начало фильма: {self.time}\n"
              f"Номер зала: {self.hall}")


movie = TicketOffice("Аватар", "fantasy", 1, 10.15, 60, 60)
movie.addition_info()
movie.deletion_info()
movie.replacement_info("Легенды ночных стражей")
movie.ticket_info(15)
movie.new_info("Жизнь Пи", "adventure-drama", 15.15, 2)