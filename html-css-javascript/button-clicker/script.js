function loginLogout() {
  const button = document.querySelector(".login-btn");

  if (button.textContent === "Login") {
    button.textContent = "Logout";
  } else {
    button.textContent = "Login";
  }
}
