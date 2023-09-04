// Initialize CodeMirror
const editor = CodeMirror.fromTextArea(document.getElementById("code-editor"), {
    lineNumbers: true,
    mode: "python",
    theme: "default",
  });
  
/// Function to run the Python code
function runCode() {
    const pythonCode = editor.getValue();
  
    // Clear previous output
    document.getElementById("output").innerHTML = "";
  
    // Send the Python code to the server for execution
    fetch('http://localhost:5500/runcode', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: `code=${encodeURIComponent(pythonCode)}`
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok.');
      }
      return response.json();
    })
    .then(data => {
      console.log(data); // Log the data received from the server for debugging
  
      if (data.output) {
        // Display the output in the "output" div
        document.getElementById("output").innerHTML = "<pre>" + data.output + "</pre>";
      } else if (data.error) {
        // Display any errors that occurred during code execution
        document.getElementById("output").innerHTML = "<pre>Error: " + data.error + "</pre>";
      } else {
        // Handle unexpected response
        document.getElementById("output").innerHTML = "<pre>Unexpected response from server.</pre>";
      }
    })
    .catch(error => {
      console.error(error);
      document.getElementById("output").innerText = "Error occurred while running the code.";
    });
  }



// Initialize CodeMirror
const editor2 = CodeMirror.fromTextArea(document.getElementById("code-editor2"), {
  lineNumbers: true,
  mode: "python",
  theme: "default",
});

/// Function to run the Python code
function runCode2() {
  const pythonCode = editor2.getValue();

  // Clear previous output
  document.getElementById("output").innerHTML = "";

  // Send the Python code to the server for execution
  fetch('http://localhost:5500/runcode', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: `code=${encodeURIComponent(pythonCode)}`
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok.');
    }
    return response.json();
  })
  .then(data => {
    console.log(data); // Log the data received from the server for debugging

    if (data.output) {
      // Display the output in the "output" div
      document.getElementById("output").innerHTML = "<pre>" + data.output + "</pre>";
    } else if (data.error) {
      // Display any errors that occurred during code execution
      document.getElementById("output").innerHTML = "<pre>Error: " + data.error + "</pre>";
    } else {
      // Handle unexpected response
      document.getElementById("output").innerHTML = "<pre>Unexpected response from server.</pre>";
    }
  })
  .catch(error => {
    console.error(error);
    document.getElementById("output").innerText = "Error occurred while running the code.";
  });
}