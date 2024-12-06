// const product_photo = document.getElementById('product_photo');

/*async function fetchUser() {
    try {
        // Fetch data from the Random User API
        const response = await fetch('https://randomuser.me/api/');
        const data = await response.json();

        // Extract user details from the API response
        const product = user.picture.large;
        // Update the DOM elements with the user data
        userPhoto.src = photo;

    } catch (error) {
        // Log errors to the console
        console.error('Error fetching user:', error);
        userName.textContent = 'Failed to load user. Try again!';
        userEmail.textContent = '';
        userPhoto.src = '';
    }
}*/

const apiUrl = 'http://127.0.0.1:5000';
let api_key = localStorage.getItem("api_key");


async function login() {
    const passwordInput = document.getElementById("password").value;
    const emailInput = document.getElementById("email").value;
    alert(emailInput + passwordInput)
    const newItem = {
        'email': emailInput,
        'password': passwordInput,
    };

    try {
        const response = await fetch(apiUrl + '/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newItem),
        });
        if (!response.ok) {
            alert("login faild")
            throw new Error(`POST failed: ${response.status}`);
        }
        const data = await response.json();
        api_key = data['api_key']
        localStorage.setItem("api_key", api_key);
        alert(JSON.stringify(data))

        window.location.href = 'index.html';

    } catch (error) {
        displayResponse({error: error.message});
    }
}

async function addProduct() {

    // Get the values from the form
    const productName = document.getElementById('product-name').value;
    const productPrice = document.getElementById('product-price').value;
    const productImg = document.getElementById('product-img').value;

    // Create an object representing the product
      //  required_fields = ['api_key', 'name', 'price', 'image', 'quantity']
    //
    const newItem = {
        api_key: api_key,
        name: productName,
        price: productPrice,
        quantity: 1,
        account_type: "ADMIN",
        image: productImg,
    };

    try {
        const response = await fetch(apiUrl + '/admin/product/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newItem),
        });
        if (!response.ok) {
            throw new Error(`POST failed: ${response.status}`);
        }
        const data = await response.json();
        window.location.href = 'index.html';

    } catch (error) {
        displayResponse({error: error.message});
    }


}

// Function to dynamically add the product to the page
function addProductToPage(product) {
    const productsContainer = document.getElementById('products-container');
    const productDiv = document.createElement('div');
    productDiv.classList.add('product');
    productDiv.innerHTML = `
        <img src="${product.img}" alt="${product.name}" />
        <h3>${product.name}</h3>
        <p>Price: $${product.price}</p>
    `;
    productsContainer.appendChild(productDiv);
}


async function onPageLoad() {
    if (api_key === "") {
        //not logged in
    } else {
        newItem = {
            'api_key': api_key
        }
        const response = await fetch(apiUrl + '/account/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newItem),
        });
        if (!response.ok) throw new Error(`POST failed: ${response.status}`);
        if (response['account_type'] === 'ADMIN') {

            //TODO: Show admin page
            //show admin page
        } else if (response['account_type'] === 'USER') {
            //show user page
            //TODO: Show user page
        }
    }
}

async function loadProducts(productsData) {
    try {
        const response = await fetch(apiUrl + '/products', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });
        if (!response.ok) throw new Error(`GET failed: ${response.status}`);
        const productsData = await response.json();

        const productsContainer = document.querySelector('.sec-3 .contener');
        productsContainer.innerHTML = ''; // Clear existing content
        productsData.forEach(product => {
            const productDiv = document.createElement('div');
            productDiv.classList.add('img-item');
            productDiv.innerHTML = `
                <img src="${product.ImageSrc}" width="340px" height="190px">
                <div class="img-overlay">
                    <h2>${product.Name}</h2>
                    <p>Price: $${product.price}</p>
                    <a href="#"><i class="fas fa-cart-arrow-down"></i></a>
                </div>
            `;
            productsContainer.appendChild(productDiv);
        });
    } catch (error) {
        console.error('Error loading products:', error);
    }
}

async function withdrawMoney() {
    const amount = document.getElementById('money-input').value;
    alert(amount)
    const newItem = {
        'api_key': api_key,
        'amount': parseInt(amount)
    }
    try {
        const response = await fetch(apiUrl + '/payment/withdraw', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newItem),
        });
        if (!response.ok) throw new Error(`POST failed: ${response.status}`);
        await checkLogin();

    } catch (error) {
        displayResponse({error: error.message});
    }
}

async function depositMoney() {
    const amount = document.getElementById('money-input').value;
    alert(amount)
    const newItem = {
        'api_key': api_key,
        'amount': parseInt(amount)
    }
    try {
        const response = await fetch(apiUrl + '/payment/deposit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newItem),
        });
        if (!response.ok) throw new Error(`POST failed: ${response.status}`);
        await checkLogin();
    } catch (error) {
        displayResponse({error: error.message});
    }
}

async function checkLogin() {
    alert(api_key)
    if (api_key === "") {
        window.location.href = 'index.html';
    } else {
        newItem = {
            'api_key': api_key
        }
        const response = await fetch(apiUrl + '/account/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newItem),
        });
        if (!response.ok) throw new Error(`POST failed: ${response.status}`);
        const data = await response.json();

        document.getElementById('profile-name').textContent = data['Name'];
        document.getElementById('profile-email').textContent = data['Email'];
        document.getElementById('profile-mode').textContent = data['AccountType'];
        document.getElementById('profile-money').textContent = data['Balance'];

    }
}

async function logout() {
    const newItem = {
        'api_key': api_key,
    }
    try {
        const response = await fetch(apiUrl + '/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newItem),
        });
        if (!response.ok) throw new Error(`POST failed: ${response.status}`);
        localStorage.setItem("api_key", "");
        api_key = "";
    } catch (error) {
        displayResponse({error: error.message});
    }
}