''' Different ways to test multiple flags in Python '''
NUM_1, NUM_2, NUM_3 = 0,1,0

if NUM_1 ==1 or NUM_2 == 1 or NUM_3 ==1:
    print('passed')


if 1 in (NUM_1,NUM_2,NUM_3):
    print('passed')

# boolean condition (2 ways)
if NUM_1 or NUM_2 or NUM_3:
    print('passed')

if any((NUM_1,NUM_2,NUM_3)):
    print('passed')
