import React from "react";
import {Route, BrowserRouter, Routes} from "react-router-dom"
import Home from "./Home.js";
import Invoices from "./Invoices";
import LoginPage from "./LoguinPage.js";
import UserPage from "./UserP.js";
import SingUpPage from "./singUp.js";
import Certify from "./FogotPass.js";

export const Routies = () =>{
    return (
        <BrowserRouter>
            <Routes>
                <Route Component={Home} path = "/"/>
                <Route Component={Invoices} path ="/invoices"/>
                <Route Component={LoginPage} path="/login"/>
                <Route Component={UserPage} path = "/UserPage"/>
                <Route Component={SingUpPage} path="/Singup"/>
                <Route Component={Certify} path="/ForgotPass"/>
            </Routes>
        </BrowserRouter>
    )
}
export default Routies;