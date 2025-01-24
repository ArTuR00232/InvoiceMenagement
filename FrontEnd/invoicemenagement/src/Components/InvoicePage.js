import React, { useState, useEffect } from 'react';
import InputMask from 'react-input-mask';
import Menu from './MenuHeader';
import Cookies from 'js-cookie';
import Namer from './userName';
import Edit from './edit';
//import Graph from './graph';
import { useNavigate } from 'react-router-dom';



export const Invoices = () => {
 const [Info, setInfo] = useState([])
 const [total, setSpended] = useState([{
    id:'ID',
    Spended:'Money',
    Date:'DD/MM/YYYY'
 }])
 const [data, serData] = useState([{
    id:'',
    spent:'',
    Date:'',
    Description:'',
    Marker:'',
    Color:'',
 }])
 const [search, setSearch] = useState('')
 const [selected, setSelected] = useState(null)
 const cookie = Cookies.get()
 const userID = () => {
    if(String(cookie.session) !== 'undefined'){
        return JSON.parse(cookie.session).ID
    }
    if(String(cookie.session) === 'undefined'){
        return false
    }
 }
 const user = userID()
 const nav = useNavigate()

 useEffect(() => {
    fetchData()
 },[])
 useEffect(() => {
    filterData()
 },[search])
 function fetchData(){
    fetch('/API/Money/'+user)
    .then(Response => Response.json())
    .then(data => {serData(data)})
    .catch(error => console.error('fetching error: ', error))

    fetch('/API/Months/'+user)
    .then(Response => Response.json())
    .then(total => {setSpended(total)})
    .catch(error => console.error('fetching error: ', error))

 }
 function filterData(){
    let infos = []
    for(let i = 0; i < data.length;i++){
        let dateToCompare = data[i].Date
        dateToCompare = dateToCompare.split('-')
        dateToCompare = dateToCompare[0]+'-'+dateToCompare[1]
        if(search == dateToCompare){
            infos.push(data[1])
        }
    }
    setInfo(infos)
 }
 const Description = (Id) =>{
    if(selected === Id){
        if(data.Description == 'Null'){
            serData.Description = ''
        }
        return setSelected(null)
    }
    setSelected(Id)
 }
 const Delete =(Item) =>{
    try{
        var url ='/API/Money/delete/'+Item.Id
        fetch(url, {
            method: 'DELETE',
            headers:{
                'Content-Type':'application/Json'
            }
        })
        .then(()=>fetchData())
    }
    catch(item){
        console.error('fetch error: '+item)
    }
 }
 function addS(){
    if(Cookies.get('session') !== undefined){
        nav('/addSpend')
    }
    else{
        nav('/login')
    }
 }
 function refresh(){
    setSearch('')
    fetchData()
 }
 return(
    <div className='spendBox'>
        <div className='top-menu'>
            <Menu/>
        </div>
        <div className='container'>
            {user === false
            ?<Namer/>
            :<div>
                <Namer/>
                <div className='searcher'>
                    <InputMask className='searcher' mask='9999-99' placeholder='searcher' onChange={(value) => setSearch(value.target.value)}/>
                </div>
                <div className='content'>
                    <div>
                        <div className='montSpend'>
                            {total.filter((total)=>{
                                return search === ''
                                ? <p></p>
                                : total.Data.includes(search)
                            }).map(total =>(
                                <div className = 'bankContent' key = {total.Id}>
                                    <div className='spendedBank'>
                                        R${total.TotalSpend}
                                    </div>
                                    <div className='dateBank'>
                                        Date:{total.Data}
                                    </div>
                                    <div className='Centralize'>
                                        <button onClick={()=>setSearch((total.Data))}>🔍</button>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
                <div>
                    {/* <Graph data = {Info} filter = {search}/> */}
                </div>
                <div className='contM'>
                    <div className='utility-box'>
                        <button className='addSpend' type='button' title='Add invoice' onClick={addS}>+</button>
                        <button className='refresh' title='Refresh' onClick={()=>refresh()}>⟳</button>
                    </div>
                    <headers className='spendBox-header'>
                        <div className='boxer'>
                        {data.filter((Item) =>{
                                return search === ''
                                ?Item
                                :Item.Date.includes(search)
                            }).map(Item => (
                                <div className='money_box' key = {Item.Id}>
                                    <div className='conv'>
                                        <p className='marker' style={{backgroundColor: Item.Color}}>
                                            <span className='hoverMarker'>{Item.Marker}</span>
                                        </p>
                                        <div className='grade'>
                                            <div className='Spend'>
                                                💸 Spended: R${Item.Spended}
                                            </div>
                                        </div>
                                        <div className = 'grade'>
                                            <div className='Date'>
                                                📅 Date: {Item.Date}
                                            </div>
                                        </div>
                                        <div className='grade'>
                                            <div className='buttons'>
                                                <button className='delete' title='Delete' onClick={()=>Delete(Item)}>🗑</button>
                                                <Edit Item={Item}/>
                                                <div className='read'>
                                                    <button className='image' onClick={()=>Description(Item.Id)} title='Description'>📝</button>
                                                    <div className='DescriptionBox'>
                                                        <div className={selected===Item.Id ? 'descriptionShow' :'description'}>
                                                            {Item.Description}
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </headers>
                </div>
            </div>}
        </div>
    </div>
 )
}

export default Invoices;
