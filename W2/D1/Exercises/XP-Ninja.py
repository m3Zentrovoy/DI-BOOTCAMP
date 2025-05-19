

class Phone:
    def __init__(self,phone_number):
        self.call_history = []
        self.messages = []
        self.phone_number = phone_number

    def call(self,other_phone):
        call_record = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_record)
        self.call_history.append(call_record)
       
    def show_call_history(self):
        print(self.call_history)

    def send_message(self, other_phone, content):
        message = {
            'to': other_phone.phone_number,
            'from': self.phone_number,
            'content': content}
        self.messages.append(message)

    def show_outgoing_messages(self):
        for message in self.messages:
            if message['from'] == self.phone_number:
                print(message)

    def show_incoming_messages(self):
        for message in self.messages:
            if message['to'] == self.phone_number:
                print(message)

    def show_messages_from(self,phone_number):
        for message in self.messages:
            if message ['from'] == phone_number:
                print(message)


# Тестируем код
phone1 = Phone("123")
phone2 = Phone("456")

# Тест звонков
phone1.call(phone2)
phone2.call(phone1)
phone1.show_call_history()
phone2.show_call_history()

# Тест сообщений
phone1.send_message(phone2, "Hello!")
phone2.send_message(phone1, "Hi!")
phone1.show_outgoing_messages()
phone2.show_incoming_messages()
phone2.show_messages_from("123")