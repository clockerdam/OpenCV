import { useEffect, useState } from "react";
import { getUnlabeled, getAnalysis } from "../../api/api";
import { CV } from "../../CV/CV";

import _ from "lodash"
import './tabs.css'

type OutputLoadingState = "loading" | "done";


function Profile() {
  const [cvUnlabeled, setUnlabeledCV] = useState(new CV()); // Initialize with an empty CV until an unlabeled one is fetched from DB

  const [cvAnalyzed, setAnalyzedCV] = useState(new CV()); // Initialize with an empty CV until an analyzed one is fetched from DB

  const [outputLoadingState, setOutputLoadingState] =
    useState<OutputLoadingState>("loading");

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

  // Fetch the unlabeled CV upon initial load of page
  useEffect(() => {
    getUnlabeled().then((unlabeledCV: CV) => {
      console.log(unlabeledCV);
      setUnlabeledCV(unlabeledCV);
      getAnalysis(JSON.stringify(unlabeledCV)).then((analyzedCV: CV) => {
        console.log(analyzedCV);
        setOutputLoadingState("done");
        setAnalyzedCV(analyzedCV);
      });
    });
  }, []);

  return (
    <div className="Template">
      <label>
        <h1>Previous CV:</h1>
      </label>
      <label>
        <h2>{cvUnlabeled.title}</h2>
      </label>
      <div className="section">
        <h2 className="item">Summary</h2>
        <div className="rating">
          <p className="item">{cvUnlabeled.summary.value}</p>
        </div>
      </div>
      {mapFields(cvUnlabeled)}
    </div>
  );

  function mapFields(cv: CV) {
    return (
      <div>
        {Object.keys(cv).map((field) => {
          if (field === "title" || field === "summary" || field === "_id") {
            return;
          }
          if (field === "contactInfo") {
            return; //mapField(field)
          }
          return mapNestedField(cv, field);
        })}
      </div>
    );
  }

  function mapNestedField(cv: CV, field: string) {
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

    function color(cv: CV, field: string, index: number): string {
      if (cvAnalyzed.title === "" || cvUnlabeled.title === "") {
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

      let items = cvAnalyzed[field].value.map((item) => {
        // lodash compares items without thinking about ordering of the keys
        return _.isEqual(item.value, itemToCheck );
      })

      let exists = items.includes(true)
      if (exists) {
        return index % 2 === 0 ? "item light" : "item dark"
      }
      return index % 2 === 0 ? "item lightRed" : "item darkRed"
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
            </div>
          );
        })}
      </div>
    );
  }

}

export { Profile };