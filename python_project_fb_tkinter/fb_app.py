import tkinter as tk
from tkinter import messagebox
import sqlite3


class App:
    admin = {
        'admin': '1234'
    }

    # to do replace with db users
    user = {
        'user1': '1234',
        'user2': '1234'
    }

    def __init__(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.frame.grid()
        self.create_login_view()
        self.root.mainloop()

    def create_login_view(self):
        def perform_login():
            self.perform_login(username_field.get(), password_field.get())

        self.clear_screen()
        tk.Label(self.frame, text='Welcome.\n\nPlease log in!\n').grid(row=0)
        tk.Label(self.frame, text='Username').grid(row=2, column=0)
        tk.Label(self.frame, text='Password').grid(row=3, column=0)
        username_field = tk.Entry(self.frame)
        username_field.grid(row=2, column=1)
        password_field = tk.Entry(self.frame)
        password_field.grid(row=3, column=1)
        tk.Button(self.frame,
                  text='Login',
                  command=perform_login).grid(row=4, column=1)

    def perform_login(self, username, password):
        if username in self.admin.keys() and self.admin[username] == password:
            print("logged in as admin")
            self.create_admin_view()

        elif username in self.user.keys() and self.user[username] == password:
            print("logged in as user")
            self.create_user_view()

    def create_admin_view(self):
        self.clear_screen()
        tk.Button(self.frame, text='Add user', command=self.admin_add_user_view).grid(row=0, column=0)
        tk.Button(self.frame, text='Update user', command=self.admin_update_user_view).grid(row=1, column=0)
        tk.Button(self.frame, text='Delete user', command=self.admin_delete_user_view).grid(row=2, column=0)
        tk.Button(self.frame, text='Show all users', command=self.admin_show_all_users).grid(row=3, column=0)
        tk.Button(self.frame, text='See user posts').grid(row=4, column=0)
        tk.Button(self.frame, text='Logout', command=self.create_login_view).grid(row=5, column=0)

    def admin_add_user_view(self):
        def post_user():
            query = f'INSERT INTO users VALUES("{username_field.get()}","{password_field.get()}")'
            self.perform_db_query(query)
            messagebox.showinfo("New user info", f"User: {username_field.get()} was added correctly")
            self.create_admin_view()

        self.clear_screen()
        tk.Label(self.frame, text='Username').grid(row=2, column=0)
        tk.Label(self.frame, text='Password').grid(row=3, column=0)
        username_field = tk.Entry(self.frame)
        username_field.grid(row=2, column=1)
        password_field = tk.Entry(self.frame)
        password_field.grid(row=3, column=1)
        tk.Button(self.frame,
                  text='Create user',
                  command=post_user).grid(row=4, column=1)

    def admin_update_user_view(self):
        self.clear_screen()

        def load_user_data():
            def update_user():
                query2 = f'''UPDATE 
                                users 
                            SET 
                                name = "{username_field.get()}", 
                                password = "{password_field.get()}"
                            WHERE 
                                rowid = "{rowid}"'''
                self.perform_db_query(query2)
                messagebox.showinfo("New user info", f"User with id: {rowid} was updated correctly")
                self.create_admin_view()

            query = f'SELECT * FROM users WHERE rowid = {id_field.get()}'
            print(query)
            rowid = id_field.get()
            user = self.perform_db_query_and_return_data(query)
            self.clear_screen()
            tk.Label(self.frame, text='Username').grid(row=2, column=0)
            tk.Label(self.frame, text='Password').grid(row=3, column=0)
            username_field = tk.Entry(self.frame)
            username_field.insert(0, user[0][0])
            username_field.grid(row=2, column=1)
            password_field = tk.Entry(self.frame)
            password_field.insert(0, user[0][1])
            password_field.grid(row=3, column=1)
            tk.Button(self.frame,
                      text='Update user',
                      command=update_user).grid(row=4, column=1)

        id_field = tk.Entry(self.frame)
        id_field.grid(row=0, column=0)
        tk.Button(self.frame,
                  text='Load user',
                  command=load_user_data).grid(row=1, column=0)

    def admin_delete_user_view(self):
        self.clear_screen()

        def delete_user():
            query = f'DELETE FROM users WHERE rowid = {id_field.get()}'
            print(query)
            self.perform_db_query(query)
            messagebox.showinfo("New user info", f"User with id: {id_field.get()} was deleted correctly")
            self.create_admin_view()

        id_field = tk.Entry(self.frame)
        id_field.grid(row=0, column=0)
        tk.Button(self.frame,
                  text='Delete user',
                  command=delete_user).grid(row=1, column=0)

    def admin_show_all_users(self):
        self.clear_screen()

        tk.Label(self.frame, text='ID').grid(row=0, column=0)
        tk.Label(self.frame, text='Username').grid(row=0, column=1)
        tk.Label(self.frame, text='Password').grid(row=0, column=2)

        row_num = 1
        query = 'SELECT rowid, name, password FROM users;'
        all_users = self.perform_db_query_and_return_data(query)

        for user in all_users:
            tk.Label(self.frame, text=str(user[0])).grid(row=row_num, column=0)
            tk.Label(self.frame, text=str(user[1])).grid(row=row_num, column=1)
            tk.Label(self.frame, text=str(user[2])).grid(row=row_num, column=2)
            row_num += 1

        tk.Button(self.frame, text='Back to admin menu', command=self.create_admin_view).grid(row=row_num+1)

    # to do
    def admin_show_user_posts(self):

        # to do
        # to do
        # to do
        # to do
        # to do
        # to do
        # to do
        self.clear_screen()

        def show_user_posts():
            query = f'SELECT * FROM users WHERE rowid = {id_field.get()}'
            print(query)
            self.perform_db_query(query)
            messagebox.showinfo("New user info", f"User with id: {id_field.get()} was deleted correctly")
            self.create_admin_view()

        id_field = tk.Entry(self.frame)
        id_field.grid(row=0, column=0)
        tk.Button(self.frame,
                  text='Show user posts',
                  command=show_user_posts).grid(row=1, column=0)

    # to do
    def create_user_view(self):
        self.clear_screen()
        tk.Button(self.frame, text='Dodaj post').grid(row=0, column=0)
        tk.Button(self.frame, text='Zobacz wszystkie posty').grid(row=1, column=0)
        tk.Button(self.frame, text='Wyloguj', command=self.create_login_view).grid(row=2, column=0)

    def clear_screen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def perform_db_query(self, query):
        conn = sqlite3.connect('facebook.db')
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        conn.close()

    def perform_db_query_and_return_data(self, query):
        conn = sqlite3.connect('facebook.db')
        c = conn.cursor()
        c.execute(query)
        all_data = c.fetchall()
        conn.commit()
        conn.close()
        return all_data


def main():
    app = App()


main()
