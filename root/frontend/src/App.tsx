import './App.css';
import { Labeller } from './Labeller/Labeller';
import {
  createBrowserRouter,
  RouterProvider
} from "react-router-dom";
import { Home } from './Home/Home';
import { CV } from './CV/CV';
import { useState } from 'react';
import cvContext from './cvContext';
import { Output } from './InputView/Output/Output';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home></Home>,
    errorElement: <p>Page not found.</p>
  },
  {
    path: "/label",
    element: <Labeller></Labeller>,
  },
  {
    path: "/improve",
    element: <Output></Output>,
  },
]);

function App() {
  const [cv, setCV] = useState(new CV())
  const [analyzedCV, setAnalyzedCV] = useState(new CV())
  const [loading, setLoading] = useState("loading")

  return <cvContext.Provider value={{ cv, setCV, analyzedCV, setAnalyzedCV, loading, setLoading }}>
    <RouterProvider router={router} />
  </cvContext.Provider>
}

export default App;