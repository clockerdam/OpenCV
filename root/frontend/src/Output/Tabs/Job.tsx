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