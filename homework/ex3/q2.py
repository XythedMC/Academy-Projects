x = int(input("Enter a number: "))
if x == 0:
    print("")
else:
    strs_list = [input("Enter a string: ") for _ in range(x)]

    if not strs_list:
        print("No common prefix.")
    else:
        prefix = strs_list[0]
        for s in strs_list[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    break

        print(prefix)