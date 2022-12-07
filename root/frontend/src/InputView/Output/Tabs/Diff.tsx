import { useContext } from "react";
import './tabs.css'
import { MoonLoader } from "react-spinners";
import cvContext from "../../../cvContext";
import { mapFields, showLabel } from "../Displayer/displayer";
import { CV } from "../../../CV/CV";

function Diff() {
  const {analyzedCV, loading} = useContext(cvContext);

  let excludedFields = ["title", "summary", "stats", "contactInfo", "_id", "description"]
  return (
    <div>
        {loading === "loading" ? (
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
              <h2>{analyzedCV.title}</h2>
            </label>
            {displaySummary(analyzedCV)}
            {mapFields(excludedFields, analyzedCV, analyzedCV, true)}
          </>
        )}
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
        {showLabel(analyzedCV.summary, true)}
      </div>
    </div>
  }
}

export { Diff };