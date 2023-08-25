class Clock(object):
    def __init__(self,time):
        self.time = time

    def print_time(self,time):
        print (time)


clock = Clock('5:30')
clock.print_time('10:30')

# Result: '10:30' . Self keyword distingushes parameters fromm instance attributes when they have the same name