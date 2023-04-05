const chatMessages = document.getElementById("chat-messages");
const chatForm = document.getElementById("chat-form");
const chatInput = document.getElementById("chat-input");

let conversation = [];

// Load conversation from localStorage
if (localStorage.getItem("conversation")) {
  conversation = JSON.parse(localStorage.getItem("conversation"));
  displayMessages();
}

chatForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const message = chatInput.value.trim();
  if (message) {
    addMessageToConversation(message);
    chatInput.value = "";
    // Save conversation to localStorage
    localStorage.setItem("conversation", JSON.stringify(conversation));
    displayMessages();
    // Add your AI chatbot logic here
  }
});

function addMessageToConversation(message) {
  conversation.push(message);
}

function displayMessages() {
  chatMessages.innerHTML = conversation
    .map((message) => `<div class="message">${message}</div>`)
    .join("");
  chatMessages.scrollTop = chatMessages.scrollHeight;
}
