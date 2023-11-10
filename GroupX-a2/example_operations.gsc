["sequential",
    ["multiplication", 3, 4],

    ["division", 3, ["multiplication", 3, 4]],

    ["print", "This is just a test"],

    ["while_loops", 
        ["sequential",
            ["print", "testing"],
            ["update", "n", ["addition", ["call", "n"], 3]]
        ],
        ["set", "n", 1],
        ["n <= 20"]
    ],

    ["create_array", "name", [2, 4, 5]],
    ["get_array", "name", 1],
    ["set_array", "name", 2, 4],

    ["create_dictionary", "name", ["one"], [1]],
    ["get_dictionary_key_value", "name", "one"],
    ["set_dictionary_key_value", "name", "one", 4],
    ["create_dictionary", "name2", ["test", "test1", "test2"], [2,4,5]],
    ["get_dictionary_key_value", "name2", "test1"],
    ["set_dictionary_key_value", "name2", "test1", 6],
    ["merge_dictionary", "name", "name2"]
]



