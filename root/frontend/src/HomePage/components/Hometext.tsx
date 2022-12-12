import "./hometext.css";
import keyboard from "./assets/icons8-keyboard-60.png";
import hired from "./assets/icons8-teacher-hiring-60.png";
import arrow from "./assets/icons8-right-arrow-50.png";
import process from "./assets/icons8-services-50.png";
import download from "./assets/icons8-downloading-updates-50.png";
import { useNavigate } from "react-router-dom";
function Hometext() {

  const navigate = useNavigate()
  return (
    <>
      <div className="body">
      <div className="maintext">
        <div className='bigtext'>
          Get an AI-generated resume<br></br>
          based on your input,<br></br>instantly!
        </div>
        <div className='smalltext'>
          Our free AI-resume checker analysis your resumee depending on the job
          you are applying for and generates the perfect resumee for it.
          <br></br><button className="bigbutton" onClick={() => navigate('/improve')}> Get started</button>
        </div>
        <div className="picture">
        </div>
      </div>

      <div className="offer">
        <p className="stylefortitles"> What we offer</p>
        <ul>
          <li> We tailor the resume to the position you are applying for, thanks to our state-of-the-art AI-model.</li>
          <li> We select your key skills and information which are crucial for the position.</li>
          <li> We make sure that everything fits on a small number of pages, which recruiters like.</li>
        </ul>
        <p className="stylefortitles"> Why use our product?</p>
        <div className="whydescr"><li>
          Most companies use screening software to filter and
          rank applicant for the position.<br></br> By including the
          appropriate skills and experience regarding the position you are applying for in your
          resume <br></br> we can make your resumee stand out!</li>
        </div>
        <p className="stylefortitles">How it works</p>
        <div className="howdescr"> <li>Click the get started button. <br></br>
          Input all your information.<br></br>
          Give us a second to process it.<br></br>
          Download your resume.<br></br>
          Land the job you have always wanted.</li>
          <div className="animation">
            <ul>
              <li><button className="smallbutton" onClick={() => navigate('/improve')}> Get started</button></li>
            <li className="arrow1"><img alt="" src={arrow}></img></li>
            <li className="keyboard"><img alt="" src={keyboard}></img></li>
            <li className="arrow2"><img alt="" src={arrow}></img></li>
            <li className="process"><img alt="" src={process}></img></li>
            <li className="arrow3"><img alt="" src={arrow}></img></li>
            <li className="download"><img alt="" src={download}></img></li>
            <li className="arrow4"><img alt="" src={arrow}></img></li>
            <li className="hired"><img alt="" src={hired}></img></li>
            </ul>
          
          </div>
          </div>
      </div>
      </div>
    </>
  )
}
export default Hometext;
