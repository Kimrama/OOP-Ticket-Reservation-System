class Route:
    def __init__(self, train, reminder_list):
        self.__train = train
        self.__reminder_list = reminder_list

    def get_reminder_list(self):
        return self.__reminder_list

    def get_train(self):
        return self.__train