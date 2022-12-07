import _ from "lodash";
import { CV, LabelledCertification, LabelledEducation, LabelledExperience, LabelledItem, LabelledSkill, LabelledString } from "../../../CV/CV";

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

function mapFields(excludedFields: string[], analyzedCV: CV, cv: CV, output: boolean) {
    return (
      <div>
        {Object.keys(cv).map((field) => {
          if (excludedFields.includes(field)) {
            return null
          }
          return mapNestedField(analyzedCV, cv, field, output);
        })}
      </div>
    )
  }

  function mapNestedField(analyzedCV: CV, cv: CV, field: string, output: boolean) {
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
      <div className="section" key={field}>
        <h2 className="item">{field}</h2>
        {cv[field].value.map((listItem, index) => {
          return (
            <div className="rating" key={index}>
              <div className={color(analyzedCV, cv, field, index)}>
                {Object.keys(listItem.value).map((key, index) => {
                  return (
                    <p key={index}>
                      <b>{key}: </b> {Object.values(listItem.value)[index]}
                    </p>
                  );
                })}
              </div>
              {showLabel(cv[field].value.map((item) => {return item.label}), listItem, field, output)}
            </div>
          );
        })}
      </div>
    );
  }

  function showLabel(labels: number[], item: LabelledString | LabelledItem | LabelledSkill | LabelledExperience | LabelledCertification | LabelledEducation, field: string, output: boolean) {
    if (!output) {
      return null
    }

    let label = item.label
    let sortedLabels = labels.sort()
    let rank = sortedLabels.indexOf(label) + 1
    
    if (field.endsWith("s")) {
      field = field.substring(0, field.length-1)
    }

    return <div className="label">
            <h5>{field} #{rank} of {labels.length}</h5>
          </div>
  }

  function color(analyzedCV: CV, cv: CV, field: string, index: number): string {
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

  export { mapFields, showLabel, displaySummary }