class phone:
    def __init__(self,brand,model,battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def use(self, minutes):
        x = 2 * int(minutes)
        self.battery = int(self.battery) - x

    def describe(self):
        print(f"{self.model} - battery at {self.battery}%")


def main():
    brand , model , battery = get_user_specs()
    minutes = input("How many minutes have you used your phone today? : ")
    use = phone(brand,model,battery)
    use.use(minutes)
    use.describe()


def get_user_specs():
    bra = input("Whats the brand of ur phone? : ")
    mode = input("What model is it? : ")
    batter = input("Whats your Battery percentage? : ")
    return bra,mode,batter


    
if __name__ == "__main__":
    main()