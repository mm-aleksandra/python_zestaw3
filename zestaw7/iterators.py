from itertools import cycle, count
from random import choice

#a
print('Modulo 2')

mod2_iter = cycle(range(0,2))

for _ in range(5):
    print(next(mod2_iter), end=' ')

#c
print('\nDays of the week')

day_num_iter = cycle(range(0,7))

for i in range(9):
    print(next(day_num_iter), end=' ')
    
#b
print('\nRandom direction')

def random_direction():
    directions = ["N", "E", "S", "W"]
    while True:
        yield choice(directions)

rand_dir_iter = random_direction()

for _ in range(10):
    print(next(rand_dir_iter), end=' ')

