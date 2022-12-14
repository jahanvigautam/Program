from tkinter import *

root = Tk()
root.title("Chat Bot GUI")
root.geometry("500x500")
root.resizable(width = FALSE, height = FALSE)

# Main Menu
main_menu = Menu(root)

# Sub-menu
file_menu = Menu(root)

# Commands
file_menu.add_command(label = 'New..')
file_menu.add_command(label = 'Save As..')
file_menu.add_command(label = 'Exit')
file_menu.add_cascade(label = 'File', menu = file_menu)

main_menu.add_command(label = 'Edit')
main_menu.add_command(label = 'Quit')
root.config(menu = main_menu)

chatWindow = Text(root, bd = 1, bg = 'black', width = '50', height = '8', font = ('Arial', 23), foreground = '#00ffff')
chatWindow.place(x = 6, y = 6, height = 385, width = 370)

messageWindow = Text(root, bd = 0, bg = 'black', width = '30', height = '4', font = ('Arial', 23), foreground = '#00ffff')
messageWindow.place(x = 128, y = 400, height = 88, width = 260)

scrollbar = Scrollbar(root, command = chatWindow.yview, cursor = 'star')
scrollbar.place(x = 375, y = 5, height = 385)

Button = Button(root, text = 'Send', width = '12', height = 5, bd = 0, bg = '#0080ff', activebackground = '#00bfff', foreground = '#ffffff', font = ('Arial', 12))
Button.place(x = 6, y = 400, height = 88)

root.mainloop()