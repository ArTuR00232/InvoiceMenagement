import { React } from "react";
import Cookies  from "js-cookie";
import { useNavigate } from "react-router-dom";

const LoginOut = ()=>{
    console.log(Cookies.get('session'))
    if(Cookies.get("session") !== undefined){
        var log = 'logout'
    }
    else{
        var log = 'login'
    }
    const  nav = useNavigate()
    function handleLogout(){
        console.log('asd')
        console.log(Cookies.get('session'))
       if(Cookies.get("session") !== undefined){
           Cookies.remove("session")
           nav("/")
       }
       else{
           nav("/login")
       }
    }
    return(
        <div className="login">
            <button name="buttonLogout" type="button" onClick={handleLogout}>{log}</button>
        </div>
    )
}
export default LoginOut;