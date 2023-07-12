"""
Given an integer array A of size N. In one second, you can increase the value of one element by 1.

Find the minimum time in seconds to make all elements of the array equal
"""
"""
approach : find maximum and subtract element from maximum
"""
class Solution:
    @staticmethod
    def minimum_time_equality(array):
        maximum=float('-inf')
        time =0
        for element in array:
            if element>maximum:
                maximum=element
        for element in array:
            time+=(maximum-element)
        return time

if __name__ == '__main__':
    ob=Solution()
    array=list(map(int,input().split()))
    print(ob.minimum_time_equality(array))