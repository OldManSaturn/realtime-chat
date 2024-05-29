from flet import Column, TextField, ElevatedButton, Text

def chat_view():
    messages = Column()
    input_field = TextField(hint_text="Type a message")
    send_button = ElevatedButton("Send", on_click=lambda _: send_message(input_field, messages))

    return Column(controls=[messages, input_field, send_button])

def send_message(input_field, messages):
    message_content = input_field.value
    if message_content:
        messages.controls.append(Text(message_content))
        input_field.value = ""
        input_field.update()
