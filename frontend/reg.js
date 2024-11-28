const apiUrl = 'http://127.0.0.1:5000';
async function register() {
    alert("hi mostafa")
    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password");
    const emailInput = document.getElementById("email");
    const newItem = {
            'username':usernameInput,
            'email':   emailInput,
            'password':passwordInput
    };

    try {
        const response = await fetch(apiUrl+'/auth/register', {
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
        displayResponse({ error: error.message });
    }
}
