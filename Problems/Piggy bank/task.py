class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        dollars = 1
        cents = 1

        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        if (self.cents + deposit_cents) > 99:
            temp_dollars = int((self.cents + deposit_cents) // 100)
            temp_cents = int((self.cents + deposit_cents) % 100)

            self.dollars += temp_dollars
            self.cents = temp_cents
        else:
            self.cents += deposit_cents


