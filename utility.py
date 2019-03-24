def fast_pow(base, pow):
    if pow == 0:
        return base
    
    if pow & 1:
        return base * fast_pow(base * base, pow // 2)
    
    return fast_pow(base * base, pow // 2)

if __name__ == "__main__": 
    print("Please run the main.py file")