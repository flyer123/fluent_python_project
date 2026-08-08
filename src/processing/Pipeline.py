class Pipeline:
    """A pipeline to process data with any given number of function"""

    def __init__(self, *steps):
        self.steps = list(steps)

    def add_step(self, func):
        """Dinamycally adding new function"""
        if not callable(func):
            raise TypeError("Pipeline steps must be callable.")
        self.steps.append(func)
        return self # Enables method chaining

    def __call__(self, initial_data):
        """Executes all sequential pipeline steps on the input data"""
        result = initial_data
        for step in self.steps:
            result = step(result)
        return result