#keep checking until something occurs

import time


hungry = True

while (hungry):
    print('Openingn the front door .....')
    front_door = open('front_door.txt', 'r')

    if "Pizza Guy" in front_door:
        print("Pizza Guy is here ....yammy")
        hungry = False

    else:
        print('Pizza guy not yet ----')
    print('Closing the front door ....')
    front_door.close()

    time.sleep(1)

