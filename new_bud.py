class Budget:
    def __init__(self, name):
        self.name = name
        self.balance = 5000
        self.expenditure = 0

    def deposit(self):
        amount = float(input("Enter the amount you want to deposit: \n"))
        if amount >= 1:
            self.balance += amount
            print(f"You have just deposited {amount :.2f} into {self.name} balance")
            print(f"Current balance: {self.balance :.2f}")
    def withdraw(self):
        amount = float(input("Enter the amount you want to withdraw: \n"))
        if amount > self.balance:
            print("insufficient funds")
        if amount <= self.balance:
            self.balance -= amount
            self.expenditure += amount
            print(f"You just withdrew {amount :.2f}")
            print(f"Your current balance: {self.balance :.2f}")
            print(f"Your expenditure: {self.expenditure :.2f}")

    def fund_transfer(self):
        category = input("Enter the category you want to transfer to: \n")
        transfer = float(input("Enter the amount you want to transfer: \n"))
        print(f"You have successfully transferred {transfer :.2f} to {category}")
        print("Transfer of funds = 0.00 expenditure")


    def get_balance(self):
        print(f"{self.name}    {self.balance :.2f}")
        return self.balance

class Food(Budget):
    def __init__(self):
        name = type(self).__name__
        super().__init__(name)

class Clothing(Budget):
    def __init__(self):
        name = type(self).__name__
        super().__init__(name)

class Entertainment(Budget):
    def __init__(self):
        name = type(self).__name__
        super().__init__(name)


food = Food()
food.withdraw()
print(food.withdraw())