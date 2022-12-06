import { useContext, useState } from "react";
import { CV } from "../CV/CV"
import cvContext from "../cvContext";
import { Form } from "../Form/Form";

function Output() {
    // Fetch input CV
    // Fetch output CV
    // Display side by side
    const {cv} = useContext(cvContext)

    enum Page {
        Output,
        Form
    }

    const [currentPage, setCurrentPage] = useState(Page.Output)

    if (currentPage === Page.Output) {
        return <div>
            <button onClick={() => setCurrentPage(Page.Form)}>Go to input</button>
            {representCV(cv)}
            {representCV(new CV())}
        </div>
    }
    if (currentPage === Page.Form) {
        return <div>
                <button onClick={() => setCurrentPage(Page.Output)}>Go to output</button>
                <Form></Form>
            </div>
    }
    return <p>Invalid page.</p>
}

function representCV(cv: CV) {
    return <p>Representation of CV: {cv.title}</p>
}

export { Output }