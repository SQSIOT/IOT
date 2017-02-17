#To read from TXT file

import linecache
import re

para1 = []
para2 = []

line_number = 0
with open('text.txt') as f:
    for line in f:
        line_number += 1
        flag = False
        i= k = 0
        if(re.findall('[a-zA-Z0-9_]*\s[a-zA-Z0-9_]*\(.*\)',line)):
            if re.findall('int main' or 'printf' or 'scanf',line):
                pass
            else:
                next_line = f.next()
                if '{' in next_line:
                    formal = re.findall('\(.*\)',line)
                    para = re.sub("[^\w]", " ",formal[0]).split()
##                print para
                    print line_number
                    while(i < len(para)):
                        if( i % 2 != 0 and i != 0 ):
                            print "Entered"
                            para1.insert(k,para[i])
                            k += 1
                            print k,para1
##                        print"parameter1 is:",i, para1
##                        print len(para1)
                        else:
##                        print"parameter2 is:",k
                            para2 = para[i]
##                        print"parameter2 is:",i,k, para2
                    i += 1
                    print len(para1),len(para2)
                    print para1
                    print para2
##                while(True):
##                            print next_line
##                            print para1
##                            if '}' in next_line:
####                                print "Checking for }"
##                                break
##                            
##                            elif para1 in next_line:
####                                match = re.findall(para,next_line
####                                print match
####                                print "Finding para1 in line"
####                                print para1   
##                                flag = True
##                                next_line = saved_line
##                                break
##                            next_line = f.next()
####                            print"End of loop", next_line
##                            
##                        if (flag):
##                            print "found"
##                            flag = False
##                        else:
##                            print "not found"
##                                
line_number = 0
