class MyComponent {
    constructor(element, text) {
        element.className += ' my-component'
        this.mydiv = document.createElement('div')
        this.mydiv.className = 'my-inner-element'
        this.mydiv.innerHTML = text
        element.appendChild(this.mydiv)
    }
}