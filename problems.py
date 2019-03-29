def loop():
	varNum = 0;
	while varNum < 10:
		varNum += 2;
		print (varNum); #end

def add():
	first = "first3 second1 ha2ha fourth4";
	output ="";
	wew = first.split(' ');
	temp = wew;
	for x in wew:
		for char in x:
			if char.isdigit() == True:
				temp[int(char)-1] = x;
	output = ' '.join(temp);
	print(output); #end

def descending():
	number =21345;
	sort =[];
	wew = str(number);
	for x in wew:
		sort.append(x);
	sort.sort(reverse=True)	
	output = ''.join(sort);
	print(int(output)); #end

if __name__ == "__main__":
	
	# loop();
	# print add();
	# descending();
