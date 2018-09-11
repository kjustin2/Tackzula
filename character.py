class Character:
    __name = ""
    __health = 10
    __progress = 0
    __stamina = 10
    __max_health = 10
    __max_stamina = 10
    __rest_up = 6

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, change):
        self.__name = change

    def get_health(self):
        return self.__health

    def set_health(self, change):
        self.__health = change

    def minus_health(self, change):
        self.__health = self.__health - change
        if self.__health < 0:
            self.__health = 0
        if self.__health > self.__max_health:
            self.__health = self.__max_health

    def get_progress(self):
        return self.__progress

    def set_progress(self, num):
        self.__progress = num

    def plus_progress(self):
        self.__progress += 1

    def get_stamina(self):
        return self.__stamina

    def minus_stamina(self, change):
        self.__stamina = self.__stamina - change
        if self.__stamina < 0:
            self.__stamina = 0
        if self.__stamina > self.__max_stamina:
            self.__stamina = self.__max_stamina

    def set_stamina(self, change):
        self.__stamina = change

    def get_max_health(self):
        return self.__max_health

    def get_max_stamina(self):
        return self.__max_stamina

    def plus_max_health(self, change):
        self.__max_health += change

    def set_max_health(self, change):
        self.__max_health = change

    def plus_max_stamina(self, change):
        self.__max_stamina += change

    def set_max_stamina(self, change):
        self.__max_stamina = change

    def plus_rest_up(self, change):
        self.__rest_up += change

    def get_rest_up(self):
        return self.__rest_up

    def set_rest_up(self, change):
        self.__rest_up = change