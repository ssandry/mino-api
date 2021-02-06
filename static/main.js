const input     = document.querySelector(".form input");
const link      = document.querySelector("#id-placed");
const button    = document.querySelector("#id-b");

input.addEventListener( "change", (e) => {
    let num = parseInt(input.value)
    if( num > 3 ) {
        button.style.cssText = "transition: 1s;background: linear-gradient(100.28deg, #6f0000 14.35%, #440000 85.65%);";
    } else {
        button.style.cssText = "linear-gradient(100.28deg, #0F6F00 14.35%, #094400 85.65%)";
        link.pathname = `/mino-api/v.1.0/get-collections/${input.value}`
    }
} )