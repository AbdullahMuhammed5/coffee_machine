class CoffeeMachine:
    machine_data = {
      "water": 400,
      "milk": 540,
      "coffee_beans": 120,
      "disposal_cups": 9,
      "money": 550
    }

    menu = {
      '1': {
        "name": "espresso",
        "water": 250,
        "milk": 0,
        "beans": 16,
        "price": 4
      },
      '2': {
        "name": "latte",
        "water": 350,
        "milk": 75,
        "beans": 20,
        "price": 7
      },
      '3': {
        "name": "cappuccino",
        "water": 200,
        "milk": 100,
        "beans": 12,
        "price": 6
      },
    }

    def print_banner(self, data):
      print("""The coffee machine has:
        {} of water
        {} of milk
        {} of coffee beans
        {} of disposable cups
        ${} of money"""
        .format(data['water'], data['milk'], data['coffee_beans'], data['disposal_cups'], data['money']))

    def buy(self, order_id):
      # case failure order
      if self.machine_data['water'] < self.menu[order_id]["water"]:
         return "Sorry, not enough water!"
      elif self.machine_data['milk'] < self.menu[order_id]["milk"]:
        return "Sorry, not enough milk!"
      elif self.machine_data['coffee_beans'] < self.menu[order_id]["beans"]:
        return "Sorry, not enough coffee beans!"
      elif self.machine_data['disposal_cups'] < 1:
        return "Sorry, not enough disposable cups!"

      # case success order
      self.machine_data['water'] -= self.menu[order_id]["water"]
      self.machine_data['milk'] -= self.menu[order_id]["milk"]
      self.machine_data['coffee_beans'] -= self.menu[order_id]["beans"]

      self.machine_data['money'] += self.menu[order_id]["price"]
      self.machine_data['disposal_cups'] -=1

      return "I have enough resources, making you a coffee!"

    def fill(self):
      self.machine_data['water'] += int(input("Write how many ml of water do you want to add: "))
      self.machine_data['milk'] += int(input("Write how many ml of milk do you want to add: "))
      self.machine_data['coffee_beans'] += int(input("Write how many grams of coffee beans do you want to add: "))
      self.machine_data['disposal_cups'] += int(input("Write how many disposable cups of coffee do you want to add: "))

    def take(self):
      print("I gave you ${}".format(self.machine_data['money']))
      self.machine_data["money"] = 0

    def get_order(self, machine_input):
      if machine_input == "remaining":
        self.print_banner(self.machine_data)
      elif machine_input == "buy":
        order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")
        if order == 'back':
          return True
        print(self.buy(order))
      elif machine_input == "fill":
        self.fill()
      elif machine_input == "take":
        self.take()
      elif machine_input == "exit":
        return False

      return True


coffee_machine = CoffeeMachine()

working = True

while working:
  machine_input = input("Write action (buy, fill, take, remaining, exit): \n")
  working = coffee_machine.get_order(machine_input)


