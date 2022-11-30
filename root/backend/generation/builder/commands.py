from pylatex.base_classes import CommandBase, Command, ContainerCommand
from pylatex.utils import NoEscape
from . import jsonresume


class MakeCVHeader(CommandBase):
    _latex_name = "makecvheader"


class Section(CommandBase):
    _latex_name = "cvsection"

    def __init__(self, title):
        self.title = title
        super(Section, self).__init__(title)


class BaseObject(ContainerCommand):
    _props = ""

    def __init__(self, **kwargs):
        self._props = tuple(self._props.split())
        kwargs["arguments"] = [kwargs.pop(p) for p in self._props]
        super(BaseObject, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            idx = self._props.index(key)
        except ValueError:
            self.__getattribute__(key)
        return self.arguments[idx]

    def __setattr__(self, key, value):
        try:
            idx = self._props.index(key)
            self.arguments[idx] = value
        except ValueError:
            object.__setattr__(self, key, value)

    def __repr__(self):
        return "{}({})".format(
            type(self).__name__,
            ", ".join(
                [
                    "{}={!r}".format(key, getattr(self, key))
                    for key in self._props
                ]
            ),
        )

    def dumps(self):
        # note: most of the following was copied from the pyLaTeX library so
        #       in order to fix a logic error at the end of the function.

        content = self.dumps_content()

        if not content.strip() and self.omit_if_empty:
            return ""

        string = ""

        start = Command(
            self.latex_name, arguments=self.arguments, options=self.options
        )

        string += start.dumps()

        if content != "":
            string += "{{ \n {} \n}}".format(content)

        return string


class Item(BaseObject):
    _latex_name = "item"
    _props = "content"

    def __init__(self, content=""):
        lcls = locals()
        lcls.pop("self")
        BaseObject.__init__(self, **lcls)


class Accomplishment(BaseObject):
    _latex_name = "cvhonor"
    _props = "date title description location"

    def __init__(self, date="", title="", description="", location=""):
        lcls = locals()
        lcls.pop("self")
        BaseObject.__init__(self, **lcls)

    @classmethod
    def from_jsonresume(cls, dict_):
        data = jsonresume.parse_common("title location", dict_)
        data["date"] = jsonresume.format_date(dict_.get("date", ""), fmt="%Y")
        data["description"] = dict_.get("summary", "")
        return cls(**data)


class Skill(BaseObject):
    _latex_name = "cvskill"
    _props = "name skills"

    def __init__(self, name="", skills=""):
        lcls = locals()
        lcls.pop("self")
        BaseObject.__init__(self, **lcls)

    @classmethod
    def from_jsonresume(cls, dict_):
        data = jsonresume.parse_common("name", dict_)
        data["skills"] = NoEscape(
            jsonresume.stringify_sequence(dict_.get("keywords")).replace(
                "LaTeX", "\LaTeX"
            )
        )
        return cls(**data)


class Entry(BaseObject):
    seperate_paragraph = True
    _latex_name = "cventry"
    _date_range_format = "%m/%Y"


class Experience(Entry):
    _props = "position organization dates location"

    def __init__(self, position="", organization="", dates="", location=""):
        lcls = locals()
        lcls.pop("self")
        Entry.__init__(self, **lcls)

    @classmethod
    def from_jsonresume(cls, dict_):
        data = jsonresume.parse_common("position location", dict_)
        data["organization"] = dict_.get("company", "")
        data["dates"] = jsonresume.format_date_range(
            start=dict_.get("startDate"),
            end=dict_.get("endDate", "Present"),
            fmt=cls._date_range_format,
        )
        return cls(**data)


class Activity(Experience):
    _props = "position organization dates location"
    _date_range_format = "%Y"

    @classmethod
    def from_jsonresume(cls, dict_):
        data = jsonresume.parse_common("position organization location", dict_)
        data["dates"] = jsonresume.format_date_range(
            start=dict_.get("startDate"),
            end=dict_.get("endDate"),
            fmt=cls._date_range_format,
        )
        return cls(**data)


class Education(Entry):
    _props = "area institution dates location summary"

    def __init__(self, area="", institution="", location="", dates="", summary=""):
        lcls = locals()
        lcls.pop("self")
        BaseObject.__init__(self, **lcls)
        self.arguments += ["", ""]

    @classmethod
    def from_jsonresume(cls, dict_):
        data = jsonresume.parse_common("area institution location summary", dict_)
        data["dates"] = jsonresume.format_date_range(
            start=dict_.get("startDate"),
            end=dict_.get("endDate"),
            fmt=cls._date_range_format,
        )
        return cls(**data)


class Project(BaseObject):
    _latex_name = "cvproject"
    _props = "name url summary keywords"

    def __init__(self, name="", url="", summary="", keywords=""):
        lcls = locals()
        lcls.pop("self")
        BaseObject.__init__(self, **lcls)


class OSProject(Project):
    @classmethod
    def from_jsonresume(cls, dict_):
        data = jsonresume.parse_common("name url summary", dict_)
        # data["keywords"] = jsonresume.stringify_sequence(dict_.get("keywords"))
        return cls(**data)
