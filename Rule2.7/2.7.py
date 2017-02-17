import re

exampleString = '''
int main(void){
    int c,d;
    c =0;
    d = 0;
    func(c,d);
    return 0;
}
int func1(int* a, int* b)
{
    int a = 1;
    return a;

}
int func2(a,b)
{
    int a = 1;
    return a;
}
int func3(int* a, float b)
{
    int a = 1;
    return a;
}
int func4(char a, int* b)
{
    int a = 1;
    return a;
}'''


names = re.findall('[a-zA-Z0-9_]*\s[a-zA-Z0-9_]*\(.*\)',exampleString)
print names
Length = len(names)
print"Length of the List",Length
i = 0

while( i < Length ):
    if (re.findall("int main",names[0])):
        del names[0]
##        print"Length of string after del", len(names)
        i += 1
##        print i
##        print names
        
    elif (re.findall('\(.*\)',names[0])):
        if(re.findall('int'or'float'or'char' or 'int*'or'float*'or'char*',names[0])):
            print"Required"
            i += 1
        else:
            del names[0]
            print"Not Required"
            #print"Length of string after del", len(names)
            i += 1
            #print i
            #print names
        

print "Final:", (names)
