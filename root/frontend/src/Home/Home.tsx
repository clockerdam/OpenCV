import { useNavigate } from "react-router-dom"

function Home() {
    const navigate = useNavigate()

    return <div>
        <h1>OpenCV</h1>
        <button onClick={() => navigate('/input')}>Improve CV</button>
        <button onClick={() => navigate('/label')}>Label CV</button>
        <button onClick={() => navigate('/output')}>Output page</button>
    </div>
}

export { Home }