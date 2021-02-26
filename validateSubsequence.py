array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

def isValidSubsequence(array, sequence):
    # Write your code here.
    index = 0
    for i in range(0, len(array)):
        if sequence[index] == array[i]:
            index = index + 1
            if index > len(sequence) - 1:
                return True
    return False
    
print(isValidSubsequence(array, sequence))