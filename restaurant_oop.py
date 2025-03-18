class Restaurant:
    def __init__(self, name, cuisine, served=0):
        self.name = name
        self.cuisine = cuisine
        self.served = served

    def desc(self):
        print(f"{self.name}, {self.cuisine}, {self.served}")

    def is_open(self):
        print("open")

    def been_served(self,served):
        if served >= 0:
            self.served = served
        else:
            print("can't be negative")

    def total_served(self,customer):
        if customer >= 0:
            self.served += customer
        else:
            print("can't be negative")    


class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine,flavours):
        super().__init__(name,cuisine)
        self.flavours = flavours

    def flavours_desc(self):
        print(f"Available flavors: {', '.join(self.flavours)}")



ice_cream_stand1 = IceCreamStand("Sweet Treats", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry", "Mango"])
ice_cream_stand1.flavours_desc()


# restaurant1 = Restaurant("Le Méridien", "Turkish delicacies",)
# restaurant2 = Restaurant("The Olive Tree", "Italian cuisine",)
# restaurant3 = Restaurant("Sushi World", "Japanese cuisine",)

# restaurant1.desc()
# restaurant2.desc()
# restaurant3.desc()

# restaurant1.been_served (1200)
# restaurant2.been_served (1500)
# restaurant3.been_served (1900)

# print("\nAfter updating customers served:")
# restaurant1.desc()
# restaurant2.desc()
# restaurant3.desc()

# restaurant1.total_served(200)
# restaurant2.total_served(300)
# restaurant3.total_served(500)

# restaurant1.desc()
# restaurant2.desc()
# restaurant3.desc()