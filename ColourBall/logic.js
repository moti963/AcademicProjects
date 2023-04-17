function gen_colour() {
    const chars = '0123456789abcdef';
    let hex = '#';
    for (let i = 0; i < 6; i++) {
        const randomIndex = Math.floor(Math.random() * chars.length);
        hex += chars[randomIndex];
    }
    return hex;
}

function createButtons() {
    const size = parseInt(document.getElementById("size").value);
    if (size > 200 || size < 0) {
        alert("Please enter value between 1 and 200");
        return;
    }
    const colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "gray", "brown"];
    const buttonContainer = document.getElementById("button-container");
    buttonContainer.innerHTML = "";
    for (let i = 0; i < size; i++) {
        // const color = colors[i % colors.length];
        const button = document.createElement("button");
        let color = gen_colour();
        button.style.backgroundColor = color;
        button.style.color = gen_colour();
        button.style.border = color;
        button.textContent = `Button ${i + 1}`;
        button.className = "btn btn-sm m-2";
        button.onclick = function () {
            const circle = document.getElementById("circle");
            circle.style.color = button.style.color;
            circle.style.backgroundColor = button.style.backgroundColor;
            circle.style.border = button.style.color;
        }
        buttonContainer.appendChild(button);
        if (i >= 200) {
            break;
        }
    }
}