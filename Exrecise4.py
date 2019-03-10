# Exrecise 4:
# String contraction Exrecise:
def ContractionString(st):
    if len(st) == 0:
        return ""
    count = 0
    let = st[0]
    for letter in st:
        if letter == let:
            count += 1
        else:
            break
    return "" + str(let) + "" + str(count) + "" + str(ContractionString(st[count:]))

def main():
	# Exrecise 4 Example:
    st = "aabbbbcdddeaaaaa"
    st = ContractionString(st)
    print(st)

if __name__ == '__main__':
    main()
