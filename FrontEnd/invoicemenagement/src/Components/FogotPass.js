import { React, useEffect, useState }  from "react";
import Menu from "./MenuHeader";
import  { useNavigate } from 'react-router-dom'

export function Certify(){
    const [pass, setPass] = useState({
        pw:'',
        repeatpw:'',
    })
    const [code, setCode] = useState({
        user:'',
        CodeR:'',
    })
    const [modal, setModal] = useState(false)
    const [isTrue, setIsTrue] = useState(false)
    const nav = useNavigate()
    const toggleCloseModal = () => {
        setModal(!modal)
        if(modal){
            document.body.classList.add('active-modal')
        }
        else{
            document.body.classList.remove('active-modal')
        }
    }

    useEffect(()=>{
        fetchCode()
    }, [code.CodeR])
    function HanddlePass(e){
        const {name, value} = e.target
        setPass(prevState =>({
            ...prevState,
            [name]:value,
        }))
    }
    function HandleCode(e){
        const {name, value} = e.target
        setCode(prevState =>({
            ...prevState,
            [name]:value,
        }))
    }
    function loginpage(){
        nav('/login')
    }
    const submit = (e)=>{
        e.preventDefault();
        if(code.CodeR === '' || code.user === ''){
            alert('Insert the info to reset the password')
        }
        else{
            if(isTrue[0] == false){
                alert('Wrong credentials')
            }
            if(isTrue[0] == true){
                toggleCloseModal()
            }
        }
    }
    function fetchCode(){
        fetch('/API/code/'+code.CodeR+'+'+code.user)
        .then(Response => Response.json())
        .then(isTrue => {setIsTrue(isTrue)})
        .catch(e => console.log('fetch error: ',e) )
    }
    function submitpass(){
        if(pass.pw != pass.repeatpw){
            alert('the passwords are not the same!')
        }
        if(pass.pw == pass.repeatpw &&pass.pw != ''){
            fetchpass()
        }
    }
    function fetchpass(){
        var url = '/API/User/update/'+code.user+'+'+pass.pw+'+'+code.CodeR
        fetch(url,{
            method:'POST',
            headers:{
                'content-Type':'application/Json',
            }
        })
        .then(Response=>Response.json())
        .then(alert('password updated'))
        .then(nav('/login'))
        .catch(error=>console.log('fetch error was ocorred: ', error))
    }
    return(
        <div>
            <div>
                <Menu/>
            </div>
            <div className ='codeButton'>
                <div className ='log_title'>
                    <h3>
                        Insert the resset pass code
                    </h3>     
               </div>
               <form className='form_box'>
                    <div className='content_form'>
                        <div>
                            <div className='form_centralize'>
                                <h4>User:</h4>
                            </div>
                            <div className='form_centralize'> 
                                <input className='input' placeholder = 'ex:user' name='user' value = {code.user} onChange={HandleCode}></input>
                            </div>
                        </div>
                        <div className=''>
                            <div className='form_centralize'>
                                <input className='input' placeholder='ex:P34I5u6P6y' name ='CodeR' value = {code.CodeR} onChange={HandleCode}></input>
                            </div>
                        </div>
                        <div className='form_submit'>
                            <button className='button' type ='button' onClick={submit}>submit</button>
                        </div>
                        <div className='form_submit'>
                            <button className='button' type='button' onClick={loginpage}>Login Page</button>
                        </div>
                    </div>
               </form>
               {modal&&(
                    <div className='modal-box'>
                        <div className='overlay'>
                            <div className='update-content'>
                                <div className='title_gen'>
                                    <h2>
                                       Set yout new password 
                                    </h2>
                                </div>
                                <div className='form_centralize'>
                                    <input placeholder='pass' name='pw' value ={pass.pw} onChange={HanddlePass} type='password'></input>
                                </div>
                                <div className='form_centralize'>
                                    <input placeholder='pass' name='repeatpw' value ={pass.repeatpw} onChange={HanddlePass} type='password'></input>
                                </div>
                                <div className='form_submit'>
                                    <button className='button' type ='button' onClick={submitpass}>submit</button>
                                </div>
                                <button className='close-modal' onClick={toggleCloseModal}>X</button>
                            </div>
                        </div>
                    </div>
               )}
            </div>
        </div>
    )
}
export default Certify;