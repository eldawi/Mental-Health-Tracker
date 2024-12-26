document.getElementById("submit-request").addEventListener("click", function() {
    // Get values from the request form
    const issue = document.getElementById("issue").value;
    const contact = document.getElementById("contact").value;

    // Basic validation
    if (!issue || !contact) {
        alert("Please fill out both fields.");
        return;
    }

    // Process the psychiatrist request (Here we are simply alerting the submission)
    alert("Your request has been submitted successfully! A psychiatrist will contact you soon.");

    // Clear the form fields
    document.getElementById("issue").value = "";
    document.getElementById("contact").value = "";
});
