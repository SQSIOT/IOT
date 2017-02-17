file = open('text.txt','r')
files_lines = [line for line in file]
counter = 0
keywords = 'int a'
import re

for line in files_lines:
    counter += 1
##    print files_lines[2],'line number',counter    
    if(re.findall('[a-zA-Z0-9_]*\s[a-zA-Z0-9_]*\(.*\)',line)):
        if re.findall('int main' or 'printf' or 'scanf',line):
            print line
            pass
        else:
            line_number = counter
            line_number += 1
            next_line = files_lines[line_number]
            print"Line by line", files_lines[line_number]
            if '{' in next_line:
                formal = re.findall('\(.*\)',line)
                para = re.sub("[^\w]", " ",formal[0]).split()
                print line_number
                print "found",para
    


counter = 0
