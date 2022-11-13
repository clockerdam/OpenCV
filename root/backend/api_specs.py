unlabeled_resume_dict = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        },
        "contactInfo": {
            "type": "object",
            "properties": {
                "address": {
                    "type": "string"
                },
                "website": {
                    "type": "string"
                },
                "linkedin": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "phoneNumber": {
                    "type": "string"
                },
                "email": {
                    "type": "string"
                },
                "github": {
                    "type": "string"
                },
                "birthday": {
                    "type": "string"
                },
                "family": {
                    "type": "string"
                }
            }
        }
    }
}
labeled_resume_dict = {
    "type": "object",
    "properties": {
        "title": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "string"
                },
                "label": {
                    "type": "integer"
                }
            },
            "required": [
                "value",
                "label"
            ]
        },
        "contactInfo": {
            "type": "object",
            "properties": {
                "address": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "string"
                        },
                        "label": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "value",
                        "label"
                    ]
                },
                "website": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "string"
                        },
                        "label": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "value",
                        "label"
                    ]
                },
                "linkedin": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "string"
                        },
                        "label": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "value",
                        "label"
                    ]
                },
                "name": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "string"
                        },
                        "label": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "value",
                        "label"
                    ]
                },
                "phoneNumber": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "string"
                        },
                        "label": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "value",
                        "label"
                    ]
                },
                "email": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "string"
                        },
                        "label": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "value",
                        "label"
                    ]
                },
                "github": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "string"
                        },
                        "label": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "value",
                        "label"
                    ]
                },
                "birthday": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "string"
                        },
                        "label": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "value",
                        "label"
                    ]
                },
                "family": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "string"
                        },
                        "label": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "value",
                        "label"
                    ]
                }
            },
            "required": [
                "address",
                "website",
                "linkedin",
                "name",
                "phoneNumber",
                "email",
                "github",
                "birthday",
                "family"
            ]
        },
        "summary": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "string"
                },
                "label": {
                    "type": "integer"
                }
            },
            "required": [
                "value",
                "label"
            ]
        },
        "experience": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "company": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "location": {
                            "type": "string"
                        },
                        "fromDate": {
                            "type": "string"
                        },
                        "toDate": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "company",
                        "title",
                        "location",
                        "fromDate",
                        "toDate",
                        "description"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "company": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "location": {
                            "type": "string"
                        },
                        "fromDate": {
                            "type": "string"
                        },
                        "toDate": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "company",
                        "title",
                        "location",
                        "fromDate",
                        "toDate",
                        "description"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "company": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "location": {
                            "type": "string"
                        },
                        "fromDate": {
                            "type": "string"
                        },
                        "toDate": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "company",
                        "title",
                        "location",
                        "fromDate",
                        "toDate",
                        "description"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "company": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "location": {
                            "type": "string"
                        },
                        "fromDate": {
                            "type": "string"
                        },
                        "toDate": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "company",
                        "title",
                        "location",
                        "fromDate",
                        "toDate",
                        "description"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "company": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "location": {
                            "type": "string"
                        },
                        "fromDate": {
                            "type": "string"
                        },
                        "toDate": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "company",
                        "title",
                        "location",
                        "fromDate",
                        "toDate",
                        "description"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "company": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "location": {
                            "type": "string"
                        },
                        "fromDate": {
                            "type": "string"
                        },
                        "toDate": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "company",
                        "title",
                        "location",
                        "fromDate",
                        "toDate",
                        "description"
                    ]
                }
            ]
        },
        "education": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "institution": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "location": {
                            "type": "string"
                        },
                        "fromDate": {
                            "type": "string"
                        },
                        "toDate": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "institution",
                        "title",
                        "location",
                        "fromDate",
                        "toDate",
                        "description"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "institution": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "location": {
                            "type": "string"
                        },
                        "fromDate": {
                            "type": "string"
                        },
                        "toDate": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "institution",
                        "title",
                        "location",
                        "fromDate",
                        "toDate",
                        "description"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "institution": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "location": {
                            "type": "string"
                        },
                        "fromDate": {
                            "type": "string"
                        },
                        "toDate": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "institution",
                        "title",
                        "location",
                        "fromDate",
                        "toDate",
                        "description"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "institution": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "location": {
                            "type": "string"
                        },
                        "fromDate": {
                            "type": "string"
                        },
                        "toDate": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "institution",
                        "title",
                        "location",
                        "fromDate",
                        "toDate",
                        "description"
                    ]
                }
            ]
        },
        "interests": {
            "type": "array",
            "items": [
                {
                    "type": "string"
                }
            ]
        },
        "accomplishments": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string"
                        },
                        "fromDate": {
                            "type": "string"
                        },
                        "toDate": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "title",
                        "fromDate",
                        "toDate",
                        "description"
                    ]
                }
            ]
        },
        "languages": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "proficiency": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "name",
                        "proficiency"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "proficiency": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "name",
                        "proficiency"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "proficiency": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "name",
                        "proficiency"
                    ]
                }
            ]
        },
        "projects": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string"
                        },
                        "fromDate": {
                            "type": "string"
                        },
                        "toDate": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "title",
                        "fromDate",
                        "toDate",
                        "description"
                    ]
                }
            ]
        },
        "softSkills": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "proficiency": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "name",
                        "proficiency"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "proficiency": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "name",
                        "proficiency"
                    ]
                }
            ]
        },
        "hardSkills": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "proficiency": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "name",
                        "proficiency"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "proficiency": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "name",
                        "proficiency"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "proficiency": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "name",
                        "proficiency"
                    ]
                }
            ]
        },
        "certifications": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string"
                        },
                        "level": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "date": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "title",
                        "level",
                        "description",
                        "date"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string"
                        },
                        "level": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "date": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "title",
                        "level",
                        "description",
                        "date"
                    ]
                }
            ]
        },
        "patents": {
            "type": "array",
            "items": {}
        },
        "extracurriculars": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string"
                        },
                        "fromDate": {
                            "type": "string"
                        },
                        "toDate": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "title",
                        "fromDate",
                        "toDate",
                        "description"
                    ]
                }
            ]
        }
    },
    "required": [
        "title",
        "contactInfo",
        "summary",
        "experience",
        "education",
        "interests",
        "accomplishments",
        "languages",
        "projects",
        "softSkills",
        "hardSkills",
        "certifications",
        "patents",
        "extracurriculars"
    ]
}
unlabeled_example = {
    "title": "Data scientist",
    "contactInfo": {
        "address": "Stockholmsvägen 15",
        "website": "",
        "linkedin": "www.linkedin.com/in/caterina- bonazzi ",
        "name": "Caterina Bonazzi",
        "phoneNumber": "",
        "email": "caterinabonazzi@gmail.com",
        "github": "",
        "birthday": "",
        "family": "Husband and two children"
    },
    "summary": "I am a passionate data scientist curious and ambitious. I love to dig into data trying to bring order in a word of chaos.",
    "experience": [
        {
            "company": "IKEA",
            "title": "Data Scientist",
            "location": "Malmö, Sweden",
            "fromDate": "September 2021",
            "toDate": "Present",
            "description": ""
        },
        {
            "company": "Accenture",
            "title": "Data Scientist @ A>RACE",
            "location": "Milano, Italy",
            "fromDate": "November 2019",
            "toDate": "September 2021",
            "description": "A>RACE is the Accenture Risk Analytics Center of Excellence. It is a center created within Accenture which deals with risk management projects with the objective to provide innovative IT solutions."
        },
        {
            "company": "Accenture",
            "title": "Stage Consulting @ A>RACE",
            "location": "Milano, Italy",
            "fromDate": "April 2019",
            "toDate": "October 2019",
            "description": ""
        },
        {
            "company": "Università di Bologna",
            "title": "Tutor",
            "location": "Bologna, Italy",
            "fromDate": "October 2017",
            "toDate": "October 2018",
            "description": "I was the tutor of the Master degree Direzione aziendale taught in the University of Bologna for one year. I managed the relations between professors and students, organized the schedules for the academic year and dealt with administrative issues related to the course's admission and graduation."
        },
        {
            "company": "Fondazione Golinelli",
            "title": "Mentee",
            "location": "",
            "fromDate": "November 2017",
            "toDate": "July 2018",
            "description": "Mentee in the ICARO project. The project which last 9 months is an intensive entrepreneurial path aimed to bring university students close to the business culture. During this path, I learned to work together with students coming from different realities using a design thinking approach to solve real business cases."
        },
        {
            "company": "Trade Marketing Studio",
            "title": "Market research intern",
            "location": "Bologna, Italy",
            "fromDate": "June 2016",
            "toDate": "September 2016",
            "description": "The company is specialized in trade marketing and GDO marketing. The competences and responsibilities I undertook concerned: marketing, market researches, the creation of databases, store-check, CRM I also created presentations for customers and infographics for fair events."
        }
    ],
    "education": [
        {
            "institution": "Università di Bologna",
            "title": "Second cycle degree, Statistical science",
            "location": "Bologna",
            "fromDate": "2017",
            "toDate": "2019",
            "description": ""
        },
        {
            "institution": "Lund University School of Economics and Management",
            "title": "Erasmus exchange student",
            "location": "Lund",
            "fromDate": "August 2018",
            "toDate": "January 2019",
            "description": "Erasmus exchange student"
        },
        {
            "institution": "Università di Bologna",
            "title": "Laurea triennale in Scienze dell'Economia e della Gestione Aziendale, Management e marketing",
            "location": "Bologna",
            "fromDate": "2014",
            "toDate": "2017",
            "description": ""
        },
        {
            "institution": "ITC Enrico Mattei",
            "title": "",
            "location": "Rome, Italy",
            "fromDate": "2009",
            "toDate": "2014",
            "description": ""
        }
    ],
    "interests": [
        "VALUE",
        "VALUE"
    ],
    "accomplishments": [
        {
            "title": "Olympic gold medal in rowing",
            "fromDate": "2010-01-23",
            "toDate": "",
            "description": "Tight race"
        }
    ],
    "languages": [
        {
            "name": "Spanish",
            "proficiency": 5
        },
        {
            "name": "Korean",
            "proficiency": 4
        },
        {
            "name": "English",
            "proficiency": 1
        }
    ],
    "projects": [
        {
            "title": "Project for Data Science",
            "fromDate": "2022-08-23",
            "toDate": "Today",
            "description": "Built a NLP tool for optimizing ebay item descriptions. The professor didn't like it."
        }
    ],
    "softSkills": [
        {
            "name": "Presenting",
            "proficiency": 5
        },
        {
            "name": "Debating",
            "proficiency": 2
        }
    ],
    "hardSkills": [
        {
            "name": "R",
            "proficiency": 5
        },
        {
            "name": "Python",
            "proficiency": 5
        },
        {
            "name": "Machine Learning",
            "proficiency": 4
        }
    ],
    "certifications": [
        {
            "title": "Entrepreneurship - ICARO Bologna",
            "level": "",
            "description": "",
            "date": ""
        },
        {
            "title": "SAS Certified Base Programmer for SAS 9",
            "level": "Basic",
            "description": "",
            "date": ""
        }
    ],
    "patents": [
    ],
    "extracurriculars": [
        {
            "title": "",
            "fromDate": "2010-01-23",
            "toDate": "Today",
            "description": "Runs a dog-shelter on the weekends for homeless dogs."
        }
    ]
}
labeled_example = {
    "title": {
        "value": "Audio Research Software Engineer at Meta Reality Labs",
        "label": 0
    },
    "contactInfo": {
        "value": {
            "address": {
                "value": "",
                "label": 0
            },
            "website": {
                "value": "alex8b.com",
                "label": 0
            },
            "linkedin": {
                "value": "www.linkedin.com/in/alex8b",
                "label": 0
            },
            "name": {
                "value": "Alexi Bezugly",
                "label": 0
            },
            "phoneNumber": {
                "value": "222222222",
                "label": 0
            },
            "email": {
                "value": "alexi@gmail.com",
                "label": 0
            },
            "github": {
                "value": "github.com/alex8b",
                "label": 0
            },
            "birthday": {
                "value": "",
                "label": 0
            },
            "family": {
                "value": "",
                "label": 0
            }
        },
        "label": 0
    },
    "summary": {
        "value": "- Software development - C#, .NET, Unity, VR, Unreal Engine (Basic skills), Rust (Basic skills), C++, git, SCRUM, React (Basic skills), Node.js (Basic skills) - Generating product ideas. Fast prototyping new concepts and demos. Generating leads for software partnership. - Reverse engineering - Unity modding, HarmonyLib, dnSpy, IDA Pro, Cheat Engine, ReClass.",
        "label": 0
    },
    "experience": {
        "value": [
            {
                "value": {
                    "company": "Meta",
                    "title": "Audio Research Software Engineer",
                    "location": "Stockholm, Sweden",
                    "fromDate": "July 2022",
                    "toDate": "Present",
                    "description": ""
                },
                "label": 0
            },
            {
                "value": {
                    "company": "Arena Personal AB",
                    "title": "CW Software Engineer onsite at Meta",
                    "location": "Stockholm, Sweden",
                    "fromDate": "August 2021",
                    "toDate": "June 2022",
                    "description": "Software development at Meta Reality Labs Audio Research"
                },
                "label": 0
            },
            {
                "value": {
                    "company": "Tobii",
                    "title": "Software Developer",
                    "location": "Stockholm, Sweden",
                    "fromDate": "September 2013",
                    "toDate": "July 2021",
                    "description": "- Developing Tobii Ocumen. https://vr.tobii.com/sdk/solutions/tobii-ocumen/ - Foveated video streaming. - Exploring eye tracking features in VR. https://vr.tobii.com/sdk/ - Integrating eye tracking features into computer games. https:// tobiigaming.com/games/ - Idea, development and software architecture for Tobii Ghost (eye tracking bubble overlay) and Twitch Extension. https://gaming.tobii.com/software/ghost/ - Developing Tobii Game Hub and Unity mods. - Developing Tobii Unity SDK. https://developer.tobii.com/pc-gaming/unity-sdk/ - Generating product ideas. - Fast prototyping new concepts and demos. - Generating leads for software partnership/game integrations. - Supervising student projects. - Developer support on Tobii Developer Zone. - Helping out with Tobii Eye Tracker media reviews."
                },
                "label": 0
            },
            {
                "value": {
                    "company": "Scania",
                    "title": "Summer Worker",
                    "location": "S\u00f6dert\u00e4lje, Sweden",
                    "fromDate": "June 2013",
                    "toDate": "August 2013",
                    "description": "Development of pedestrian tracking and collision warning algorithms."
                },
                "label": 0
            },
            {
                "value": {
                    "company": "Scania Group",
                    "title": "Master Thesis Student",
                    "location": "S\u00f6dert\u00e4lje, Sweden",
                    "fromDate": "September 2012",
                    "toDate": "March 2013",
                    "description": "Development of a pedestrian tracking algorithm, which utilizes data from a ToF camera: - Multiple objects tracking using an array of Kalman filters - Tracking in absolute coordinates using truck's odometry data received through CANbus - Merging data from multiple ToF cameras and a laser scanner"
                },
                "label": 0
            },
            {
                "value": {
                    "company": "KTH",
                    "title": "Research Engineer",
                    "location": "",
                    "fromDate": "February 2012",
                    "toDate": "July 2012",
                    "description": "Working on an international robotics research project CogX Dora by testing, debugging and implementing new features in navigation and AI."
                },
                "label": 0
            }
        ],
        "label": 0
    },
    "education": {
        "value": [
            {
                "value": {
                    "institution": "Kungliga tekniska h\u00f6gskolan",
                    "location": "Sweden",
                    "title": "Master of Science (MSc) (unfinished), Systems, Control and Robotics",
                    "fromDate": "2010",
                    "toDate": "2013",
                    "description": ""
                },
                "label": 0
            },
            {
                "value": {
                    "institution": "ITMO University",
                    "location": "Sweden",
                    "title": "Master of Science (MSc), Automation and control",
                    "fromDate": "2009",
                    "toDate": "2011",
                    "description": ""
                },
                "label": 0
            },
            {
                "value": {
                    "institution": "ITMO University",
                    "location": "Sweden",
                    "title": "Bachelor of Science (BSc), Automation and control",
                    "fromDate": "2005",
                    "toDate": "2009",
                    "description": ""
                },
                "label": 0
            }
        ],
        "label": 0
    },
    "interests": {
        "value": [],
        "label": 0
    },
    "accomplishments": {
        "value": [],
        "label": 0
    },
    "languages": {
        "value": [
            {
                "value": {
                    "name": "English",
                    "proficiency": 5
                },
                "label": 0
            },
            {
                "value": {
                    "name": "Swedish",
                    "proficiency": 3
                },
                "label": 0
            }
        ],
        "label": 0
    },
    "projects": {
        "value": [],
        "label": 0
    },
    "softSkills": {
        "value": [],
        "label": 0
    },
    "hardSkills": {
        "value": [
            {
                "value": {
                    "name": "C#",
                    "proficiency": 5
                },
                "label": 0
            },
            {
                "value": {
                    "name": "Unity",
                    "proficiency": 5
                },
                "label": 0
            },
            {
                "value": {
                    "name": "Scrum",
                    "proficiency": 5
                },
                "label": 0
            }
        ],
        "label": 0
    },
    "certifications": {
        "value": [],
        "label": 0
    },
    "patents": {
        "value": [],
        "label": 0
    },
    "extracurriculars": {
        "value": [],
        "label": 0
    }
}
get_all_unlabeled_resumes_spec = {
    "tags": [
        "Unlabeled Resumes"
    ],
    "parameters": [],
    "definitions": {
        "Resume": {
            "type": "object",
            "properties": unlabeled_resume_dict
        },
        "ResumeList": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Resume"
            }
        }
    },
    "responses": {
        "200": {
            "description": "List of resume objects",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/Resume"
                        }
                    },
                    "example": [
                        unlabeled_example
                    ]
                }
            },
        }
    }
}
upload_unlabeled_resume_spec = {
    "tags": [
        "Unlabeled Resumes"
    ],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "schema": {
                "$ref": "#/definitions/Resume"
            },
            "example": unlabeled_example,
            "required": "true",
            "default": {}
        }
    ],
    "consumes": [
        "application/json"
    ],
    "definitions": {
        "Resume": unlabeled_resume_dict,
    },
    "responses": {
        "201": {
            "description": "Upload successful",
        },
        "400": {
            "description": "Upload unsuccessful. Check the resume format.",
        }
    }
}
upload_labeled_resume_spec = {
    "tags": [
        "Labeled Resumes"
    ],
    "definitions": {
            "Resume": labeled_resume_dict,
    },
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "schema": {
                "$ref": "#/definitions/Resume"
            },
            "example": labeled_example,
            "required": "true",
            "default": {}
        }
    ],
    "example": labeled_example,
    "responses": {
        "201": {
            "description": "Upload successful",
        },
        "400": {
            "description": "Upload unsuccessful. Check the resume format.",
        }
    }
}
get_all_labeled_resumes_spec = {
    "tags": [
        "Labeled Resumes"
    ],
    "parameters": [],
    "definitions": {
        "Resume": labeled_resume_dict,
        "ResumeList": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Resume"
            }
        }
    },
    "responses": {
        "200": {
            "description": "List of resume objects",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "array",
                        "items": labeled_resume_dict,
                    },
                    "example": [
                        labeled_example
                    ]
                }
            },

        }
    }
}
analyze_resume_spec = {
    "tags": [
        "Analysis"
    ],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "schema": {
                "$ref": "#/definitions/Resume"
            },
            "required": "true",
            "default": {}
        }
    ],
    "definitions": {
        "Resume": {
            "type": "object",
            "properties": unlabeled_resume_dict
        },
    },
    "responses": {
        "201": {
            "description": "Upload successful",
        },
        "400": {
            "description": "Upload unsuccessful. Check the resume format.",
        }
    }
}
