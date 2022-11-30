from pylatex.base_classes import Environment


class EnvironmentBase(Environment):
    content_separator = "\n"


class Paragraph(EnvironmentBase):
    _latex_name = "cvparagraph"


class Accomplishments(EnvironmentBase):
    _latex_name = "cvhonors"


class Skills(EnvironmentBase):
    _latex_name = "cvskills"


class Entries(EnvironmentBase):
    _latex_name = "cventries"
    seperate_paragraph = True


class Projects(EnvironmentBase):
    _latex_name = "cvprojects"


class Items(EnvironmentBase):
    _latex_name = "cvitems"
