import React from 'react';
import {useNavigate} from 'react-router-dom'
import './signup.css'
export default function Signup() {
    let navigate = useNavigate();
    return (
        <div className='lgin'>
            <input type="email" placeholder='email'className='ema' />
            <input type="passwode"placeholder='password'className='pass' />
            <input type="passwode"placeholder='Confirm Password'className='wode' />
            <button className='signu' onClick={()=>{navigate('/')} }>signup</button>
        </div>
    );
}


