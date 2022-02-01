""" Blueprint for Jeans"""
class jeans:

    def __init__(self, waist,length, color):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False
    
    def put_on(self):
        print('Putting on {} x {}  {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = True

    def take_off(self):
        print('Taking off {} x {}  {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = False




new_jeans = jeans(30,31,'blue')


new_jeans.put_on()
print(new_jeans.wearing)
new_jeans.take_off()
print(new_jeans.wearing)
 


