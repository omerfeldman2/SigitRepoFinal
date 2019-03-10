Cache = {}


# Exrecise 2 B :
# Summing list function for cache decorator example
def SumOfList(ls):
    sum = 0
    for i in range(len(ls)):
        sum += ls[i]
    return sum


# Exrecise 7:
# Decorator Cache Exrecise:
def Decorator_Cache(ls):  # ls represent the input can be to the function:
    CacheFunction = SumOfList  # For example SumOfList is our heavy function
    global Cache
    if (str(ls) in Cache) == False:
        Cache[str(ls)] = CacheFunction(ls)
    return Cache[str(ls)]


def main():   
    # Exrecise 7 Example:
    ls1 = [1, 2, 3, 4, 5]
    ls2 = [2, 4, 6, 8, 10]
    ls3 = [1, 2, 3, 4, 5]
    print(Decorator_Cache(ls1))
    print(Decorator_Cache(ls2))
    print(Decorator_Cache(ls3))

if __name__ == '__main__':
    main()