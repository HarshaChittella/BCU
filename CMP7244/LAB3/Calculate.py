def add(n1,n2):
    disp('Adding %d by %d = %d'%(n1,n2,n1+n2))
def sub(n1,n2):
    disp('Subtractign %d by %d = %d'%(n1,n2,n1-n2))
def mul(n1,n2):
    disp('Multiplying %d by %d = %d'%(n1,n2,n1*n2))
def div(n1,n2):
    disp('Dividing %d by %d = %d'%(n1,n2,n1/n2))
def disp(s):
    print(s)
def  calculate(n1,n2,opt):
    if opt == '+':
        add(n1,n2)
    elif opt == '-':
        sub(n1, n2)
    elif opt == '*':
        mul(n1,n2)
    elif opt == '/':
        div(n1,n2)

def main():
    a=int(input('Enter value 1'))
    b=int(input('Enter value 2'))
    c=input('Enter operator')
    calculate(a,b,c)
    
main()