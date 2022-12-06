import json, yaml
import subprocess

import os
from dateutil.parser import parse
from invoke import task, run
from builder import ResumeDocument

FILEPATH = os.path.join(os.getcwd(), 'tmp')
JSON_FILE = os.path.join(FILEPATH, 'temp.json')
YAML_FILE = os.path.join(FILEPATH, 'temp.yaml')
TEX_FILE = os.path.join(FILEPATH, 'temp')
PDF_FILE = os.path.join(FILEPATH, 'output.pdf')
def convert_json_to_yaml():
    os.makedirs(FILEPATH, exist_ok=True)

    with open('data/apple.json', 'r') as file:
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

    with open('data/apple.yaml', 'w') as yaml_file:
        yaml.dump(configuration, yaml_file)

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


import os

from invoke import task

VERSION = "2.1.0"


@task
def build_docker(ctx):
    ctx.run("docker build -t joeblackwaslike/texlive:2016 docker-texlive")


@task
def generate_thumbnails(ctx):
    filedir = "export"
    filename = (
        f"Joe_Black_resume_backend-software-engineer_python_v{VERSION}.pdf"
    )
    ctx.run("pdftoppm -png {} preview".format(os.path.join(filedir, filename)))


@task
def dump_json(ctx):
    ctx.run("yq . data/bse-python.yaml")


@task
def build_package(ctx):
    ctx.run("pip3 install -r requirements.txt")


def _build_pdf(ctx):
    p = subprocess.run([ "/usr/bin/xelatex", "temp" ])
    # "pdftoppm -png {} preview".format(os.path.join(filedir, filename))



def build_pdf():
    print("Hier angekommen")
    # run("scripts/xelatex temp")
    print(TEX_FILE)
    # os.system(['xelatex', 'temp'])
    subprocess.run([ "/usr/bin/xelatex", "temp" ])


def _move_and_rename(ctx, file_name):
    ctx.run(f"mv latex/temp.pdf export/{file_name}")


def _clean_up(ctx):
    ctx.run("rm -f latex/temp*")


def _extract_txt(ctx, file_name):
    ctx.run(f"pdftotext -layout export/{file_name}")


def _preview(ctx, file_name):
    ctx.run(f"open export/{file_name}")


@task
def _render(ctx, data="bse-python", pty=True):

    data_path = f"data/{data}.yaml"

    # Generate latex
    doc = ResumeDocument.from_jsonresume(YAML_FILE)
    print(doc)
    doc.export(TEX_FILE)
    file_name = PDF_FILE
    _build_pdf(ctx)
    _move_and_rename(ctx, file_name)
    _clean_up(ctx)
    # _extract_txt(ctx, file_name)
    _preview(ctx, file_name)

    print(f"Finished generating: {file_name}")


def save_to_json(resume):
    # with open('data/temp.json', 'r') as file:
    #     file = json.dump(resume,file)
    json_obj = json.dumps(resume, indent=4)
    with open(JSON_FILE, "w") as outfile:
        outfile.write(json_obj)



def render_from_json(input):
    # from invoke import run
    # run("inv render --data=temp")

    save_to_json(input)
    convert_json_to_yaml()

    data = 'temp'
    data_path = f"data/{data}.yaml"

    # Generate latex
    doc = ResumeDocument.from_jsonresume('temp')
    doc.export(TEX_FILE)
    file_name = PDF_FILE
    # file_name = f"{doc.file_name}.pdf"

    build_pdf()
    # doc2 = ResumeDocument(doc)
    # build_pdf()
    # subprocess.call("inv render --data=temp")


convert_json_to_yaml()