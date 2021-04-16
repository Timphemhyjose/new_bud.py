class Budget:
    def __init__(self):
        self.entries = []
        self.main = ()

    def prompt(self, type):
        while True:
            more = input(f'Enter (y/n) {type}')
            if more == 'n':
                break

            value = int(input(f'Enter amount: {type} \n'))
            label = input(f'Enter name {type}')

            self.entries.append({
                'value': value if type == "income" else -value,
                'label': label
            })

    def main(self):
        self.prompt('income')
        self.prompt("expense")

        balance = sum(entry['value'] for entry in entries)
        self.print_balance_message(balance)

print(Budget.prompt(type= 'y'))