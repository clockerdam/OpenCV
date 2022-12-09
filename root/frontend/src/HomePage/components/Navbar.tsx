import "./navbar.css";
import { MenuItems } from "./menu_items";
import logo from "./assets/icons8-resume-30.png";
import { useNavigate } from "react-router-dom";
function Navbar() {
  const navigate = useNavigate()

  return <nav className="NavbarItems">
      <h1 className="Navbarlogo" onClick={() => navigate('/')}> <img alt="" src={logo}></img> </h1>
      <h1 className="naam" onClick={() => navigate('/')}>OpenCV</h1>
      <ul className="Navmenu">
        {MenuItems.map((item, index) => {
          return (
            <li key={index}>
              <a className={item.cName} href="/">
                {item.title}
              </a>
            </li>
          );
        })}

      </ul>
      <button className="navbarbutton" onClick={() => navigate('/improve')}> Get started</button>
    </nav>
}
export { Navbar };
