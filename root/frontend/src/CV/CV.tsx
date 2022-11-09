export class ContactInfo {
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

export class CV {
    title: string = '';
    summary: string = '';
    interests: string[] = [];
    contactInfo: ContactInfo = new ContactInfo();
    accomplishments: {title: string, fromDate: Date, toDate: Date, description: string}[] = [];
    projects: {title: string, fromDate: Date, toDate: Date, description: string}[] = [];
    softSkills: {name: string, proficiency: number}[] = [];
    hardSkills: {name: string, proficiency: number}[] = [];
    languages: {name: string, proficiency: number}[] = [];
    experience: {company: string, title: string, location: string, fromDate: Date, toDate: Date, description: string}[] = [];
    certifications: {title: string, level: string, description: string, date: Date}[] = [];
    education: {institution: string, title: string, location: string, fromDate: Date, toDate: Date, description: string}[] = [];
    patents: string[] = [];
    extracurriculars: {title: string, fromDate: Date, toDate: Date, description: string}[] = [];
}