# Table of Content
1. File Manager -- **‘file_manager.py’**
   - File Manager Functions
     - read_file
     - create_file
     - write_file
     - delete_file
   - Usage
   - Exception Handling
2. File Manager Test Suite -- **‘run_tests.py’**
   - Test Functions
     - Read File Tests
     - Create File Tests
     - Write File Tests
     - Delete File Tests
   - Test File Class
   - Script Execution

# 1. File Manager _‘file_manager.py’_

File Manager is a Python script that performs basic file manipulation functions. These functions allow you to interface with files on your system.

## File Manager Functions
### read_file
> Read the content of a file if it exists. If the file does not exist, it returns None.

Parameters
- **_‘file_name’_** (str) : The name of the file you want to read.

Returns
- **_‘str’_** : The content of the file.
- **_‘None’_** : If the file does not exist.

### create_file_
> Create a new file. If the file is successfully created, it returns True. If there's an issue creating the file, it returns False.

Parameters
- **_‘file_name’_** (str) : The name of the file you want to create.
- **_‘content’_** (str, optional) : Optional content to write to the file when it is created. The default is an empty string.

Returns
- **_‘True’_** : If the content is successfully written.
- **_‘False’_** : If there's an issue writing to the file.

### write_file
> Add text to an existing file. It returns True if the material is successfully written. It returns False if there is an error while writing to the file.

Parameters
- **_‘file_name’_** (str) : The name of the file you want to write to.
- **_‘content’_** (str) : The content you want to write to the file.

Returns
- **_‘True’_** : If the content is successfully written.
- **_‘False’_** : If there's an issue writing to the file.


### delete_file
> Remove a file. It returns True if the file is successfully removed. If the file cannot be deleted, it returns False.

Parameters
- **_‘file_name’_** (str) : The name of the file you want to delete.

Returns
- **_‘True’_** : If the content is successfully deleted.
- **_‘False’_** : If there's an issue deleting the file.

## Usage
You can use the functions in the File Manager script to interact with files in your Python projects. Here's an example of how to use these functions:

```
import file_manager

# Read a file
content = file_manager.read_file("/path/to/your/file.txt")
if content is not None:
    print("File content:")
    print(content)
else:
    print("The file does not exist.")

# Create a new file
if file_manager.create_file("/path/to/new/file.txt"):
    print("File created successfully.")
else:
    print("Failed to create the file.")

# Write to a file
if file_manager.write_file("/path/to/existing/file.txt", "This is the new content."):
    print("Content written successfully.")
else:
    print("Failed to write content to the file.")

# Delete a file
if file_manager.delete_file("/path/to/your/file.txt"):
    print("File deleted successfully.")
else:
print("Failed to delete the file.")
```

Replace /path/to/your/file.txt with the actual file path you want to read.

## Exception Handling
Exception handling is built into the **_‘read_file’_** function to address any potential problems. It manages two different kinds of exceptions:

- **_‘FileNotFoundError’_** : The function returns None if the provided file does not exist.
- **_‘Exception’_** : If the function encounters any other unexpected errors, it emits an error message and returns None.

This error handling ensures that the program does not crash while attempting to read a non-existent file or when other unforeseen issues arise.

# 2. File Manager Test Suite _‘run_tests.py’_

File Manager Test Suite is a Python script that executes a series of tests on the File Manager's file manipulation functions. These tests guarantee that file operations including reading, creating, writing, and removing function properly.

## Test Functions
### Read File Tests

### Test ‘test_read_file_not_exists(file_path)’
> This test examines the behavior of the read_file function when given the path to a non-existent file, asserting that the function should return None in this situation.

Parameters
- **_‘file_path’_** (str) : The path to the non-existing file to be tested.

Assertion
- The test asserts that the function's result is None, indicating that the file does not exist.

### Test ‘test_read_file_content_different(file_path, content)’
> This test determines whether the read_file function can read the content of an existing file and compare it to the provided content. The objective is to guarantee that the function reads the file accurately and matches it with the provided content.

Parameters
- **_‘file_path’_** (str) : The path to the file to be tested.
- **_‘content’_** (str) : The expected content that should match the file's content.

Assertion
- The test asserts that the function's result matches the provided content, indicating that the file's content is the same as expected.

### Create File Tests

- ### Test ‘test_create_file_already_existed(file_path)’
> This test ensures that the create_file function handles scenarios where a file with the same name already exists correctly.

Parameters
- **_‘file_path’_** (str) : The path to the file that may already exist.

Assertion
- The rest asserts that the function detects the existing file and raises an error.

### Test ‘test_create_file_not_exists(file_path, content)’
> This test checks if the create_file function successfully creates a new file with the provided content when the file does not already exist.

Parameters
- **_‘file_path’_** (str) : The path to the file to be created.
- **_‘content’_** (str) : The initial content of the file.

Assertion
- The test asserts that the function successfully creates the new file with the provided content.

### Write File Tests

### Test ‘test_write_file_not_exists(file_path)’
> This test ensures that the write_file function correctly handles attempts to write to a non-existing file.

Parameters
- **_‘file_path’_** (str) : The path to the file that may not exist.

Assertion
- The test asserts that the function raises an error when trying to write to a non-existing file.

### Test ‘test_write_file_existed(file_path, content)’
> This test checks if the write_file function successfully writes content to an existing file.

Parameters
- **_‘file_path’_** (str) : The path to the existing file.
- **_‘content’_** (str) : The content to be written to the file.

Assertion
- The test asserts that the function successfully writes the content to the existing file.

### Delete File Tests

### Test ‘test_delete_file_not_exists(file_path)’
> This test verifies that the delete_file function correctly handles attempts to delete a non-existing file.

Parameters
- **_‘file_path’_** (str) : The path to the file that may not exist.

Assertion
- The test asserts that the function raises an error when trying to delete a non-existing file.

### Test ‘test_delete_file_existed(file_path)’
> This test checks if the delete_file function successfully deletes an existing file.

Parameters
- **_‘file_path’_** (str) : The path to the existing file to be deleted.

Assertion
- The test asserts that the function successfully deletes the existing file.	

## TestFile Class
> The TestFile class provides a structure for organizing and executing the tests for a specific file and its associated content. It allows for test setup, execution, and teardown.

### ‘setup()’
- The **_‘setup’_** method is used to set up the environment before running a test. It starts counting the time when it's called.

### ‘teardown()’
- The **_‘teardown’_** method is responsible for cleaning up the environment after a test has been executed. It stops counting the time, calculates the execution time, and reports it in the test results.

### ‘update_results(result, key_word)’
- The **_‘update_results’_** method records the results (Pass, Fail, Error) for each test function. This dynamic behavior allows the **_‘update_results’_** function to adapt to different test methods and categories, keeping track of the test results dynamically as tests are executed. It ensures that you can monitor and collect real-time information about how many tests passed, failed, or resulted in errors for each category.

### ‘execute_functions(key_word)’
- The **_‘execute_functions’_** method adapts its behavior based on the **_‘key_word’_** (e.g., 'read', 'create', 'write', 'delete') and dynamically executes the relevant test functions while tracking their results dynamically. It allows you to select and run tests for specific categories and handle the results as they occur.

### Test Execution Method
> The class defines separate methods for running tests related to reading, creating, writing, and deleting files.

### ‘introspection()’
- The **_‘introspection’_** method uses the inspect module to dynamically introspect and find all the methods (test functions) within the current instance of the class. It dynamically adapts to the provided selected_pattern by checking if any of the discovered test methods match the pattern. This allows users to specify a pattern (e.g., using a command-line argument) to select which specific test methods to run. It dynamically executes the selected test methods based on the matching pattern and provides dynamic feedback by printing a message if no matching methods are found based on the provided pattern.

## Script Execution

### Parser Argument
Parser arguments, also known as command-line arguments or command-line options, are a way to configure the behavior of a Python script or program when it is executed from the command line. They allow users to pass input, configuration settings, or instructions to the program at runtime.

### **_‘--select’_** (Optional)
- Description: This argument allows users to specify a pattern for selecting and running specific tests.
- Usage: Users can provide a pattern as an argument value to --select to filter tests by their names. Only the tests with names containing the specified pattern will be executed.

### Example Command 1: Run Tests with Pattern Selection
```
python run_tests.py --select read
```
This command selects and runs only the tests containing the pattern "read" in their names.

### Example Command 2: Run All Tests (No --select Argument):
```
python run_tests.py
```
Running the script without the --select argument will execute all available tests.

These parser arguments provide flexibility for users to customize their testing experience. Users can choose to run a specific subset of tests by providing a pattern with --select or run all available tests by omitting the --select argument.

By using parser arguments, your project becomes more user-friendly and adaptable to different testing scenarios. Users can easily control which tests to execute without modifying the script's code.
