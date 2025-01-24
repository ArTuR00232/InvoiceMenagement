import { React, useState } from "react";
import Namer from "./userName";
import Menu from "./MenuHeader";
import Cookies from "js-cookie";
import { useNavigate } from "react-router-dom";

export const UserPage = ()=>{
    const [code, setCode] = useState({
        code:'••••••'
    })
    const cookie = Cookies.get()
    const userID =  JSON.parse(cookie.session).ID
    const nav = useNavigate()

    function fetchCode(){
        fetch('/API/code/'+userID)
        .then(Response => Response.json())
        .then(code =>{setCode(code)})
        .catch(error => console.error('fetching error: ', error))
    }
    const showcode = () =>{
        let cod = {code:'••••••'}
        if(code.code === '••••••'){
            fetchCode()
        }
        if(code.code !== '••••••'){
            setCode(cod)
        }
    }
    function fetchDelete(){
        try{
            var url ='/API/User/delete/'+userID
            fetch(url,{
                method: 'DELETE',
                headers:{
                    'Content-Type':'Application/Json',
                }
            })
        }
        catch(e){
            console.log('fetching error: ' +e)
        }    
    }
    function deleteAccount(){
        fetchDelete()
        Cookies.remove('session')
        nav('/')
    }
    return(
        <div>
            <div>
                <Menu/>
            </div>
            <div className = 'space'>
                <div className = 'form_box'>
                    <div className = 'content_form'>
                        <Namer/>
                        <div className = 'Centralize'>
                            <div>
                                <h3 className = 'code'>code for reset password</h3>
                            </div>
                        </div>
                        <div className = 'Centralize'>
                            <h2 className = 'code'>{code.code}</h2>
                        </div>
                        <div className='Centralize'>
                            <button className='button' onClick={showcode}>👁</button>
                        </div>
                        <div className = 'Centralize'>
                            <div>
                                <h5 className = 'codeImportant'>do not share this code!!</h5>
                            </div>
                        </div>    
                        <div className = 'Centralize'>
                            <h5 className = 'codeImportant'>this decission is irreversible!</h5>
                        </div>
                        <div className='Centralize'>
                            <button className='button' onClick={deleteAccount}>Delete Account</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
export default UserPage;