

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

let carts = document.querySelectorAll('.add-cart-btn');

let products = [
    {
        name: 'Margarita',
        tag: 'margarita',
        price: 2990,
        inCart: 0
    },
    {
        name: 'Azalea',
        tag: 'azalea',
        price: 2990,
        inCart: 0
    },
    {
        name: 'Hortensia',
        tag: 'hortensia',
        price: 2990,
        inCart: 0
    },
    {
        name: 'Lirio Rosado',
        tag: 'lirio',
        price: 2990,
        inCart: 0
    }
];

for (let i=0; i < carts.length; i++){
    carts[i].addEventListener('click', () => {
        cartNumbers(products[i]);
        totalCost(products[i])
    })
}

function onLoadCartNumbers(){
    let productNumbers = localStorage.getItem('cartNumbers');

    if(productNumbers){
        document.querySelector('.cart-btn span').textContent = productNumbers;
    }
}

function cartNumbers(product){
    let productNumbers = localStorage.getItem('cartNumbers');

    productNumbers = parseInt(productNumbers);

    if(productNumbers){
        localStorage.setItem('cartNumbers', productNumbers + 1);
        document.querySelector('.cart-btn span').textContent = productNumbers + 1;
    } else {
        localStorage.setItem('cartNumbers', 1);
        document.querySelector('.cart-btn span').textContent = 1;
    }

    setItems(product);
}

function setItems(product){
    let cartItems = localStorage.getItem('productsInCart');
    cartItems = JSON.parse(cartItems);

    if(cartItems != null){
        if(cartItems[product.tag] == undefined){
            cartItems = {
                ...cartItems,
                [product.tag]: product
            }
        }
        cartItems[product.tag].inCart += 1;
    } else {
        product.inCart = 1;
        cartItems = {
            [product.tag] : product
        }
    }

    localStorage.setItem("productsInCart", JSON.stringify(cartItems));
}

function totalCost(product){
    //console.log("El precio del producto es", product.price);
    let cartCost = localStorage.getItem('totalCost');

    console.log("My cartCost is", cartCost);
    console.log(typeof cartCost);

    if(cartCost != null){
        cartCost = parseInt(cartCost);
        localStorage.setItem("totalCost", cartCost + product.price);
    } else{
        localStorage.setItem("totalCost", product.price);
    }
}

function displayCart(){
    let cartItems = localStorage.getItem("productsInCart");
    cartItems = JSON.parse(cartItems);
    let productContainer = document.querySelector(".products");
    if(cartItems && productContainer){
        productContainer.innerHTML = '';
        Object.values(cartItems).map(item =>{
            productContainer.innerHTML += `
            <div class="product">
                <i class="bi bi-trash3"></i>
                <img src="./img/${item.tag}.jpg">
                <span>${item.name}</span>
            </div>
            `
            
            
        });
    }
}

onLoadCartNumbers();

function initMap(){
    const ubicacion = new Localizacion(()=>{

        const options = {
            center: {
                lat: ubicacion.latitude,
                lng: ubicacion.longitude
            },

            zoom: 15
        }

        var map = document.getElementById('map');

        const mapa = new google.map.Map(map, options);
    });
}

function validate()
{
    var email=document.getElementById("email").value;
    var password=document.getElementById("password").value;
    if(email=="admin@gmail.com" && password =="admin")
    {
        alert("Ingreso satisfactorio");
        return false;
    }
    else
    {
        alert("Ingreso no valido")
    }
}