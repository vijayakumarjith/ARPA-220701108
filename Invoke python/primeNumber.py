def isPrime():
	n=45
	i=2
	if(n==1 or n==0):
		return False
	while(i<n):
		if(n%i==0):
			return False
		i=i+1
	return True