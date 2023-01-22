
var btn1 = document.getElementById("btnOne")
var el = document.documentElement;
btn1.addEventListener("click", () => {
  if (el.requestFullscreen) {
    el.requestFullscreen();
  }  
})
btn1.addEventListener("click", () => {
  if (document.exitFullscreen) {
    document.exitFullscreen();
  }
})