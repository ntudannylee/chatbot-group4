from sql import DB_function

class history:
    def __init__(self):
        self.db_func = DB_function()

    def get_history(self, user_id):
        res = self.db_func.DB_query('SELECT recently FROM user_info WHERE ID=\'' + user_id + '\'')
        if (res[0] is not None):
            history = res[0].split(' ')
            return history
        return None

    def add_history(self, user_id, restaurant_name):
        counter = self.db_func.DB_query('SELECT counter FROM user_info WHERE ID=\'' + user_id + '\'')
        res = self.db_func.DB_query('SELECT recently FROM user_info WHERE ID=\'' + user_id + '\'')
        if (res[0] is not None):
            history = res[0].split(' ')
            if (restaurant_name not in history):
                history[counter] = restaurant_name
                put_back = ''
                for i in range(len(history)):
                    put_back += history[i]
                counter = (counter + 1) % 10
                self.db_func.DB_insert('UPDATE user_info SET recently=\'' + put_back + '\' WHERE ID=\'' + user_id + '\';')
                self.db_func.DB_insert('UPDATE user_info SET counter=\'' + counter + '\' WHERE ID=\'' + user_id + '\';')
                self.db_func.DB_commit()
        else:
            print(restaurant_name)
            self.db_func.DB_insert('UPDATE user_info SET recently=\'' + restaurant_name + '\' WHERE ID=\'' + user_id + '\';')
            self.db_func.DB_commit()