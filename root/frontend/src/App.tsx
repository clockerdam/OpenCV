import { useState } from 'react';
import './App.css';
import { Form } from './Form/Form';
import { Labeller } from './Labeller/Labeller';
import { Output } from './Output/Output';

enum Page {
  Input,
  Labelling,
  Output
}

function App() {
  const [page, setPage] = useState(Page.Input)

  function showPage() {
    switch (page) {
      case Page.Input:
        return <Form></Form>
      case Page.Labelling:
        return <Labeller></Labeller>
      case Page.Output:
        return <Output></Output>
    }
  }

  return <div>
    <button 
      className={page === Page.Input ? "selected" : "unselected"} 
      onClick={() => setPage(Page.Input)}>
        Input</button>
    <button 
      className={page === Page.Labelling ? "selected" : "unselected"} 
      onClick={() => setPage(Page.Labelling)}>
        Labelling</button>
    <button 
      className={page === Page.Output ? "selected" : "unselected"} 
      onClick={() => setPage(Page.Output)}>
        Output</button>
    {showPage()}
  </div>
}

export default App;
