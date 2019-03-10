# Exrecise 5:
# ID validation check Exrecise:
def ID_Validation(id):
    if len(id) != 9:
        return False
    if id.isdigit() is False:
        return False
    sum = 0
    num1 = 0
    num2 = 0
    for i in range(0,8,2):
        num1 = int(id[i]) * 1
        num2 = int(id[i+1]) * 2
        if num2 > 9:
            num2 = int(num2 / 10 + num2 % 10)
        sum += num1 + num2
    num = (int(sum/10) + 1)*10 - sum
    if num == int(id[8]):
        return True
    return False
	
def main():
	#Exrecise 5 Example:
    id = '322536319'
    print(ID_Validation(id))
	
if __name__ == '__main__':
    main()
