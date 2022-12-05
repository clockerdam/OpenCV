import { CV } from "../CV/CV"

function Output() {
    // Fetch input CV
    // Fetch output CV
    // Display side by side

    return <div>
        {representCV(new CV())}
        {representCV(new CV())}
    </div>
}

function representCV(cv: CV) {
    return <p>Representation of CV: {cv.title}</p>
}

export { Output }