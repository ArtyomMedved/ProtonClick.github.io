function incrementClicks() {
  if (typeof(Storage) !== "undefined") {
    if (localStorage.numClicks) {
      localStorage.numClicks = Number(localStorage.numClicks) + 1;
    } else {
      localStorage.numClicks = 1;
    }
    document.getElementById("numClicks").innerHTML = localStorage.numClicks;
  } else {
    document.getElementById("numClicks").innerHTML = "Unfortunately, your browser does not support web storage...";
  }
}


