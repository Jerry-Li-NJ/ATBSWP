#! /usr/bin/python3
# xinJing.py - Used for nianJing.

# Print the Wan.
print('''
			##########
			##########
			    
''')

# Print kaiJingji and Namo.
input('XiangZan')
input('KaiJingJi')

# Count the 7 times.
i=1
while i<8:
	input('Reading...')
	if i == 7:
		print('#####|'*6 + '#####')
	else:
		print('#####|'*i)
	i = i + 1

# Peint huiXiangJis.
input('HuiXiangJi')
print('Done')
