from pydantic import BaseModel, Field as PydanticField
from bson import ObjectId
from .resume import ContactInfo

class LabeledList:
    value: list
    label: int

class LabeledStr:
    value: str
    label: int

class LabeledObj:
    value: object
    label: int

class LabeledContactInfo(BaseModel):
    value: ContactInfo
    label: int

    class Config:
        schema_extra = {
            "example": {
                'value': {
                    "name": "Max Musterman",
                    "website": "www.max-musterman.com",
                    "address": "",
                    "linkedin": "",
                    "phoneNumber": "+8210123456789",
                    "email": "max@muster.com",
                    "github": "",
                    "birthday": "",
                    "family": ""
                },
                'label': 5,
            }
        }


class LabeledExperienceFields(BaseModel):
    company: LabeledStr
    title: LabeledStr
    location: LabeledStr
    fromDate: LabeledStr
    toDate: LabeledStr
    description: LabeledStr

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "company": "Hyundai",
                "title": "Data Analyst",
                "location": "Seoul, South Korea",
                "fromDate": "2022-08-01",
                "toDate": "Today",
                "description": "Analysing financial data.",
            }
        }


class LabeledExperience(BaseModel):
    value: LabeledExperienceFields
    label: int

class LabeledEducationFields(BaseModel):
    institution: LabeledStr
    title: LabeledStr
    location: LabeledStr
    fromDate: LabeledStr
    toDate: LabeledStr
    description: LabeledStr

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "company": "Hyundai",
                "title": "Data Analyst",
                "location": "Seoul, South Korea",
                "fromDate": "2022-08-01",
                "toDate": "Today",
                "description": "Analysing financial data.",
            }
        }


class LabeledEducation(BaseModel):
    value: LabeledEducationFields
    label: int

class LabeledExtracurricularFields(BaseModel):
    title: LabeledStr
    fromDate: LabeledStr
    toDate: LabeledStr
    description: LabeledStr

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "Shepard",
                "fromDate": "2010-01-23",
                "toDate": "Today",
                "description": "Keeping sheep in my garden.",
            }
        }


class LabeledExtracurricular(BaseModel):
    value: LabeledExtracurricularFields
    label: int

class LabeledSkillFields(BaseModel):
    name: LabeledStr
    proficiency: LabeledStr

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "Korean",
                "proficiency": "Fluent",
            }
        }


class LabeledSkill(BaseModel):
    value: LabeledSkillFields
    label: int

class LabeledCertificationFields(BaseModel):
    title: LabeledStr
    level: LabeledStr
    description: LabeledStr
    date: LabeledStr

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "CFA",
                "level": "2",
                "description": "Chartered Financial Analyst",
                "date": "2022-10-20"
            }
        }


class LabeledCertification(BaseModel):
    value: LabeledCertificationFields
    label: int


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Resume(BaseModel):
    id: PyObjectId = PydanticField(default_factory=PyObjectId, alias="_id")
    title: LabeledStr = PydanticField(...)
    contactInfo: ContactInfo
    summary: LabeledStr
    experience: LabeledList  # [LabeledExperience]
    education: LabeledList  # [LabeledEducation]
    softSkills: LabeledList  # [LabeledSkill]
    hardSkills: LabeledList  # [LabeledSkill]
    languages: LabeledList  # [LabeledSkill]
    certifications: LabeledList  # [LabeledCertification]
    accomplishments: LabeledList  # [LabeledExtracurricular]
    projects: LabeledList  # [LabeledExtracurricular]
    extracurriculars: LabeledList  # [LabeledExtracurricular]
    patents: LabeledList  # [LabeledStr]
    interests: LabeledList  # [LabeledStr]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "..."
            }
        }
