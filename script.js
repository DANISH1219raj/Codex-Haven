async function startWebcam() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        document.getElementById("video").srcObject = stream;
    } catch (error) {
        alert("Error accessing webcam: " + error);
    }
}

startWebcam();

// Placeholder: Replace with AI Integration
function simulateSignDetection() {
    const words = ["Hello", "Thank You", "Yes", "No", "Please", "Goodbye"];
    const randomWord = words[Math.floor(Math.random() * words.length)];
    document.getElementById("output-text").textContent = randomWord;
}

// Simulate sign detection every 3 seconds (replace with real AI model)
setInterval(simulateSignDetection, 3000);
