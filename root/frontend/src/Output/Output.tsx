import { FormEvent, useEffect, useState } from "react";
import { getUnlabeled, getAnalysis } from "../api/api";
import { CV } from "../CV/CV";
import "./output.css";
import { Form } from '../Form/Form';

import { MoonLoader } from "react-spinners";
import { Document, Page, Text, View, StyleSheet, PDFDownloadLink } from "@react-pdf/renderer"

import ReactPDF from '@react-pdf/renderer';
import { PDFViewer } from '@react-pdf/renderer';

//import { PDFDownloadLink} from '@react-pdf/renderer'

type OutputLoadingState = "loading" | "done";


///// use https://github.com/joeblackwaslike/resume-builder !!!!


type downloadParams = {
    data: string,
    fileName: string,
    fileType: string
}

function Output() {

  // const App = () => (
  //   <PDFViewer>
  //     <MyDocument />
  //   </PDFViewer>
  // );
  
  // ReactDOM.render(<App />, document.getElementById('root'));

  const [cv, setUnlebeledCV] = useState(new CV()); // Initialize with an empty CV until an unlabeled one is fetched from DB

  const [cvAnalyzed, setAnalyzedCV] = useState(new CV()); // Initialize with an empty CV until an analyzed one is fetched from DB

  const downloadFile = ({ data, fileName, fileType}: downloadParams) => {
      // Create a blob with the data we want to download as a file
      const blob = new Blob([data], { type: fileType })
      // Create an anchor element and dispatch a click event on it
      // to trigger a download
      const a = document.createElement('a')
      a.download = fileName
      a.href = window.URL.createObjectURL(blob)
      const clickEvt = new MouseEvent('click', {
        view: window,
        bubbles: true,
        cancelable: true,
      })
      a.dispatchEvent(clickEvt)
      a.remove()
    }

  // Create styles
  const styles = StyleSheet.create({
      page: {
      flexDirection: 'row',
      backgroundColor: '#E4E4E4'
      },
      section: {
      margin: 10,
      padding: 10,
      flexGrow: 1
      }
  });
  
  // Create Document Component
  const MyDocument = () => (
    <Document>
      <Page size="A4" style={styles.page}>
        <View style={styles.section}>
        </View>
        <View style={styles.section}>
          <Text>{JSON.stringify(cvAnalyzed)}</Text>
        </View>
      </Page>
    </Document>
  );


  // const MyDoc = () => (
  //   <Document>
  //     <Page>
  //       <Html>{html}</Html>
  //     </Page>
  //   </Document>
  // )
    
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
      setUnlebeledCV(unlabeledCV);
      getAnalysis(JSON.stringify(unlabeledCV)).then((analyzedCV: CV) => {
        console.log(analyzedCV);
        setOutputLoadingState("done");
        setAnalyzedCV(analyzedCV);
      });
    });
  }, []);

  return (
    <form onSubmit={handleSubmit}>
      <div className="split left">
        {/* <label>
          <h1>Previous CV:</h1>
        </label>
        <label>
          <h2>{cv.title}</h2>
        </label>
        <div className="section">
          <h2 className="item">Summary</h2>
          <div className="rating">
            <p className="item">{cv.summary.value}</p>
          </div>
        </div>
        {mapFields_P()} */}
        <Form></Form>
      </div>
      <div className="bar"> </div>
      <div className="split right">
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
            <button onSubmit={(e) => handleSubmit(e)}>Download</button>
            <PDFDownloadLink document={<MyDocument/>} fileName="Your_Winning_CV.pdf">
              {({ blob, url, loading, error }) => (loading ? 'Loading document...' : 'Download PDF')}
            </PDFDownloadLink>
            <label>
              <h1>Your winning CV:</h1>
            </label>
            <label>
              <h2>{cvAnalyzed.title}</h2>
            </label>
            <div className="section">
              <h2 className="item">Summary</h2>
              <div className="rating">
                <p className="item">{cvAnalyzed.summary.value}</p>
              </div>
            </div>
            {mapFields()}
          </>
        )}
      </div>
    </form>
  );

  function mapFields() {
    return (
      <div>
        {Object.keys(cvAnalyzed).map((field) => {
          if (field === "title" || field === "summary" || field === "_id") {
            return;
          }
          if (field === "contactInfo") {
            return; //mapField(field)
          }
          return mapNestedField(field);
        })}
      </div>
    );
  }

  function mapFields_P() {
    return (
      <div>
        {Object.keys(cv).map((field) => {
          if (field === "title" || field === "summary" || field === "_id") {
            return;
          }
          if (field === "contactInfo") {
            return; //mapField(field)
          }
          return mapNestedField_P(field);
        })}
      </div>
    );
  }

  function mapField(field: string) {
    // Verify field
    switch (field) {
      case Field.ContactInfo:
        break;
      default:
        console.log("Unrecognized field: " + field);
        return <p>ERROR: UNRECOGNIZED FIELD - {field}</p>;
    }

    return (
      <div className="section">
        <h2 className="item">{field}</h2>
        <div className="item">
          {Object.keys(cv[field]).map((key, index) => {
            return (
              <p>
                <b>{key}: </b> {Object.values(cv[field])[index]}
              </p>
            );
          })}
        </div>
      </div>
    );
  }

  function mapNestedField(field: string) {
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
    if (cvAnalyzed[field].value.length === 0) {
      return;
    }

    // Map field values
    return (
      <div className="section">
        <h2 className="item">{field}</h2>
        {/* {label(field)} */}
        {cvAnalyzed[field].value.map((listItem, index) => {
          return (
            <div className="rating" key={index}>
              <div className={index % 2 === 0 ? "item light" : "item dark"}>
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

  function mapNestedField_P(field: string) {
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
              <div className={index % 2 === 0 ? "item light" : "item dark"}>
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

  function label(field: string, index?: number) {
    return (
      <input
        type="number"
        min="1"
        max="10"
        name="rating"
        onChange={(e) => {
          let label = Number(e.target.value);
          if (index === undefined) {
            labelItem(field, label);
          } else {
            labelListItem(field, label, index);
          }
        }}
      />
    );
  }

  function labelItem(field: string, label: number) {
    switch (field) {
      case "summary":
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
        let data = cv[field];
        let value = data.value;
        data.label = label;
        setUnlebeledCV((prevState) => ({
          ...prevState,
          [field]: { label: label, value: value },
        }));
        break;
      default:
        console.log("Unknown field: " + field);
    }
  }

  function labelListItem(field: string, label: number, index: number) {
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
        let value = cv[field].value;
        let listLabel = cv[field].label;
        value[index].label = label;
        setUnlebeledCV((prevState) => ({
          ...prevState,
          [field]: { label: listLabel, value: value },
        }));
        break;
      default:
        console.log("Unknown field: " + field);
    }
  }

  function handleSubmit(e: FormEvent) {
    e.preventDefault()
    
    // let json = JSON.stringify(cvAnalyzed)
    // console.log(json)
    // //uploadLabeled(json).then(e => console.log(e))

    //ReactPDF.render(<MyDocument />, "example.pdf");
    downloadFile({
        data: JSON.stringify(cvAnalyzed),
        fileName: 'ImprovedCV.json',
        fileType: 'text/json',
      })
   }
  }
 

export { Output }
