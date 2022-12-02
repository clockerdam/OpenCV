import { useEffect, useState } from "react";
import { getUnlabeled, getAnalysis } from "../../api/api";
import { CV, LabelledCertification, LabelledEducation, LabelledExperience, LabelledItem, LabelledSkill, LabelledString } from "../../CV/CV";

import _ from "lodash"
import './tabs.css'

import { MoonLoader } from "react-spinners";

type OutputLoadingState = "loading" | "done";


function Diff() {
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
    <div>
        {outputLoadingState === "loading" ? (
          <div
            style={{
              width: "100%",
              height: "100%",
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <MoonLoader color="#36d7b7" />
          </div>
        ) : (
          <>
            <label>
              <h1>Refined CV:</h1>
            </label>
            <label>
              <h2>{cvAnalyzed.title}</h2>
            </label>
            <div className="section">
              <h2 className="item">Summary</h2>
              <div className="rating">
                <p className="item">{cvAnalyzed.summary.value}</p>
                {showLabel(cvAnalyzed.summary, true)}
              </div>
            </div>
            {mapFields(cvAnalyzed, true)}
          </>
        )}
    </div>
  );

  function mapFields(cv: CV, output: boolean) {
    return (
      <div>
        {Object.keys(cv).map((field) => {
          if (field === "title" || field === "summary" || field === "_id") {
            return;
          }
          if (field === "contactInfo") {
            return; //mapField(field)
          }
          return mapNestedField(cv, field, output);
        })}
      </div>
    );
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
  
}

export { Diff };