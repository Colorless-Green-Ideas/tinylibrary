// import {TlScanner} from './tl-scanner.js';
import './main.scss';
import {Button} from "@material/mwc-button";
import {Icon} from "@material/mwc-icon"

// import {Card} from "@material/mwc-card"

export default function do_binds() {
  if (document.forms.length > 0) {
  	document.querySelector("mwc-button.mwc-submit").addEventListener('click', function(e){
  		document.forms[0].submit()
  	})
  }
}

do_binds()