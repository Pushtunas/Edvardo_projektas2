function refreshTime() {
  const timeDisplay = document.getElementById("time");
  const dateString = new Date().toLocaleString('lt');
  timeDisplay.textContent = dateString;
}
  setInterval(refreshTime, 1000);
