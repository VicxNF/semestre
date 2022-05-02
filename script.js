function iniciarMap(){
    var coord = {lat:-33.4997506,lng:-70.6151254};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 10,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}

const allHoverImages = document.querySelectorAll('.hover-container div img');
const imgContainer = document.querySelector('.img-container');

window.addEventListener('DOMContentLoaded', () =>{
    allHoverImages[0].parentElement.classList.add('active');
});

allHoverImages.forEach((image) => {
    image.addEventListener('mouseover', () =>{
        imgContainer.querySelector('img').src = image.src;
        resetActiveImg();
        image.parentElement.classList.add('active');
    });
});

function resetActiveImg(){
    allHoverImages.forEach((img) => {
        img.parentElement.classList.remove('active');
    });
}