import tkinter as tk
from tkinter import messagebox
import sqlite3

 

class App:

 


    def __init__(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.frame.grid()
        #self.create_hello_world_view()
        self.create_main_menu_view()

 

    def create_hello_world_view(self):
        tk.Label(self.frame, text='Hello world!').grid(row=0,column=0)

 

    def create_main_menu_view(self):
        self.clear_screen()
        tk.Button(self.frame, text='Dodaj ksiazke', command=self.create_add_book_view).grid(row=0,column=0)
        tk.Button(self.frame, text='Zaktualizuj ksiazke', command=self.create_update_book_view).grid(row=1,column=0)
        tk.Button(self.frame, text='Usun ksiazke', command=self.create_delete_book_view).grid(row=2, column=0)
        tk.Button(self.frame, text='Pokaz wszystkie ksiazki').grid(row=3, column=0)

 

    def clear_screen(self):

 

        for widget in self.frame.winfo_children():
            widget.destroy()

 

    def create_add_book_view(self):

 

        def post_book():
            conn = sqlite3.connect('wypozyczalnia.db')
            c = conn.cursor()
            query = f'INSERT INTO ksiazki VALUES("{e.get()}","{tytul.get()}")'
            c.execute(query)
            conn.commit()
            conn.close()
            messagebox.showinfo('Tytul ramki', 'Ksiazka dodana pomyslnie')
            self.create_main_menu_view()
        
        self.clear_screen()
        tk.Label(self.frame, text='Autor').grid(row=0,column=0)
        e = tk.Entry(self.frame)
        e.grid(row=0, column=1)
        tk.Label(self.frame, text='Tytul').grid(row=1,column=0)
        tytul = tk.Entry(self.frame)
        tytul.grid(row=1,column=1)
        tk.Button(self.frame, text='Dodaj ksiazke', command=post_book).grid(row=2, column=1)

 

    def create_update_book_view(self):

 

        def update_book():
            conn = sqlite3.connect('wypozyczalnia.db')
            c = conn.cursor()
            attr = var.get()
            query = f'UPDATE ksiazki SET "{attr}"="{new_value.get()}" WHERE rowid = "{_id.get()}"'
            c.execute(query)
            conn.commit()
            conn.close()
            messagebox.showinfo('Tytul ramki', 'Ksiazka zmodyfikowana pomyslnie')
            self.create_main_menu_view()
            
            
        self.clear_screen()
        var = tk.StringVar()
        #I rzad
        tk.OptionMenu(self.frame, var, 'Tytul', 'Autor').grid(row=0, column=1)
        #II rzad
        tk.Label(self.frame, text='Podaj ID').grid(row=1, column=0)
        _id = tk.Entry(self.frame)
        _id.grid(row=1, column=1)
        #III rzad
        tk.Label(self.frame, text='Podaj nowa wartosc').grid(row=2, column=0)
        new_value = tk.Entry(self.frame)
        new_value.grid(row=2, column=1)
        #IV rzad
        tk.Button(self.frame, text='Zmodyfikuj', command=update_book).grid(row=3, column=1)

    def create_delete_book_view(self):

        def delete_book():
            conn = sqlite3.connect('wypozyczalnia.db')
            c = conn.cursor()
            attr = var.get()
            query = f'DELETE FROM ksiazki WHERE rowid = "{_id.get()}"'
            c.execute(query)
            conn.commit()
            conn.close()
            messagebox.showinfo('Tytul ramki', 'Ksiazka usunieta pomyslnie')
            self.create_main_menu_view()

        self.clear_screen()
        var = tk.StringVar()

        tk.Label(self.frame, text='Podaj ID').grid(row=0, column=0)
        _id = tk.Entry(self.frame)
        _id.grid(row=0, column=1)

        tk.Button(self.frame, text='Usun', command=delete_book).grid(row=2, column=1)
            

 

def main():
    app = App()

 


main()
