import React from 'react';
import './login.css';
import {useNavigate} from 'react-router-dom'

export default function Login()  {
    let navigate = useNavigate();
    return (
        <div className = 'background'>
            <button className='login' onClick={()=>{navigate('./main')}}>signin</button>
            <h3 className='heading'>Sportygram</h3>
            <button className='signup' onClick={()=>{navigate('./signup')}}>signup</button>
            <input type="email" placeholder='email'className='email' />
            <input type="password"placeholder='password'className='password' />
            
        </div>
        
        
    );
}


