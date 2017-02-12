def hi(name):
	print('hi ' + name)

names=['john', 'jairo']


def hiAll():
	for name in names:
		hi(name)


hiAll()

def printIndex():
	print([i for i,x in enumerate(names) if x == 'john'])

printIndex()