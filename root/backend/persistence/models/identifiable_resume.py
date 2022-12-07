from pydantic import BaseModel, Field as PydanticField, create_model
from bson import ObjectId


class ContactInfo(BaseModel):
    name: str
    website: str
    address: str
    linkedin: str
    phoneNumber: str
    email: str
    github: str
    birthday: str
    family: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Max Musterman",
                "website": "www.max-musterman.com",
                "address": "",
                "linkedin": "",
                "phoneNumber": "+8210123456789",
                "email": "max@muster.com",
                "github": "",
                "birthday": "",
                "family": ""
            }
        }


class Experience(BaseModel):
    company: str
    title: str
    location: str
    fromDate: str
    toDate: str
    description: str

    class Config:
        allow_population_by_field_name = True
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


class Education(BaseModel):
    institution: str
    title: str
    location: str
    fromDate: str
    toDate: str
    description: str

    class Config:
        allow_population_by_field_name = True
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


class Extracurricular(BaseModel):
    title: str
    fromDate: str
    toDate: str
    description: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Shepard",
                "fromDate": "2010-01-23",
                "toDate": "Today",
                "description": "Keeping sheep in my garden.",
            }
        }


class Skill(BaseModel):
    name: str
    proficiency: int

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Korean",
                "proficiency": 5,
            }
        }


class Certification(BaseModel):
    title: str
    level: str
    description: str
    date: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "title": "CFA",
                "level": "2",
                "description": "Chartered Financial Analyst",
                "date": "2022-10-20"
            }
        }


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


LabeledExperience = create_model('Experience', value=(Experience, ...), label=(int, ...))
LabeledEducation = create_model('Education', value=(Education, ...), label=(int, ...))
LabeledSoftSkill = create_model('SoftSkill', value=(Skill, ...), label=(int, ...))
LabeledHardSkill = create_model('HardSkill', value=(Skill, ...), label=(int, ...))
LabeledLanguage = create_model('Language', value=(Skill, ...), label=(int, ...))
LabeledCertification = create_model('Certification', value=(Certification, ...), label=(int, ...))
LabeledExtracurricular = create_model('Extracurricular', value=(Extracurricular, ...), label=(int, ...))
LabeledProject = create_model('Project', value=(Extracurricular, ...), label=(int, ...))
LabeledAccomplishment = create_model('Accomplishment', value=(Extracurricular, ...), label=(int, ...))
LabeledInterest = create_model('Interest', value=(str, ...), label=(int, ...))
LabeledPatent = create_model('Patent', value=(str, ...), label=(int, ...))


class IdentifiableResume(BaseModel):
    id: PyObjectId = PydanticField()
    title: str = PydanticField(...)
    contactInfo: ContactInfo
    summary: create_model('Summary', value=(str, ...), label=(int, ...))
    experience: create_model('Experience', value=(list[LabeledExperience], ...),
                             label=(int, ...))
    education: create_model('Education',
                            value=(list[LabeledEducation], ...),
                            label=(int, ...))
    softSkills: create_model('SoftSkills',
                             value=(list[LabeledSoftSkill], ...),
                             label=(int, ...))
    hardSkills: create_model('HardSkills',
                             value=(list[LabeledHardSkill], ...),
                             label=(int, ...))
    languages: create_model('Languages',
                            value=(list[LabeledLanguage], ...),
                            label=(int, ...))
    certifications: create_model('Certifications', value=(
    list[LabeledCertification], ...),
                                 label=(int, ...))
    accomplishments: create_model('Accomplishments', value=(
    list[LabeledAccomplishment], ...),
                                  label=(int, ...))
    projects: create_model('Projects', value=(
    list[LabeledProject], ...),
                           label=(int, ...))
    extracurriculars: create_model('Extracurriculars', value=(
    list[LabeledExtracurricular], ...),
                                   label=(int, ...))
    patents: create_model('Patents', value=(list[LabeledPatent], ...),
                          label=(int, ...))
    interests: create_model('Interests',
                            value=(list[LabeledInterest], ...),
                            label=(int, ...))

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


