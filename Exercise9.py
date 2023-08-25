class Clock(object):
    def __init__(self, time):
        self.time = time

    def print_time(self):
        time = '6:30'
        print(self.time)


boston_clock = Clock('5:30')

# Assigns the memory address of the object boston_clock to the object paris_clock. So, they now reference the same attributes and values.
paris_clock = boston_clock

paris_clock.time = '10:30'

boston_clock.print_time()

KIRK = 'HELLO'

SIMEON = KIRK

DAVID = SIMEON
