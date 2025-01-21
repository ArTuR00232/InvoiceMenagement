import React from "react";
import { useState, useEffect } from "react";
import Cookies from "js-cookie";
import InputColor from "react-input-color"
import { useNavigate } from "react-router-dom";



export const Edit = (M)=>{

    const [modal, setModal] = useState(false) 
    const invoice = M.Item
    const cookie = Cookies.get()
    const Iduser = JSON.parse(cookie.session).ID
    const [search, setSearch] = useState('')
    const [Markers,SetMarkers] = useState({
      name : '',
      id : ''
    })
    const[Filter, setFilter] = useState([Markers])
    const [Color, setColor] = useState('')
    const nav = useNavigate()
  

   const handleInputChange = (e) => {
   const searchMarker = e.target.value;
   setSearch(searchMarker)

    const filteredMarker = Markers.filter((Marker)=>
    Marker.name.includes(searchMarker))
    setFilter(filteredMarker)
    onChange(e)
    }

    const [form, Setform] = useState({
     ID: '',
     Spended :'',
     Date :'',
      Description :'',
      Marker :'',
    })

    useEffect(()=>{
    checkMarker()
    },[modal])
    useEffect(()=>{
    checkMarker()
    },[search])


    const onChange= (M)=>
      {
          const name = M.target.name
          const value = M.target.value
          Setform(values=>({...values, [name]:value}))
      }

    const check = ()=>{
        if(form.Spended == '')
        {
        form.Spended = invoice.Spended
        }
        if(form.Date == '')
        {
        form.Date = invoice.Date
        }
        if(form.Description == '')
        {
        form.Description = invoice.Description
        if(form.Description == '')
            form.Description = "Null"
        }
        if(form.Marker == '') 
        {
        form.Marker = invoice.Marker
        }
        if(form.Marker !='')
        {
            checkMarker()
        }


    }

    const Edit = () =>{
    console.log('edit')
    check()
    try
    {
        var url = `http:  127.0.0.1:5000/Api/Money/update/${Iduser}+${invoice.Id}+${form.Spended}+${form.Date}+${form.Marker}+${form.Description}+${invoice.Spended}+${invoice.Date}`
        fetch(url,{
            method: 'Post',
            headers:{
            'Content-Type': "application/Json"
            }
        })
        .then(toggleCloseModal())
            .then(window.location.reload())
    }
    catch(e)
    {
        console.error('fetch error: ' + e)
    }
    }

    const toggleCloseModal = ()=>{
    setModal(!modal)
    if(modal) {
        document.body.classList.add('active-modal')
    } else {
        document.body.classList.remove('active-modal')
    }
    }

    function checkMarker(){
    fetch("/Api/Marker/"+Iduser)
    .then(Response=>Response.json())
    .then(Markers => {SetMarkers(Markers)})
    .catch(err => console.error('error fetching:',err ))
    }

    function setMarker(){
        let color = Color.hex.split('#')
        let url = '/Api/marker/post/'+Iduser+'+'+search+'+'+color[1]
        console.log(url)
        fetch(url,{
            method: 'POST',
            headers: {
                'Content-Type':'Application/Json'
            }
        })
        Edit()
    }

    function deleteMarker(Id){     
        let url='/Api/marker/delete/'+Id
        fetch(url,({
        method : 'DELETE',
        'Content-Type':'Application/Json'
        }))
        .then(nav('/Spend'))
    }

    return(
    <div>
        <button className='edit' type='submit' title="Edit" onClick={()=>toggleCloseModal()}>✎</button>
        {modal &&(
        <div className='modalBox'>
            <div className='overlay'>
            <div className='update-content'>
                <div className="centralize">
                <h2>
                    update your invoice
                </h2>
                </div>
                <div className='forms'>
                <div > 
                <p className="centralize">Spend: </p>
                </div>
                <div className="centralize">
                <input className='Spendbox' name="Spended" min={0} type="number"  key={invoice.Id} placeholder={invoice.Spended} onChange={onChange}></input>
                </div>

                <p className="centralize">Date: </p>
                <div className="centralize">
                <input className='Spendbox' name="Date" type="date"  key={invoice.Id} placeholder={invoice.Date}  onChange={onChange}></input>
                </div>

                <p className="centralize">Description: </p>
                <div className="centralize">
                <input className='Spendbox' name="Description" type="text"  key={invoice.Id} placeholder={invoice.Description}  onChange={onChange}></input>
                </div>

                {/* <p className="centralize">Marker: </p>
                <div className="centralize">
                <input className='Spendbox' name="Marker" type="text" key={invoice.Id} placeholder={invoice.Marker|| 'ex: shopping'}  onChange={'onChange'}></input>
                </div> */}

                <p className="centralize">Marker: </p>
                <div className="centralize">
                <div>
                    <input className="Spendbox" name="Marker" type ='text' value={search} onChange={handleInputChange}  placeholder={invoice.Marker|| 'ex: shopping'}/>
                </div>
                </div>

                <div className="form">
                {search === ''
                ?<div>
                    <button className="button" onClick={Edit}>
                        submit
                    </button>
                </div>
            
                :<div>
                    {Filter.length === 0
                ?<div>
                    <div  className="centralize">
                        <InputColor initialValue="#5e72e4" onChange={setColor} placement="right" className='color'/>
                    </div>
                    <div>
                        <button className="button" onClick={()=>(setMarker())}>
                        submit
                        </button>
                    </div>
                    </div>
            
                :<div>
                    <div className="centralize">
                    <ul>
                        {Filter.map(Marker=><div className="buttons">
                                            <li key={Marker.id} onClick={()=>setSearch(Marker.name)}>{Marker.name}</li>
                                            <button className="button" onClick={()=>deleteMarker(Marker.id)}>🗑</button>
                                            </div>)}

                    </ul>
                    </div>
                    <div className="centralize">
                    <button className="button" onClick={Edit}>
                        submit
                    </button>
                    </div>                  
                </div> 
                }
                </div>}
                </div>                

                <p></p>
                <button className="close-modal" onClick={toggleCloseModal}>
                X
                </button>
                </div>
            </div>
        
            </div>
        </div>
        )}
    </div>
    )
}

export default Edit;