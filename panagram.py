import string
def panagram(str):
	alphabet="abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		if char not in str.lower():
			return False
	return True