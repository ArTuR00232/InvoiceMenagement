import React from "react";
import Cookies from "js-cookie";

export const Namer = () =>{
    let name =''
    if(Cookies.get("session") === undefined){
        name = 'Get Login!!'
    }
    else{
        let aux = JSON.parse(Cookies.get("session"))
        name = aux.username
    }
    return(
        <div className="Centralize">
            {name === 'Get Login!!'
            ?<a className="toUserP" title="User page" href="/">{name}</a>
            :<a className="toUserP" title="User page" href="/userPage">{name}</a>}
        </div>
    )
}
export default Namer;