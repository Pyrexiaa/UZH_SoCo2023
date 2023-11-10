["sequential",
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
    ["addition", ["call_object", "square_density", "Square"], ["call_object", "circle_density", "Circle"]]
]