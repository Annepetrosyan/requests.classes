# class Country:
    # def __init__(self, name, continent):
        # self.name = name
        # self.continent = continent
        
    # def ret(self):
        # return f"Country: {self.name}, its in {self.continent}"
        
# class Brand:
    # def __init__(self, brand_name, start_date):
        # self.brand_name = brand_name
        # self.start_date = start_date
        
    # def present(self):
        # return f"The brand {self.brand_name} started the business in {self.start_date}"
        
# class Season:
    # def __init__(self, season_name, average_temp):
        # self.season_name = season_name
        # self.average_temp = average_temp
        
    # def present(self):
        # return f"in {self.season_name} the average temperature is {self.average_temp} degree"
        
# class Product(Country, Brand, Season):
    # def __init__(self, product_name, product_type, product_price, product_quantity, discount_percent):
        # self.product_name = product_name
        # self.product_type = product_type
        # self.product_price = product_price
        # self.product_quantity = product_quantity
        # self.discount_percent = discount_percent
        # self.discounted_product = self.product_price - self.product_price/100 * self.discount_percent
        
    # def present(self):
        # return f"{self.product_name} is a {self.product_type}, it costs {self.product_price}, existing quantity of {self.product_name} is {self.product_quantity}"
        
    # def discount(self):
        # return f"the product is discounted with {self.discount_percent} % and now it costs {self.discounted_product}"
        
        
# p1 = Product("Gar", "mis", 25000, 200, 50)
# print(p1.discount())


#2 create 3 classes (Hotel, Taxi, Tour)

class Hotel:
    def __init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price):
        self.name = name
        self.place = place
        self.rooms_mid = {room1:free, room2:free, room3: free}
        self.mid_room_price = mid_room_price
        self.rooms_lux = {room1:free, room2:free, room3: free}
        self.lux_room_price = lux_room_price
        
    def present(self):
        return f"our hotel {self.name} is located in {self.place}, delux room price is {self.mid_room_price}, lux rooms cost {self.lux_room_price}"
        
  
            

        
            
    
    

































