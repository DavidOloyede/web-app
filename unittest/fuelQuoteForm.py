import datetime

class Order:
    def __init__(self, numberOfGallons, date):
        self.numberOfGallons= numberOfGallons
        self.date= date
        self.customerPrice= pricingModule()


    def checkInput(self): #Private function that checks the user inputs
        if not self.date: #Date was not provided 
            return (False, "Date is required")
        else:
            day,month,year= self.date.split('/') #Splitting the date that was provided by / 
            invalidDate= False

            try: 
                datetime.datetime(int(year), int (month), int (day))
            except ValueError:
                invalidDate= True #You have a date in the incorrect format so you have to trigger an error 


        if(invalidDate):
            print (self.date)
            return(False, "Date is in the wrong format: dd/mm/yyyy")
        else:
            #If you have a date and it is in the correct format then check if you have the number of gallons 
            if not self.numberOfGallons:
                return (False, "Need number of gallons")
            #If you have the number of gallons then check the format for the number of gallons 
            else: 
                if self.numberOfGallons<0:
                    return (False, "Number of gallons requested cant be negative")
                elif self.numberOfGallons>100:
                    return (False, "Cant request more than 100 gallons")
                elif isinstance(self.numberOfGallons, float):
                    self.numberOfGallons= int (round(self.numberOfGallons))
                    return (True, "Fractional")
                else:
                    self.numberOfGallons= int (self.numberOfGallons)
                    return (True,"" )


    def totalAmount(self): 
        #Calling the private function checkInput to make sure we have the correct inputs 
        validData, message= self.checkInput()

        if not validData: #An input or error has occured so we trigger a message
            return (message)

        elif validData:
            #We have the correct input but user requested a fractional number of gallons which is not allowed so we're rounding to closest whole number 
            if message=="Fractional":
                print("Cant request fractional number of gallons. Rounding to the closest whole number gallon")
                total= self.numberOfGallons * self.customerPrice.price
                return total
            #all inputs are correct 
            else: 
                total= self.numberOfGallons * self.customerPrice.price
                return total


#Class for the pricing module. Will be developed later in the assignment
class pricingModule:
    def __init__(self):
        self.price=10

#Hardcoded list of user history. We will receive this information from the database later on 
orderHistory= [("02/26/2021", "4800 Calhoun Rd, Houston, TX, 77004", 99, 990), ("01/15/2020", "501 Crawford St, Houston TX 77005", 10, 100 )]
    

#set up your values, hardcoded  
#order1=Order(-5, "01/10/2021")
#order1.checkInput()
#print(order1.totalAmount())