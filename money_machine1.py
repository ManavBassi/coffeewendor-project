class MoneyMachine:
    currency="$"
    coin_values={
        'quarters':0.25,
        'dimes':0.10,
        'nickles':0.05,
        'pennies':0.01
    }
    def __init__(self):
        self.profit=0
        self.money_received=0
    def report(self):
        print(f"Money: {self.currency}{self.profit}")
    def process_coins(self):
        print("please insert coins")
        for coin in  self.coin_values:
            self.money_received+=int(input(f"how many {coin}:"))* self.coin_values[coin]
        return self.money_received
    def make_payment(self,cost):
        self.process_coins()
        if self.money_received>=cost:
            change=round(self.money_received-cost,2)
            print(f"here is {self.currency}{change} in change.")
            self.profit+=cost
            self.money_received=0
            return True
        else:
            print("sorry that's not enough money, Money refunded.")
            self.money_received=0
            return False