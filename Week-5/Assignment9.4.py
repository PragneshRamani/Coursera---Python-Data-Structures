'''
9.4 Write a program to read through the mbox-short.txt and figure out who has
the sent the greatest number of mail messages. The program looks for 'From '
lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to
a count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop
to find the most prolific committer.
'''
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = 0
d = dict()

for line in handle:
    
    if not line.startswith('From'):continue
    
    line = line.split()
    
    if line[0] == 'From':
        
        line1 =  line[1]
       
        for word in line1.split():
            
            if word not in d:
                
                d[word] = 1
            else:
                d[word]+=1
        
        count = count + 1
        
maximum = None
k = None
for key,value in d.items():
    
    if maximum is None or value>maximum:
        maximum = value
        k=key
print k,maximum
