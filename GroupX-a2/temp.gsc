["multiplication", 3, 4]
["multiplication", 'test', 4]
["division", 3, 4]
["division", 3, 0]
["division", 'test', 0]
["division", 3, ["multiplication", 3, 4]]
["print", 3]
["print", ["multiplication", 3, 4]]
["print", "This is just a test"]

["while_loops", 
    ["print", "testing"],
    ["set", "n", 1],
    ["n <= 20"]
]

["sequential",
    ["create_array", "name", [2, 4, 5]],
    ["get_array", "name", 1],
    ["set_array", "name", 2, 4]
]

["sequential",
    ["create_dictionary", "name", ["one"], [1]],
    ["get_dictionary_key_value", "name", "one"],
    ["set_dictionary_key_value", "name", "one", 4],
    ["create_dictionary", "name2", ["test", "test1", "test2"], [2,4,5]],
    ["get_dictionary_key_value", "name2", "test1"],
    ["set_dictionary_key_value", "name2", "test1", 6],
    ["merge_dictionary", "name", "name2"]
]

["sequential",
    ["create_class", "Shape", "", ["name"],
        ["sequential",
            ["set", "shape_density",
                ["function", ["thing", "weight"],
                    ["division", "weight", "thing"]
                ]
            ]
        ]
    ],

    ["create_class", "Square", "Shape", ["name", "side"],
        ["sequential", 
            ["set", "square_area",
                ["function", ["thing"],
                    ["multiplication", "side", "side"]
                ]
            ]
        ]
    ],

    ["create_class", "Circle", "Shape", ["name", "radius"],
        ["sequential", 
            ["set", "circle_area",
                ["function", ["thing"],
                    ["multiplication", 
                        ["3.14", 
                            ["multiplication", "side", "side"]
                        ]
                    ]
                ]
            ]
        ]  
    ]
]