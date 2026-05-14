class FakeNotifier:
    def __init__(self):
        self.messages = []

    def notify(self, message: str):
        self.messages.append(message)