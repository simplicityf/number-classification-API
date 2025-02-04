import requests

# function for getting funfacts
def get_fun_fact(n):
    '''
    Fetch fun fact from Numbers API
    '''
    url = f"http://numbersapi.com/{n}/math?json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json().get("text", "No funfact available")
    except requests.exceptions.RequestException:
        return "Could not fetch fun fact."
    return "No fun fact found"

def is_prime(num):
    ''' 
    Check if a number is prime
    '''
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    '''
    Check if a number is perfect
    '''
    sum_divisor = sum(i for i in range(1, num) if num % i == 0) == num
    return sum_divisor

def is_armstrong(num):
    '''
    Check if a number is Armstrong
    '''
    digits = [int(d) for d in str(num)]
    power = len(digits)
    armstrong = sum(d ** power for d in digits) == num
    return armstrong
