import React, { useState } from "react";

import {Diff} from "./Tabs/Diff";
import {Pdf} from "./Tabs/Pdf";
import {Profile} from "./Tabs/Profile";
import {Job} from "./Tabs/Job";

import './output.css'

function Output () {


  const [activeTab, setActiveTab] = useState("tab1");

    //  Functions to handle Tab Switching
    const handleTab1 = () => {
      // update the state to tab1
      setActiveTab("tab1");
    };
    const handleTab2 = () => {
      // update the state to tab2
      setActiveTab("tab2");
    };


  return (

    <div>
      <div className="split left">
        <Profile />
      </div>
      {/* <div className="bar"></div> */}
      <div className="split right">
        <div className="split_v top">
          <Job />
        </div>  
        <div className="split_v bottom">
          <div className="Tabs">
            <ul className="nav">
              <li
                className={activeTab === "tab1" ? "active" : ""}
                onClick={handleTab1}
              >
                Diff
              </li>
              <li
                className={activeTab === "tab2" ? "active" : ""}
                onClick={handleTab2}
              >
                Pdf
              </li>
            </ul>
            <div className="outlet">
                {activeTab === "tab1" ? <Diff /> : <Pdf />}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export {Output};