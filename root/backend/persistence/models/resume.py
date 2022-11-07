from pydantic import BaseModel, Field as PydanticField
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
    proficiency: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Korean",
                "proficiency": "Fluent",
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
        
class Resume(BaseModel):
    id: PyObjectId = PydanticField(default_factory=PyObjectId, alias="_id")
    title: str = PydanticField(...)
    contactInfo: ContactInfo = PydanticField(...)
    summary: str = PydanticField()
    experience: list[Experience]
    education: list[Education]
    softSkills: list[Skill]
    hardSkills: list[Skill]
    languages: list[Skill]
    certifications: list[Certification]
    accomplishments: list[Extracurricular]
    projects: list[Extracurricular]
    extracurriculars: list[Extracurricular]
    patents: list[str]
    interests: list[str]

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
