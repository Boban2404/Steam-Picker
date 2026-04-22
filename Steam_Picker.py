import customtkinter
import webbrowser

window = customtkinter.CTk()
window.geometry('600x200')
window.title('Steam Picker')
window.fg_color='#202326'

def background():
    def background_app_id():
        background_app_id = background_enter.get()
        webbrowser.open(f'https://steamcdn-a.akamaihd.net/steam/apps/{background_app_id}/library_hero.jpg')

    background = customtkinter.CTkFrame(master=window, fg_color='#202326', height=200, width=600)
    background.place(x=0, y=0)
    
    background_label = customtkinter.CTkLabel(master=background, text='enter app id', font=('arial', 30, 'bold'))
    background_label.place(x=198, y=20)

    background_enter = customtkinter.CTkEntry(master=background, height=30, width=200)
    background_enter.place(x=200, y=80)

    button3 = customtkinter.CTkButton(master=background, text='download', height=35, width=100, fg_color='#292C30', command=background_app_id)
    button3.place(x=250, y=120)

    button4 = customtkinter.CTkButton(master=background, text='back', height=30, width=35, fg_color='#292C30', command=menu)
    button4.place(x=275, y=160)

def logo():
    def logo_app_id():
        logo_app_id = logo_enter.get()
        webbrowser.open(f'https://steamcdn-a.akamaihd.net/steam/apps/{logo_app_id}/logo.png')

    logo_frame = customtkinter.CTkFrame(master=window, fg_color='#202326', height=200, width=600)
    logo_frame.place(x=0, y=0)
    
    logo_label = customtkinter.CTkLabel(master=logo_frame, text='enter app id', font=('arial', 30, 'bold'))
    logo_label.place(x=198, y=20)

    logo_enter = customtkinter.CTkEntry(master=logo_frame, height=30, width=200)
    logo_enter.place(x=200, y=80)

    button7 = customtkinter.CTkButton(master=logo_frame, text='download', height=35, width=100, fg_color='#292C30', command=logo_app_id)
    button7.place(x=250, y=120)

    button8 = customtkinter.CTkButton(master=logo_frame, text='back', height=30, width=35, fg_color='#292C30', command=menu)
    button8.place(x=275, y=160)

def cover_art():
    def cover_art_app_id():
        cover_art_app_id = cover_enter.get()
        webbrowser.open(f'https://steamcdn-a.akamaihd.net/steam/apps/{cover_art_app_id}/library_600x900_2x.jpg')

    cover_frame = customtkinter.CTkFrame(master=window, fg_color='#202326', height=200, width=600)
    cover_frame.place(x=0, y=0)

    cover_label = customtkinter.CTkLabel(master=cover_frame, text='enter app id', font=('arial', 30, 'bold'))
    cover_label.place(x=198, y=20)

    cover_enter = customtkinter.CTkEntry(master=cover_frame, height=30, width=200)
    cover_enter.place(x=200, y=80)

    button5 = customtkinter.CTkButton(master=cover_frame, text='download', height=35, width=100, fg_color='#292C30', command=cover_art_app_id)
    button5.place(x=250, y=120)

    button6 = customtkinter.CTkButton(master=cover_frame, text='back', height=30, width=35, fg_color='#292C30', command=menu)
    button6.place(x=275, y=160)

def menu():
    menu = customtkinter.CTkFrame(master=window, fg_color='#202326', height=200, width=600)
    menu.place(x=0, y=0)

    label_menu = customtkinter.CTkLabel(master=menu, text='Chose one', font=('arial', 35, 'bold'))
    label_menu.place(x=190, y=20)

    button = customtkinter.CTkButton(master=menu, text='Download Background', height=35, width=35, fg_color='#292C30', command=background)
    button.place(x=20, y=87.5)

    button1 = customtkinter.CTkButton(master=menu, text='Download Logo', height=35, width=35, fg_color='#292C30', command=logo)
    button1.place(x=230, y=87.5)

    button2 = customtkinter.CTkButton(master=menu, text='Download Game Cover', height=35, width=35, fg_color='#292C30', command=cover_art)
    button2.place(x=390,  y=87.5)
    
menu()

window.mainloop()
