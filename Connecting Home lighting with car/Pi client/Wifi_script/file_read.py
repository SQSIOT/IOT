from subprocess import call
import shlex
call(shlex.split('sh hello.sh'))
## Open the file with read only permit

f = open('Essid.txt')
## use readlines to read all lines in the file
## The variable "lines" is a list containing all lines
lines = f.read().strip()
print lines
## close the file after reading the lines.

if lines == "IoT":
 print "connected"
else:
 print "Not connected"
f.close()
