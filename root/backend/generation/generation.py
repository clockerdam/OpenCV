import json, yaml
import subprocess

import os
from dateutil.parser import parse
from .builder import ResumeDocument
from uuid import uuid4

def convert_json_to_yaml(json_file: str, yaml_file: str):

    with open(json_file, 'r') as file:
        configuration = json.load(file)

    if 'title' in configuration:
        configuration.pop('title')

    configuration['contactInfo']['profiles'] = [
        {
            'network': 'LinkedIn',
            'url': configuration['contactInfo']['linkedin'],
            'username': configuration['contactInfo']['linkedin']
        },
        {
            'network': 'Github',
            'url': configuration['contactInfo']['github'],
            'username': configuration['contactInfo']['github']
        }
    ]
    empty_sections = []
    for x, y in configuration.items():
        if type(y) == dict and 'value' in y:
            configuration[x] = y.get('value')
            if type(configuration[x]) == list:
                if len(configuration[x]) == 0:
                    configuration[x] = []
                for key, item in enumerate(configuration[x]):
                    if type(item) == dict and item.get('value'):
                        configuration[x][key] = item.get('value')

        # check for empty section to drop later, so they will be excluded from rendering
        if type(y) == dict and 'value' in y and len(y.get('value')) == 0:
            empty_sections.append(x)

    hard_skill_list = []
    for hardSkill in configuration['hardSkills']:
        hard_skill_list.append(hardSkill['name'] + ' (' + str(hardSkill['proficiency']) + ')')
    hard_skills = {
        'name': 'Hard Skills',
        'keywords': hard_skill_list
    }
    soft_skill_list = []
    for softSkill in configuration['softSkills']:
        soft_skill_list.append(softSkill['name'] + ' (' + str(softSkill['proficiency']) + ')')
    soft_skills = {
        'name': 'Soft Skills',
        'keywords': soft_skill_list
    }

    language_list = []
    for language in configuration['languages']:
        language_list.append(language['name'] + ' (' + str(language['proficiency']) + ')')
    languages = {
        'name': 'Languages',
        'keywords': language_list
    }

    configuration.pop('softSkills')
    configuration.pop('hardSkills')
    configuration.pop('languages')

    if not (len(language_list) == 0 and len(hard_skill_list) == 0 and len(soft_skill_list) == 0):
        configuration['skills'] = []
        if len(soft_skills.get('keywords')) != 0:
            configuration['skills'].append(soft_skills)
        if len(hard_skills.get('keywords')) != 0:
            configuration['skills'].append(hard_skills)
        if len(languages.get('keywords')) != 0:
            configuration['skills'].append(languages)

    # if summary is short display it as one-liner above the contactInfo
    if configuration.get('summary') and len(configuration['summary']) < 120:
        configuration['contactInfo']['label'] = configuration['summary']
        configuration.pop('summary')

    for accomplishment in configuration['accomplishments']:
        date = accomplishment['fromDate']
        accomplishment['date'] = format_date(date)

    for certification in configuration['certifications']:
        date = certification['date']
        certification['date'] = format_date(date)

    for experience in configuration['experience']:
        experience['fromDate'] = format_date(experience['fromDate'])
        experience['toDate'] = format_date(experience['toDate'])
        if len(experience['description']) == 0:
            experience['description'] = ""

    for extracurricular in configuration['extracurriculars']:
        extracurricular['fromDate'] = format_date(extracurricular['fromDate'])
        extracurricular['toDate'] = format_date(extracurricular['toDate'])

    for education in configuration['education']:
        education['fromDate'] = format_date(education['fromDate'])
        education['toDate'] = format_date(education['toDate'])
        if len(education['description']) == 0:
            education['description'] = ""

    for project in configuration['projects']:
        project['fromDate'] = format_date(project['fromDate'])
        project['toDate'] = format_date(project['toDate'])
        if len(project['description']) == 0:
            project['description'] = ""

    # drop all empty sections so they are excluded from rendering
    for section in empty_sections:
        if section in configuration:
            configuration.pop(section)

    with open(yaml_file, 'w') as y:
        yaml.dump(configuration, y)

    return configuration


def format_date(date):
    # if(date is not in ["","Present","Today"]):
    if len(date) != 0 and not any(date in s for s in ["Present", "Today", "Now"]):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
        for index, month in enumerate(months):
            date.replace(month, f"{index + 1:02}")
        date = parse(str(date)).strftime("%m/%Y")

    return date




def build_pdf(file_name: str):
    result = subprocess.run(["xelatex", "-interaction=nonstopmode", f"{file_name}" ], capture_output=True)


    if(result.stderr == b''): 
        print("Latex output: ")
        print(result.stdout)
        print()
        print("OK")
    else: 
        print(f"Returncode {result.returncode}")
        print(f"stderr {result.stderr}")
        raise Exception("Failed running subprocess")



def save_to_json(resume, json_file: str):
    # with open('data/temp.json', 'r') as file:
    #     file = json.dump(resume,file)
    json_obj = json.dumps(resume, indent=4)
    with open(json_file, "w") as outfile:
        outfile.write(json_obj)



def render_from_json(input) -> str:

    file_prefix = f"temp_{str(uuid4())}"
    print("Starting to generate: {file_prefix}")


    save_to_json(input, f"{file_prefix}.json")
    convert_json_to_yaml(f"{file_prefix}.json", f"{file_prefix}.yaml")

    # Generate latex
    doc = ResumeDocument.from_jsonresume(f'{file_prefix}.yaml')
    doc.export(f"{file_prefix}")

    build_pdf(f"{file_prefix}")

    return file_prefix
