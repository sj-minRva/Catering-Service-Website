document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('loginForm');
  const messageDiv = document.getElementById('message');
  const togglePasswordBtn = document.getElementById('togglePassword');
  const passwordInput = document.getElementById('password');

  // Toggle password visibility
  togglePasswordBtn.addEventListener('click', () => {
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
    togglePasswordBtn.textContent = type === 'password' ? 'Show' : 'Hide';
  });

  // Form submission
  loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const password = passwordInput.value;

    // Basic validation
    if (!isValidEmail(email)) {
      showMessage('Please enter a valid email address', 'error');
      return;
    }

    if (username.length < 3) {
      showMessage('Username must be at least 3 characters long', 'error');
      return;
    }

    if (password.length < 6) {
      showMessage('Password must be at least 6 characters long', 'error');
      return;
    }

    // If validation passes, show success message
    showMessage('Login successful!', 'success');
    loginForm.reset();
  });
  document.getElementById("loginBtn").addEventListener("click", function() {
    // Here you can add validation if needed before redirecting
    window.location.href = "afterlogin.html"; // Redirects to book.html
});


  // Helper function to validate email
  function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  // Helper function to show messages
  function showMessage(text, type) {
    messageDiv.textContent = text;
    messageDiv.className = `message ${type}`;
    
    // Clear message after 3 seconds
    setTimeout(() => {
      messageDiv.textContent = '';
      messageDiv.className = 'message';
    }, 3000);
  }
});