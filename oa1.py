
def reverseString(oriString):
	return oriString[::-1]

def reverseSubString(oriString):

	newString=""

	tempString=oriString.split(" ")
	for tstr in tempString:
		newString=newString+tstr[::-1]+" "
	return newString[:-1]

if __name__ == '__main__':
	testString1="ymedacaiynuj"
	new1Str=reverseString(testString1)
	print(new1Str)
	testString2="flipped class room is important"
	new2Str=reverseSubString(testString2)
	print(new2Str)