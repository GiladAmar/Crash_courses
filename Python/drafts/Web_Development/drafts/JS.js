// JS

// To reset media element
const mediaElem = document.getElementById("my-media-element");
mediaElem.load();

/* Using the <script>...</script>
or <script src="script.js" defer></script> //defer says only execute after loading DOM
        there is also async
        but scripts aren't even run in the order they appear
    defer runs in order of appearnace
* Interpreted language
* Just in time compiler*/

Server-side: Executed on server PHP, Python, Ruby, ASP.NET and JS, Node.js
Client-side: Run on user's computer'

Browser APIs
    DOM (Document Object Model) - Manipulate HTML and CSS
    Geolocation                 - Geolocation
    Canvas / WebGL              - 2D/3D graphics
    HTMLMediaElement/WebRTC     - Audio/Video

Third-party APIs:
    Twitter
    Google
    OpenStreetMap
...

* Need to ensure JS is loaded after component sso issues do't occur
    * One tab cannot affect another


To ensure js code runs after loading in browser:
document.addEventListener("DOMContentLoaded", function() {
    // do stuff here
    });

Implicit Modules/Objects:
Math.rna
document


Variables:
// Use let and const over var
let a=1       // Can only initialise once, but still changable e.g. a=2
const pi=3.14 //document.querySelector('.guessSubmit') is also const even though an element thereof may change
var x=16       // Can init many times

// DOn't use underscofres in na,es
use lower camelcase
case sensitive

int
toString()
boolean     true/false
array let myNameArray = ['Chris', 'Bob', 'Jim'];
myNameArray[0]; // should return 'Chris'
let dog = { name : 'Spot', breed : 'Dalmatian' }; object
* dynamically typed like pyton
