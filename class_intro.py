
# examples of OOP 

# 1. Building an restaurant

class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"This is restaurant is called {self.restaurant_name}.")
		return (f"It serves {self.cuisine_type} food!")

	def open_restaurant(self):
		return (f"{self.restaurant_name} is now open!")

	def set_customers_served(self, num):
		self.number_served = num

	def increment_number_served():
		self.number_served += 100

	def customers_served(self):
		return (f"{self.restaurant_name} has served {self.number_served} customers.")

indian_restaurant = Restaurant("Paradise Biryani", "indian")
italian_restaurant = Restaurant("Fettecini", "italian")
chinese_restaurant = Restaurant("Golden Dragon", "chinese")

print(chinese_restaurant.describe_restaurant())
print(italian_restaurant.describe_restaurant())
indian_restaurant.describe_restaurant()
print(chinese_restaurant.customers_served())
chinese_restaurant.set_customers_served(20)
print(chinese_restaurant.customers_served())

# 2. OOP with Users

class User:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
		self.password = "secret"

	def describe_user(self):
		user_info = {
			"first_name": self.first_name, 
			"last_name": self.last_name,
			"password": self.password
		}

		print(user_info)

	def greet_user(self):
		print (f"Hey there {self.first_name} {self.last_name}!")

	def num_login_attempts(self):
		return self.login_attempts

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

praneeth = User("Praneeth", "Chandu")
madhu = User("Madhavi", "Chandu")
srini = User("Srinivasa", "Chandu")
rohith = User("Rohith", "Chandu")

print()
praneeth.describe_user()
praneeth.greet_user()
madhu.describe_user()
madhu.greet_user()
srini.describe_user()
srini.greet_user()
rohith.describe_user()
rohith.greet_user()
print()

praneeth.increment_login_attempts()
praneeth.increment_login_attempts()
praneeth.increment_login_attempts()
praneeth.increment_login_attempts()
praneeth.increment_login_attempts()
print(praneeth.num_login_attempts())
praneeth.reset_login_attempts()
print(praneeth.num_login_attempts())
print()

# 3. Inheritance with an ice cream stand

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type, flavors):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def show_flavors(self):
		print(self.flavors)

ritas = IceCreamStand("ritas", "ice cream", ["vanilla", "sorbet", "chocolate"])
ritas.describe_restaurant();
ritas.show_flavors()
print()

# 4. Inheritance with a user admin

class Admin(User):
	def __init__(self, first_name, last_name, privileges):
		super().__init__(first_name, last_name)
		self.privileges = Priviliges(privileges)


class Priviliges:
	def __init__(self, privileges):
		self.privileges = privileges

	def show_privileges(self):
		print("This admin's privileges include: ")
		for privilege in self.privileges:
			print(f"\t{privilege}")

admin = Admin("admin", "user", ["can update posts", "can delete posts", "can shut down service"])
admin.privileges.show_privileges()
