import React from "react";
import { useNavigate } from "react-router-dom";

export const Menu = () => {
    var nav = useNavigate()
    const Home =()=>{
        nav("/")
    }
    const Invoice=()=>{
        nav("/invoices")
    }
    return(
        <div className="menu">
            <button className="home" onClick={Home}>Home</button>
            <button className="InvoicePage" onClick={Invoice}>Invoices</button>
        </div>
    )
}
export default Menu;