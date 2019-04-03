#python 3.5.2

'''
This Python functions finds the maximum number in a list by compares each 
number to every other number on the list.
'''



class MyMath():
    def __init__(self, list):
        self.list = list

    def findMaxNo(self):
        max = self.list[0]
        for x in self.list:
               if x > max:
                    max = x
        return max


print ('Test first element in the list is the largest number: ', MyMath( [12,0,9,3,0] ).findMaxNo() )
print ('Test the largest number is in middle of the list : ', MyMath( [0,0,12,3,0] ).findMaxNo() )
print ('Test last element in the list is largest number: ', MyMath( [12,0,9,3,0] ).findMaxNo() )

'''

OUTPUT:

Test first element in the list is the largest number:  12

Test the largest number is in middle of the list :  12

Test last element in the list is largest number:  12

'''
