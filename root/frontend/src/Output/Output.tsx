import { FormEvent, useEffect, useState } from "react"
import { getUnlabeled, getAnalysis } from "../api/api"
import { CV } from "../CV/CV"
import './output.css'

function Output() {
    const [cv, setUnlebeledCV] = useState(new CV()) // Initialize with an empty CV until an unlabeled one is fetched from DB

    const [cvAnalyzed, setAnalyzedCV] = useState(new CV()) // Initialize with an empty CV until an analyzed one is fetched from DB

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
            setUnlebeledCV(unlabeledCV)
        })
    }, [])

    // Fetch the analyzed CV upon initial load of page
    useEffect(() => {
        getAnalysis().then((analyzedCV: CV) => {
            console.log(analyzedCV)
            setAnalyzedCV(analyzedCV)
        })
    }, [])


    return <form onSubmit={handleSubmit}>
        <div className="split left">
            <label><h1>Previous CV:</h1></label>
            <label><h2>{cv.title}</h2></label>
                <div className="section">
                    <h2 className="item">Summary</h2>
                    <div className = "rating">
                        <p className="item">{cv.summary.value}</p>
                    </div>
                </div>
            {mapFields_P()}
        </div>
        <div className="bar"></div>
        <div className="split right">
            <button onSubmit={(e) => handleSubmit(e)}>Download</button>
            <label><h1>Your winning CV:</h1></label>
            <label><h2>{cvAnalyzed.title}</h2></label>
                <div className="section">
                    <h2 className="item">Summary</h2>
                    {/* {label("summary")} */}
                    <div className = "rating">
                        <p className="item">{cvAnalyzed.summary.value}</p>
                    </div>
                </div>
            {mapFields()}
        </div>
    </form>

    function mapFields() {
        return <div>
            {Object.keys(cvAnalyzed).map((field) => {
                if (field === "title" 
                    || field === "summary"
                    || field === "_id" ) {
                    return
                }
                if (field === "contactInfo") {
                    return //mapField(field)
                }
                return mapNestedField(field)
            })}
        </div>
    }

    function mapFields_P() {
        return <div>
            {Object.keys(cv).map((field) => {
                if (field === "title" 
                    || field === "summary"
                    || field === "_id" ) {
                    return
                }
                if (field === "contactInfo") {
                    return //mapField(field)
                }
                return mapNestedField_P(field)
            })}
        </div>
    }

    function mapField(field: string) {
        // Verify field
        switch (field) {
            case Field.ContactInfo:
                break
            default:
                console.log("Unrecognized field: " + field)
                return <p>ERROR: UNRECOGNIZED FIELD - {field}</p>
        }

        return <div className="section">
            <h2 className="item">{field}</h2>
            <div className="item">
                {Object.keys(cv[field]).map((key, index) => {
                    return <p><b>{key}: </b> {Object.values(cv[field])[index]}</p>
                })}
            </div>
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
        if (cvAnalyzed[field].value.length === 0) {
            return
        }

        // Map field values
        return <div className="section">
            <h2 className="item">{field}</h2>
            {/* {label(field)} */}
            {cvAnalyzed[field].value.map((listItem, index) => {
                return (<div className="rating" key={index}>
                        <div className={index % 2 === 0 ? "item light" : "item dark"}>
                            {Object.keys(listItem.value).map((key, index) => {
                                return <p><b>{key}: </b> {Object.values(listItem.value)[index]}</p>
                            })}
                        </div>
                        {/* {label(field, index)} */}
                    </div>
            )})}
    </div>
    }

    function mapNestedField_P(field: string) {
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
            {cv[field].value.map((listItem, index) => {
                return (<div className="rating" key={index}>
                        <div className={index % 2 === 0 ? "item light" : "item dark"}>
                            {Object.keys(listItem.value).map((key, index) => {
                                return <p><b>{key}: </b> {Object.values(listItem.value)[index]}</p>
                            })}
                        </div>
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
                setUnlebeledCV(prevState => ({...prevState, [field]: {label: label, value: value}}))
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
                setUnlebeledCV(prevState => ({...prevState, [field]: {label: listLabel, value: value}}))
                break
            default:
                console.log("Unknown field: " + field)
        }
    }

    function handleSubmit(e: FormEvent) {
        e.preventDefault()
        let json = JSON.stringify(cv)
        console.log(json)
        //uploadLabeled(json).then(e => console.log(e))
    }
}

export { Output }