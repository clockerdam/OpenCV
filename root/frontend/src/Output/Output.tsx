import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { CV } from "../CV/CV"

function Output() {
    // Fetch input CV
    // Fetch output CV
    // Display side by side
    const [cvUnlabeled, setUnlabeledCV] = useState(new CV())
    const navigate = useNavigate()
    const {state} = useLocation()
    useEffect(() => {
        setUnlabeledCV(state)
    }, [state])

    return <div>
        <button onClick={() => navigate('/input', {state: cvUnlabeled})}>Edit CV</button>
        {representCV(new CV())}
        {representCV(new CV())}
    </div>
}

function representCV(cv: CV) {
    return <p>Representation of CV: {cv.title}</p>
}

export { Output }