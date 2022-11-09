import { useEffect, useState } from "react"
import { getUnlabeled } from "../api/api"
import { CV } from "../CV/CV"
import './labeller.css'

function Labeller() {
    const [cv, setCV] = useState(new CV()) // Initialize with an empty CV until an unlabeled one is fetched from DB

    // Fetch the unlabeled CV upon initial load of page
    useEffect(() => {
        getUnlabeled().then((unlabeledCV: CV) => {
            setCV(unlabeledCV)
        })
    })

    return <div>
        <h1>{cv.title}</h1>
        <div>
            <p>Summary</p>
            <div className = "rating">
                <p className="item">{cv.summary}</p>
                <input
                        type="number" min="1" max="10"
                        name="rating"
                        //value={cv.summary}
                        //onChange={(e) => setCV(prevState => ({ ...prevState, summary: e.target.value }))}
                    />
            </div>
        </div>
        <div>
            <p>Experience</p>
            {cv.experience.map((experience, index) => {
                return (<div className="rating" key={index}>
                        <div className={index % 2 === 0 ? "item light" : "item dark"}>
                            <p><b>Company:</b> {experience.company}</p>
                            <p><b>Title:</b> {experience.title}</p>                  
                            <p><b>Location:</b> {experience.location}</p>
                            <p><b>From:</b> </p>
                            <p><b>To:</b> </p>
                            <p><b>Description:</b> {experience.description}</p>
                        </div>
                        <input
                            type="number" min="1" max="10"
                            name="rating"
                            //value={cv.summary}
                            //onChange={(e) => setCV(prevState => ({ ...prevState, summary: e.target.value }))}
                        />
                    </div>
            )})}
        </div>
        </div>
}

export { Labeller }