import React from 'react';
import {useNavigate} from 'react-router-dom'
import './main.css';
import { useState } from 'react';
export default function Main () {
    let navigate = useNavigate();
    const[popup,setPop]=useState(false);
    const handleClichOpen=()=>{
        setPop(!popup);
    } 
    const closePopup=()=>{
        setPop(false);
    }
    return (
        <div className='login'>
        <button onClick={handleClichOpen} className='write_post' >글쓰기</button>
        <button className='searchh' onClick={()=>{navigate('/eheqhrl')}}>검색</button>
        <div>
            {popup?
        <div className='popup-c'>
            <div className='popup'>
                <div className='popup-header'>
                <button onClick={closePopup} className='X'>X</button>
                <input type="text" placeholder='제목입력'className='title'/>
                </div>
                <div>
                <textarea placeholder='내생각입력'className='cont'></textarea>
                <button onClick={closePopup} className='Registration'>등록</button>
                <button onClick={closePopup} className='photo'>사진</button>
                <button onClick={closePopup} className='Play'>플레이</button>
                    </div>
                </div>
        </div>:""}
        
        </div>
        </div>
    );
}


