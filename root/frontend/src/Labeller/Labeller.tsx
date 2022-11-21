import { FormEvent, useEffect, useState } from "react"
import { getUnlabeled, labelCV } from "../api/api"
import { CV } from "../CV/CV"
import './labeller.css'

function Labeller() {
    const [cv, setCV] = useState(new CV()) // Initialize with an empty CV until an unlabeled one is fetched from DB

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

    // Fetch the unlabeled CV upon initial load of page
    useEffect(() => {
        getUnlabeled().then((unlabeledCV: CV) => {
            console.log(unlabeledCV)
            setCV(unlabeledCV)
        })
    }, [])

    return <form onSubmit={handleSubmit}>
        <div>
            <h1>{cv.title}</h1>
            <div className="section">
                <h2 className="item">Summary</h2>
                {label("summary")}
                <div className = "rating">
                    <p className="item">{cv.summary.value}</p>
                </div>
            </div>
            {mapFields()}
        </div>
        <button onSubmit={(e) => handleSubmit(e)}>Submit</button>
    </form>

    function mapFields() {
        return <div>
            {Object.keys(cv).map((field) => {
                if (field === "title" 
                    || field === "summary"
                    || field === "_id" ) {
                    return
                }
                return mapNestedField(field)
            })}
        </div>
    }

    function mapNestedField(field: string) {
        // Verify field
        switch (field) {
            case Field.Interests:
            case Field.Patents:
            case Field.Extracurriculars:
            case Field.Accomplishments:
            case Field.Projects:
            case Field.SoftSkills: 
            case Field.HardSkills:
            case Field.Languages:
            case Field.Experience:
            case Field.Certifications:
            case Field.Education:
                break
            default:
                console.log("Unrecognized field: " + field)
                return <p>ERROR: UNRECOGNIZED FIELD - {field}</p>
        }

        // We do not want to show empty lists
        if (cv[field].value.length === 0) {
            return
        }

        // Map field values
        return <div className="section">
            <h2 className="item">{field}</h2>
            {label(field)}
            {cv[field].value.map((listItem, index) => {
                return (<div className="rating" key={index}>
                        <div className={index % 2 === 0 ? "item light" : "item dark"}>
                            {Object.keys(listItem.value).map((key, index) => {
                                return <p><b>{key}: </b> {Object.values(listItem.value)[index]}</p>
                            })}
                        </div>
                        {label(field, index)}
                    </div>
            )})}
    </div>
    }

    function label(field: string, index?: number) {
        return <input
                    type="number" min="1" max="10"
                    name="rating"
                    onChange={(e) => {
                        let label = Number(e.target.value)
                        if (index === undefined) {
                            labelItem(field, label)
                        } else {
                            labelListItem(field, label, index)
                        }
                    }}
                />
    }

    function labelItem(field: string, label: number) {
        switch (field) {
            case "summary":
            case Field.Interests:
            case Field.Patents:
            case Field.Extracurriculars:
            case Field.Accomplishments:
            case Field.Projects:
            case Field.SoftSkills: 
            case Field.HardSkills:
            case Field.Languages:
            case Field.Experience:
            case Field.Certifications:
            case Field.Education:
                let data = cv[field]
                let value = data.value
                data.label = label
                setCV(prevState => ({...prevState, [field]: {label: label, value: value}}))
                break
            default:
                console.log("Unknown field: " + field)
        }
    }

    function labelListItem(field: string, label: number, index: number) {
        switch (field) {
            case Field.Interests:
            case Field.Patents:
            case Field.Extracurriculars:
            case Field.Accomplishments:
            case Field.Projects:
            case Field.SoftSkills: 
            case Field.HardSkills:
            case Field.Languages:
            case Field.Experience:
            case Field.Certifications:
            case Field.Education:
                let value = cv[field].value
                let listLabel = cv[field].label
                value[index].label = label
                setCV(prevState => ({...prevState, [field]: {label: listLabel, value: value}}))
                break
            default:
                console.log("Unknown field: " + field)
        }
    }

    function handleSubmit(e: FormEvent) {
        e.preventDefault()
        let json = JSON.stringify(cv)
        labelCV(json).then((e: any) => console.log(e))
    }
}

export { Labeller }