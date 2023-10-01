const input = document.getElementById("myInput");
const placeholder = document.getElementById("placeholder");

input.addEventListener("focus", () => {
  placeholder.style.opacity = "0";
});

input.addEventListener("blur", () => {
  if (input.value === "") {
    placeholder.style.opacity = "1";
  }
});