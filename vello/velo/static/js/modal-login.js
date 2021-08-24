var login_modal = document.getElementById("login-modal");
var login_btn = document.getElementById("login-button");
var closeButton = document.querySelector(".close")

login_btn.onclick = function() {
  login_modal.style.display = "block";
}

closeButton.onclick = function() {
  login_modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == login_modal) {
    login_modal.style.display = "none";
  }
}