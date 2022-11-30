import { useState } from 'react';
import './App.css';
import { Form } from './Form/Form';
import { Labeller } from './Labeller/Labeller';
import { Output } from './Output/Output';

import { Document, Page, Text, View, StyleSheet, PDFDownloadLink } from "@react-pdf/renderer"

enum webPage {
  Input,
  Labelling,
  Output
}

// Create Document Component
const MyDocument = () => (
  <Document>
    <Output></Output>
  </Document>
);

function App() {
  const [page, setPage] = useState(webPage.Output)

  function showPage() {
    switch (page) {
      // case webPage.Input:
      //   return <Form></Form>
      // case webPage.Labelling:
      //   return <Labeller></Labeller>
      case webPage.Output:
        return <Output></Output>
    }
  }



  return <div>
    {/* <button 
      className={page === webPage.Input ? "selected" : "unselected"} 
      onClick={() => setPage(webPage.Input)}>
        Input</button>
    <button 
      className={page === webPage.Labelling ? "selected" : "unselected"} 
      onClick={() => setPage(webPage.Labelling)}>
        Labelling</button> */}
    {/* <button 
      className={page === webPage.Output ? "selected" : "unselected"} 
      onClick={() => setPage(webPage.Output)}>
        Output</button> */}
    {/* <PDFDownloadLink document={<MyDocument/>} fileName="Your_Winning_CV.pdf">
              {({ blob, url, loading, error }) => (loading ? 'Loading document...' : 'Download PDF')}
    </PDFDownloadLink> */}
    {showPage()}
  </div>
}

export default App;
