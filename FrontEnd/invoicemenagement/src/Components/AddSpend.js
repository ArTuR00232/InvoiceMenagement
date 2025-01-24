import { React, useEffect, useState } from "react";
import Menu from "./MenuHeader";
import Namer from "./userName";
import Cookies from "js-cookie";
import { useNavigate } from "react-router-dom";

export function AddSpend(){
    const [modal, setModal] = useState(false)
    const [spend, setSpend] = useState({
        spend:'',
        date:'',
        description:''
    })
    const  userId =JSON.parse(Cookies.get('session')).ID
    const handdleInput = (e)=>{
        const name = e.target.name
        const value = e.target.value
        setSpend(values=>({...values, [name]:value}))
    }
    const nav = useNavigate()
    const onSubmit = (e)=>{
        e.preventDefault();
        spend.spend = parseFloat(spend.spend)
        if(Number.isNaN(spend.spend)){
            alert('Please insert an available value in the spend input')
        }
        if(spend.date == ''){
            alert('Please insert a date to submit')
        }
        if(!Number.isNaN(spend.spend)){
            if(spend.description == ''){
                spend.description = 'Null'
            }
            if(spend.date != ''){
                console.log()
                var url = '/API/Money/post/'+userId+'+'+spend.spend+'+'+spend.date+'+'+spend.description
                fetch(url, {
                    method:'POST',
                    headers:{
                        'Content-Type':'application/Json'
                    }
                })
                .catch(e=> console.error('fetching error: '+e)) 
                var info = []
                info.push(spend.date)
                info.push(spend.spend)
                setSpend({
                    spend:'',
                    date:'',
                    description:''
                })
                modalwindow()
            }
            
        }
    }
    function  modalwindow(){
        setModal(!modal)
        if(modal){
            document.body.classList.add('active-modal')
        }
        else{
            document.body.classList.remove('active-modal')
        }
    }
    function handlesubmit(e){
        if(e == 0){
            modalwindow()
        }
        if(e == 1){
            console.log(e===1)
            nav('/invoices')
        }
    }
    return(
        <div className = 'home'>
            <div className ='top-menu'>
                <Menu/>
            </div>
            <div className = 'container'>
                <div className = 'container-spend'>
                    <Namer/>
                    <div className = 'text'>
                        <h3>Insert the new invoice.</h3>
                    </div>
                </div>
                <div className = 'content_addspend'>
                    <form className = 'form'>
                        <input className = 'Spendbox' name='spend' value = {spend.spend|| ''} type='number' step = {0.01} min = {0} placeholder = 'ex: 25.65' onChange = {handdleInput}></input>
                        <input className = 'Spendbox' name='date' value = {spend.date||''} type = 'date' onChange={handdleInput}></input>
                        <input className = 'Spendbox' name='description' value = {spend.description||''} type = 'text' placeholder='description' onChange={handdleInput}></input>
                    </form>
                    <button className = 'submit_spend' onClick = {onSubmit}>Submit</button>
                    {modal&&(
                    <div className = 'modalBox'>
                        <div className = 'overlay'>
                            <div className = 'update-content'>
                                <div className = 'centralize'>
                                    <h2 className = 'Centralize'>
                                        Submit successfully
                                    </h2>
                                </div>
                                <div className = 'forms'>
                                    <div className = 'lineblock'>
                                        <h4 className = 'Centralize'>Continue Adding?</h4>
                                        <button className = 'button' onClick = {()=>handlesubmit(0)}>yes</button>
                                        <button className = 'button-right' onClick = {()=>handlesubmit(1)}>no</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                )}
                </div>
            </div>
        </div>
    )
}
export default AddSpend;