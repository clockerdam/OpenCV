import { createContext } from "react";
import { CV } from "./CV/CV";

const cvContext = createContext({
  cv: new CV(),
  setCV: (cv: any) => { },
  analyzedCV: new CV(),
  setAnalyzedCV: (cv: any) => { },
  loading: 'loading',
  setLoading: (loading: string) => { },
  pdfData: "",
  setPdfData: (pdfData: string) => { },
});

export default cvContext;
