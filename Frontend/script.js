// const chatbox = document.getElementById("chatbox");
// const userInput = document.getElementById("userInput");
// const sendBtn = document.getElementById("sendBtn");
// const speakBtn = document.getElementById("speakBtn");

// function appendMessage(sender, message) {
//   const msgDiv = document.createElement("div");
//   msgDiv.className = sender;
//   msgDiv.textContent = `${sender === "user" ? "🧑" : "🤖"} ${message}`;
//   chatbox.appendChild(msgDiv);
//   chatbox.scrollTop = chatbox.scrollHeight;
// }

// sendBtn.addEventListener("click", () => sendQuery());
// userInput.addEventListener("keypress", e => {
//   if (e.key === "Enter") sendQuery();
// });

// async function sendQuery() {
//   const query = userInput.value.trim();
//   if (!query) return;
//   appendMessage("user", query);
//   userInput.value = "";

//   const res = await fetch("http://127.0.0.1:5000/api/command", {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify({ query })
//   });

//   const data = await res.json();
//   appendMessage("bot", data.reply);
// }

// // 🎤 Voice input
// speakBtn.addEventListener("click", () => {
//   const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
//   recognition.lang = "en-IN";
//   recognition.start();
//   recognition.onresult = async (event) => {
//     const query = event.results[0][0].transcript;
//     appendMessage("user", query);
//     const res = await fetch("http://127.0.0.1:5000/api/command", {
//       method: "POST",
//       headers: { "Content-Type": "application/json" },
//       body: JSON.stringify({ query })
//     });
//     const data = await res.json();
//     appendMessage("bot", data.reply);
//   };
// });


const chatbox = document.getElementById("chatbox");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");
const speakBtn = document.getElementById("speakBtn");

function appendMessage(sender, message) {
  const msgDiv = document.createElement("div");
  msgDiv.className = `message ${sender}`;
  msgDiv.textContent = message;
  chatbox.appendChild(msgDiv);
  chatbox.scrollTop = chatbox.scrollHeight;
}

// typing animation for bot
async function botTypingEffect(text) {
  const msgDiv = document.createElement("div");
  msgDiv.className = "message bot";
  chatbox.appendChild(msgDiv);

  let index = 0;
  function type() {
    msgDiv.textContent = text.substring(0, index++);
    if (index <= text.length) {
      setTimeout(type, 20);
    }
  }
  type();
  chatbox.scrollTop = chatbox.scrollHeight;
}

sendBtn.addEventListener("click", sendQuery);

userInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") sendQuery();
});

async function sendQuery() {
  const query = userInput.value.trim();
  if (!query) return;

  appendMessage("user", query);
  userInput.value = "";

  const response = await fetch("http://127.0.0.1:5000/api/command", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ query })
  });

  const data = await response.json();
  botTypingEffect(data.reply);
}

// 🎤 Voice input
speakBtn.addEventListener("click", () => {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-IN";
  recognition.start();

  recognition.onresult = async (event) => {
    const spoken = event.results[0][0].transcript;
    appendMessage("user", spoken);

    const response = await fetch("http://127.0.0.1:5000/api/command", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ query: spoken })
    });

    const data = await response.json();
    botTypingEffect(data.reply);
  };
});
