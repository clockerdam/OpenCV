import { useContext } from "react";
import { getAnalysis, getPdfData } from "../../../api/api";
import { CV } from "../../../CV/CV";
import cvContext from "../../../cvContext";
import './job.css'

function Job() {
  const { cv, setCV, setAnalyzedCV, setLoading, setPdfData } = useContext(cvContext)

<<<<<<< HEAD
  function analyzeCV() {
    console.log(cv)
    getAnalysis(JSON.stringify(cv)).then((analyzedCV: CV) => {

      console.log(analyzedCV);
      setAnalyzedCV(analyzedCV);
      getPdfData(analyzedCV).then((pdfData) => {
        console.log(pdfData)
        setPdfData(pdfData);
        setLoading("done")

      }).catch(err => {
        console.log("Failed to load pdf?");
        console.log(err)
      })
    });
  }

  return <div className="Template">
    <button onClick={() => analyzeCV()}>Analyze CV</button>
    <p>Your job description that will tailor your resume:</p>
    <input
      name="title"
      placeholder="Input the job title"
      value={cv.title}
      onChange={(e) => setCV((prevState: CV) => ({ ...prevState, title: e.target.value }))}
    />
    <textarea className="textArea"
      name="description"
      placeholder="Input the job description"
      value={cv.description}
      onChange={(e) => setCV((prevState: CV) => ({ ...prevState, description: e.target.value }))}
    />
  </div>
=======
    return <div className="jobcontainer">

        <div className="Template_job">
        <p className="jd">Input the job title and description below.</p>
        <input
            name="title"
            placeholder="Input the job title"
            value={cv.title}
            onChange={(e) => setCV((prevState: CV) => ({ ...prevState, title: e.target.value}))}
        />
        
        <textarea
        className="textArea" name="description" placeholder="Input the job description" value={cv.description}
        onChange={(e) => setCV((prevState: CV) => ({ ...prevState, description: e.target.value}))}>
        </textarea>
  
        </div>
        <button className= "job_button" onClick={() => analyzeCV()}>Analyze CV</button>
        <p className="finaltext"> press the button "Analyze CV" to get your resume tailored to the job description.</p>
        </div>
>>>>>>> 615b8e7 (styling frontend)
}

export { Job }
