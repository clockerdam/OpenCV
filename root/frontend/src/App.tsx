import './App.css';
import { Labeller } from './Labeller/Labeller';
import {
  createBrowserRouter,
  RouterProvider
} from "react-router-dom";
import Home from './HomePage/components/Hometext';
import { CV } from './CV/CV';
import { useState } from 'react';
import cvContext from './cvContext';
import { Output } from './InputView/Output/Output';
import Navbar from './HomePage/components/Navbar';
import Footer from './HomePage/components/footer';

const router = createBrowserRouter([
  {
    path: "/",
    element:
      <Home></Home>

  },
  {
    path: "/label",
    element: <Labeller></Labeller>,
  },
  {
    path: "/improve",
    element: <>
      <Output />
    </>
  },
]);

function App() {
  const [cv, setCV] = useState(new CV())
  const [analyzedCV, setAnalyzedCV] = useState(new CV())
  const [loading, setLoading] = useState("not_started")
  const [pdfData, setPdfData] = useState("")

  return <cvContext.Provider value={{ cv, setCV, analyzedCV, setAnalyzedCV, loading, setLoading, pdfData, setPdfData }}>
    <div >
      <Navbar />
      <RouterProvider router={router} />
      <Footer />
    </div>
  </cvContext.Provider>
}

export default App;
