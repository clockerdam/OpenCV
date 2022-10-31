resume_dict = {
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
        },
        "summary": {
            "type": "string"
        },
        "experience": {
            "type": "array",
            "items": {
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
                }
            }
        },
        "education": {
            "type": "array",
            "items": {
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
                }
            }
        },
        "interests": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "accomplishments": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string"
                    },
                    "fromDate": {
                        "type": "string",
                        "format": "date"
                    },
                    "toDate": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    }
                }
            }
        },
        "languages": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "proficiency": {
                        "type": "string"
                    }
                }
            }
        },
        "projects": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string"
                    },
                    "fromDate": {
                        "type": "string",
                        "format": "date"
                    },
                    "toDate": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    }
                }
            }
        },
        "softSkills": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "proficiency": {
                        "type": "string"
                    }
                }
            }
        },
        "hardSkills": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "proficiency": {
                        "type": "string"
                    }
                }
            }
        },
        "certifications": {
            "type": "array",
            "items": {
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
                }
            }
        },
        "patents": {
            "type": "array",
            "items": {
            }
        },
        "extracurriculars": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string"
                    },
                    "fromDate": {
                        "type": "string",
                        "format": "date"
                    },
                    "toDate": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    }
                }
            }
        }
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
            "properties": resume_dict
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
                  "description": "A complex object array response",
                  "content": {
                    "application/json": {
                      "schema": {
                        "type": "array",
                        "items": {
                          "$ref": "#/components/schemas/Resume"
                        }
                      }
                    }
                  },

                "examples": [{
                    "title": "Data scientist",
                    "contactInfo":
                    {
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
                        "proficiency": "Native"
                    },
                    {
                        "name": "Korean",
                        "proficiency": "Fluent"
                    },
                    {
                        "name": "English",
                        "proficiency": "Beginner"
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
                        "proficiency": "5"
                    },
                    {
                        "name": "Debating",
                        "proficiency": "2"
                    }
                ],
                "hardSkills": [
                    {
                        "name": "R",
                        "proficiency": "5"
                    },
                    {
                        "name": "Python",
                        "proficiency": "Fluent"
                    },
                    {
                        "name": "Machine Learning",
                        "proficiency": "4"
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
            ]
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
            "required": "true",
            "default": {}
        }
    ],
    "definitions": {
        "Resume": {
            "type": "object",
            "properties": resume_dict
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
upload_labeled_resume_spec = {
    "tags": [
            "Labeled Resumes"
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
            "properties": resume_dict
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
            "properties": resume_dict
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
