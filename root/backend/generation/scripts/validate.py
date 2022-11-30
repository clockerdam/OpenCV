import yaml

from jsonresume import Resume


MY_RESUME_YAML_FILEPATH = "data/bse-python.yaml"

with open(MY_RESUME_YAML_FILEPATH, "r") as yaml_file:
    data = yaml.load(yaml_file)
    r = Resume(data)
    if r.is_valid():
        print("Yay! We're good")
    else:
        print("Houston, we have a problem")
        r.validate()
