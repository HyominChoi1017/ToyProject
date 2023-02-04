import './App.css';
import{ BrowserRouter, Routes, Route, Link} from 'react-router-dom';
import Login from './login';
import Signup from './signup';

import Main from './main';
import Eheqhrl from './eheqhrl';
import Player from './player';

function App() {
  return (
   
    <div className='App'>
      

      
    <BrowserRouter>
    
    <Routes>
      <Route path='/' element={<Login />} />
      <Route path='/signup' element={<Signup />} />
      <Route path='/main' element={<Main />} />
      <Route path='/player' element={<Player />} />
      <Route path='/eheqhrl' element={<Eheqhrl />} />

      </Routes>
      </BrowserRouter>
      </div>
  );
}


export default App;
