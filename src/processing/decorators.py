import time
from functools import wraps

def timer(func):
    """
    A decorator that measures and prints the execution time of a function.
    
    Parameters:
        func (Callable): The function to be wrapped and timed.
        
    Returns:
        Callable: The wrapped function that executes and logs time.
    """
    @wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        name = func.__name__
        elapsed = time.perf_counter() - t0
        print(f"{name} completed in {elapsed:0.8f}")
        return result
    return clocked

def log_execution(func):
    """
    A decorator that prints steps of a function execution.
    
    Parameters:
        func (Callable): The function to be wrapped and logged.
        
    Returns:
        Callable: The wrapped function that executes and needs to be logged.
    """
    @wraps(func)
    def logged(*args, **kwargs):
        name = func.__name__
        print(f"START {name}")
        try:
           result = func(*args, **kwargs)
           print(f"END {name}")
           return result
        except ValueError as e:
            print(f"FAILED {name}")
            raise
    return logged

def retry(retries: int = 3, delay :float = 1.0, allowed_exception: tuple = (Exception,)):
    """
    A decorator that retries a function multiple times if it raises specified exceptions.
    
    :param retries: Maximum number of attempts before giving up.
    :param delay: Wait time between attempts in seconds.
    :param allowed_exceptions: A tuple of exception classes to catch and retry.
    """
    def decorator_retry(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except allowed_exception as e:
                    attempts += 1
                    if attempts >= retries:
                        print(f"Attempt {attempts}/{retries} failed permanently. Raising exception")
                        raise e
                    print(f"Attempt {attempts}/{retries} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator_retry