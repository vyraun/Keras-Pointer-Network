import tsp

if __name__ == "__main__":
	p = tsp.Tsp()
	p.prepare()
	X, Y = p.open_data()  
	
	for x, y in X, Y:
	    print(x,y)
