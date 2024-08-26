# Bài 3.
# Thực hiện các yêu cầu sau:
# Xây dựng ba lớp Vehicle, Car và ElectricCar. Car kế thừa từ Vehicle và ElectricCar kế thừa từ Car. Mỗi lớp sẽ có phương thức description() ghi đè
# phương thức của lớp cha.
# Lớp Vehicle có thuộc tính make (hãng sản xuất) và phương thức description()
# in ra thông tin của phương tiện.
# Lớp Car kế thừa từ Vehicle, có thêm thuộc tính model (tên dòng xe), và có
# phương thức description() in ra thông tin của ô tô.
# Lớp ElectricCar kế thừa từ Car, có thêm thuộc tính battery_size (dung lượng
# pin), và phương thức description() in ra thông tin của xe điện.
# Tạo ra các đối tượng thuộc các lớp đã xây dựng và in thông tin của các đối
# tượng đó ra màn hình.

class Vehicle:
    def __init__(self,make) -> None:
        self.make=make
    def description(self):
        print(self.make)

class Car(Vehicle):
    def __init__(self, make,model) -> None:
        super().__init__(make)
        self.model=model
    def description(self):
        super().description()
        print(self.model)
    
class ElectricCar(Car):
    def __init__(self, make, model,battery_size) -> None:
        super().__init__(make, model)
        self.battery_size=battery_size
    def description(self):
        super().description() 
        print(self.battery_size)
vehicle = Vehicle("Vinfast")
vehicle.description()
car =Car("Vinfast","VF")
car.description()
electriccar = ElectricCar("Vinfast","VF","87,7 kWh")
electriccar.description()

