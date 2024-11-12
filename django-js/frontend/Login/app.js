document.getElementById('loginForm').addEventListener('submit', async function (event) {
    event.preventDefault(); // Prevent default form submission

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const data = { username, password };

    try {
        // Send login data to the Django backend API endpoint
        const response = await fetch('http://127.0.0.1:8000/api/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        // Check if the response is OK (200-299 status codes)
        if (response.ok) {
            const responseData = await response.json();
            // Handle successful login (store token or session)
            alert('Login successful!');
        } else {
            const errorData = await response.json();
            document.getElementById('errorMessage').textContent = errorData.error;
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('errorMessage').textContent = 'Network error. Please try again.';
    }
});
