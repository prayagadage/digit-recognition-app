const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

// Drawing setup
ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);

let drawing = false;

canvas.addEventListener("mousedown", () => { drawing = true; });
canvas.addEventListener("mouseup", () => { drawing = false; ctx.beginPath(); });
canvas.addEventListener("mousemove", draw);

function draw(e) {
    if (!drawing) return;
    ctx.lineWidth = 15;
    ctx.lineCap = "round";
    ctx.strokeStyle = "black";

    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(e.offsetX, e.offsetY);
}

function clearCanvas() {
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function predict() {
    const image = canvas.toDataURL("image/png");

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ image: image })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText = "Predicted: " + data.prediction;
    })
    .catch(err => console.error(err));
}
