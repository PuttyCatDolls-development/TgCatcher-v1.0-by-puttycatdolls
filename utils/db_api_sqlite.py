import sqlite3


class BotDB:

    def __init__(self, file_name):
        '''Инициализация соединения с базой данных'''
        self.conn = sqlite3.connect(file_name)
        self.curr = self.conn.cursor()

    def message_exists(self, message_id):
        '''Проверяем есть ли сообщение в базе данных'''
        result = self.curr.execute("SELECT `id` FROM `messages` WHERE `message_id` = ?", (message_id,))
        return bool(len(result.fetchall()))

    def get_message_id(self, message_id):
        '''Получем id сообщения в базе по message_id в телеграмме'''
        result = self.curr.execute("SELECT `id` FROM `messages` WHERE `message_id` = ?", (message_id,))
        return result.fetchone()[0]

    def add_message(self, message_id):
        '''Добавляем сообщения в базу данных'''
        self.curr.execute("INSERT INTO `messages` (`message_id`) VALUES (?)", (message_id,))
        return self.conn.commit()

    def close(self):
        '''Закрытие соединение с базой данных'''
        self.conn.close()
