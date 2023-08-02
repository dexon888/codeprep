def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0): return False
        temp = x
        reverse = 0

        while (temp != 0):
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp //= 10
        return x == reverse
    
x = 121
print(isPalindrome(x))