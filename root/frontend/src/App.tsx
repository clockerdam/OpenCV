import './App.css';
import { Form } from './Form/Form';
import { Labeller } from './Labeller/Labeller';
import { Output } from './Output/Output';
import {
  createBrowserRouter,
  RouterProvider
} from "react-router-dom";
import { Home } from './Home/Home';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home></Home>,
    errorElement: <p>Page not found.</p>
  },
  {
    path: "/input",
    element: <Form></Form>,
  },
  {
    path: "/label",
    element: <Labeller></Labeller>,
  },
  {
    path: "/output",
    element: <Output></Output>,
  },
]);

function App() {
  return <RouterProvider router={router} />
}

export default App;
