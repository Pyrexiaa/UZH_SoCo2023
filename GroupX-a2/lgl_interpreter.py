import sys
import json
import datetime
import string
import random

FUNCTION_CALLS = {}

def wrap(func):
    def wrapper(*args):
        start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        func_id = ''.join(random.choices(string.digits, k=6))
        result = func(*args) # do function
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

        # Update function call information
        func_name = func.__name__
        if func_id not in FUNCTION_CALLS:
            FUNCTION_CALLS[func_id] = {'func_id': func_id,'func_name': func_name, 'start_time': start_time, 'end_time': end_time}

        return result

    return wrapper

@wrap
def do_function(envs,args):
    assert len(args) == 2
    params = args[0]
    body = args[1]
    return ["function",params,body]

@wrap
def do_apply(envs,args):
    assert len(args) >= 1
    name = args[0]
    arguments = args[1:]
    # eager evaluation
    values = [do(envs,arg) for arg in arguments]
    func = envs_get(envs,name)
    assert isinstance(func,list)
    assert func[0] == "function"
    func_params = func[1]
    assert len(func_params) == len(values)

    local_frame = dict(zip(func_params,values))
    envs.append(local_frame)
    body = func[2]
    result = do(envs,body)
    envs.pop()

    return result

@wrap
def do_set(envs,args):
    assert len(args) == 2
    assert isinstance(args[0],str)
    var_name = args[0]
    value = do(envs,args[1])
    envs_set(envs,var_name, value)
    return value

@wrap
def envs_get(envs, name):
    name = name.strip()
    assert isinstance(name,str)
    for e in reversed(envs):
        if name in e:
            return e[name]
    assert False, f"Unknown variable name {name}"

@wrap
def envs_set(envs, name, value):
    assert isinstance(name, str)
    envs[-1][name] = value
    return value

@wrap
def do_call(envs,args):
    assert len(args) == 1
    return envs_get(envs,args[0])

@wrap
def do_call_object(envs, args):
    assert len(args) == 2
    target_envs = envs_get(envs, args[1])
    return envs_get(target_envs, args[0])

@wrap
def do_addition(envs,args):
    assert len(args) == 2
    left = do(envs,args[0])
    right = do(envs,args[1])
    return left + right

@wrap
def do_absolute(envs,args):
    assert len(args) == 1
    value = do(envs,args[0])
    return abs(value)

@wrap
def do_subtraction(envs,args):
    assert len(args) == 2
    left = do(envs,args[0])
    right = do(envs,args[1])
    return left - right

@wrap
def do_multiplication(envs, args):
    assert len(args) == 2
    left = do(envs, args[0])
    right = do(envs, args[1])
    assert isinstance(left, (int, float)) or isinstance(right, (int, float)), "Both arguments must be numeric (int or float)."
    result = left * right
    return round(result, 2)

@wrap
def do_division(envs, args):
    assert len(args) == 2
    left = do(envs, args[0])
    right = do(envs, args[1])
    assert right != 0, "Division by zero is not allowed."
    assert isinstance(left, (int, float)) or isinstance(right, (int, float)), "Both arguments must be numeric (int or float)."
    result = left/right
    return round(result, 2)

@wrap
def do_power(envs, args):
    assert len(args) == 2
    left = do(envs, args[0])
    right = do(envs, args[1])
    assert isinstance(left, (int, float)) or isinstance(right, (int, float)), "Both arguments must be numeric (int or float)."
    result = left/right
    return round(result, 2)

@wrap
def do_print(envs, args):
    assert len(args) == 1
    value = do(envs, args[0])
    print(value)

@wrap
def do_update(envs, args):
    assert len(args) == 2 # chosen operation, chosen var, what number
    assert isinstance(args[0], str)
    updated_value = do(envs, args[1])
    envs_set(envs, args[0], updated_value)
    return updated_value

@wrap
def evaluate_condition(envs, condition):
    condition = condition.strip()
    if "<=" in condition:
        var_name, value = condition.split("<=")
        return envs_get(envs, var_name) <= float(value)
    elif ">=" in condition:
        var_name, value = condition.split(">=")
        return envs_get(envs, var_name) >= float(value)
    elif "<" in condition:
        var_name, value = condition.split("<")
        return envs_get(envs, var_name) < float(value)
    elif ">" in condition:
        var_name, value = condition.split(">")
        return envs_get(envs, var_name) > float(value)
    elif "==" in condition:
        var_name, value = condition.split("==")
        return envs_get(envs, var_name) == float(value)
    else:
        raise ValueError("Invalid condition format")

@wrap  
def do_while_loops(envs, args):
    assert len(args) >= 3 # starting, stopping condition and operation
    # set the starting variables
    initial_value = do(envs,args[1])
    assert args[1][0] == "set", "You have not initialize your variable!"
    operation = args[0]
    assert isinstance(operation, list)
    stopping_conditions = args[2]
    assert len(stopping_conditions) == 1
    stopping_condition = stopping_conditions[0]

    while evaluate_condition(envs, stopping_condition):
        result = do(envs, operation)
    return result

@wrap
def do_create_array(envs, args):
    assert len(args) == 2 # name of array and content of array 
    assert isinstance(args[0], str)
    assert isinstance(args[1], list)
    array_name = args[0]
    array_content = args[1]
    envs_set(envs, array_name, array_content)
    return array_content

@wrap 
def do_set_array(envs, args):
    assert len(args) == 3 # name of array, index of array, new_number
    assert isinstance(args[0], str)
    assert isinstance(args[1], int)
    assert isinstance(args[2], int)
    array_name = args[0]
    array_idx = args[1]
    array_new_number = args[2]
    array = envs_get(envs, array_name)
    array[array_idx] = array_new_number
    envs_set(envs, array_name, array)
    return array

@wrap
def do_get_array(envs, args):
    assert len(args) == 2 # name of array and index of array
    assert isinstance(args[0], str)
    assert isinstance(args[1], int)
    array_name = args[0]
    array_idx = args[1]
    array = envs_get(envs, array_name)
    return array[array_idx]

@wrap
def do_create_dictionary(envs, args):
    assert len(args) == 3 # name of dictionary, key and value
    assert isinstance(args[0], str)
    assert isinstance(args[1], list) and isinstance(args[2], list), "Please input your key and value with a list format"
    dictionary_name = args[0]
    dictionary = {}
    keys = args[1]
    values = args[2]
    assert len(keys) == len(values), "Key length doesn't match value length"
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    envs_set(envs, dictionary_name, dictionary)
    return dictionary

@wrap
def do_get_dictionary_key_value(envs, args):
    assert len(args) == 2 # name of dictionary, key
    assert isinstance(args[0], str)
    assert isinstance(args[1], str)
    dictionary = envs_get(envs, args[0])
    wanted_key_value = dictionary[args[1]]
    return wanted_key_value

@wrap
def do_set_dictionary_key_value(envs, args):
    assert len(args) == 3 # name of dictionary, key and new value
    assert isinstance(args[0], str)
    assert isinstance(args[1], str)
    dictionary = envs_get(envs, args[0])
    dictionary[args[1]] = args[2]
    envs_set(envs, args[0], dictionary)
    return dictionary

@wrap
def do_merge_dictionary(envs, args):
    assert len(args) == 2 # name of dictionary1, dictionary2
    dictionary1 = envs_get(envs, args[0])
    dictionary2 = envs_get(envs, args[1])
    merged_dictionary = dictionary1 | dictionary2
    return merged_dictionary

@wrap
def do_sequential(envs,args):
    assert len(args) > 0
    for operation in args:
        result = do(envs,operation)
    return result

@wrap
def do_create_class(envs, args):
    assert len(args) == 4  # class name, inheritance, constructor, all methods

    class_name = args[0]
    assert isinstance(args[0], str)
    # Check if the class already exists, and if not, create it
    envs_set(envs, class_name, [{}])
    class_env = envs_get(envs, class_name)

    base_class = None
    inherited_class = args[1]
    if inherited_class != "":
        assert isinstance(inherited_class, str)
        base_class = envs_get(envs, inherited_class)
        # Inherit constructor and functions to current class
        for dictionary in base_class:
            for key, value in dictionary.items():
                envs_set(class_env, key, value)   
        
    # Define the constructor and its parameters
    constructor_args = args[2]
    assert isinstance(constructor_args, list)
    # store value of constructor into class env
    do(class_env, constructor_args)

    function_code = args[3]  # The function code
    assert isinstance(function_code, list)
    
    if base_class is not None:
        # add the existing function of parent class to child class
        for dictionary in base_class:
            for method_name, method_func in dictionary.items():
                envs_set(class_env, method_name, method_func)
    # execute all the functions
    result = do(class_env, function_code)

    return result

OPERATIONS = {
    func_name.replace("do_",""): func_body
    for (func_name, func_body) in globals().items()
    if func_name.startswith("do_")
}

@wrap
def do(envs,expr):
    if isinstance(expr, int):
        return expr
    if isinstance(expr, float):
        return expr
    if isinstance(expr, str):
        return expr
    assert isinstance(expr,list)
    assert expr[0] in OPERATIONS, f"Unknown operation {expr[0]}"
    func = OPERATIONS[expr[0]]
    return func(envs, expr[1:])

def main():
    assert len(sys.argv) >= 2, "Usage: lgl_interpreter.py example_operations.gsc"
    if len(sys.argv) > 2:
        assert sys.argv[2] == "--trace"
        assert len(sys.argv) == 4, "must include a log file"

    with open(sys.argv[1], "r") as source_file:
        program = json.load(source_file)
    assert isinstance(program,list)
    envs = [{}]
    result = do(envs,program)
    print(f"=> {result}")
    if len(sys.argv) > 2:
        with open(sys.argv[3], "w") as trace_file:
            sys.stdout = trace_file

            events_list = []

            for func_id, info in FUNCTION_CALLS.items():
                events_list.append((info['start_time'], func_id, 'start', info))
                events_list.append((info['end_time'], func_id, 'stop', info))

            sorted_events = sorted(events_list, key=lambda x: x[0])

            header = "{:<10} {:<20} {:<10} {:<26}".format("id", "function_name", "event", "timestamp")
            print(header, file=trace_file)

            for event_time, func_id, event_type, info in sorted_events:
                line = "{:<10} {:<20} {:<10} {:<26}".format(func_id, info['func_name'], event_type, event_time)
                print(line, file=trace_file)

            sys.stdout = sys.__stdout__


if __name__ == "__main__":
    main()