
bus_types = ['Volvo A/C Semi Sleeper (2+2)',
            'Non A/C Sleeper (2+1)',
            'Scania AC Multi Axle Semi Sleeper(2+2)',
            'Volvo A/C Multi Axle Sleeper(2+1)',
            'Non A/C Seater/Sleeper (2+1)',
            'Volvo Multi Axle SemiSleeper I-Shift B11R (2+2)',
            'Mercedes Benz Multi Axle (2+2)',
            'Volvo A/C Seater Multi Axle (2+2)']

basic_charge = 750

departure =[]
arrival =[]
no_of_pax = []
name_of_pax = []
age_of_pax = []
contact = []

class Main:

    def __init__(self, seats):
        self.seats = seats

    def journey_from_and_to(self):
        global departure
        global arrival

        departure = input("From:")
        arrival = input("To:")


    def ask_booking_details(self):
        global name_of_pax
        global age_of_pax
        global contact

        print("")
        no_of_pax = int(input("Booking for:"))
        print("")
        for i in range(no_of_pax):
            name_of_pax = input("Enter Name:")
            age_of_pax = input("Enter age:")
            contact = input("Enter mobile number:")

    def ask_bus_type(self):
        global bus_types
        print("")
        print(' 1. Volvo A/C Semi Sleeper (2+2)\n',
            '2. Non A/C Sleeper (2+1)\n',
            '3. Scania AC Multi Axle Semi Sleeper(2+2)\n',
            '4. Volvo A/C Multi Axle Sleeper(2+1)\n',
            '5. Non A/C Seater/Sleeper (2+1)\n',
            '6. Volvo Multi Axle SemiSleeper I-Shift B11R (2+2)\n',
            '7. Mercedes Benz Multi Axle (2+2)\n',
            '8. Volvo A/C Seater Multi Axle (2+2)')
        inp_for_bus_type = int(input("Which bus would you like to travel in:"))

        if inp_for_bus_type == 1:
            print(bus_types[0])
        elif inp_for_bus_type == 2:
            print(bus_types[1])
        elif inp_for_bus_type == 3:
            print(bus_types[2])
        elif inp_for_bus_type == 4:
            print(bus_types[3])
        elif inp_for_bus_type == 5:
            print(bus_types[4])
        elif inp_for_bus_type == 6:
            print(bus_types[5])
        elif inp_for_bus_type == 7:
            print(bus_types[6])
        else:
            print(bus_types[7])

    def print_booking_details(self):

        global departure
        global arrival
        global no_of_pax
        print("")
        print("From:", departure)
        print("To  :", arrival)
        print("")

    def print_pax_details(self):

        global name_of_pax
        global age_of_pax
        global contact
        print("")
        print("Name:", name_of_pax)
        print("Age:", age_of_pax)
        print("Contact:", contact)



m = Main(10)

m.journey_from_and_to()

m.ask_booking_details()

m.ask_bus_type()

m.print_pax_details()

m.print_booking_details()

