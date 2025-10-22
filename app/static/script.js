async function predict() {
    const input = document.getElementById("userInput").value;
    const token = document.getElementById("apiKey").value;

    const response = await fetch(`/predict?input=${encodeURIComponent(input)}`, {
        headers: {
            "X-API-Key": token
        }
    });

    const data = await response.json();
    document.getElementById("output").innerText = JSON.stringify(data, null, 2);
}
