




if __name__ == "__main__":
    # s = "Bubble"
    # taking input from user
    s = input("Enter input string : ")

    if len(s) == 0 or len(s) == 1:
        print(s)
        exit(0)

    # maintaining a dictionary for letter counts and order
    # key = lower case letter
    # value = list of tuples. tuple = (letter, index)
    temp = {}
    for i,l in enumerate(s):
        if l.lower() not in temp:
            temp[l.lower()] = [(l,i)]
        else:
            temp[l.lower()].append((l,i))

    # sorting the dictionary based on the length of value
    temp = {k: v for k, v in sorted(temp.items(), key=lambda item: len(item[1]))}

    # print(temp)

    # constructing ans as final string for output by reading and adding the letters(in value) for each key in dictionary
    ans = ""
    for key in temp:
        for l in temp[key]:
            # the letter is the
            ans = ans + l[0]

    # First character in input string with one occurrence
    print(ans[0])
    # Input string in the order of number of occurrences and order from the inputted string
    print(ans)
