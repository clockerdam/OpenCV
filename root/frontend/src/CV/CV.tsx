export class LabelledString {
    value: string = '';
    label: number = 0;
}

export class LabelledStrings {
    value: LabelledString[] = [];
    label: number = 0;
}

class Item {
    title: string = '';
    fromDate: Date = new Date();
    toDate: Date = new Date();
    description: string = '';
}

export class LabelledItem {
    value: Item = new Item();
    label: number = 0;
}

class LabelledAccomplishments {
    value: LabelledItem[] = [];
    label: number = 0;
}

class LabelledExtracurriculars {
    value: LabelledItem[] = [];
    label: number = 0;
}

class Project {
    title: string = '';
    fromDate: Date = new Date();
    toDate: Date = new Date();
    description: string = '';
}

export class LabelledProject {
    value: Project = new Project();
    label: number = 0;
}

class LabelledProjects {
    value: LabelledProject[] = [];
    label: number = 0;
}

class Skill {
    name: string = '';
    proficiency: number = 0;
}

export class LabelledSkill {
    value: Skill = new Skill();
    label: number = 0;
}

class LabelledSkills {
    value: LabelledSkill[] = [];
    label: number = 0;
}

class Experience {
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

class LabelledExperiences {
    value: LabelledExperience[] = [];
    label: number = 0;
}

class Certification {
    title: string = '';
    level: string = '';
    description: string = '';
    date: Date = new Date();
}

export class LabelledCertification {
    value: Certification = new Certification();
    label: number = 0;
}

class LabelledCertifications {
    value: LabelledCertification[] = [];
    label: number = 0;
}

class Education {
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

class LabelledEducations {
    value: LabelledEducation[] = [];
    label: number = 0;
}

class ContactInfo {
    address: string = '';
    website: string = '';
    linkedin: string = '';
    name: string = '';
    phoneNumber: string = '';
    email: string = '';
    github: string = '';
    birthday: string = '';
    family: string = '';
}

class Stats {
    all_original_keywords: string[] = [];
    included_keywords: string[] = [];
    missing_keywords: string[] = [];
    removed_keywords: string[] = [];
}

export class CV {
    title: string = '';
    summary: LabelledString = new LabelledString();
    interests: LabelledStrings = new LabelledStrings();
    contactInfo: ContactInfo = new ContactInfo();
    accomplishments: LabelledAccomplishments = new LabelledAccomplishments();
    projects: LabelledProjects = new LabelledProjects();
    softSkills: LabelledSkills = new LabelledSkills();
    hardSkills: LabelledSkills = new LabelledSkills();
    languages: LabelledSkills = new LabelledSkills();
    experience: LabelledExperiences = new LabelledExperiences();
    certifications: LabelledCertifications = new LabelledCertifications();
    education: LabelledEducations = new LabelledEducations();
    patents: LabelledStrings = new LabelledStrings();
    extracurriculars: LabelledExtracurriculars = new LabelledExtracurriculars();
    stats: Stats = new Stats();
}