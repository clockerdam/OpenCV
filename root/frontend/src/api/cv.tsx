type CV = {
    title: string,
    summary: string,
    interests: string[],
    contactInfo: ContactInfo,
    accomplishments: Feat[],
    projects: Feat[],
    softSkills: Skill[],
    hardSkills: Skill[],
    languages: Skill[],
    experience: Experience[],
    certifications: Certification[],
    education: Education[],
    patents: string[],
    extracurriculars: string[]
}

type ContactInfo = {
    address: string,
    website: string,
    linkedIn: string,
    name: string,
    phoneNumber: string,
    email: string,
    github: string,
    birthday: string,
    family: string
}

type Feat = {
    name: string,
    time: string
}

type Skill = {
    name: string,
    proficiency: number
}

type Experience = {
    company: string,
    title: string,
    from: Date,
    to: Date,
    description: string
}

type Certification = {
    name: string,
    level: string,
    description: string
}

type Education = {
    institution: string,
    title: string,
    from: Date,
    to: Date,
    description: string
}

export type { CV }