class ShoppingCart:

    def __init__(self, items):
        self.items = items
        
    def add_item(self,item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed.")
        else:
            print(f"{item} not found.")

    def show(self):
        for i in self.items:
            print(i)

cart = ShoppingCart(['Apple','Banana','Cherry'])

cart.add_item('Mango')
cart.remove_item('Banana')
cart.show()