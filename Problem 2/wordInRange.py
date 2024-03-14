def wordInRange():
    #Type your code here
    filenames = input()
    lower_bound = input()
    upper_bound = input()
    with open(filenames, 'r') as file:
            strings = file.readlines()
    strings = [s.strip() for s in strings]
    for string in strings:
        if lower_bound <= string <= upper_bound:
                print(string + " - in range")
        else:
                print(string + ' - not in range')
    return
if __name__ == '__main__':
    wordInRange()