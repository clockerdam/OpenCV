import { useContext } from "react";
import './tabs.css'
import { MoonLoader } from "react-spinners";
import cvContext from "../../../cvContext";

import { displaySummary, mapFields } from "../Displayer/displayer";
function Diff() {
  const { analyzedCV, loading } = useContext(cvContext);

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

          <div className="score">
            {mapFields(excludedFields, analyzedCV, analyzedCV, true)}
          </div>
        </>
      )}

    </div>
  );
}

export { Diff };
