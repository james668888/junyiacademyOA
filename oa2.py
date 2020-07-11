
def removeNumber(n):

	count=0
	for i in range(1,n+1):
		if i%3==0 and i%5==0:
			count+=1
		elif i%3!=0 and i%5!=0:
			count+=1
	return count


if __name__ == '__main__':
	count=removeNumber(21)
	print(count)