class bike : 
    def __init__ (self, desc, cost, sale_price, condition):
        self.desc=desc
        self.cost=cost
        self.sale_price=sale_price
        self.condition=condition
        self.sold=False

    def update_sale_price(self, sale_price):
        if self.sold==True:
            print ("Action not allowed ,Bike has already been sold")
        else:
            self.sale_price= sale_price
    def update_cost(self):
        if self.sold==True:
            print('Action not allowed , Bike has already been sold')
        else:
            print('please , set the new cost = ')
            self.cost= input()
            print ( 'the new cost is \n'+ self.cost )


    def sell(self):
           
        if self.sold:
            print('Bike has already sold ')
        else:
            print ('Bike is available ')
            


#Create a bike in the factory 
bike1=bike('Univega Alpina, orange', cost=100, sale_price=500, condition=0.5)
        

print(dir(bike1))

        
    

