// const apiUrl = 'http://192.168.0.15:5000';
// const apiUrl = 'http://192.168.0.15:5000';
// const apiUrl = 'http://192.168.0.15:5000';
const apiUrl = 'http://127.0.0.1:5000';

let api_key;

async function register() {
    const usernameInput = document.getElementById("username").value
    const passwordInput = document.getElementById("password").value;
    const emailInput = document.getElementById("email").value;
    const newItem = {
        'username': usernameInput,
        'email': emailInput,
        'password': passwordInput,
        'account_type': 'USER'
    };

    try {
        const response = await fetch(apiUrl + '/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newItem),
        });
        if (!response.ok) throw new Error(`POST failed: ${response.status}`);
        const data = await response.json();
        alert(JSON.stringify(data, null, 2)); // Display JSON in a readable format
    } catch (error) {
        displayResponse({error: error.message});
        alert(`Failed to register: ${error.message}`);
    }
}

async function login() {
    const passwordInput = document.getElementById("password").value;
    const emailInput = document.getElementById("email").value;
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
        if (!response.ok) throw new Error(`POST failed: ${response.status}`);
        const data = await response.json();
        alert(JSON.stringify(data))

    } catch (error) {
        displayResponse({error: error.message});
    }
}

async function testApi() {
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        alert(JSON.stringify(data, null, 2)); // Display JSON in a readable format
    } catch (error) {
        console.error("Error while testing API:", error);
        alert(`Failed to fetch API data: ${error.message}`);
    }
}

async function testLogin() {

    const passwordInput = document.getElementById("password").value;
    const emailInput = document.getElementById("email").value;
    const apiUrl = 'http://127.0.0.1:5000/login'; // Replace with your Flask server URL
    const payload = {
        email: emailInput,
        password: passwordInput
    };

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log("Response from server:", data);
        alert(`Success: ${JSON.stringify(data, null, 2)}`);
    } catch (error) {
        console.error("Error while testing /login endpoint:", error);
        alert(`Failed to test /login: ${error.message}`);
    }
}


async function logout() {
    if (api_key == null) {

    } else {
        api_key = null;
    }
}