import flet as ft 


def main(page: ft.Page):
    text_hello = ft.Text('Hello world')

    text_button = ft.TextButton('SEND')
    elevated_button = ft.ElevatedButton('send')
    icon_button = ft.IconButton(icon=ft.Icons.SEND)

    name_input = ft.TextField(label='Введите что-нибудь')

    # добавление на страницу
    page.add(text_hello, text_button, elevated_button, icon_button, name_input)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)