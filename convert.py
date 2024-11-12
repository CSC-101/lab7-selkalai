from typing import Optional
#Task 1
#function str_to_float takes one parameter of type str and converts it to a float
# value if the str represents a float and returns it. If it doesn't it will
# return None
def str_to_float(string_a:str)->Optional[float]:
    try:
        float_one = float(string_a)
        return float_one
    except ValueError:
        return None



