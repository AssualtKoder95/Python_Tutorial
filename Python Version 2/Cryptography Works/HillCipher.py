import numpy as np
from string import ascii_lowercase
#aaray of lowercase letters
alph = list(ascii_lowercase)




mx = np.matrix([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
my = np.matrix([[1,2],[1,2],[3,4]])   


#print mx * my

dM = []
em = []
list = []
finalMatrix = []


def hillCipher():

	while True:
		try:
			num = ord(raw_input("Enter a letter in to encrypt: "))
			if num > 96 and num < 123:
				list.append((num - 19) % 26)
			else:
				break
		except ValueError:
			print "tyy again not valid"
		

	print list


def getText():
	print "give me the text: "
	str = raw_input()
	str= str.lower()
	str = str.replace(" ","")


	return str




def encrypt():
	print "list the encryption array rows separated by spaces for each leeter and commas for each row (,)\n  \
	example :  2  3 , 4  5 = [ [2,3],[4,5]]. "
	str = raw_input()
	a = str.split(",")
	print a
	for item in a:
		item = item.strip()
		items = item.split()
		list.append(items)

	encryptonMatrix = []
	print list
	for elementList in list:
		length = len(elementList)
		for element in elementList:
			encryptonMatrix.append(int(element))
		
		finalMatrix.append(encryptonMatrix)
		encryptonMatrix = []

	print finalMatrix

	str = getText()
	if len(str) % length != 0:
		str = str + ( length -  (len(str) % length ))*'a'


	lengthOfMatrix = length
	length = 0
	listofElms = []
	
	end = lengthOfMatrix
	while length < len(str):
		listofElms.append(str[length:end])
		length = length + lengthOfMatrix
		end = end + lengthOfMatrix

	encryptionStuff = []

	finalMultiplicationMatrix = []
	for item in listofElms:
		for element in item:
			encryptionStuff.append((ord(element)-19 )% 26)
		finalMultiplicationMatrix.append(encryptionStuff)
		encryptionStuff = []

	print finalMultiplicationMatrix

	characterMatrix = []
	for x in finalMultiplicationMatrix:
		characterMatrix.append( np.matrix(x) * np.matrix(finalMatrix))


	cipherText = []
	for item in characterMatrix:
		A = np.array(item).tolist()
		for i in A:
			for f in i:
				cipherText.append(alph[f % 26])

	print "Cipher text is: "+''.join(cipherText)



if __name__ == '__main__':

	encrypt()









