
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    count =1
    for i in range(k):
        count *=n
        n=n-1
    return count




def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    count =0
    for i in range(1,n+1):
        if i%k==0:
            print(i)
            count =count+1
    return count
   

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    count=0
    while y!=0:
        remainder=y%10
        count=count+remainder
        y=y//10
    return count
    """
    此处为整除应用，//为地板除(floor division)，取整数。/除结果保留小数
    """



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    nums=[]
    while n!=0:
        nums=nums+[n%10]
        n=n//10
    for a,b in zip(nums,nums[1:]):
        if a==b and a==8:
            return True
    return False
    """
    边界问题：从1开始，当前与前一个比
    for i in range(1,len):
        if i[i-1]==i[i]:
            return True
    使用zip同理
    """