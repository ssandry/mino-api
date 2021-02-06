const input = document.querySelector(".form input");
const link = document.querySelector("#id-placed");

input.addEventListener( "change", (e) => {
    console.log( input.value )
    link.pathname = `/mino-api/v.1.0/get-collections/${input.value}`
} )