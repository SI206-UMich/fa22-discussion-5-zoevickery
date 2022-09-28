import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for char in sentence:
		if char == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items#[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)
		return self.items
		pass

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		if len(self.items) == 0:
			return None
		max_item = None
		max_q = 0
		for item in self.items:
			if item.stock > max_q:
				max_q = item.stock
				max_item = item
		return max_item
		pass
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		if len(self.items) == 0:
			return None
		max_item = None
		max_price = 0
		for item in self.items:
			if item.price > max_price:
				max_price = item.price
				max_item = item
		return max_item
		pass	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("Water"), 1, "count_a(Water)")
		self.assertEqual(count_a("cider"), 0, "count_a(Cider)")
		self.assertEqual(count_a(""), 0, "count_a('')")
		pass


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		self.w =  Warehouse()
		self.w.add_item(self.item1)
		self.assertEqual(self.w.add_item(self.item2), self.w.items, "testing that item1 is added")
		pass


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		self.w = Warehouse()
		self.w.add_item(self.item1)
		self.w.add_item(self.item2)
		self.assertEqual(self.w.get_max_stock(), self.item2, "item2 has the most stock")
		pass


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.w = Warehouse()
		self.w.add_item(self.item1)
		self.w.add_item(self.item2)
		self.assertEqual(self.w.get_max_stock(), self.item1, "item1 has the highest price")
		pass
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()