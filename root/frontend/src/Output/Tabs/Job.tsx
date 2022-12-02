import { FormEvent, useState } from "react";
import { Job_description } from "../../Job_description/Job_description";
import './tabs.css'


function Job() {
    const [job, setJob] = useState(new Job_description())

    return <form onSubmit={handleSubmit}>
        <div className="Template">
            <button onSubmit={(e) => handleSubmit(e)}>Submit</button>
            <label>
                <p>Your job description that will tailor your resume:</p>
                <input
                    name="job_title"
                    placeholder="Input the job title"
                    value={job.job_title}
                    onChange={(e) => setJob(prevState => ({ ...prevState, job_title: e.target.value}))}
                />
                <input className="textArea"
                    name="job_description"
                    placeholder="Input the job description"
                    value={job.job_description}
                    onChange={(e) => setJob(prevState => ({ ...prevState, job_description: e.target.value}))}
                />
            </label>
        </div>
    </form>

    function handleSubmit(e: FormEvent) {
        e.preventDefault()
        let json = JSON.stringify(job)
        console.log(json)
        //uploadUnlabeled(json).then(e => console.log(e))
    }
}

export { Job }