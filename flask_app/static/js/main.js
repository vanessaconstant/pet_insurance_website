const toggleBar = document.querySelector(".iconToggle")


toggleBar.addEventListener("click",
function collapse(){

    const dropNav = document.querySelector('.collapsible__body');
    dropNav.classList.toggle('collapsible__expand');
    toggleBar.classList.toggle('nav__icon-active');
});


let map;

let latcoor =(document.querySelectorAll('.lat'));
let lngcoor =(document.querySelectorAll('.lng'));


  function initMap() {

    map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: Number(latcoor[1].innerHTML), lng:Number(lngcoor[1].innerHTML) },
      zoom: 12,
    });

    for (let i = 0; i<latcoor.length; i++){
      console.log(i);
  
    let marker = new google.maps.Marker({
      position: { lat: Number(latcoor[i].innerHTML), lng:Number(lngcoor[i].innerHTML) },
      map:map
  })

}
window.initMap = initMap;

}
  
  
  
  




