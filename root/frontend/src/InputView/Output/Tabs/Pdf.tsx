import { useContext, } from 'react';
import cvContext from '../../../cvContext';
import './tabs.css'

//Option: https://www.pdftron.com/blog/react/how-to-build-a-react-pdf-viewer/#step-5-implementing-pdfjs

//http://africau.edu/images/default/sample.pdf

function Pdf() {
  const { pdfData } = useContext(cvContext)


  return (
    <div className="FirstTab">
      {/* <p>Pdf Tab!! Hurray!!</p> */}
      {/* First tab content will go here */}
      {/* <embed src="CV.pdf" width="100%" height="600px" /> */}
      {pdfData !== "" &&
        <>
          <object style={{ width: "100%" }} data={pdfData} type="application/pdf" width="500px" height="800px">
            The object tag is not supported in your browser
          </object>
        </>

      }
    </div>
  );
};
export { Pdf };

