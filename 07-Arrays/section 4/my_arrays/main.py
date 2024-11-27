import MainArrays

if __name__ == "__main__":
    array = [7, 3, 8, 5, 2]
    print('Numbers: ', MainArrays.display(array))
    print('Second largest number: ', MainArrays.second_max(array))
    print('Median: ', MainArrays.find_mid(array))
    print('Smallest and largest number: ', MainArrays.min_max(array))
    print('Numbers as a string: ', MainArrays.dashes(array))