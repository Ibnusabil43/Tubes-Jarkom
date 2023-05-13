const navbar = document.querySelector(".navbar");
window.addEventListener("scroll", () => {
  console.log(window.scrollY);
  if (this.window.scrollY >= 56) {
    navbar.classList.add("nav-color");
  } else if (this.window.scrollY < 56) {
    navbar.classList.remove("nav-color");
  }
});
