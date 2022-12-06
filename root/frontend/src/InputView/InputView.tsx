import { useState } from "react"
import { Form } from "./Form/Form"
import { Output } from "./Output/Output"

function InputView() {
    enum Page {
        Output,
        Form
    }

    const [currentPage, setCurrentPage] = useState(Page.Output)

    if (currentPage === Page.Output) {
        return <div>
            <button onClick={() => setCurrentPage(Page.Form)}>Go to input</button>
            <Output></Output>
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

export { InputView }