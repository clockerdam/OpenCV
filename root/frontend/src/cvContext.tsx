import { createContext } from "react";
import { CV } from "./CV/CV";

const cvContext = createContext({
  cv: new CV(),
  setCV: (cv: any) => {}
});

export default cvContext;