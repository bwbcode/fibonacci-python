import sys

def fibonacci_recursive(a,b,length):
    if length == 2: # First two numbers already printed
        print('') # Closes print line
        exit()
    print(a+b,end=' ')
    fibonacci_recursive(b,a+b,length-1)

try:
    if int(sys.argv[1]) < 2:
        print('The minimum length of a sequence is 2')
    else:
        print(0,1,end=' ')
        fibonacci_recursive(0,1,int(sys.argv[1]))
except ValueError:
    print('The series length submitted is not an integer')