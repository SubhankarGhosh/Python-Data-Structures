def mail():
	fh=open("abc.txt",'r');
	for line in fh:
		line=line.strip()
		if line.startswith("From"):
			atpos=line.find("@")
			beg= 1 + line.rfind(" ",0,atpos)
			end=line.find(" ",atpos)
			print line[beg:end]