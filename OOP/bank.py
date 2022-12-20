class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 1000

    def get_balance(self):
        return self.balance

    def withdrawl(self,amount):
        if amount< self.min_withdraw:
            return f'no money for you. Minimum withdraw limit: {self.min_withdraw}'
        elif amount > self.max_withdraw:
            return f'You crossed max limit: {self.max_withdraw}'
        elif amount>self.balance:
            return 'you are a brokie'
        else:
            self.balance -= amount
            return f'Heere is your money: {amount}'

my_bank = Bank(8000)

reply = my_bank.withdrawl(800)

print(reply)