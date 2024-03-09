class ElectronicDevice:
    def __init__(self, name, brand, power_source):
        self.name = name
        self.brand = brand
        self.power_source = power_source

    def turn_on(self):
        return f"{self.name} is turning on."

    def turn_off(self):
        return f"{self.name} is turning off."


class Smartphone(ElectronicDevice):
    def __init__(self, brand, model, operating_system):
        super().__init__('Smartphone', brand, 'Battery')
        self.model = model
        self.operating_system = operating_system

    def make_call(self, contact):
        return f"{self.brand} {self.model} is making a call to {contact}."

    def send_message(self, contact, message):
        return f"{self.brand} {self.model} sent a message to {contact}: '{message}'."


class Laptop(ElectronicDevice):
    def __init__(self, brand, model, screen_size):
        super().__init__('Laptop', brand, 'Electricity')
        self.model = model
        self.screen_size = screen_size

    def open_browser(self):
        return f"{self.brand} {self.model} is opening the web browser."

    def run_program(self, program):
        return f"{self.brand} {self.model} is running the program: {program}."


class Smartwatch(ElectronicDevice):
    def __init__(self, brand, model, health_monitoring):
        super().__init__('Smartwatch', brand, 'Battery')
        self.model = model
        self.health_monitoring = health_monitoring

    def track_steps(self):
        return f"{self.brand} {self.model} is tracking steps."

    def monitor_heart_rate(self):
        return f"{self.brand} {self.model} is monitoring heart rate."


smartphone = Smartphone('Samsung', 'Galaxy S21', 'Android')
print(smartphone.turn_on())
print(smartphone.make_call('Mushni'))
print(smartphone.send_message('Giorgi', 'Hello!'))
print(smartphone.turn_off())

laptop = Laptop('Dell', 'XPS 13', '13 inches')
print(laptop.turn_on())
print(laptop.open_browser())
print(laptop.run_program('Pycharm'))
print(laptop.turn_off())

smartwatch = Smartwatch('Apple', 'Watch Series 6', True)
print(smartwatch.turn_on())
print(smartwatch.track_steps())
print(smartwatch.monitor_heart_rate())
print(smartwatch.turn_off())
