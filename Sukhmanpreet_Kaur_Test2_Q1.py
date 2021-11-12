
def factorial():
    value =  int(input("Enter a number: "))
    product = 1;
    for i in range(1,value+1):
        product *=i
    print(product)

factorial()