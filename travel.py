

class Travel:

    def __init__(self ):
        #Add value to variables

        self.name = "Summer Travel"
        self.person = 5
        self.days = 0

    # Method get and set

    def getName(self):
        return self.person
    

    def setPerson(self,person):
        self.person = person

    
    def getPerson(self):
        return self.person


    #def setPrice(self, price):
     #       return self.price


    #def getPrice(self):
     #   return self.price
    

    def setDays(self, days):
        self.days = days

    def getDays(self):
        return self.days
    
    
    def full(self):
        return self.name, self.person, self.days





