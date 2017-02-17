#To read from TXT file

import linecache

theFile = open("Line.txt", "r")
text_file = open("text.txt", "r")

line = []
i = 0
for val in theFile.read().split(): 
    line.append(int(val)) 
    i += 1
j = i
#print"Initial value of I", i
i = 0
#Jump to specific line
while(i < j):
    print"line number:", line[i]
    line_number = linecache.getline('text.txt', line[i])
    print line_number
    i += 1
    
theFile.close()
text_file.close()

