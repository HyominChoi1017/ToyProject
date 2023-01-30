import React from 'react';
import {useNavigate} from 'react-router-dom'
import './writing.css'
export default function Writing()  {
    let navigate = useNavigate();
    return (
        <div className='lgin'>
            <dl>
             <dd ><input type="text" placeholder='제목입력'className='title'/></dd>
            </dl>
            <div className='hea'>제목</div>
            
            <textarea placeholder='내생각입력'className='cont'></textarea>
            <div className='writee'></div>
            <button className='plo'onClick={()=>{navigate('/main')} }>플레이리스트등록</button>
            <button className='no' onClick={()=>{navigate('/main')} }>취소</button>
            
        </div>
    );
}


