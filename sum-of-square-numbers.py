# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

def judgeSquareSum(c):
        if c < 0:
            return False
    
        a = 0
        b = int(c**0.5)  # Compute square root without importing math
        
        while a <= b:
            current_sum = a * a + b * b
            if current_sum == c:
                return True
            elif current_sum < c:
                a += 1
            else:
                b -= 1
                
        return False
            

print(judgeSquareSum(5)) 