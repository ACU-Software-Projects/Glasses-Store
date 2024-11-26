const apiUrl = 'http://127.0.0.1:5000'; // Replace with your Flask API base URL

async function createItem() {
    // Capture the input values from the HTML form
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Create the new item object
    const newItem = {
        username: username,
        email: email,
        password: password,
        account_type: 'user'
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
        displayResponse(data);
    } catch (error) {
        displayResponse({error: error.message});
    }
}

// Function to display the response in the <pre> element
function displayResponse(data) {
    document.getElementById('response').textContent = JSON.stringify(data, null, 2);
}

async function hellow() {
    const response = await fetch(apiUrl + '/');
    const data = await response.json();
    displayResponse(data);
}