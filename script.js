let name = prompt("What's your name?");
document.getElementById("greeting").textContent = "Hello, " + name;


document.getElementById("submit").addEventListener("click", function() {
    // Get values from the form
    const mood = document.getElementById("mood").value;
    const notes = document.getElementById("notes").value;
    const rating = document.getElementById("rating").value;

    // Validate the rating
    if (rating < 1 || rating > 10 || isNaN(rating)) {
        alert("Please provide a valid rating between 1 and 10.");
        return;
    }

    // Create a new list item to show in the mood history
    const historyList = document.getElementById("history-list");
    const historyItem = document.createElement("li");
    
    // Create a formatted entry
    const moodText = document.createElement("span");
    moodText.textContent = `Mood: ${mood} (Rating: ${rating})`;
    historyItem.appendChild(moodText);

    // Add notes if available
    if (notes.trim() !== "") {
        const notesText = document.createElement("p");
        notesText.textContent = `Notes: ${notes}`;
        historyItem.appendChild(notesText);
    }

    // Add the item to the history list
    historyList.appendChild(historyItem);

    // Clear the form inputs after submission
    document.getElementById("mood").value = "Happy";
    document.getElementById("notes").value = "";
    document.getElementById("rating").value = "";
});
