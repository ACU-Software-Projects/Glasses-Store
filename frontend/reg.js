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
        'account_type': 'user'
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

    } catch (error) {
        displayResponse({error: error.message});
    }
}

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
        if (!response.ok) throw new Error(`POST failed: ${response.status}`);
        const data = await response.json();
        api_key = data['api_key'];
        alert(api_key);

    } catch (error) {
        displayResponse({error: error.message});
    }
}

async function logout() {
    if (api_key == null) {

    } else {
        api_key = null;
    }
}