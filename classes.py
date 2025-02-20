class Car:
    def __init__(self,model,year,mileage=0):
        self.model=model
        self.year=year
        self.mileage=mileage
    
    def display_info(self):
        print(f'model : {self.model}\nyear : {self.year}\nmileage : {self.mileage}')

    def drive (self):
        q=int(input('distance drived? : '))
        self.mileage +=q


car1 = Car('eon',2011,65000)
car2 = Car('etios',2018,40000)

car1.display_info()
car1.drive()

car2.display_info()
car2.drive()


print(f'updated mileage:\ncar1:{car1.mileage}\tcar2:{car2.mileage} ')