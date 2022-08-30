import math

x = 9000
y = 1500
##　算第三邊
def calculate_triangle_third_edge(edge_1, edge_2, is_third_edge_long_edge=True): 
    if is_third_edge_long_edge:
        return math.sqrt(edge_1*edge_1 + edge_2*edge_2)
    else:
        return math.sqrt(abs(edge_1*edge_1 - edge_2*edge_2))

def use_args_kwargs(*args, **kwargs):
    for arg in args:
        print("arg: ", arg)
    for k, v in kwargs.items():
        print("kwargs: ", k, v)