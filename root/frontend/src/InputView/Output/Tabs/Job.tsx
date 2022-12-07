import { useContext } from "react";
import { getAnalysis, getPdfData } from "../../../api/api";
import { CV } from "../../../CV/CV";
import cvContext from "../../../cvContext";
import './tabs.css'

function Job() {
  const { cv, setCV, setAnalyzedCV, setLoading, setPdfData } = useContext(cvContext)

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
}

export { Job }
