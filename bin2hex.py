#!/usr/bin/python

num = raw_input()

for i in num:
	if i != '0' and i != '1':
		print("Invalid Input")
		exit(0)

binary = (list(num))

length = len(binary)
plusZ = 4 - length % 4

temp = []
for i in range(0,plusZ):
	temp.append( '0' )

binary = temp + binary
length = len(binary)
thing = 4 - ((length/4)%4)
zero = ['0','0','0','0']
for i in range(0,thing):
	binary = zero + binary

length = (len(binary)/4)

decimal = []
string = ''
result = ''

for i in range(0,length):
	for j in range(0,4):
		decimal.append(int(binary[i*4+j]))
		string = string + str(binary[i*4+j])
	result = result + ("%x" % (int(string,2)))
	if (i+1)%4 == 0 : 
		result = result + ' '
	del(decimal[0:4])
	string = ''
print(result)

