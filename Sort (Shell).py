# python 3.5.2

unsorted_list = [7, 6, 8, 9, 3, 2, 10, 5, 1]

def shellSwap(result, index_left, index_right):
    if result[index_left] > result[index_right]:
        value_left = result[index_left]
        result[index_left] = result[index_right]
        result[index_right] = value_left
    return result

# shellSwap(unsorted_list, 2 ,5)
print('_' * 20)

def sortShell(result, gap):
    for gap_count in range(gap, 1, -1):
        used = [False] * len(result)
        for shell_left in range(0, len(result)):
            shell_right = shell_left + gap_count
            # 1) If gap is 4, shell_left is 4, shell_right (9) IN THIS LIST THERE IS NO INDEX NINE
            # 2,3) You can not used index that was used by previous shell
            if shell_right < len(result) and used[shell_left] != True and used[shell_right] != True:
                used[shell_left], used[shell_right] = True, True
                print('sortShell 1 - { ' + str(shell_left) + ', ' + str(shell_right) + ' }')
                result = shellSwap(result,shell_left,shell_right)
            if used [shell_left] == False and shell_left < len(result) -2:
                print('sortShell 2 - { ' + str(shell_left) + ', ' + str(shell_right -1) + ' }')
                result = shellSwap(result, shell_left, shell_right-1)
        print(result)
        print('_' * 20)

    return result


print(sortShell(unsorted_list, 4))

'''
OUTPUT:
sortShell 1 - { 0, 4 }
sortShell 1 - { 1, 5 }
sortShell 1 - { 2, 6 }
sortShell 1 - { 3, 7 }
[3, 2, 8, 5, 7, 6, 10, 9, 1]
____________________
sortShell 1 - { 0, 3 }
sortShell 1 - { 1, 4 }
sortShell 1 - { 2, 5 }
sortShell 2 - { 6, 8 }
[3, 2, 6, 5, 7, 8, 1, 9, 10]
____________________
sortShell 1 - { 0, 2 }
sortShell 1 - { 1, 3 }
sortShell 1 - { 4, 6 }
sortShell 1 - { 5, 7 }
[3, 2, 6, 5, 1, 8, 7, 9, 10]
____________________
[3, 2, 6, 5, 1, 8, 7, 9, 10]
'''
