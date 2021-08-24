var signup_modal = document.getElementById("signup-modal");
var signup_btn = document.getElementById("signup-button");
var closeButton = document.querySelector(".close")


signup_btn.onclick = function() {
  signup_modal.style.display = "block";
}

closeButton.onclick = function() {
  signup_modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == signup_modal) {
    signup_modal.style.display = "none";
  }
}