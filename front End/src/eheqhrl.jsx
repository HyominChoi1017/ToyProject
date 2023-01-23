import React from 'react';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {useNavigate} from 'react-router-dom'
import {faHouse} from "@fortawesome/free-solid-svg-icons";
import {faMagnifyingGlass} from "@fortawesome/free-solid-svg-icons";
import {faPlay} from "@fortawesome/free-solid-svg-icons";
import {faArrowRightToBracket} from "@fortawesome/free-solid-svg-icons";
export default function Eheqhrl()  {
    let navigate = useNavigate();
    return (
        <div>
            <FontAwesomeIcon icon={faHouse} size="4x" color="blue" className="hous"/>
            <input type="text" className='search' placeholder='검색'/>
            <FontAwesomeIcon icon={faMagnifyingGlass}  size="4x"color="Gray"className="ehe"/>
            <FontAwesomeIcon icon={faPlay } size="4x" color="Gray" className="pl"/>
            <FontAwesomeIcon icon={faArrowRightToBracket} size="4x" color="red" className ="Arr"/>
            <p className ="chl">최근들은곡</p>
            <div className='topp'>탑100차트</div>
            
            <div className='lately'>최근에 발매된 앨범</div>
            <div className='rec'>Spotigram 추천 아티스트</div>
        </div>
    );
}