import sqlite3

class Database_Access:
    def __init__(self, database_name):
        self.sqliteConnection = sqlite3.connect(database_name)
        self.crsr = self.sqliteConnection.cursor()

    def execute_command(self, sql_command):
        self.crsr.execute(sql_command)

    def commit_connection(self):
        self.sqliteConnection.commit()

    def close_connection(self):
        self.sqliteConnection.close()

    def commit_close(self):
        self.commit_connection()
        self.close_connection()



class Login_Interfaces:
    def __init__(self, database_name):
        self.database_access = Database_Access(database_name)
        self.database_access.execute_command("create table if not exists Logins (username VARCHAR(25) PRIMARY KEY, password VARCHAR(100));")
        self.login_status = False

    def create_login_cmd(self):
        username_check = False
        while not username_check:
            try:
                username = input("Enter your username: ")
                username_2 = input("Confirm your username: ")

                if not username:
                    print("PLEASE ENTER A USERNAME.")
                elif username == username_2:
                    print("USERNAME VERIFICATION PASSED!")
                elif username != username_2:
                    print("USERNAMES DO NOT MATCH! PLEASE TRY AGAIN.")

            except Exception as e:
                print("SORRY. AN ERROR HAS OCCURRED. PLEASE TRY AGAIN.")
                print(e)

            else:
                username_check = True


        password_check = False
        while not password_check:
            try:
                password = input("Enter your password: ")
                password_2 = input("Confirm your password: ")

                if not password:
                    print("PLEASE ENTER A PASSWORD.")
                elif password == password_2:
                    print("PASSWORD VERIFICATION PASSED!")
                elif password != password_2:
                    print("PASSWORDS DO NOT MATCH! PLEASE TRY AGAIN.")

            except Exception as e:
                print("SORRY. AN ERROR HAS OCCURRED. PLEASE TRY AGAIN.")
                print(e)

            else:
                password_check = True

        self.database_access.crsr.execute("SELECT * FROM Logins WHERE username = ?", (username,))
        logins = self.database_access.crsr.fetchall()

        if not logins:
            self.database_access.crsr.execute("INSERT INTO Logins('username', 'password') VALUES(?,?)", (username, password))

        self.database_access.commit_connection()

    def login_cmd(self):
        username_check = False
        while not username_check:
            try:
                username = input("Enter your username: ")

            except Exception as e:
                print("SORRY. AN ERROR HAS OCCURRED. PLEASE TRY AGAIN.")
                print(e)

            else:
                username_check = True

        password_check = False
        while not password_check:
            try:
                password = input("Enter your password: ")

            except Exception as e:
                print("SORRY. AN ERROR HAS OCCURRED. PLEASE TRY AGAIN.")
                print(e)

            else:
                password_check = True

        self.database_access.crsr.execute("SELECT * FROM Logins WHERE username = ?", (username,))
        logins = self.database_access.crsr.fetchall()

        if not logins:
            print("USERNAME NOT FOUND.")
        elif (logins[0][0] == username) and (logins[0][1] == password):
            print(f"Login Success: Welcome {logins[0][0]}")
            self.login_status = True

    def delete_login_cmd(self):
        username_check = False
        while not username_check:
            try:
                username = input("Enter the username of the login that you want to delete: ")

            except Exception as e:
                print("SORRY. AN ERROR HAS OCCURRED. PLEASE TRY AGAIN.")
                print(e)

            else:
                username_check = True

        self.database_access.crsr.execute("DELETE FROM Logins WHERE username = ?", (username,))
        self.database_access.commit_connection()

    def create_login_gui(self, username, password):
        self.database_access.crsr.execute("SELECT * FROM Logins WHERE username = ?", (username,))
        logins = self.database_access.crsr.fetchall()

        if not logins:
            self.database_access.crsr.execute("INSERT INTO Logins('username', 'password') VALUES(?,?)", (username, password))

        self.database_access.commit_connection()

    def login_gui_bool(self, username, password):
        self.database_access.crsr.execute("SELECT * FROM Logins WHERE username = ?", (username,))
        logins = self.database_access.crsr.fetchall()

        if not logins:
            return False
        elif (logins[0][0] == username) and (logins[0][1] == password):
            return True
            self.login_status = True


if __name__ == "__main__":
    valid_runtime = False
    while not valid_runtime:
        try:
            correct_option = False
            while not correct_option:
                login_1 = Login_Interfaces(database_name="logins.db")
                option = int(input("Enter Option, 1: Create Login, 2: Login, 3: Delete Login; "))
                if option == 1:
                    login_1.create_login_cmd()
                    correct_option = True
                elif option == 2:
                    login_1.login_cmd()
                    correct_option = True
                elif option == 3:
                    login_1.delete_login_cmd()
                    correct_option = True
                else:
                    print("ERROR: Incorrect option, please pick between the options given.")

        except Exception as e:
            print(e)

        else:
            login_1.database_access.close_connection()
            valid_runtime = True