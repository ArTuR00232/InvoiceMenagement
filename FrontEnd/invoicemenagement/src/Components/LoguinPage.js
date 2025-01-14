import React from "react";
import Menu from "./MenuHeader";
import { useState, useEffect } from "react";
import Cookies from 'js-cookie';
import { useNavigate } from "react-router-dom";

export const LoginPage = () =>
    {
        const [login, setLogin] = useState({
            user: "",
            pass:"",
        })
        const [isTrue, setisTrue] = useState(false)
        const nav = useNavigate()
        
        useEffect(() =>{
            fetchingUser()
        },[login.pass])     

        function handleLogin(e){
            const {name, value} = e.target
            setLogin(prevState => ({
                ...prevState,
                [name]: value,
            }))
        }

        const HandleForgot = ()=>{
            nav('/ForgotPass')
        }

        const HandleSingup = ()=>{
            
            nav('/Singup')
        }

        function fetchingUser(){
            try{
                fetch("/Api/User/"+login.user+"+"+login.pass)
                .then(Response => Response.json())
                .then(isTrue => {setisTrue(isTrue)})
                .catch(error => console.log(' '));
            }
            catch(e){ 
                console.error('fetching error: ', e)
            }
        }
        function HandleSubmit(){
            if(login.user !== '' & login.pass!==''){
                try{
                    if(isTrue[0].Session === 'true'){
                            Cookies.set('session',JSON.stringify(isTrue[0]), {expires:1, sameSite:'Strict'})
                            return  nav("/")
                        }
                    if(isTrue[0].Session !== 'true')
                        alert("Wrong credentials!")
                }
                catch{
                    alert("Wrong credentials!")
                }
            }
            else{
                alert("Insert the credentials")
            }
        }
        return(
            <div>
                <div>
                    <Menu/>
                </div>
                <div className="log_title">
                            <h4>
                                Login
                            </h4>
                        </div>
                <form className = "form_box" >
                    <div className = "content_form">
                        <div className ="form">
                            <input className="input"  name = 'user' placeholder="user" value ={login.user} onChange={handleLogin}></input>
                        </div>
                        <div className ="form">
                             <input className="input" name = 'pass' placeholder="pass" type = "password" value ={login.pass} onChange={handleLogin}></input>
                        </div>
                        <div className ="form_submit">
                             <button className="button" type="button"  onClick = {HandleSubmit}>login</button>
                        </div>

                        <div className ="form_submit">
                             <button className="button" type="button"  onClick = {HandleSingup}>Sing Up</button>
                        </div>

                        <div className ="form_submit">
                             <button className="button" type="button"  onClick = {HandleForgot}>forgot the password?</button>
                        </div>
                    </div>
                </form>
            </div>
        )
    }

export default LoginPage;