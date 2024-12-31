import React from "react";
import {Route, BrowserRouter, Routes} from "react-router-dom"
import Home from "./Home.js";
import Invoices from "./Invoices";


export const Routies = () =>{
    return (
        <BrowserRouter>
            <Routes>
                <Route Component={Home} path = "/"/>
                <Route Component={Invoices} path ="/invoices"/>
            </Routes>
        </BrowserRouter>
    )
}
export default Routies;