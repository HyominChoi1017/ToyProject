import './App.css';
import{ BrowserRouter, Routes, Route, Link} from 'react-router-dom';
import Login from './login';
import Signup from './signup';
import Writing from './writing';
import Main from './main';
import Eheqhrl from './eheqhrl';
import Player from './player';
function App() {
  return (
    
    <div className='App'>
      
    <BrowserRouter>
    <nav>
      <Link to={'/main'}>main</Link>
      <Link to={'/player'}>player</Link>
      <Link to={'/profile'}>profile</Link>
      <Link to={'/eheqhrl'}>eheqhrl</Link>
      <Link to={'/writing'}>writing</Link>

    </nav>
    <Routes>
      <Route path='/' element={<Login />} />
      <Route path='/signup' element={<Signup />} />
      <Route path='/main' element={<Main />} />
      <Route path='/player' element={<Player />} />
      <Route path='/profile' element={<profile />} />
      <Route path='/eheqhrl' element={<Eheqhrl />} />
      <Route path='/writing' element={<Writing />} />
      </Routes>
      </BrowserRouter>
     
      </div>
  );
}


export default App;
