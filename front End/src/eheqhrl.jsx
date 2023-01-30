import React from 'react';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {useNavigate} from 'react-router-dom'
import {faHouse} from "@fortawesome/free-solid-svg-icons";
import {faMagnifyingGlass} from "@fortawesome/free-solid-svg-icons";
import {faPlay} from "@fortawesome/free-solid-svg-icons";
import {faArrowRightToBracket} from "@fortawesome/free-solid-svg-icons";
import './eheqhrl.css'
export default function Eheqhrl()  {
    let navigate = useNavigate();
    return (
        <div>
           <a href="/main"><FontAwesomeIcon icon={faHouse}className="hous" size = '4x'/></a>  
            <input type="text" className='earch' placeholder='검색'/> 
            <a href="/eheqhrl"><FontAwesomeIcon icon={faMagnifyingGlass}  size="4x"className="ehe"/></a>
            
            <a href="/player"><FontAwesomeIcon icon={faPlay } size="4x"className="pl"/></a>
             
             <a href="/"><FontAwesomeIcon icon={faArrowRightToBracket} size="4x"  className ="Arr"/></a>
             
            <p className ="chl">최근들은곡</p>
            <div className='topp'>탑100차트</div>
            
            <div className='lately'>최근에 발매된 앨범</div>
            <div className='rec'>Spotigram 추천 아티스트</div>
        </div>
    );
}
