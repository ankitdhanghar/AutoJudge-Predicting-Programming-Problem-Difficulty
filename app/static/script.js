function predict() {
  const description = document.getElementById("description").value.trim();
  const inputDesc = document.getElementById("input_desc").value.trim();
  const outputDesc = document.getElementById("output_desc").value.trim();

  if (!description || !inputDesc || !outputDesc) {
    alert("Please fill all fields!");
    return;
  }

  const payload = {
    description: description,
    input_description: inputDesc,
    output_description: outputDesc
  };

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  })
  .then(response => {
    if (!response.ok) {
      throw new Error("Server error: " + response.status);
    }
    return response.json();
  })
  .then(data => {
    // Update difficulty and score in HTML
    document.getElementById("difficulty").innerText = data.class || "N/A";
    document.getElementById("score").innerText = data.score !== undefined ? data.score : "N/A";
  })
  .catch(error => {
    console.error("Error:", error);
    alert("Error connecting to the backend. Make sure Flask is running.");
  });
}
