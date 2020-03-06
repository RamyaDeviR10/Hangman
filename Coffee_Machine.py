class Coffee_Machine():
	def __init__(self):
		self.water = 400
		self.milk = 540
		self.coffee_beans = 120
		self.cups = 9
		self.cash = 550

	def remaining(self):
		print("The coffee machine has:")
		print("{} of water".format(self.water))
		print("{} of milk".format(self.milk))
		print("{} of coffee beans".format(self.coffee_beans))
		print("{} of disposable cups".format(self.cups))
		print("{} of money""".format(self.cash))

	def take(self):
		print("I gave you {}".format(self.cash))		    
		self.cash=0

	def fill(self,water,milk,coffee_beans,cups):
		self.water+=water
		self.milk+=milk
		self.coffee_beans+=coffee_beans
		self.cups+=cups

	def buy(self):
		print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
		option=input()
		if option=='1':
		  	if self.water>=250 and self.coffee_beans>=16:
		  		self.water-=250
		  		self.coffee_beans-=16
		  		self.cups-=1
		  		self.cash+=4
		  		print("I have enough resources, making you a coffee!")
		  	else:
		  		print("it can't make a cup of coffee")

		elif option=='2':
		   	if self.water>=350 and self.milk>=75 and self.coffee_beans>=20:
		   		self.water-=350
		   		self.milk-=75
		   		self.coffee_beans-=20
		   		self.cups-=1
		   		self.cash+=7
		   		print("I have enough resources, making you a coffee!")

		elif option=='3':
		   	if self.water>=200 and self.milk>=100 and self.coffee_beans>=12:
		   		self.water-=200
		   		self.milk-=100
		   		self.coffee_beans-=12
		   		self.cash+=6
		   		self.cups-=1
		   		print("I have enough resources, making you a coffee!")
		   	else:
		   		print("it can't make a cup of coffee")

		elif option=='back':
			pass

		
def main():
	coffee_obj=Coffee_Machine()
	action=None
	while(action!='exit'):		
		print("Write action (buy, fill, take,remaining, exit):")
		action=input()
		print()

		if action == 'buy':
			coffee_obj.buy()		        
		    
		elif action=='fill':    
		    print("Write how many ml of water do you want to add:")
		    water=int(input())
		    print("Write how many ml of milk do you want to add:")
		    milk=int(input())
		    print("Write how many grams of coffee beans do you want to add:")
		    coffee_beans=int(input())
		    print("Write how many disposable cups of coffee do you want to add:")
		    cups=int(input())
		    coffee_obj.fill(water,milk,coffee_beans,cups)

		elif action=='take':
			coffee_obj.take()
		    
		elif action=='remaining':
			coffee_obj.remaining()
		print()



if __name__ == '__main__':
	main()


