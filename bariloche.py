from travel import Travel

class Bariloche(Travel):

    def __init__(self):
        self.price = 800
        self.excursions = "Mountain, Party, Hotel"

    def getPrice(self):
        return self.price 
    
    def getExcursions(self):
        return  self.excursions
    

    def discount(self, person, days):
        if person > 5 and days > 11:
            self.price = self.price * 0.25

        else:
            return self.price