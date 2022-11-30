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

    def add_basics(self, basics):
        location = basics["location"]

        for command in [
            Command("name", basics["name"].split()),
            Command("position", basics["label"]),
            Command("address", location['address']),
            Command("mobile", basics["phone"]),
            Command("email", basics["email"]),
            # Command("homepage", basics["website"]),
        ]:
            self.preamble.append(command)

        for profile in basics["profiles"]:
            self.preamble.append(
                Command(profile["network"].lower(), profile["username"])
            )

    def add_header(self):
        self.append(MakeCVHeader(options=["L"]))

    def add_section(self, title):
        self.append(Section(title))

    def load_metadata(self, resume):
        self._meta = resume["meta"]
        self._basic = resume["basics"]

    @property
    def file_name(self):
        m = self._meta
        print(m)
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
        return "resume" + "_" + m["version"]

    def export(self, path):
        with open(path, "w") as fd:
            fd.write(self.dumps())

    @classmethod
    def from_jsonresume(cls, path, **kwargs):
        with open(path) as fd:
            resume = yaml.load(fd,yaml.Loader)

        doc = cls(**kwargs)
        doc.load_metadata(resume)
        doc.add_basics(resume["basics"])
        doc.add_header()

        # doc.add_section("Summary")
        # with doc.create(Paragraph()) as block:
        #     block.append(resume["basics"]["summary"])

        doc.add_section("Skills")
        with doc.create(Skills()) as skills:
            for item in resume["skills"]:
                skills.append(Skill.from_jsonresume(item))

        doc.add_section("Work Experience")
        with doc.create(Entries()) as entries:
            for item in resume["work"]:
                entry = Experience.from_jsonresume(item)
                with entry.create(Items()) as items:
                    summary = item.get("summary")
                    if summary:
                        items.append(Item(summary))
                    for bullet in item.get("highlights", []):
                        items.append(Item(bullet))
                entries.append(entry)
                
        doc.add_section("Education")
        with doc.create(Entries()) as entries:
            for item in resume["education"]:
                entry = Education.from_jsonresume(item)
                entries.append(entry)

        doc.add_section("Extracurricular Activities")
        with doc.create(Entries()) as entries:
            for item in resume["volunteer"]:
                entry = Activity.from_jsonresume(item)
                with entry.create(Items()) as items:
                    summary = item.get("summary")
                    if summary:
                        items.append(Item(summary))
                entries.append(entry)

        doc.add_section("Accomplishments")
        with doc.create(Accomplishments()) as accomplishments:
            for item in resume["Accomplishments"]:
                accomplishments.append(Accomplishment.from_jsonresume(item))

        doc.add_section("Projects")
        with doc.create(Projects()) as entries:
            for item in resume["projects"]:
                entry = OSProject.from_jsonresume(item)
                entries.append(entry)

        return doc
