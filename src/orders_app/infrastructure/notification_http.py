class HttpNotifier:
    def notify(self, message: str) -> None:
        print(f"Notificando vía HTTP: {message}")