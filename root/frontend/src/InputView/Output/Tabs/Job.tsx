import { useContext } from "react";
import { getAnalysis } from "../../../api/api";
import { CV } from "../../../CV/CV";
import cvContext from "../../../cvContext";
import './tabs.css'

function Job() {
    const {cv, setCV} = useContext(cvContext)
    const {analyzedCV, setAnalyzedCV} = useContext(cvContext)
    
    function analyzeCV() {
        console.log(cv)
        getAnalysis(JSON.stringify(cv)).then((analyzedCV: CV) => {
          console.log(analyzedCV);
          setAnalyzedCV(analyzedCV);
        });
      }

    return <div className="Template">
        <button onClick={() => analyzeCV()}>Analyze CV</button>
        <p>Your job description that will tailor your resume:</p>
        <input
            name="title"
            placeholder="Input the job title"
            value={cv.title}
            onChange={(e) => setCV((prevState: CV) => ({ ...prevState, title: e.target.value}))}
        />
        <input className="textArea"
            name="description"
            placeholder="Input the job description"
            value={cv.description}
            onChange={(e) => setCV((prevState: CV) => ({ ...prevState, description: e.target.value}))}
        />
    </div>
}

export { Job }