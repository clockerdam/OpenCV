import "./navbar.css";
import { Component } from 'react';
import { MenuItems } from "./menu_items";
import logo from "./assets/icons8-resume-30.png";
class Navbar extends Component {
  render() {
    return (
      <nav className="NavbarItems">

        <h1 className="Navbarlogo"> <img alt="" src={logo}></img> </h1>
        <h1 className="naam">OpenCV</h1>
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
        <button className="navbarbutton"> Get started</button>
      </nav>
    );
  }
}
export default Navbar;
