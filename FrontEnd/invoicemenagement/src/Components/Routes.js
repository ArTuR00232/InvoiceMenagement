import React from "react";
import {Route, BrowserRouter, Routes} from "react-router-dom"
import Home from "./Home.js";
import Invoices from "./Invoices";
import LoginPage from "./LoguinPage.js";


export const Routies = () =>{
    return (
        <BrowserRouter>
            <Routes>
                <Route Component={Home} path = "/"/>
                <Route Component={Invoices} path ="/invoices"/>
                <Route Component={LoginPage} path="/login"/>
            </Routes>
        </BrowserRouter>
    )
}
export default Routies;