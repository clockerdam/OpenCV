import { useNavigate } from "react-router-dom"

function Home() {
    const navigate = useNavigate()

    return <div>
        <h1>OpenCV</h1>
        <button onClick={() => navigate('/label')}>Label a CV</button>
        <button onClick={() => navigate('/improve')}>Improve your CV</button>
    </div>
}

export { Home }