import { FormEvent, useState } from "react";
import { CV, LabelledCertification, LabelledEducation, LabelledExperience, LabelledProject, LabelledSkill, LabelledString } from "../CV/CV";
import './form.css'


// https://www.freecodecamp.org/news/build-dynamic-forms-in-react/
function Form() {
    const [cv, setCV] = useState(new CV())

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
        LinkedIn = "linkedin",
        Name = "name",
        PhoneNumber = "phoneNumber",
        Email = "email",
        GitHub = "github",
        Birthday = "birthday",
        Family = "family",
        Time = "time",
        Proficiency = "proficiency",
        Company = "company",
        Location = "location",
        Title = "title",
        FromDate = "fromDate",
        ToDate = "toDate",
        Description = "description",
        Level = "level",
        Institution = "institution",
        Date = "date",
        Empty = ""
    }

    return <form onSubmit={handleSubmit}>
        <div>
            <button onSubmit={(e) => handleSubmit(e)}>Submit</button>
            <label>
                <p>Title</p>
                <input 
                    name="title"
                    placeholder="Title"
                    value={cv.title}
                    onChange={(e) => setCV(prevState => ({ ...prevState, title: e.target.value}))}
                />
            </label>
            <label>
                <p>Summary</p>
                <input 
                    name="summary"
                    placeholder="Summary"
                    value={cv.summary.value}
                    onChange={(e) => setCV(prevState => ({ ...prevState, summary: {value: e.target.value, label: 0}}))}
                />
            </label>
            <label>
                <p>Interests</p>
                {cv.interests.value.map((interest, index) => {
                return (<div key={index}>
                        <input
                            name="interest"
                            placeholder="Interest"
                            value={interest.value}
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
                    value={cv.contactInfo.address}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.Address)}
                />
                <p>Website</p>
                <input 
                    name="website"
                    placeholder="Website"
                    value={cv.contactInfo.website}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.Website)}
                />
                <p>LinkedIn</p>
                <input 
                    name="linkedIn"
                    placeholder="LinkedIn"
                    value={cv.contactInfo.linkedin}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.LinkedIn)}
                />
                <p>Name</p>
                <input 
                    name="name"
                    placeholder="Name"
                    value={cv.contactInfo.name}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.Name)}
                />
                <p>Phone Number</p>
                <input 
                    name="phoneNumber"
                    placeholder="Phone Number"
                    value={cv.contactInfo.phoneNumber}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.PhoneNumber)}
                />
                <p>Email</p>
                <input 
                    name="email"
                    placeholder="Email"
                    value={cv.contactInfo.email}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.Email)}
                />
                <p>GitHub</p>
                <input 
                    name="github"
                    placeholder="GitHub"
                    value={cv.contactInfo.github}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.GitHub)}
                />
                <p>Birthday</p>
                <input 
                    name="birthday"
                    placeholder="Birthday"
                    value={cv.contactInfo.birthday}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.Birthday)}
                />
                <p>Family</p>
                <input 
                    name="family"
                    placeholder="Family"
                    value={cv.contactInfo.family}
                    onChange={(e) => change(Field.ContactInfo, e, undefined, SubField.Family)}
                />
            </div>
            <label>
                <p>Accomplishments</p>
                {cv.accomplishments.value.map((accomplishment, index) => {
                return (<div key={index}>
                        <input
                            name="title"
                            placeholder="Title"
                            value={accomplishment.value.title}
                            onChange={e => change(Field.Accomplishments, e, index, SubField.Title)}
                        />
                        <input
                            type="date"
                            name="toDate"
                            placeholder="To"
                            //value={experience.to}
                            onChange={e => change(Field.Accomplishments, e, index, SubField.ToDate)}
                        />
                        <input
                            type="date"
                            name="fromDate"
                            placeholder="From"
                            //value={experience.from}
                            onChange={e => change(Field.Accomplishments, e, index, SubField.FromDate)}
                        />
                        <input
                            name="description"
                            placeholder="Description"
                            value={accomplishment.value.description}
                            onChange={e => change(Field.Accomplishments, e, index, SubField.Description)}
                        />
                        <button onClick={() => remove(Field.Accomplishments, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Accomplishments)}>Add accomplishment</button>
            </label>
            <label>
                <p>Projects</p>
                {cv.projects.value.map((project, index) => {
                return (<div key={index}>
                        <input
                            name="title"
                            placeholder="Title"
                            value={project.value.title}
                            onChange={e => change(Field.Projects, e, index, SubField.Title)}
                        />
                        <input
                            type="date"
                            name="toDate"
                            placeholder="To"
                            //value={project.to}
                            onChange={e => change(Field.Projects, e, index, SubField.ToDate)}
                        />
                        <input
                            type="date"
                            name="fromDate"
                            placeholder="From"
                            //value={experience.from}
                            onChange={e => change(Field.Projects, e, index, SubField.FromDate)}
                        />
                        <input
                            name="description"
                            placeholder="Description"
                            value={project.value.description}
                            onChange={e => change(Field.Projects, e, index, SubField.Description)}
                        />
                        <button onClick={() => remove(Field.Projects, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Projects)}>Add project</button>
            </label>
            <label>
                <p>Soft Skills</p>
                {cv.softSkills.value.map((softSkill, index) => {
                return (<div key={index}>
                        <input
                            name="name"
                            placeholder="Name"
                            value={softSkill.value.name}
                            onChange={e => change(Field.SoftSkills, e, index, SubField.Name)}
                        />
                        <input
                            name="proficiency"
                            placeholder="Proficiency"
                            value={softSkill.value.proficiency}
                            onChange={e => change(Field.SoftSkills, e, index, SubField.Proficiency)}
                        />
                        <button onClick={() => remove(Field.SoftSkills, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.SoftSkills)}>Add soft skill</button>
            </label>
            <label>
                <p>Hard Skills</p>
                {cv.hardSkills.value.map((hardSkill, index) => {
                return (<div key={index}>
                        <input
                            name="name"
                            placeholder="Name"
                            value={hardSkill.value.name}
                            onChange={e => change(Field.HardSkills, e, index, SubField.Name)}
                        />
                        <input
                            name="proficiency"
                            placeholder="Proficiency"
                            value={hardSkill.value.proficiency}
                            onChange={e => change(Field.HardSkills, e, index, SubField.Proficiency)}
                        />
                        <button onClick={() => remove(Field.HardSkills, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.HardSkills)}>Add hard skill</button>
            </label>
            <label>
                <p>Languages</p>
                {cv.languages.value.map((language, index) => {
                return (<div key={index}>
                        <input
                            name="name"
                            placeholder="Name"
                            value={language.value.name}
                            onChange={e => change(Field.Languages, e, index, SubField.Name)}
                        />
                        <input
                            name="proficiency"
                            placeholder="Proficiency"
                            value={language.value.proficiency}
                            onChange={e => change(Field.Languages, e, index, SubField.Proficiency)}
                        />
                        <button onClick={() => remove(Field.Languages, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Languages)}>Add language</button>
            </label>
            <label>
                <p>Experience</p>
                {cv.experience.value.map((experience, index) => {
                return (<div key={index}>
                        <input
                            name="company"
                            placeholder="Company"
                            value={experience.value.company}
                            onChange={e => change(Field.Experience, e, index, SubField.Company)}
                        />
                        <input
                            name="title"
                            placeholder="Title"
                            value={experience.value.title}
                            onChange={e => change(Field.Experience, e, index, SubField.Title)}
                        />
                        <input
                            name="location"
                            placeholder="Location"
                            value={experience.value.location}
                            onChange={e => change(Field.Experience, e, index, SubField.Location)}
                        />
                        <input
                            type="date"
                            name="fromDate"
                            placeholder="From"
                            //value={experience.from}
                            onChange={e => change(Field.Experience, e, index, SubField.FromDate)}
                        />
                        <input
                            type="date"
                            name="toDate"
                            placeholder="To"
                            //value={experience.to}
                            onChange={e => change(Field.Experience, e, index, SubField.ToDate)}
                        />
                        <input
                            name="description"
                            placeholder="Description"
                            value={experience.value.description}
                            onChange={e => change(Field.Experience, e, index, SubField.Description)}
                        />
                        <button onClick={() => remove(Field.Experience, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Experience)}>Add experience</button>
            </label>
            <label>
                <p>Certifications</p>
                {cv.certifications.value.map((certification, index) => {
                return (<div key={index}>
                        <input
                            name="Title"
                            placeholder="Title"
                            value={certification.value.title}
                            onChange={e => change(Field.Certifications, e, index, SubField.Title)}
                        />
                        <input
                            name="level"
                            placeholder="Level"
                            value={certification.value.level}
                            onChange={e => change(Field.Certifications, e, index, SubField.Level)}
                        />
                        <input
                            name="description"
                            placeholder="Description"
                            value={certification.value.description}
                            onChange={e => change(Field.Certifications, e, index, SubField.Description)}
                        />
                        <input
                            type="date"
                            name="date"
                            placeholder="Date"
                            //value={experience.to}
                            onChange={e => change(Field.Experience, e, index, SubField.Date)}
                        />
                        <button onClick={() => remove(Field.Certifications, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Certifications)}>Add certification</button>
            </label>
            <label>
                <p>Education</p>
                {cv.education.value.map((education, index) => {
                return (<div key={index}>
                        <input
                            name="institution"
                            placeholder="Institution"
                            value={education.value.institution}
                            onChange={e => change(Field.Education, e, index, SubField.Institution)}
                        />
                        <input
                            name="location"
                            placeholder="Location"
                            value={education.value.location}
                            onChange={e => change(Field.Education, e, index, SubField.Location)}
                        />
                        <input
                            name="title"
                            placeholder="Title"
                            value={education.value.title}
                            onChange={e => change(Field.Education, e, index, SubField.Title)}
                        />
                        <input
                            type="date"
                            name="fromDate"
                            placeholder="From"
                            //value={education.from}
                            onChange={e => change(Field.Education, e, index, SubField.FromDate)}
                        />
                        <input
                            type="date"
                            name="toDate"
                            placeholder="To"
                            //value={education.to}
                            onChange={e => change(Field.Education, e, index, SubField.ToDate)}
                        />
                        <input
                            name="description"
                            placeholder="Description"
                            value={education.value.description}
                            onChange={e => change(Field.Education, e, index, SubField.Description)}
                        />
                        <button onClick={() => remove(Field.Education, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Education)}>Add education</button>
            </label>
            <label>
                <p>Patents</p>
                {cv.patents.value.map((patent, index) => {
                return (<div key={index}>
                        <input
                            name="patent"
                            placeholder="Patent"
                            value={patent.value}
                            onChange={e => change(Field.Patents, e, index)}
                        />
                        <button onClick={() => remove(Field.Patents, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Patents)}>Add patent</button>
            </label>
            <label>
                <p>Extracurriculars</p>
                {cv.extracurriculars.value.map((extracurricular, index) => {
                return (<div key={index}>
                        <input
                            name="title"
                            placeholder="Title"
                            value={extracurricular.value.title}
                            onChange={e => change(Field.Extracurriculars, e, index, SubField.Title)}
                        />
                        <input
                            type="date"
                            name="toDate"
                            placeholder="To"
                            //value={experience.to}
                            onChange={e => change(Field.Extracurriculars, e, index, SubField.ToDate)}
                        />
                        <input
                            type="date"
                            name="fromDate"
                            placeholder="From"
                            //value={experience.from}
                            onChange={e => change(Field.Extracurriculars, e, index, SubField.FromDate)}
                        />
                        <input
                            name="description"
                            placeholder="Description"
                            value={extracurricular.value.description}
                            onChange={e => change(Field.Extracurriculars, e, index, SubField.Description)}
                        />
                        <button onClick={() => remove(Field.Extracurriculars, index)}>-</button>
                    </div>)
                })}
                <button onClick={() => add(Field.Extracurriculars)}>Add extracurricular</button>
            </label>
        </div>
        {/* <button onSubmit={(e) => handleSubmit(e)}>Submit</button> */}
    </form>

    function change(field: Field, event: any, index: number = 0, subField?: SubField) {
        let data: any
        switch (field) {
            case Field.Interests:
            case Field.Patents:
                data = cv[field].value
                data[index].value = event.target.value
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
                        data = cv[field]
                        data[subField] = event.target.value
                        setCV(prevState => ({...prevState, [field]: data}))
                        return 
                    default:
                        console.log("Unknown field: " + field)
                        return
                }
            case Field.Extracurriculars:
            case Field.Accomplishments:
            case Field.Projects:
                data = cv[field].value
                switch (subField) {
                    case SubField.Title:  
                    case SubField.Description:  
                        data[index].value[subField] = event.target.value
                        break
                    case SubField.ToDate:
                    case SubField.FromDate:
                        data[index].value[subField] = new Date(event.target.value)
                        break
                    default:
                        console.log("Unknown field: " + field)
                        return
                }
                break
            case Field.SoftSkills: 
            case Field.HardSkills:
            case Field.Languages:
                data = cv[field].value
                switch (subField) {
                    case SubField.Name:  
                        data[index].value[subField] = event.target.value
                        break
                    case SubField.Proficiency: 
                        data[index].value[subField] = +event.target.value
                        break
                    default:
                        console.log("Unknown field: " + field)
                        return
                }
                break
            case Field.Experience:
                data = cv[field].value
                switch (subField) {
                    case SubField.Company:
                    case SubField.Title:
                    case SubField.Location:
                    case SubField.Description:
                        data[index].value[subField] = event.target.value
                        break
                    case SubField.FromDate:
                    case SubField.ToDate:
                        data[index].value[subField] = new Date(event.target.value)
                        break
                    default:
                        console.log("Unknown field: " + field)
                        return
                }
            break
            case Field.Certifications:
                data = cv[field].value
                switch (subField) {
                    case SubField.Title:  
                    case SubField.Level: 
                    case SubField.Description:
                        data[index].value[subField] = event.target.value
                        break
                    case SubField.Date:
                        data[index].value[subField] = new Date(event.target.value)
                        break
                    default:
                        console.log("Unknown field: " + field)
                        return
                }
                break
            case Field.Education:
                data = cv[field].value
                switch (subField) {
                    case SubField.Institution:
                    case SubField.Title:
                    case SubField.Location:
                    case SubField.Description:
                        data[index].value[subField] = event.target.value
                        break
                    case SubField.FromDate:
                    case SubField.ToDate:
                        data[index].value[subField] = new Date(event.target.value)
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
        setCV(prevState => ({...prevState, [field]: {label: 0, value: data}}))
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
                data = cv[field].value
                data.splice(index, 1)
                break
            default:
                console.log("Unknown field: " + field)
                return
        }
        setCV(prevState => ({...prevState, [field]: {label: 0, value: data}}))
    }

    function add(field: string) { 
        let newItem: any
        switch (field) {
            case Field.Interests:
            case Field.Patents:
                newItem = new LabelledString()
                break
            case Field.Extracurriculars:
            case Field.Accomplishments:
            case Field.Projects:
                newItem = new LabelledProject()
                break
            case Field.SoftSkills:
            case Field.HardSkills:
            case Field.Languages:
                newItem = new LabelledSkill()
                break
            case Field.Experience:
                newItem = new LabelledExperience()
                break
            case Field.Certifications:
                newItem = new LabelledCertification()
                break
            case Field.Education:
                newItem = new LabelledEducation()
                break
            default:
                console.log("Unknown field: " + field)
                return
        }
        let data = cv[field].value
        data.push(newItem)
        setCV(prevState => ({...prevState, [field]: {label: 0, value: data}}))
    }

    function handleSubmit(e: FormEvent) {
        e.preventDefault()
        let json = JSON.stringify(cv)
        console.log(json)
        //uploadUnlabeled(json).then(e => console.log(e))
    }
}

export { Form }