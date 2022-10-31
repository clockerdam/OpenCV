import { FormEvent, useState } from "react";
import './cvForm.css'
import { cvUpload } from "../api/api";

// https://www.freecodecamp.org/news/build-dynamic-forms-in-react/
function CVForm() {
    const [state, setState] = useState({
        title: '',
        summary: '',
        interests: [] as string[],
        contactInfo: {
            address: '',
            website: '',
            linkedIn: '',
            name: '',
            phoneNumber: '',
            email: '',
            github: '',
            birthday: '',
            family: ''
        },
        accomplishments: [] as {name: string, time: string}[],
        projects: [] as {name: string, time: string}[],
        softSkills: [] as {name: string, proficiency: number}[],
        hardSkills: [] as {name: string, proficiency: number}[],
        languages: [] as {name: string, proficiency: number}[],
        experience: [] as {company: string, title: string, from: Date, to: Date, description: string}[],
        certifications: [] as {name: string, level: string, description: string}[],
        education: [] as {institution: string, title: string, from: Date, to: Date, description: string}[],
        patents: [] as string[],
        extracurriculars: [] as string[]
    })

    enum Field {
        Interests = "interests",
        ContactInfo = "contactInfo",
        Accomplishments = "accomplishments",
        Projects = "projects",
        SoftSkills = "softSkills",
        HardSkills = "hardSkills",
        Languages = "languages",
        Experience = "experience",
        Certifications = "certifications",
        Education = "education",
        Patents = "patents",
        Extracurriculars = "extracurriculars"
    }

    enum SubField {
        Address = "address",
        Website = "website",
        LinkedIn = "linkedIn",
        Name = "name",
        PhoneNumber = "phoneNumber",
        Email = "email",
        GitHub = "github",
        Birthday = "birthday",
        Family = "family",
        Time = "time",
        Proficiency = "proficiency",
        Company = "company",
        Title = "title",
        From = "from",
        To = "to",
        Description = "description",
        Level = "level",
        Institution = "institution",
        Empty = ""
    }

    return <form onSubmit={handleSubmit}>
        <div>
            <label>
                <p>Title</p>
                <input 
                    name="title"
                    placeholder="Title"
                    value={state.title}
                    onChange={(e) => setState(prevState => ({ ...prevState, title: e.target.value }))}
                />
            </label>
            <label>
                <p>Summary</p>
                <input 
                    name="summary"
                    placeholder="Summary"
                    value={state.summary}
                    onChange={(e) => setState(prevState => ({ ...prevState, summary: e.target.value }))}
                />
            </label>
            <label>
                <p>Interests</p>
                {state.interests.map((interest, index) => {
                return (<div key={index}>
                        <input
                            name="interest"
                            placeholder="Interest"
                            value={interest}
                            onChange={e => change(Field.Interests, e, index)}
                        />
                        <button onClick={() => remove(Field.Interests, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Interests)}>Add interest</button>
            </label>
            <p>Contact Information</p> 
            <div className="inner">
                <p>Address</p>         
                <input 
                    name="address"
                    placeholder="Address"
                    value={state.contactInfo.address}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.Address)}
                />
                <p>Website</p>
                <input 
                    name="website"
                    placeholder="Website"
                    value={state.contactInfo.website}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.Website)}
                />
                <p>LinkedIn</p>
                <input 
                    name="linkedIn"
                    placeholder="LinkedIn"
                    value={state.contactInfo.linkedIn}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.LinkedIn)}
                />
                <p>Name</p>
                <input 
                    name="name"
                    placeholder="Name"
                    value={state.contactInfo.name}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.Name)}
                />
                <p>Phone Number</p>
                <input 
                    name="phoneNumber"
                    placeholder="Phone Number"
                    value={state.contactInfo.phoneNumber}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.PhoneNumber)}
                />
                <p>Email</p>
                <input 
                    name="email"
                    placeholder="Email"
                    value={state.contactInfo.email}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.Email)}
                />
                <p>GitHub</p>
                <input 
                    name="github"
                    placeholder="GitHub"
                    value={state.contactInfo.github}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.GitHub)}
                />
                <p>Birthday</p>
                <input 
                    name="birthday"
                    placeholder="Birthday"
                    value={state.contactInfo.birthday}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.Birthday)}
                />
                <p>Family</p>
                <input 
                    name="family"
                    placeholder="Family"
                    value={state.contactInfo.family}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.Family)}
                />
            </div>
            <label>
                <p>Accomplishments</p>
                {state.accomplishments.map((accomplishment, index) => {
                return (<div key={index}>
                        <input
                            name="name"
                            placeholder="Name"
                            value={accomplishment.name}
                            onChange={e => change(Field.Accomplishments, e, index, SubField.Name)}
                        />
                        <input
                            name="time"
                            placeholder="Time"
                            value={accomplishment.time}
                            onChange={e => change(Field.Accomplishments, e, index, SubField.Time)}
                        />
                        <button onClick={() => remove(Field.Accomplishments, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Accomplishments)}>Add accomplishment</button>
            </label>
            <label>
                <p>Projects</p>
                {state.projects.map((project, index) => {
                return (<div key={index}>
                        <input
                            name="name"
                            placeholder="Name"
                            value={project.name}
                            onChange={e => change(Field.Projects, e, index, SubField.Name)}
                        />
                        <input
                            name="time"
                            placeholder="Time"
                            value={project.time}
                            onChange={e => change(Field.Projects, e, index, SubField.Time)}
                        />
                        <button onClick={() => remove(Field.Projects, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Projects)}>Add project</button>
            </label>
            <label>
                <p>Soft Skills</p>
                {state.softSkills.map((softSkill, index) => {
                return (<div key={index}>
                        <input
                            name="name"
                            placeholder="Name"
                            value={softSkill.name}
                            onChange={e => change(Field.SoftSkills, e, index, SubField.Name)}
                        />
                        <input
                            name="proficiency"
                            placeholder="Proficiency"
                            value={softSkill.proficiency}
                            onChange={e => change(Field.SoftSkills, e, index, SubField.Proficiency)}
                        />
                        <button onClick={() => remove(Field.SoftSkills, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.SoftSkills)}>Add soft skill</button>
            </label>
            <label>
                <p>Hard Skills</p>
                {state.hardSkills.map((hardSkill, index) => {
                return (<div key={index}>
                        <input
                            name="name"
                            placeholder="Name"
                            value={hardSkill.name}
                            onChange={e => change(Field.HardSkills, e, index, SubField.Name)}
                        />
                        <input
                            name="proficiency"
                            placeholder="Proficiency"
                            value={hardSkill.proficiency}
                            onChange={e => change(Field.HardSkills, e, index, SubField.Proficiency)}
                        />
                        <button onClick={() => remove(Field.HardSkills, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.HardSkills)}>Add hard skill</button>
            </label>
            <label>
                <p>Languages</p>
                {state.languages.map((language, index) => {
                return (<div key={index}>
                        <input
                            name="name"
                            placeholder="Name"
                            value={language.name}
                            onChange={e => change(Field.SoftSkills, e, index, SubField.Name)}
                        />
                        <input
                            name="proficiency"
                            placeholder="Proficiency"
                            value={language.proficiency}
                            onChange={e => change(Field.Languages, e, index, SubField.Proficiency)}
                        />
                        <button onClick={() => remove(Field.Languages, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Languages)}>Add language</button>
            </label>
            <label>
                <p>Experience</p>
                {state.experience.map((experience, index) => {
                return (<div key={index}>
                        <input
                            name="company"
                            placeholder="Company"
                            value={experience.company}
                            onChange={e => change(Field.Experience, e, index, SubField.Company)}
                        />
                        <input
                            name="title"
                            placeholder="Title"
                            value={experience.title}
                            onChange={e => change(Field.Experience, e, index, SubField.Title)}
                        />
                        <input
                            type="date"
                            name="from"
                            placeholder="From"
                            //value={experience.from}
                            onChange={e => change(Field.Experience, e, index, SubField.From)}
                        />
                        <input
                            type="date"
                            name="to"
                            placeholder="To"
                            //value={experience.to}
                            onChange={e => change(Field.Experience, e, index, SubField.To)}
                        />
                        <input
                            name="description"
                            placeholder="Description"
                            value={experience.description}
                            onChange={e => change(Field.Experience, e, index, SubField.Description)}
                        />
                        <button onClick={() => remove(Field.Experience, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Experience)}>Add experience</button>
            </label>
            <label>
                <p>Certifications</p>
                {state.certifications.map((certification, index) => {
                return (<div key={index}>
                        <input
                            name="name"
                            placeholder="Name"
                            value={certification.name}
                            onChange={e => change(Field.Certifications, e, index, SubField.Name)}
                        />
                        <input
                            name="level"
                            placeholder="Level"
                            value={certification.level}
                            onChange={e => change(Field.Certifications, e, index, SubField.Level)}
                        />
                        <input
                            name="description"
                            placeholder="Description"
                            value={certification.description}
                            onChange={e => change(Field.Certifications, e, index, SubField.Description)}
                        />
                        <button onClick={() => remove(Field.Certifications, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Certifications)}>Add certification</button>
            </label>
            <label>
                <p>Education</p>
                {state.education.map((education, index) => {
                return (<div key={index}>
                        <input
                            name="institution"
                            placeholder="Institution"
                            value={education.institution}
                            onChange={e => change(Field.Education, e, index, SubField.Institution)}
                        />
                        <input
                            name="title"
                            placeholder="Title"
                            value={education.title}
                            onChange={e => change(Field.Education, e, index, SubField.Title)}
                        />
                        <input
                            type="date"
                            name="from"
                            placeholder="From"
                            //value={education.from}
                            onChange={e => change(Field.Education, e, index, SubField.From)}
                        />
                        <input
                            type="date"
                            name="to"
                            placeholder="To"
                            //value={education.to}
                            onChange={e => change(Field.Education, e, index, SubField.To)}
                        />
                        <input
                            name="description"
                            placeholder="Description"
                            value={education.description}
                            onChange={e => change(Field.Education, e, index, SubField.Description)}
                        />
                        <button onClick={() => remove(Field.Education, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Education)}>Add education</button>
            </label>
            <label>
                <p>Patents</p>
                {state.patents.map((patent, index) => {
                return (<div key={index}>
                        <input
                            name="patent"
                            placeholder="Patent"
                            value={patent}
                            onChange={e => change(Field.Patents, e, index)}
                        />
                        <button onClick={() => remove(Field.Patents, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Patents)}>Add patent</button>
            </label>
            <label>
                <p>Extracurriculars</p>
                {state.extracurriculars.map((extracurricular, index) => {
                return (<div key={index}>
                        <input
                            name="extracurricular"
                            placeholder="Extracurricular"
                            value={extracurricular}
                            onChange={e => change(Field.Extracurriculars, e, index)}
                        />
                        <button onClick={() => remove(Field.Extracurriculars, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Extracurriculars)}>Add extracurricular</button>
            </label>
        </div>
        <button onSubmit={(e) => handleSubmit(e)}>Submit</button>
    </form>

    function change(field: Field, event: any, index: number = 0, subField?: SubField) {
        let data: any
        switch (field) {
            case Field.Interests:
            case Field.Patents:
            case Field.Extracurriculars:
                data = state[field]
                data[index] = event.target.value
                break
            case Field.ContactInfo:
                switch (subField) {
                    case SubField.Address:  
                    case SubField.Website: 
                    case SubField.LinkedIn:
                    case SubField.Name:
                    case SubField.PhoneNumber:   
                    case SubField.Email:
                    case SubField.GitHub:
                    case SubField.Birthday:     
                    case SubField.Family:
                        data = state[field]
                        data[subField] = event.target.value
                        break
                    default:
                        console.log("Unknown field: " + field)
                        return
                }
                break
            case Field.Accomplishments:
            case Field.Projects:
                switch (subField) {
                    case SubField.Name:  
                    case SubField.Time: 
                        break
                    default:
                        console.log("Unknown field: " + field)
                        return
                }
                data = state[field]
                data[index][subField] = event.target.value
                break
            case Field.SoftSkills: 
            case Field.HardSkills:
            case Field.Languages:
                data = state[field]
                switch (subField) {
                    case SubField.Name:  
                        data[index][subField] = event.target.value
                        break
                    case SubField.Proficiency: 
                        data[index][subField] = +event.target.value
                        break
                    default:
                        console.log("Unknown field: " + field)
                        return
                }
                break
            case Field.Experience:
                data = state[field]
                switch (subField) {
                    case SubField.Company:
                    case SubField.Title:
                    case SubField.Description:
                        data[index][subField] = event.target.value
                        break
                    case SubField.From:
                    case SubField.To:
                        data[index][subField] = new Date(event.target.value)
                        break
                    default:
                        console.log("Unknown field: " + field)
                        return
                }
                break
            case Field.Certifications:
                switch (subField) {
                    case SubField.Name:  
                    case SubField.Level: 
                    case SubField.Description:
                        break
                    default:
                        console.log("Unknown field: " + field)
                        return
                }
                data = state[field]
                data[index][subField] = event.target.value
                break
            case Field.Education:
                data = state[field]
                switch (subField) {
                    case SubField.Institution:
                    case SubField.Title:
                    case SubField.Description:
                        data[index][subField] = event.target.value
                        break
                    case SubField.From:
                    case SubField.To:
                        data[index][subField] = new Date(event.target.value)
                        break
                    default:
                        console.log("Unknown field: " + field)
                        return
                }
                break
            default:
                console.log("Unknown field: " + field)
                return
        }
        setState(prevState => ({...prevState, [field]: data}))
    }

    function remove(field: Field, index: number) {
        let data: any
        switch (field) {
            case Field.Accomplishments:
            case Field.Interests:
            case Field.Projects:
            case Field.SoftSkills:
            case Field.HardSkills:
            case Field.Languages:
            case Field.Experience:
            case Field.Certifications:
            case Field.Education:
            case Field.Patents:
            case Field.Extracurriculars:
                data = state[field]
                data.splice(index, 1)
                break
            default:
                console.log("Unknown field: " + field)
                return
        }
        setState(prevState => ({...prevState, [field]: data}))
    }

    function add(field: string) { 
        let newItem: any
        switch (field) {
            case Field.Interests:
            case Field.Patents:
            case Field.Extracurriculars:
                newItem = ''
                break
            case Field.Accomplishments:
            case Field.Projects:
                newItem = {name: '', time: ''}
                break
            case Field.SoftSkills:
            case Field.HardSkills:
            case Field.Languages:
                newItem = {name: '', proficiency: 0}
                break
            case Field.Experience:
                newItem = {company: '', title: '', from: new Date(), to: new Date(), description: ''}
                break
            case Field.Certifications:
                newItem = {name: '', level: '', description: ''}
                break
            case Field.Education:
                newItem = {institution: '', title: '', from: new Date(), to: new Date(), description: ''}
                break
            default:
                console.log("Unknown field: " + field)
                return
        }
        let data = state[field]
        data.push(newItem)
        setState(prevState => ({...prevState, [field]: data}))
    }

    function handleSubmit(e: FormEvent) {
        e.preventDefault()
        console.log(state)
        cvUpload().then(e => console.log(e))
    }
}

export { CVForm }