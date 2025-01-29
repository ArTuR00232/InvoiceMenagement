import React,{useEffect, useState} from "react";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Doughnut } from 'react-chartjs-2';


ChartJS.register(ArcElement, Tooltip, Legend);


export function Graph(data) {
  let list=[]
  const [GraphData, setGraphData] = useState({})
  const [Filter,setFilter] = useState({
    labels:'',
    datasets:[{
      label:'',
      data:[],
      backgroundColor:[],
      borderColor:'',
    }]

  })
  
  useEffect(()=>{
    filter()
  },[data])


  function filter(){
    let filter = data.filter

    let aux = {
      labels:[],
      datasets:[{
        label:'Spend',
        data:[],
        backgroundColor:[],
        borderColor:'rgba(0,0,0,1)',
        borderWidth:2,
      }]
    }

    if(data.data[0] !== undefined)
    {      
      SumMarkers()
      for(let i = 0;i<GraphData.length;i++)
      {
        aux.labels.push(GraphData[i].Marker)
        aux.datasets[0].data.push(GraphData[i].Spent)
        aux.datasets[0].backgroundColor.push(GraphData[i].Color)
        setFilter(aux)      
      }
    }
    else{
      setFilter(aux)
    }
  }

  function SumMarkers(){
    list.push(data.data)
    
    //data.data.sort((a,b)=>a.Date.localeCompare(b.Date))
    const sumMarkers = list[0].reduce((acc,item)=>{
      if(!acc[item.Marker]){
        acc[item.Marker] = 0
      }
      acc[item.Marker] += item.Spended
      return acc
    }, {})
      setGraphData(Object.entries(sumMarkers).map(([key, value])=>({
        Marker:key,
        Spent: value,
      })))


    for(let j = 0; j< GraphData.length;j++){
      for(let i=0; i< data.data.length; i++){
        if(GraphData[j].Marker == data.data[i].Marker){
          GraphData[j].Color = data.data[i].Color
          break
        }
      }
    }
  }

  return (
    <div className="graph">
      {data.filter === ''
      ?<div>
      </div>
      :<div>
        <Doughnut data={Filter}/>
      </div>
      }
    </div>)
}




export default Graph;