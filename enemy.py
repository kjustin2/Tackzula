class Enemy:
    __name = ""
    __health = 0
    __damage = 0

    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get__damage(self):
        return self.__damage

    def change_health(self, change):
        self.__health = self.__health - change

    def change_damage(self, change):
        self.__damage = self.__damage - change
