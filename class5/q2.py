def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Function started")
        func()
        print(f"Function ended")
    return wrapper

@log_execution
def calculate_square():
    for i in range(1, 6):
        print(f"Square of {i} is {i*i}")
        
calculate_square()
