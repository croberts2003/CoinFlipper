import time
import random
import sys
import matplotlib.pyplot as plt
import numpy as np

def flipCoin(heads_record, tails_record):
    flip = random.randint(1,2)
    if flip == 1:
        print('heads')
        heads_record += 1
    elif flip == 2:
        print('tails')
        tails_record += 1

    total_record = [heads_record, tails_record]
    return total_record

def massFlip(limit, heads_record, tails_record):
    i = 1
    while i <= limit: 
        flip = random.randint(1,2)
        if flip == 1:
            print('heads')
            heads_record += 1
        elif flip == 2:
            print('tails')
            tails_record += 1

        i += 1

    total_record = [heads_record, tails_record]
    return total_record

def options():
    data = 0,0
    heads_record = 0
    tails_record = 0

    while True:
        print('Options:')
        response = input('1. Flip Coin\n2. Generate Coin Flip Data\n3. Show session flip data\n4. Exit')
        if response == '1':
            single_data = flipCoin(heads_record, tails_record)
            
        elif response == '2':
            response = input('How many loops of data would you like to generate?')
            try:
                limit = int(response)
            except ValueError:
                print('Please enter an integer.')
            else:
                data = massFlip(limit, heads_record, tails_record)

        elif response == '3':
            heads_record = data[0] + single_data[0]
            tails_record = data[1] + single_data[1]

            print("Total Heads for this sessions is " + str(heads_record))
            print("Total Tails for this sessions is " + str(tails_record))

            objects = ('Heads', 'Tails')
            y_pos = np.arange(len(objects))
            stats = [heads_record, tails_record]

            plt.bar(y_pos, stats, align='center', alpha=0.5)
            plt.xticks(y_pos, objects)
            plt.ylabel('Amount of Flips')
            plt.title('Coin Flips')

            plt.show()

        elif response == '4':
            exit()

        else:
            print('Invalid input')