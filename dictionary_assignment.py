name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mailid=list()
for line in handle:
    if line.startswith("From "):
	    line = line.strip()
    	words= line.split()
    	mailid.append(words[1])
count=dict()
for word in mailid:
    count[word] = count.get(word, 0) + 1
max=0
for a,b in count.items() :
    if max<=b:
        max=b
        big=a
print big, max