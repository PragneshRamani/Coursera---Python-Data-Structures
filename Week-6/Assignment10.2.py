'''
10.2 Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then
splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.
'''
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d=dict()
count = 0
for line in handle:
    
    if not line.startswith('From'):continue
        
    line=line.split()
    
    if line[0]=='From':
        
        line =  line[5].split(':')
        
        for hrs in line[0].split():
            
            if hrs not in d:
                
                d[hrs]=1
            else:
                d[hrs]+=1
                
for key,value in sorted(d.items()):
    print key,value
