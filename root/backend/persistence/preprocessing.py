import json

for i in range(1,11):
    filename = "SE"+str(i)+".json"
    file = open("data/" + filename)
    my_dict = json.load(file)

    anonymized_contactInfo = {
        "address": "Abraham Lincoln Street 1, Chicago, IL",
        "website": "my-website.com",
        "linkedin": "linkedin.com/in/me123",
        "name": "Monica Music",
        "phoneNumber": "01012345",
        "email": "monica@music.co.kr",
        "github": "monicamusic123",
        "birthday": "24 December 1985",
        "family": "5 kids, divorced"
    }

    my_dict["contactInfo"] = anonymized_contactInfo

    for i,_ in enumerate(my_dict["experience"]):
        my_dict["experience"][i] = {
            'value': my_dict["experience"][i],
            'label': 0
        }

    for i, _ in enumerate(my_dict["education"]):
        my_dict["education"][i] = {
            'value': my_dict["education"][i],
            'label': 0
        }
    for i, _ in enumerate(my_dict["interests"]):
        my_dict["interests"][i] = {
            'value': my_dict["interests"][i],
            'label': 0
        }
    for i, _ in enumerate(my_dict["accomplishments"]):
        my_dict["accomplishments"][i] = {
            'value': my_dict["accomplishments"][i],
            'label': 0
        }
    for i,_ in enumerate(my_dict["languages"]):
        my_dict["languages"][i] = {
            'value': my_dict["languages"][i],
            'label': 0
        }

    for i, _ in enumerate(my_dict["projects"]):
        my_dict["projects"][i] = {
            'value': my_dict["projects"][i],
            'label': 0
        }
    for i, _ in enumerate(my_dict["softSkills"]):
        my_dict["softSkills"][i] = {
            'value': my_dict["softSkills"][i],
            'label': 0
        }
    for i, _ in enumerate(my_dict["hardSkills"]):
        my_dict["hardSkills"][i] = {
            'value': my_dict["hardSkills"][i],
            'label': 0
        }
    for i, _ in enumerate(my_dict["certifications"]):
        my_dict["certifications"][i] = {
            'value': my_dict["certifications"][i],
            'label': 0
        }
    for i, _ in enumerate(my_dict["patents"]):
        my_dict["patents"][i] = {
            'value': my_dict["patents"][i],
            'label': 0
        }
    for i, _ in enumerate(my_dict["extracurriculars"]):
        my_dict["extracurriculars"][i] = {
            'value': my_dict["extracurriculars"][i],
            'label': 0
        }

    for item in my_dict["languages"]:
        item = {
            'value': item,
            'label': 0
        }
    for item in my_dict["projects"]:
        item = {
            'value': item,
            'label': 0
        }
    for item in my_dict["softSkills"]:
        item = {
            'value': item,
            'label': 0
        }
    for item in my_dict["hardSkills"]:
        item = {
            'value': item,
            'label': 0
        }
    for item in my_dict["certifications"]:
        item = {
            'value': item,
            'label': 0
        }
    for item in my_dict["patents"]:
        item = {
            'value': item,
            'label': 0
        }
    for item in my_dict["extracurriculars"]:
        item = {
            'value': item,
            'label': 0
        }

    my_dict["experience"] = {
        'value': my_dict["experience"],
        'label': 0
    }
    my_dict["summary"] = {
        'value': my_dict["summary"],
        'label': 0
    }
    my_dict["education"] = {
        'value': my_dict["education"],
        'label': 0
    }
    my_dict["interests"] = {
        'value': my_dict["interests"],
        'label': 0
    }
    my_dict["accomplishments"] = {
        'value': my_dict["accomplishments"],
        'label': 0
    }
    my_dict["languages"] = {
        'value': my_dict["languages"],
        'label': 0
    }
    my_dict["projects"] = {
        'value': my_dict["projects"],
        'label': 0
    }
    my_dict["softSkills"] = {
        'value': my_dict["softSkills"],
        'label': 0
    }
    my_dict["hardSkills"] = {
        'value': my_dict["hardSkills"],
        'label': 0
    }
    my_dict["certifications"] = {
        'value': my_dict["certifications"],
        'label': 0
    }
    my_dict["patents"] = {
        'value': my_dict["patents"],
        'label': 0
    }
    my_dict["extracurriculars"] = {
        'value': my_dict["extracurriculars"],
        'label': 0
    }

    json_obj = json.dumps(my_dict, indent=4)
    with open("data/l_"+filename, "w") as outfile:
        outfile.write(json_obj)



