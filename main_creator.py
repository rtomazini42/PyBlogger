import creator
from tkinter import *
import os


new_window = Tk()
new_window.title("PyBlogger creator")
text_boas_vindas = Label(new_window,text="Welcome to PyBlogger Creator")
text_boas_vindas.grid(column = 1, row=1)

text_instructions = Label(new_window,text="Insert the name of the new Blogger")
text_instructions.grid(column = 1, row=2)
input_name_blog = Entry(new_window, width=100)
input_name_blog.grid(column = 1, row=3)


botao_criar = Button(new_window, text="Create a new Blog", command=lambda: creator.criar_blog(input_name_blog.get()))
botao_criar.grid(column=1, row=3)

new_window.mainloop()




