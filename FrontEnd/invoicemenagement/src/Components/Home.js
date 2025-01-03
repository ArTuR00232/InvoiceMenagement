import React from "react";
import { Menu } from "./MenuHeader.js";
import { Cookies } from "js-cookie";
import LoginOut from "./Login-out.js";
import Namer from "./userName.js";

export function Home(){
    return(
        <div className="home">
            <div className="top-menu">
                <Menu/>
            </div>
            <div className ='title'>
                <div className="text-title">
                    <h4>
                        Welcome
                    </h4>
                </div>
                    <Namer/>
                <div className="text-title">
                    <h4>
                        lets menage your finances
                    </h4>
                </div>
                <div className="content">
                    content
                    <div>
                       <LoginOut/>
                    </div>
                </div>
            </div>
        </div>
    )
}
export default Home;