import './tabs.css'

//Option: https://www.pdftron.com/blog/react/how-to-build-a-react-pdf-viewer/#step-5-implementing-pdfjs

//http://africau.edu/images/default/sample.pdf

function Pdf(){
  return (
    <div className="FirstTab">
      {/* <p>Pdf Tab!! Hurray!!</p> */}
      {/* First tab content will go here */}
      {/* <embed src="CV.pdf" width="100%" height="600px" /> */}
      <object data="http://localhost:8080/pdf" width="500px" height="1000px">
        {/* <p>Alternative text - include a link <a href="http://africau.edu/images/default/sample.pdf">to the PDF!</a></p> */}
      </object>
    </div>
  );
};
export {Pdf};

