""""Overloading a Circuit Breaker"""

class CircuitBreaker:

    def __init__(self, max_amps):
        self.capacity = max_amps
        self.load = 0


    def connect(self, amps):
        if self.load + amps > self.capacity:
            raise Exception ('Connection will exceed capacity')
        elif self.load +amps < 0:
            raise Exception ('Connection will cause negative load')
        else:
            self.load +=amps
        


cb = CircuitBreaker(20)

print(cb.load)
 
 #connect valid
try:
    cb.connect(12)

except Exception as e:
    print(e)

print(cb.load)

# connect a oversized

try:
    cb.connect(56)

except Exception as e:
    print(e)

print(cb.load)

# connect a negative load

try:
    cb.connect(-45)

except Exception as e:
    print(e)

print(cb.load)