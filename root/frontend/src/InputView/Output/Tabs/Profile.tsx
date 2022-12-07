import { useContext, useState } from "react";
import './tabs.css'
import cvContext from "../../../cvContext";
import { exampleCV } from "../example";
import { mapFields } from "../Displayer/displayer";
import { CV } from "../../../CV/CV";
import { Form } from "../../Form/Form";

function Profile() {
  const {cv, setCV, analyzedCV} = useContext(cvContext); 

  enum Page {
    Profile,
    Form
  }

  const [currentPage, setCurrentPage] = useState(Page.Form)

  function fetchExampleCV() {
    setCV(exampleCV)
  }

  function displayKeywordList(list: string[]) {
    return <div>
      {list.map((keyword, index) => {
        // Last item in list
        if (index === list.length - 1) {
          return <span key={index}>{keyword}</span>
        }
        // Regular list item
        return <span key={index}>{keyword} <b>|</b> </span>
      })}
    </div>
  }

  function displayKeywords() {
    return <div className="keywords">
      <div>
        <h3>Included keywords:</h3>
        {displayKeywordList(analyzedCV.stats.included_keywords)}
      </div>
      <div>
        <h3>Missing keywords:</h3>
        {displayKeywordList(analyzedCV.stats.missing_keywords)}
      </div>
      <div>
        <h3>Removed keywords:</h3>
        {displayKeywordList(analyzedCV.stats.removed_keywords)}
      </div>
    </div>
  }

  function displaySummary(cv: CV) {
    if (cv.summary === undefined) {
      return null
    }
    return <div className="section">
      <h2 className="item">Summary</h2>
      <div className="rating">
        <p className="item">{cv.summary.value}</p>
      </div>
    </div>
  }

  let excludedFields = ["title", "summary", "stats", "contactInfo", "_id", "description"]
  if (currentPage === Page.Form) {
    return <div>
        <button onClick={() => setCurrentPage(Page.Profile)}>Go to profile</button>
        <Form></Form>
      </div>
  }

  return <div className="Template">
      <button onClick={() => setCurrentPage(Page.Form)}>Edit profile</button>
      <button onClick={() => fetchExampleCV()}>Fetch example CV</button>
      {displayKeywords()}
      <label>
        <h1>Your input:</h1>
      </label>
      <label>
        <h2>{cv.title}</h2>
      </label>
      {displaySummary(cv)}
      {mapFields(excludedFields, analyzedCV, cv, false)}
    </div>
}

export { Profile };