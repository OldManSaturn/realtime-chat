import flet as ft
from chat.views import chat_view
import asyncio

def main(page: ft.Page):
    page.title = "Real-Time Chat App"
    page.add(chat_view())

ft.app(target=main)
