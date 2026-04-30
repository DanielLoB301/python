# Simulación de proveedor externo
class ExternalPaymentAPI:
    def send_payment(self, amount: float):
        return {"status": "ok", "amount": amount}


# Adapter que adapta la interfaz externa a la interna
class PaymentAdapter:
    def __init__(self, external_api: ExternalPaymentAPI):
        self.external_api = external_api

    def pay(self, amount: float) -> bool:
        response = self.external_api.send_payment(amount)
        return response["status"] == "ok"