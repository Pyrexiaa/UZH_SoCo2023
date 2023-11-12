# LGL Interpreter

The LGL Interpreter is a simple interpreter for a custom programming language called LGL (Let's Go Language). It supports various features, including basic operations, object-oriented programming concepts, and tracing functionalities.

# Table of Content
1. More Capabilities
   - 1.1 Implementation
   - 1.2 Usage
2. An Object System
   - 2.1 Implementation
   - 2.2 Usage
3. Tracing
   - 3.1 Logging
   - 3.2 Reporting
4. Design Decisions

# More Capabilities

## 1.1 Implementation

### 1. Mathematical Operations Functions

### a. Addition Function _‘do_addition’_
> This function performs addition on two operands.

Parameters:
- **_‘envs’_** : The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to two elements, the left operand, and the right operand.

Behavior:
- It ensures that there are exactly two arguments.
- Retrieves the values of the left and right operands by recursively invoking the **_‘do’_** function.
- Returns the sum of the left and right operands.

### b. Absolute Value Function _‘do_absolute’_
> This function calculates the absolute value of a given number.

Parameters:
- **_‘envs’_** : The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to one element, the number for which the absolute value is calculated.

Behavior:
- It ensures that there is exactly one argument.
- Retrieves the value of the operand by recursively invoking the **_‘do’_** function.
- Returns the absolute value of the operand.

### c. Subtraction Function _‘do_subtraction’_
> This function performs subtraction on two operands.

Parameters:
- **_‘envs’_** : The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to two elements, the left operand, and the right operand.

Behavior:
- It ensures that there are exactly two arguments.
- Retrieves the values of the left and right operands by recursively invoking the **_‘do’_** function.
- Returns the result of subtracting the right operand from the left operand.

### d. Multiplication Function _‘do_multiplication’_
> This function performs multiplication on two operands.

Parameters:
- **_‘envs’_** : The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to two elements.

Behavior:
- It ensures that there is exactly one argument.
- Retrieves the value of the operand by recursively invoking the **_‘do’_** function.
- Asserted that both operands are numeric instances (either integers or floats).
- Returns the result of multiplying the left and right operands, rounded to two decimal places.

### e. Division Function _‘do_division’_
> This function performs subtraction on two operands.

Parameters:
- **_‘envs’_** : The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to two elements, the numerator (left operand) and the denominator (right operand).

Behavior:
- It ensures that there are exactly two arguments.
- Retrieves the values of the left and right operands by recursively invoking the **_‘do’_** function.
- Ensures that the denominator is not zero to avoid division by zero.
- Asserted that both operands are numeric instances (either integers or floats).
- Returns the result of dividing the numerator by the denominator, rounded to two decimal places.

### f. Power Function _‘do_power’_
> This function calculates the power of one number to another.

Parameters:
- **_‘envs’_** : The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to two elements, the base and the exponent.

Behavior:
- It ensures that there are exactly two arguments.
- Retrieves the values of the left and right operands by recursively invoking the **_‘do’_** function.
- Asserted that both operands are numeric instances (either integers or floats).
- Returns the result of raising the base to the power of the exponent, rounded to two decimal places.

### 2. Print Statements

### a. Printing Function **_‘do_print’_**
> This function prints a specified value to the console.

Parameters:
- **_‘envs’_** : The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to only a single argument to be printed.

Behavior:
- It ensures that there is exactly one argument at the end.
- Retrieves the value of the argument by recursively invoking the **_‘do’_** function.
- Prints the value to the console.
- Does not return a value

### 3. While Loops
### a. Variable Update Function **_‘do_update’_**
> This function updates the value of a specified variable with a new value.

Parameters:
- **_‘envs’_** : The environment or context in which the operation is performed.
- **_‘args’_** : Asserted two elements - the variable name and the new value.

Behavior:
- It ensures that there are exactly two arguments.
- The first argument must be a string representing the variable name.
- Retrieves the new value by recursively invoking the **_‘do’_** function on the second argument.
- Updates the specified variable in the environment with the new value.
- Returns the updated value.

### b. Condition Evaluation Function **_‘evaluate_condition’_**
> This function evaluates a condition specified in a string format.

Parameters:
- **_‘envs’_** : The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to a string representing the condition to be evaluated (e.g. n <= 2).

Behavior:
- Strips any leading or trailing whitespaces from the condition string.
- Parses the condition string to identify the comparison operation (<=, >=, <, >, ==).
- Retrieves the variable name and the value from the condition.
- Performs the specified comparison operation and returns the result.
- Returns a boolean result of the condition evaluation.

### c. While Loop Function **_‘do_while_loops’_**
> This function implements a while loop in the LGL language.

Parameters:
- **_‘envs’_** : The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to three elements - the starting condition, stopping condition, and the operation.

Behavior:
- Ensures that there are at least three arguments.
- Sets the initial value by evaluating the starting condition using the **_‘do’_** function.
- Ensures that the starting condition is an initialization operation ('set').
- Retrieves the operation to be performed within the loop and the stopping condition by accessing the appropriate elements in the argument list.
- Executes the loop as long as the stopping condition, evaluated by the **_‘evaluate_condition’_** function, is true.
- Returns the result of the last operation performed within the loop.

### 4. Arrays
### a. Create Array Function **_‘do_create_array’_**
> Creating a new array of fixed size.

Parameters:
- **_‘envs’_** : The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to two elements - the name of the array and the content of the array.

Behavior:
- Ensures that there are exactly two arguments.
- Validates that the first argument is a string representing the name of the array.
- Validates that the second argument is a list, representing the content of the array.
- Sets the array in the environment using the **_‘envs_set’_** function.
- Returns the content of the created array.

### b. Set Array Element Function **_‘do_set_array’_**
> Setting the value at position I of an array to a new value.

Parameters:
- **_‘envs’_** : The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to three elements - the name of the array, the index of the array, and the new number to be set.

Behavior:
- Ensures that there are exactly three arguments.
- Validates that the first argument is a string representing the name of the array.
- Validates that the second and third arguments are integers representing the index and new number, respectively.
- Retrieves the array from the environment using the **_‘envs_get’_** function.
- Updates the array at the specified index with the new number.
- Sets the modified array back into the environment using the **_‘envs_set’_** function.
- Returns the modified array.

### c. Get Array Element Function **_‘do_get_array’_**
 > Getting the value at position i of an array.

Parameters:
- **_‘envs’_**: The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to two elements - the name of the array and the index of the array element to retrieve.

Behavior:
- Ensures that there are exactly two arguments.
- Validates that the first argument is a string representing the name of the array.
- Validates that the second argument is an integer representing the index of the array element.
- Retrieves the array from the environment using the **_‘envs_get’_** function.
- Returns the value at the specified index in the array.

### 5. Dictionaries
### a. Create Dictionary Function **_‘do_create_dictionary’_**
 > Creating a new dictionary.

Parameters:
- **_‘envs’_**: The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to three elements - the name of the dictionary, the list of keys, and the list of values.

Behavior:
- Ensures that there are exactly three arguments.
- Validates that the first argument is a string representing the name of the dictionary.
- Validates that the second and third arguments are lists representing the keys and values, respectively.
- Ensures that the lengths of the keys and values lists match.
- Creates a dictionary by pairing each key with its corresponding value.
- Sets the dictionary in the environment using the **_‘envs_set’_** function.
- Returns the created dictionary.

### b. Get Dictionary Key-Value Function **_‘do_get_dictionary_key_value’_**
 > Getting the value of a key.

Parameters:
- **_‘envs’_**: The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to two elements - the name of the dictionary and the key whose value is to be retrieved.

Behavior:
- Ensures that there are exactly two arguments.
- Validates that the first argument is a string representing the name of the dictionary.
- Validates that the second argument is a string representing the key whose value is to be retrieved.
- Retrieves the dictionary from the environment using the **_‘envs_get’_** function.
- Returns the value associated with the specified key.

### c. Set Dictionary Key-Value Function **_‘do_set_dictionary_key_value’_**
 > Setting the value of a key to a new value.

Parameters:
- **_‘envs’_**: The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to three elements - the name of the dictionary, the key to be set, and the new value.

Behavior:
- Ensures that there are exactly three arguments.
- Validates that the first argument is a string representing the name of the dictionary.
- Validates that the second argument is a string representing the key to be set.
- Retrieves the dictionary from the environment using the **_‘envs_get’_** function.
- Updates the dictionary by setting the value associated with the specified key to the new value.
- Sets the modified dictionary back into the environment using the **_‘envs_set’_** function.
- Returns the modified dictionary.

### d. Merge Dictionaries Function **_‘do_merge_dictionary’_**
 > Merging two dictionaries (using the | operator).

Parameters:
- **_‘envs’_**: The environment or context in which the operation is performed.
- **_‘args’_** : Asserted to containing two elements - the names of the two dictionaries to be merged.

Behavior:
- Ensures that there are exactly two arguments.
- Retrieves the dictionaries to be merged from the environment using the **_‘envs_get’_** function.
- Performs the merge operation using the **_‘|’_** (union) operator.
- Returns the merged dictionary.

## 1.2 Usage
To showcase the use of the implemented functionalities, a sample program has been created in a file named example_operations.gsc.
### Example Program (example_operations.gsc)
```
["sequential",

    # Multiplication
    ["multiplication", 3, 4],

    # Division
    ["division", 3, ["multiplication", 3, 4]],

    # Print Statement
    ["print", "This is just a test"],

    # While Loop
    ["while_loops", 
        ["sequential",
            ["print", "testing"],
            ["update", "n", ["addition", ["call", "n"], 3]]
        ],
        ["set", "n", 1],
        ["n <= 20"]
    ],

    # Arrays
    # Create Array, Get Array Value, Set Array Value
    ["create_array", "name", [2, 4, 5]],
    ["get_array", "name", 1],
    ["set_array", "name", 2, 4],

    # Dictionaries
    # Create Dictionary, Get Dictionary Value, Set Dictionary Value, Merge Dictionaries
    ["create_dictionary", "name", ["one"], [1]],
    ["get_dictionary_key_value", "name", "one"],
    ["set_dictionary_key_value", "name", "one", 4],
    ["create_dictionary", "name2", ["test", "test1", "test2"], [2,4,5]],
    ["get_dictionary_key_value", "name2", "test1"],
    ["set_dictionary_key_value", "name2", "test1", 6],
    ["merge_dictionary", "name", "name2"]
]
```

### Running the Interpreter
To execute the interpreter with the example program file, run the following command:
```
python lgl_interpreter.py example_operations.gsc
```

# An Object System
## 2.1 Implementation

### Create Class Function **_‘do_create_class’_**
Parameters:
- **_‘envs’_** : The environment or context in which the operation is performed.
- **_‘args’_** : A list containing four elements - class name, inheritance, constructor, and all methods.

Behavior:
- Ensures that there are exactly four arguments.
- Validates that the first argument is a string representing the name of the class.
- Checks if the class already exists. If not, it creates a new class environment in the global environment.
- Retrieves the created class environment using the **_‘envs_get’_** function.
- Handles class inheritance by checking if there is a base class specified.
   - If there is a base class, retrieves its environment using **_‘envs_get’_**.
   - Inherits the constructor and functions from the base class to the current class environment.
- Defines the constructor by executing its code using the **_‘do’_** function and storing the result in the class environment.
- Defines the class methods by executing their code using the **_‘do’_** function and storing the results in the class environment.
- If there is a base class, adds the existing functions of the parent class to the child class.
- Executes all the class functions.
- Returns the result of executing the class functions.

### Class Definition and Object Instantiation
In the LGL Interpreter, the object system allows for class definition and object instantiation. The **_“do_create_class’_** function is responsible for creating classes. It takes four arguments: class name, inheritance, constructor, and all methods.
Example:
```
['do_create_class', 'Square', 'Shape', ['square_new', 'name', 'side'], [['square_area', 'thing']]]
```

### Single Inheritance
Single inheritance is achieved by allowing a class to inherit from a single base class. The **_‘do_create_class’_** function handles the inheritance process, copying the constructor and methods from the base class to the derived class.
Example:
```
['do_create_class', 'Circle', 'Shape', ['circle_new', 'name', 'radius'], [['circle_area', 'thing']]]
```

### Polymorphism
Polymorphism is supported through the ability to define and execute methods with the same name across different classes. The **_‘do_create_class’_** function allows for the definition and execution of methods within each class.
Example:
```
['do_create_class', 'Shape', '', ['shape_new', 'name'], [['shape_density', 'thing', 'weight']]]
```

## 2.2 Usage
To test the object system capabilities, a sample program has been created in a file named **_‘example_class.gsc’_** .
### Example Class Definitions (example_class.gsc)
```
 ["sequential",

    # Shape Class
    # The **‘Shape’** class serves as the base class for geometric shapes. It includes a constructor and a method to calculate shape density.
    ["create_class", "Shape", "",   ["sequential",
                                        ["set", "name", "anyshape"],
                                        ["set", "weight", 5]
                                    ],
        ["sequential",
            ["set", "shape_density",
                ["function", ["weight", "volume"],
                    ["division", ["call", "weight"], ["call", "volume"]]
                ]
            ]
        ]
],

    # Square Class (Inherits from Shape)
    # The **‘Square’** class inherits from the **‘Shape’** class and introduces additional attributes and methods, such as **‘side’** and **‘square_area’** .
    ["create_class", "Square", "Shape", ["sequential",
                                            ["set", "name", "sq"], 
                                            ["set", "side", 3]
                                        ],
        ["sequential", 
            ["set", "square_area",
                ["function", ["side"],
                    ["multiplication", ["call", "side"], ["call", "side"]]
                ]
            ],
            ["print", ["apply", "square_area", ["call", "side"]]],
            ["set", "volume", 
                ["multiplication", ["call", "side"],
                    ["multiplication", ["call", "side"], ["call", "side"]]
                ]
            ],
            ["set", "square_density",
                ["apply", "shape_density", 
                    ["call", "weight"], ["call", "volume"]
                ]
            ]
        ]
],

    # Circle Class (Inherits from Shape)
    # Similar to **‘Square’** , the **‘Circle’** class inherits from **‘Shape’** and introduces attributes like **‘radius’** and methods like **‘circle_area’**.
    ["create_class", "Circle", "Shape", ["sequential",
                                            ["set", "name", "ci"], 
                                            ["set", "radius", 2]
                                        ],
        ["sequential", 
            ["set", "circle_area",
                ["function", ["radius"],
                    ["multiplication", 
                        3.142, 
                            ["multiplication", ["call", "radius"], ["call", "radius"]]
                        
                    ]
                ]
            ],
            ["print", ["apply", "circle_area", ["call", "radius"]]],
            ["set", "volume", 
                ["multiplication", 3.142,
                    ["multiplication", ["call", "radius"], 
                        ["multiplication", ["call", "radius"], ["call", "radius"]
                        ]
                    ]
                ]
            ],
            ["set", "circle_density",
                ["apply", "shape_density", 
                    ["call", "weight"], ["call", "volume"]
                ]
            ]
        ] 
],

    # Perform an addition operation to demonstrate polymorphism
    ["addition", ["call_object", "square_density", "Square"], ["call_object", "circle_density", "Circle"]]
]
```

### Running the Interpreter
To execute the interpreter with the example class file, run the following command:
```
python lgl_interpreter.py example_class.gsc
```

# Tracing
Tracing is an essential feature for debugging and profiling software. In this enhancement, the LGL interpreter has been augmented to include a tracing functionality. The **‘--trace option’** , when used with the interpreter, logs details about the start and end times of each function into a specified trace file. This feature is implemented using decorators introduced in Chapter 9.

## 3.1 Logging
Tracing functionalities have been added to the LGL Interpreter. You can generate a trace file by running a program with the --trace option:
```
python lgl_interpreter.py example_trace.gsc --trace trace_file.log
```
The trace file will contain details about the start and end times of each function call.

### Trace File Format
The trace file is in CSV format and contains the following columns:
- ID: A unique identifier for distinguishing separate calls of the same function.
- Function Name: The name of the function that was called.
- Event: Indicates if the function has started (start) or ended (stop).
- Timestamp: Logs the timestamp of the event.
- 
An example trace file (trace_file.log) is shown below:
```
id,function_name,event,timestamp
358887,add_cubes,start,2023-10-24 19:20:08.045086
270697,get_cube_power,start,2023-10-24 19:20:08.045279
270697,get_cube_power,stop,2023-10-24 19:20:08.045657
137801,get_cube_power,start,2023-10-24 19:20:08.045788
137801,get_cube_power,stop,2023-10-24 19:20:08.045850
358887,add_cubes,stop,2023-10-24 19:20:08.045898
```

## 3.2 Reporting
This reporting tool processes a trace file generated by the LGL interpreter with tracing enabled. It provides an aggregated summary of function calls, including the number of calls, total execution time, and average execution time.

Run the reporting tool using the following command:
```
python reporting.py trace_file.log
```
The tool provides aggregated information on function calls, including the number of calls, total execution time, and average execution time.

### Reporting Output
The reporting tool generates a table with the following columns:
- Function Name: The name of the function.
- Num. of Calls: The number of times the function was called.
- Total Time (ms): The total execution time of the function, summed across all executions.
- Average Time (ms): The average execution time, obtained by dividing the Total Time with the Num. of Calls.

An example reporting output is presented below:
```
| Function Name | Num. of Calls | Total Time (ms) | Average Time (ms)|
|----------------|---------------|------------------|-------------------|
| add_cubes      | 1             | 0.812            | 0.812             |
| get_cube_power | 2             | 0.440            | 0.220             |
```

# Design Decisions
## 1. Function Wrapping (@wrap Decorator)
We adopted a function wrapping approach using the @wrap decorator. This decision was made to implement basic tracing functionalities efficiently. By wrapping each function call, we were able to capture the start and end times, as well as other relevant information, for logging and reporting.

## 2. Mathematical Operations Functions
Each mathematical operation function (do_addition, do_subtraction, do_multiplication, do_division, do_power, do_absolute) follows a consistent structure for clarity and maintainability. They validate the number and types of arguments, recursively invoke the do function for operand evaluation, and handle specific conditions such as division by zero.

## 3. Numeric Type Checking
We added explicit checks for numeric types (int or float) in mathematical operation functions to ensure robustness. This prevents unexpected behavior and ensures that operations are performed only on valid numeric operands.

## 4. Rounding Results
To enhance result precision and readability, the mathematical operation functions return rounded results (up to two decimal places) for multiplication, division, and power operations.

## 5. Tracing Implementation
The tracing feature is introduced by providing an optional --trace argument when executing the LGL interpreter. The @wrap decorator captures function call details, and the main() function generates a CSV-formatted trace file for subsequent analysis.

## 6. Reporting Tool
The reporting tool (reporting.py) processes the trace file and presents aggregated results, including the number of function calls, total execution time, and average execution time for each function. This tool aids in performance analysis and debugging.
