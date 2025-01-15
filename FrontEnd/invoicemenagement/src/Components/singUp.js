import { React,useState } from "react";
import Menu from "./MenuHeader";
import { useNavigate } from "react-router-dom";

export function SingUpPage(){
    const [sing, Setsing] = useState({
        user:"",
        pass:"",
        passrepeat:""
    })
    const nav = useNavigate()
    function handleInput(e){
        const {name, value} = e.target
        Setsing(prevState =>({
            ...prevState,
            [name]: value,
        }))
    }
    function singups(){
        var url = '/API/User/post/'+sing.user+'+'+sing.pass
        fetch(url,{
            method:'POST',
            headers:{
                'content-Type':'application/Json'
            }
        })
        .then(Response=>Response.json())
        .catch(error=>console.log('fetching error: ', error))
    }
    function loginpage(){
        nav('/login')
    }

    function HandleSingup(){
        if(sing.user == ''){
            alert('must insert an user')
        }
        else{
            if(sing.passrepeat != sing.pass){
                alert('the pass is not the same!')
            }
            else{
                singups()
                alert('Welcome '+sing.user+' lets singin')
                nav('/login')
            }
        }
    }
    return(
        <div className='home'>
            <div className='top-menu'>
                <Menu/>
            </div>
            <div className='log_title'>
                <h4>
                    Sing up
                </h4>
            </div>
            <form className = 'form_box'>
                <div className='content_form'>
                    <div className='form'>
                        <input  className='input' name = 'user' placeholder = 'user' value = {sing.user} onChange={handleInput}></input>
                    </div>
                    <div  className='form'>
                        <input  className='input' name = 'pass' placeholder ='password' type = 'password' value = {sing.pass} onChange={handleInput}></input>
                    </div>
                    <div  className='form'>
                        <input  className='input' name = 'passrepeat' placeholder= 'repeat the pass' type = 'password' value = {sing.passrepeat} onChange ={handleInput}></input>
                    </div>
                    <div className = 'form_submit'>
                        <button className = 'button' type = 'button' onClick={HandleSingup}>Singup</button>
                    </div>
                    <div className = 'form_submit'>
                        <button className = 'button' type = 'button' onClick={loginpage}>Login Page</button>
                    </div>
                </div>
            </form>

        </div>
    )
}
export default SingUpPage;