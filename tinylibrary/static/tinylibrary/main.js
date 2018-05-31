import {TlScanner} from "./tl-scanner.js"
import "./main.scss"
import {Button} from "@material/mwc-button"
import {Icon} from "@material/mwc-icon"

// import {Card} from "@material/mwc-card"

export default function do_binds() {
    if (document.forms.length > 0) {
  	document.querySelector("mwc-button.mwc-submit").addEventListener("click", function(e){
  		document.forms[0].submit()
  	})
    }
    let startbtn = document.querySelector("mwc-button.scanner-start")
    if (startbtn) {startbtn.addEventListener("click", click_scanner)}
    let stopbtn = document.querySelector("mwc-button.scanner-stop")
    if (stopbtn){stopbtn.addEventListener("click", stop_scanner)}
}

do_binds()


function stop_scanner(e){
    console.log("trying to turn off quagga")
    Quagga.stop()
}

function click_scanner(e) {
    var s = document.querySelector("tl-scanner")
    console.log(typeof s.StartScanner)
    s.StartScanner()  
}