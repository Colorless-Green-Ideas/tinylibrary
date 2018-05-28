import {LitElement, html} from "https://unpkg.com/@polymer/lit-element@latest/lit-element.js?module"


class TlScanner extends LitElement {

    // Public property API that triggers re-render (synced with attributes)
    static get properties() {
        return {
            foo: String,
            whales: Number
        }
    }
    ProcessISBNs() {
        new Set(this.shadowRoot.querySelector("#t").data)
    }
    StartScanner(){
        Quagga.init({
            inputStream : {
                name : "Live",
                type : "LiveStream",
                target: this.shadowRoot.querySelector("#yourElement")
            },
            decoder : {
                readers : ["ean_8_reader", "ean_reader"]
            }
        }, function(err) {
            if (err) {
                console.log(err)
                return
            }
            console.log("Initialization finished. Ready to start")
        })
        Quagga.onDetected(function(data){
            console.log(data.codeResult.code)
            this.shadowRoot.querySelector("#t").push("data", data.codeResult.code)
        })
        this.shadowRoot.querySelector("#t").data = []
        Quagga.start()
    }
    constructor() {
        super()
        this.foo = "foo"
    // this.addEventListener('click', async (e) => {
    //   this.whales++;
    //   await this.renderComplete;
    //   this.dispatchEvent(new CustomEvent('whales', {detail: {whales: this.whales}}))
    // });
    }

    // Render method should return a `TemplateResult` using the provided lit-html `html` tag function
    _render() {
        return html`
      <style>
        :host {
          display: block;
        }
      </style>
      <div id='yourElement'></div>
      <h4>Quagga scanner</h4>
      <div id="t"></div>
      <slot></slot>
    `
    }

}
customElements.define("tl-scanner", TlScanner)