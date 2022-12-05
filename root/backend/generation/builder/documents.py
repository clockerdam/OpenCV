from os.path import relpath, join

import yaml
from pylatex import Document, Command, NoEscape

from .commands import (
    Section,
    Accomplishment,
    Skill,
    Experience,
    Item,
    Activity,
    Education,
    OSProject,
    MakeCVHeader,
)
from .environments import Paragraph, Accomplishments, Skills, Entries, Projects, Items


class ResumeDocument(Document):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("default_filepath", relpath(join(".", "export")))
        kwargs.setdefault("document_options", ["11pt", "letterpaper"])
        kwargs.setdefault("documentclass", "awesomecv")
        kwargs.setdefault("accent_color", "awesome-emerald")
        kwargs.setdefault("fontenc", None)
        kwargs.setdefault("inputenc", None)
        kwargs.setdefault("font_size", None)
        kwargs.setdefault("lmodern", None)
        kwargs.setdefault("textcomp", None)
        kwargs.setdefault("page_numbers", None)
        accent_color = kwargs.pop("accent_color")
        super().__init__(*args, **kwargs)
        self.preamble.append(
            Command("colorlet", ["awesome", NoEscape(accent_color)])
        )
        self.data.clear()

    def add_contactInfo(self, contactInfo):
        commands = [
            Command("name", contactInfo["name"].split()),
            Command("address", contactInfo["address"]),
            Command("mobile", contactInfo["phoneNumber"]),
            Command("email", contactInfo["email"]),
            # Command("homepage", contactInfo["website"]),
        ]
        if contactInfo.get('label'):
            print("Found label")
            Command("position", contactInfo["label"]),

        for command in commands:
            self.preamble.append(command)

        for profile in contactInfo["profiles"]:
            self.preamble.append(
                Command(profile["network"].lower(), profile["username"])
            )

    def add_header(self):
        self.append(MakeCVHeader(options=["L"]))

    def add_section(self, title):
        self.append(Section(title))

    def load_metadata(self, resume):
        self._basic = resume["contactInfo"]

    @property
    def file_name(self):
        b = self._basic
        # elements = [
        #     e.replace(" ", "_")
        #     for e in [
        #         self._basic["name"],
        #         m["name"],
        #         m["role"],
        #         m["focus"],
        #         m["company"],
        #         m["version"],
        #     ]
        #     if e
        # ]
        # return "_".join(elements)
        return "resume" + "_" + b["name"].replace(" ", "")

    def export(self, path):
        with open(path, "w") as fd:
            fd.write(self.dumps())

    @classmethod
    def from_jsonresume(cls, path, **kwargs):
        with open(path) as fd:
            resume = yaml.load(fd, yaml.Loader)

        sections_to_be_rendered = list(resume.keys())
        def should_be_rendered(section):
            return section in sections_to_be_rendered

        doc = cls(**kwargs)
        doc.load_metadata(resume)
        doc.add_contactInfo(resume["contactInfo"])
        doc.add_header()

        if should_be_rendered("summary"):
            print("found summary")
            doc.add_section("Summary")
            with doc.create(Paragraph()) as block:
                block.append(resume["summary"])

        if should_be_rendered("skills"):
            doc.add_section("Skills")
            with doc.create(Skills()) as skills:
                for item in resume["skills"]:
                    skills.append(Skill.from_jsonresume(item))

        if should_be_rendered("experience"):
            doc.add_section("Work Experience")
            with doc.create(Entries()) as entries:
                for item in resume["experience"]:
                    entry = Experience.from_jsonresume(item)
                    with entry.create(Items()) as items:
                        description = item.get("description")
                        if description and len(description) != 0:
                            items.append(Item(description))
                        for bullet in item.get("highlights", []):
                            items.append(Item(bullet))
                    entries.append(entry)

        if should_be_rendered("education"):
            doc.add_section("Education")
            with doc.create(Entries()) as entries:
                for item in resume["education"]:
                    entry = Education.from_jsonresume(item)
                    entries.append(entry)

        if should_be_rendered("extracurriculars"):
            doc.add_section("Extracurricular Activities")
            with doc.create(Entries()) as entries:
                for item in resume["extracurriculars"]:
                    entry = Activity.from_jsonresume(item)
                    with entry.create(Items()) as items:
                        description = item.get("description")
                        if description and len(description) != 0:
                            items.append(Item(description))
                    entries.append(entry)

        if should_be_rendered("accomplishments"):
            doc.add_section("Accomplishments")
            with doc.create(Accomplishments()) as accomplishments:
                for item in resume["accomplishments"]:
                    accomplishments.append(Accomplishment.from_jsonresume(item))

        if should_be_rendered("projects"):
            doc.add_section("Projects")
            with doc.create(Projects()) as entries:
                for item in resume["projects"]:
                    entry = OSProject.from_jsonresume(item)
                    entries.append(entry)

        return doc
