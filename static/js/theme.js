const btnTheme = document.querySelector("#btn-theme");



// Save theme in LocalStorage
// Define variables every theme
function changeTheme(theme){
  const root = document.documentElement
  if(theme === "light"){
    root.style.setProperty("--font-text", "#000000");
    root.style.setProperty("--background", "#FFFFFF");
    root.style.setProperty("--button-color", "#000000");
    root.style.setProperty("--button-font", "#000000");
    root.style.setProperty("--overlay", "rgba(255, 255, 255, 0.35)");
    root.style.setProperty("--login-color" , "rgb(30, 24, 157)");
    root.style.setProperty("--login-screen","radial-gradient(circle at 0% 0%, rgba(255, 90, 90, 0.15) 0%, rgba(250, 47, 47, 0.15) 50%, rgba(0, 37, 255, .15) 100%) 0px 0px ");
    root.style.setProperty("--placeholder" , "rgba(0, 0, 0, 0.41)" );
    localStorage.setItem("theme", "light");
  }
  if(theme === "dark"){
    root.style.setProperty("--font-text", "#FFFFFF");
    root.style.setProperty("--background", "#000000");
    root.style.setProperty("--button-color", "#FFFFFF");
    root.style.setProperty("--button-font", "#FFFFFF");
    root.style.setProperty("--overlay", "rgba(0, 0, 0, 0.15)");
    root.style.setProperty("--login-color" , "#FF7495" );
    root.style.setProperty("--login-screen","radial-gradient(circle at 0% 0%, rgba(55, 71, 162, 0.59) 0%, rgba(73, 87, 164, 0.59) 50%, rgba(250, 8, 168, 0.59) 100%) 0px 0px");
    root.style.setProperty("--placeholder" , "rgba(255, 255, 255, 0.41)" );
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