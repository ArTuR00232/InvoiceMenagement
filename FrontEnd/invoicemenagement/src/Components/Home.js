import React from "react";
import { Menu } from "./MenuHeader.js";
import { Cookies } from "react-cookie";


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
                    
                <div className="text-title">
                    <h4>
                        lets menage your finances
                    </h4>
                </div>
                <div className="content">
                    content
                </div>
            </div>
        </div>
    )
}
export default Home;