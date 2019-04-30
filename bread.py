from datetime import datetime as dt
class SourDough():
    
    def __init__(self):
        self.sponge = int(input("How much yeast in grams are you working with: "))
        self.percentage = self.sponge/453
        self.calc_ratio()
        
        
    def num_Loaves(self):
        self.loaf_number = int(input("how many loaves you want: "))
        self.percentage = self.loaf_number/4.0
        self.sponge = self.percentage*453
        self.calc_ratio()
        
    def calc_ratio(self):
        self.loaf_number = self.percentage *4
        self.water = 510 * self.percentage
        self.flour = self.percentage * 907
        self.oil = self.percentage * 14
        self. sugar = self.percentage * 14
        self. salt = self.percentage * 22
        print(self)
        
    def __str__(self):
        string = """        percentage...{perc}
        loaves.......{num}
        sponge.......{sponge}
        flour........{flour}
        water........{water}
        oil..........{oil}
        sugar........{sugar}
        salt.........{salt}""".format(perc=self.percentage,num=self.loaf_number,sponge=self.sponge,
        flour=self.flour,water=self.water,oil=self.oil,sugar=self.sugar,salt=self.salt)
        return(string)
        
        
class Brioche():
    def __init__(self):
        self.flour_base = 500
        self.yeast_ratio = 0.02
        self.eggs  = 2
        self.milk_ratio = 0.4
        self.sugar_ratio = 0.1
        self.salt_ratio = 0.018
        self.butter_ratio = 0.2
    
    def loaves(self):
        self.num_Loaves = int(input("How many loaves do you wanna make?"))
        self.flour_total = self.flour_base * self.num_Loaves
        self.yeast_total = self.flour_total * self.yeast_ratio
        self.eggs_total = self.eggs * self.num_Loaves
        self.milk_total = self.flour_total * self.milk_ratio 
        self.sugar_total = self.flour_total * self.sugar_ratio
        self.salt_total = self.flour_total * self.salt_ratio
        self.butter_total = self.flour_total * self.butter_ratio
        
        
        
class NolaFrenchLoaf():
    def __init__(self):
        
        
        
        