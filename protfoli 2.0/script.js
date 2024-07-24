let dayNight = document.querySelector(".dayNight");
let banner = document.querySelector(".banner");

dayNight,addEventListener("click",()=>{
    banner.classList.toggle("night");
})

let Typing = new Typed("#text",{
    string: ["Neeraj","Coder","Frontend","UI-UX"],
    loop:infinite,
    typespeed:100,
    backspeed:50,
    backdelay:1000
})