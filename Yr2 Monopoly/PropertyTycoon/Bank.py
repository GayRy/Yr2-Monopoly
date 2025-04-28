class bank_creations:
    def __init__(self, banker_name, money):
        self.banker_name = banker_name
        self.money = money
        self.set_banker(banker_name)


    def reduce_banks_money(self, balance, token):
        print("Banker:", self.banker_name, " please give", token.player, balance)
        print(self.banker_name, " has removed", balance)
        if self.money < balance:
            self.generate_money()
        self.money -= balance

    def generate_money(self):
        self.money += 50000

    def add_bank_money(self, balance, token):
        print("Banker:", self.banker_name, " please take money from", token.player, balance)
        print(self.banker_name, " has removed", balance)
        self.money += balance
        print(self.money)


    def bank_balance(self):
        return self.money

    def set_banker(self,name):
        self.banker_name = name

    def get_banker(self):
        return self




