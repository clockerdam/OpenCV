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
import { InputView } from './InputView/InputView';

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
    element: <InputView></InputView>,
  },
]);

function App() {
  const [cv, setCV] = useState(new CV())

  return <cvContext.Provider value={{ cv, setCV }}>
    <RouterProvider router={router} />
  </cvContext.Provider>
}

export default App;
