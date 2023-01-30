import React from 'react';
import {useNavigate} from 'react-router-dom'
import './main.css';
export default function Main () {
    let navigate = useNavigate();
    return (
        <div className='login'>
        <button className='write_post' onClick={()=>{navigate('/writing')}}>글쓰기</button>
        <button className='search' onClick={()=>{navigate('/eheqhrl')}}>검색</button>
        </div>
    );
}

