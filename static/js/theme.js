const btnTheme = document.querySelector("#btn-theme");



// Save theme in LocalStorage
// Define variables every theme
function changeTheme(theme){
  const root = document.documentElement
  if(theme === "light"){
    root.style.setProperty("--font-text", "#000000");
    root.style.setProperty("--background", "radial-gradient(circle at 0% 0%, rgb(255, 90, 90) 0%, rgb(250, 47, 47) 50%, rgb(0, 37, 255) 100%)");
    root.style.setProperty("--button-color", "#000000");
    root.style.setProperty("--button-font", "#FFFFFF");
    root.style.setProperty("--overlay", "rgba(255, 255, 255, 0.35)");
    root.style.setProperty("--login-color" , "rgb(30, 24, 157)");
    localStorage.setItem("theme", "light");
  }
  if(theme === "dark"){
    root.style.setProperty("--font-text", "#FFFFFF");
    root.style.setProperty("--background", "radial-gradient(circle at 0% 0%, rgb(1, 26, 171) 20%, rgb(255, 0, 54) 100%) 50% 50%");
    root.style.setProperty("--button-color", "#FFFFFF");
    root.style.setProperty("--button-font", "#000000");
    root.style.setProperty("--overlay", "rgba(0, 0, 0, 0.15)");
    root.style.setProperty("--login-color" , "#FF7495" );
    localStorage.setItem("theme", "dark");
  } 
}

btnTheme.addEventListener("click", ()=>{
  const theme = localStorage.getItem("theme");
  changeTheme(theme == "light" ? "dark" : "light");
})

document.addEventListener("DOMContentLoaded", ()=>{
  const theme = localStorage.getItem("theme") || ("dark");
  changeTheme(theme);
});