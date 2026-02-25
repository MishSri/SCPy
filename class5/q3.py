from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function started")
        # Capture the result so we can return it at the end
        result = func(*args, **kwargs) 
        print(f"Function ended")
        return result 
    return wrapper

@log_execution
def calculate_square():
    for i in range(1, 6):
        print(f"Square of {i} is {i*i}")
        
calculate_square()
