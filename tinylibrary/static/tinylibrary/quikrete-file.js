import {LitElement, html} from "https://unpkg.com/@polymer/lit-element@latest/lit-element.js?module"

class File extends LitElement {

    // Public property API that triggers re-render (synced with attributes)
    static get properties() {
        return {

        }
    }
    constructor() {
        super()
    }
    _render() {
        return html`
      <style>
        :host {
          display: block;
        }
      </style>
      <h4>FILE SELECTOR 9000</h4>
      <slot></slot>
    `
    }
}

customElements.define("quikrete-file", File)