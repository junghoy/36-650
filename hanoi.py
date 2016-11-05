

#Tower of hanoi 


def movefn(disk, start, to, acc):
	
	acc.append((disk, start, to))

def hanoi(n, start, extra, end, movefn, acc):

	if n >= 1:
		
		hanoi(n-1, start, end, extra, movefn, acc)
		movefn(n, start, end, acc)
		hanoi(n-1, extra, start, end, movefn, acc)

	return acc 

