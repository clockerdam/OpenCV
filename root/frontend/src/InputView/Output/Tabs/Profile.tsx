import { useContext, useState } from "react";
import { CV, LabelledCertification, LabelledEducation, LabelledExperience, LabelledItem, LabelledSkill, LabelledString } from "../../../CV/CV";
import _ from "lodash"
import './tabs.css'
import cvContext from "../../../cvContext";
import { exampleCV } from "../example";

function Profile() {
  const {cv, setCV} = useContext(cvContext); 
  const {analyzedCV, setAnalyzedCV} = useContext(cvContext);

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
    Extracurriculars = "extracurriculars",
  }

  function fetchExampleCV() {
    setCV(exampleCV)
  }

  function displayKeywordList(list: string[]) {
    return <div>
      {list.map((keyword, index) => {
        // Last item in list
        if (index === list.length - 1) {
          return <span>{keyword}</span>
        }
        // Regular list item
        return <span>{keyword} <b>|</b> </span>
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

  let excludedFields = ["title", "summary", "stats", "contactInfo", "_id", "description"]
  return (
    <div className="Template">
      <button onClick={() => fetchExampleCV()}>Fetch example CV</button>
      {displayKeywords()}
      <label>
        <h1>Your input:</h1>
      </label>
      <label>
        <h2>{cv.title}</h2>
      </label>
      {displaySummary(cv)}
      {mapFields(excludedFields, cv, false)}
    </div>
  );

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

  function mapFields(excludedFields: string[], cv: CV, output: boolean) {
    return (
      <div>
        {Object.keys(cv).map((field) => {
          if (excludedFields.includes(field)) {
            return null
          }
          return mapNestedField(cv, field, output);
        })}
      </div>
    )
  }

  function mapNestedField(cv: CV, field: string, output: boolean) {
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
        break;
      default:
        console.log("Unrecognized field: " + field);
        return <p>ERROR: UNRECOGNIZED FIELD - {field}</p>;
    }

    // We do not want to show empty lists
    if (cv[field].value.length === 0) {
      return;
    }

    // Map field values
    return (
      <div className="section">
        <h2 className="item">{field}</h2>
        {cv[field].value.map((listItem, index) => {
          return (
            <div className="rating" key={index}>
              <div className={color(cv, field, index)}>
                {Object.keys(listItem.value).map((key, index) => {
                  return (
                    <p>
                      <b>{key}: </b> {Object.values(listItem.value)[index]}
                    </p>
                  );
                })}
              </div>
              {showLabel(listItem, output)}
            </div>
          );
        })}
      </div>
    );
  }

  function showLabel(item: LabelledString | LabelledItem | LabelledSkill | LabelledExperience | LabelledCertification | LabelledEducation, output: boolean) {
    if (!output) {
      return null
    }

    let label = item.label

    let maxRating = 100
    let rating = maxRating - label * maxRating

    let bracket
    if (rating > maxRating / 4 * 3) {
      bracket = "ratingNumber firstBracket"
    } else if (rating > maxRating / 4 * 2) {
      bracket = "ratingNumber secondBracket"
    } else {
      bracket = "ratingNumber thirdBracket"
    }

    return <div className="label">
            <h2 className={bracket}>{Math.round(rating)}</h2>
            <hr></hr>
            <h3 className="ratingNumber maxRating">{maxRating}</h3>
          </div>
  }

  function color(cv: CV, field: string, index: number): string {
    if (analyzedCV.title === "" || cv.title === "") {
      return index % 2 === 0 ? "item light" : "item dark"
    }

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
        break;
      default:
        return index % 2 === 0 ? "item light" : "item dark"
    }

    let itemToCheck = cv[field].value[index].value

    let items = analyzedCV[field].value.map((item) => {
      // lodash compares items without thinking about ordering of the keys
      return _.isEqual(item.value, itemToCheck );
    })

    let exists = items.includes(true)
    if (exists) {
      return index % 2 === 0 ? "item light" : "item dark"
    }
    return index % 2 === 0 ? "item lightRed" : "item darkRed"
  }
}

export { Profile };