import random

dirty = True

scrub_count = 0

while(dirty):

    scrub_count +=1
    print('Scrub the pan: {}'.format(scrub_count))


    if not random.randint(0,9):
        print('All clean!')
        dirty = False
    else:
        print('still dirty ...')

    print('Rinse & check if the pan is clean.')
    