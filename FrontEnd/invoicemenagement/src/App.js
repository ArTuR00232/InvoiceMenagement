import './App.css'
import { CookiesProvider } from 'react-cookie';
import { Routies } from "./Components/Routes.js"

function App(){
  return (
    <div className='App'>
      <CookiesProvider defaultSetOptions = {{path : "/"}}>
        <header className='App-header'>
         <Routies/>
        </header>
      </CookiesProvider>
    </div>
  )
}
export default App;