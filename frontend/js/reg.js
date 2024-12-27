const apiUrl = 'http://20.46.49.0:5000';

async function register() {
    alert("register works")
    const usernameInput = document.getElementById("username").value
    const passwordInput = document.getElementById("password").value;
    const emailInput = document.getElementById("emailSignup").value;
    const roleInput = document.querySelector('input[name="role"]:checked').value.toUpperCase();
    alert(usernameInput + passwordInput + emailInput + roleInput)
    const newItem = {
        'username': usernameInput,
        'email': emailInput,
        'password': passwordInput,
        'account_type': roleInput
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
        window.location.href = 'index.html';

    } catch (error) {
        displayResponse({error: error.message});
        alert(`Failed to register: ${error.message}`);
    }
}

// async function login() {
//     const passwordInput = document.getElementById("password").value;
//     const emailInput = document.getElementById("email").value;
//     const newItem = {
//         'email': emailInput,
//         'password': passwordInput,
//     };
//
//     try {
//         const response = await fetch(apiUrl + '/login', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify(newItem),
//         });
//         if (!response.ok) throw new Error(`POST failed: ${response.status}`);
//         const data = await response.json();
//         alert(JSON.stringify(data))
//
//     } catch (error) {
//         displayResponse({ error: error.message });
//     }
// }
