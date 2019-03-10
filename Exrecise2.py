# Exrecise 2 A :
# List input interface
def CalcSum():
    ls = []
    num1 = input("Enter num : ")
    while num1 != 'stop':
        if num1.isdigit():
            ls.append(int(num1))
        else:
            print("Invalid num")
        num1 = input("Enter num : ")
    n = SumOfList(ls)
    print ("Sum : " + str(n))
    return

# Exrecise 2 B :
# Summing list function
def SumOfList(ls):
    sum = 0
    for i in range(len(ls)):
        sum += ls[i]
    return sum
	
def main():
	# Exreicse 2 init:
    CalcSum()

if __name__ == '__main__':
    main()

