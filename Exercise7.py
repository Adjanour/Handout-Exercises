class Clock(object):
    def __init__(self,time):
        self.time = time

    def print_time(self):
        time = '6:30'
        print(self.time)

clock = Clock('5:30')
clock.print_time()

#Result: '5:30' since self.time was what was referenced