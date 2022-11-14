export class LabelledString {
    value: string = '';
    label: number = 0;
}

export class Item {
    title: string = '';
    fromDate: Date = new Date();
    toDate: Date = new Date();
    description: string = '';
}

export class LabelledAccomplishment {
    value: Item = new Item();
    label: number = 0;
}

export class LabelledExtracurricular {
    value: Item = new Item();
    label: number = 0;
}

export class Project {
    title: string = '';
    fromDate: Date = new Date();
    toDate: Date = new Date();
    description: string = '';
}

export class LabelledProject {
    value: Project = new Project();
    label: number = 0;
}

export class Skill {
    name: string = '';
    proficiency: number = 0;
}

export class LabelledSkill {
    value: Skill = new Skill();
    label: number = 0;
}

export class Experience {
    company: string = '';
    title: string = '';
    location: string = '';
    fromDate: Date = new Date();
    toDate: Date = new Date();
    description: string = '';
}

export class LabelledExperience {
    value: Experience = new Experience();
    label: number = 0;
}

export class Certification {
    title: string = '';
    level: string = '';
    description: string = '';
    date: Date = new Date();
}

export class LabelledCertification {
    value: Certification = new Certification();
    label: number = 0;
}

export class Education {
    institution: string = '';
    title: string = '';
    location: string = '';
    fromDate: Date = new Date();
    toDate: Date = new Date();
    description: string = '';
}

export class LabelledEducation {
    value: Education = new Education();
    label: number = 0;
}

export class ContactInfo {
    address: LabelledString = new LabelledString();
    website: LabelledString = new LabelledString();
    linkedin: LabelledString = new LabelledString();
    name: LabelledString = new LabelledString();
    phoneNumber: LabelledString = new LabelledString();
    email: LabelledString = new LabelledString();
    github: LabelledString = new LabelledString();
    birthday: LabelledString = new LabelledString();
    family: LabelledString = new LabelledString();
}

export class CV {
    title: LabelledString = new LabelledString();
    summary: LabelledString = new LabelledString();
    interests: LabelledString[] = [];
    contactInfo: ContactInfo = new ContactInfo();
    accomplishments: LabelledAccomplishment[] = [];
    projects: LabelledProject[] = [];
    softSkills: LabelledSkill[] = [];
    hardSkills: LabelledSkill[] = [];
    languages: LabelledSkill[] = [];
    experience: LabelledExperience[] = [];
    certifications: LabelledCertification[] = [];
    education: LabelledEducation[] = [];
    patents: LabelledString[] = [];
    extracurriculars: LabelledExtracurricular[] = [];
}