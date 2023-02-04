import React from 'react';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {useNavigate} from 'react-router-dom'
import {faHouse} from "@fortawesome/free-solid-svg-icons";
import {faMagnifyingGlass} from "@fortawesome/free-solid-svg-icons";
import {faPlay} from "@fortawesome/free-solid-svg-icons";
import {faArrowRightToBracket} from "@fortawesome/free-solid-svg-icons";
import './eheqhrl.css'
import {useState} from 'react';

export default function Eheqhrl()  {
    const [isActive,setIsActive] =useState(false)
    const [vise,setVise]=useState(false)
    return (
        <div className='dropdown'>
         <div className='dropdown-btn' onClick={e =>setIsActive(!isActive)}>탑100차트
         <span className='fas fa-caret-down'></span></div>
        {isActive &&(
             <div className='dropdown-content'>
             <div className='dropdown-item'>헤이즈-헤픈우연</div>
             <div className='dropdown-item'>자이언티-회전목마</div>
             <div className='dropdown-item'>임창정-소주한잔</div>
             </div>
        )}
        <div className='dropdownn'>
         <div className='dropdown-btnn' onClick={e =>setVise(!vise)}>최근들은곡
         <span className='fas fa-caret-downn'></span></div>
        {vise &&(
             <div className='dropdown-contentt'>
             <div className='dropdown-itemm'>헤이즈-헤픈우연</div>
             <div className='dropdown-itemm'>자이언티-회전목마</div>
             <div className='dropdown-itemm'>임창정-소주한잔</div>
             </div>
        )}
        </div>
        </div>
    );
}
