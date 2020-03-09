import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

import random
guess = ''
while guess not in ('heads', 'tails'):
	print('Guess the coin toss! Enter heads or tails:')
	guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads

if toss == 1:
        toss = 'heads'
else:
        toss = 'tails'

logging.debug('toss value is %s guess value is %s' %(str(toss),str(guess)))
if toss == guess:
	print('You got it!')
else:
	print('Nope! Guess again!')
	guess = input()
	if toss == guess:
		print('You got it!')
	else:
		print('Nope. You are really bad at this game.')
