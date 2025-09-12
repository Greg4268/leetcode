
# constraints 
# n input is even 
# 32 bit int 

def solution_1(n):
    b = format(n, '032b')
    return int(b[::-1],2)

# ------- Test ------- 
def assert_results(input, res): 
    # todo 
    print(" ")

n = 123
print(f"n = {n} \n output: {solution_1(n)}")


