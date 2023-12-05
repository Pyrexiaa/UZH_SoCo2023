# Example Command: python run_tests.py --select read
# Example Command without parser: python run_tests.py 

import argparse
import inspect
import time
import os
from file_manager import read_file, create_file, write_file, delete_file

# =================== Read file tests ======================

def test_read_file_not_exists(file_path):
    file_content = read_file(file_path)
    assert file_content != None, "File does not exists"

def test_read_file_content_different(file_path, content):
    file_content = read_file(file_path)
    assert file_content == content, "File content is different with the input content"

# =================== Create file tests ======================

def test_create_file_already_existed(file_path):
    assert not os.path.exists(file_path), "File with the same name has already existed"

def test_create_file_not_exists(file_path, content):
    if not os.path.exists(file_path):
        success = create_file(file_path, content)
        assert success == True, "File was not created successfully"

# =================== Write file tests ======================

def test_write_file_not_exists(file_path):
    assert os.path.exists(file_path), "Cannot write content to non-existing file"

def test_write_file_existed(file_path, content):
    if os.path.exists(file_path):
        success = write_file(file_path, content)
        assert success == True, "Content is not written successfully on the existing file"

# =================== Delete file tests ======================

def test_delete_file_not_exists(file_path):
    assert os.path.exists(file_path), "Cannot delete a non-existing file"

def test_delete_file_existed(file_path):
    if os.path.exists(file_path):
        success = delete_file(file_path)
        assert success == True, "File is not deleted successfully"

def find_tests():
    test_functions_by_category = {}
    for (name, obj) in globals().items():
        if name.startswith(f"test_"):
            category = name.split('_')[1]
            if category not in test_functions_by_category:
                test_functions_by_category[category] = []
            test_functions_by_category[category].append(obj)
    return test_functions_by_category

class TestFile():
    def __init__(self, file_path, content="", arguments="", test_function_dictionary=""):
        super().__init__()
        self.file_path = file_path
        self.content = content
        self.arguments = arguments
        self.function_results = {} 
        self.test_function_dictionary = test_function_dictionary
        self.selected_pattern = ""

    def setup(self):
        function_name = inspect.currentframe().f_back.f_code.co_name
        print(f"Starting to setup environment for {function_name}...")
        self.starting_time = time.time()
    
    def teardown(self):
        function_name = inspect.currentframe().f_back.f_code.co_name
        ending_time = time.time()
        total_time = ending_time - self.starting_time
        print("==============================================================")
        for method, results in self.function_results.items():
            if function_name == method:
                for result_key, result_number in results.items():
                    print(f"{result_key}: {result_number}")
        print(f"Total time used for function {function_name} is {total_time}s")
        print("==============================================================")
        print(f"Cleaning up the environment for {function_name}...")

    def get_current_method_name(self):
        frame = inspect.currentframe()
        try:
            method_name = frame.f_back.f_code.co_name
            return method_name
        finally:
            del frame

    def update_results(self, result, key_word):
        method_name = "test_"+key_word+"_file"
        if method_name not in self.function_results:
            self.function_results[method_name] = {"Pass": 0, "Fail": 0, "Error": 0}
        self.function_results[method_name][result] += 1

    def execute_functions(self, key_word):
        for category, functions in self.test_function_dictionary.items():
            if category == key_word:
                function_number = len(functions)
                print(f"Executing {function_number} functions with the key word - {key_word}")
                for function in functions:
                    try:
                        num_params = len(inspect.signature(function).parameters)
                        if num_params == 1:
                            function(self.file_path)
                            self.update_results("Pass", key_word)
                        elif num_params == 2:
                            function(self.file_path, self.content)
                            self.update_results("Pass", key_word)
                    except AssertionError as e:
                        print("Assertion error: ",e)
                        self.update_results("Fail", key_word)
                    except Exception:
                        self.update_results("Error", key_word)

    def test_read_file(self):
        self.setup()
        self.execute_functions('read')
        self.teardown()

    def test_create_file(self):
        self.setup()
        self.execute_functions('create')
        self.teardown()

    def test_write_file(self):
        self.setup()
        self.execute_functions('write')
        self.teardown()

    def test_delete_file(self):
        self.setup()
        self.execute_functions('delete')
        self.teardown()

    def introspection(self):
        test_functions = [obj for _, obj in inspect.getmembers(self, inspect.ismethod)]
        self.selected_pattern = self.arguments.select
        selected_functions = 0
        for test_func in test_functions:
            if self.selected_pattern in test_func.__name__ and test_func.__name__.startswith("test_"):
                selected_functions += 1
                test_func()
        if selected_functions == 0:
            print(f"There is no method with the pattern ({self.selected_pattern}) mentioned")

        print(f"================Completed testing for {self.file_path}================\n\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='To allow users run only the tests that contain the pattern in their name')
    parser.add_argument('--select', type=str, default='', help='Function name pattern')
    args = parser.parse_args()

    test_function_dictionary = find_tests()
    test_data = {
        'test1.txt': 'Content for test 1',
        'test2.txt': 'Software Construction the best!',
        'test3.txt': 'I have no idea what am I testing',
    }
    for file_path, content in test_data.items():
        test_file = TestFile(file_path=file_path, content=content, arguments=args, test_function_dictionary=test_function_dictionary)
        test_file.introspection()
     
    

