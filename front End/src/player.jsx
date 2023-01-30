import React from 'react';
import {useNavigate} from 'react-router-dom'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {faHouse} from "@fortawesome/free-solid-svg-icons";
import {faMagnifyingGlass} from "@fortawesome/free-solid-svg-icons";
import {faPlay} from "@fortawesome/free-solid-svg-icons";
import {faForwardStep} from "@fortawesome/free-solid-svg-icons";
import {faBackwardStep} from "@fortawesome/free-solid-svg-icons";
import {faArrowRightToBracket} from "@fortawesome/free-solid-svg-icons";
import './player.css'
export default function Player () { 
    let navigate = useNavigate();
    return (
        
        <div className='lgin'>
            <p className='Lyrics'>가사</p>
            <a href="/main"><FontAwesomeIcon icon={faHouse}className="hous" size = '4x'/></a>  
            <a href="/eheqhrl"><FontAwesomeIcon icon={faMagnifyingGlass}  size="4x"className="ehe"/></a>
            <a href="/player"><FontAwesomeIcon icon={faPlay } size="4x"className="pl"/></a>
            <FontAwesomeIcon icon={faPlay } size="6x"  className="ay"/>
            <FontAwesomeIcon icon={faForwardStep} size="6x" className="for"/>
            <FontAwesomeIcon icon={faBackwardStep} size="6x"  className="bac"/>
            <a href="/"><FontAwesomeIcon icon={faArrowRightToBracket} size="4x"  className ="Arr"/></a>
            <p className ="chl">최근들은곡</p>
        </div>
    );
}


