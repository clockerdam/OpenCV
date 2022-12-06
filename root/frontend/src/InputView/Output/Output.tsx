import { useContext } from "react";
import { CV } from "../../CV/CV"
import cvContext from "../../cvContext";

function Output() {
    // Fetch input CV
    // Fetch output CV
    // Display side by side
    const {cv} = useContext(cvContext)

    return <div>
        {representCV(cv)}
        {representCV(new CV())}
    </div>
}

function representCV(cv: CV) {
    return <p>Representation of CV: {cv.title}</p>
}

export { Output }