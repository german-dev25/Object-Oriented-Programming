# класс Платежи (он же монетоприемник)
class Payments:
    def __init__(self):
        self.amount_paid: int = 0

    # добавляем монеты
    def insert_money(self, amount: int) -> int:
        self.amount_paid += amount
        return self.amount_paid

    # уменьшаем монеты
    def amount_reduce(self, amount: int) -> int:
        self.amount_paid -= amount
        return self.amount_paid

    # сброс
    def amount_reset(self) -> int:
        self.amount_paid = 0
        return self.amount_paid

    @property
    def get_amount(self) -> int:
        return self.amount_paid

    def __str__(self):
        return f'Монет: {self.amount_paid}'