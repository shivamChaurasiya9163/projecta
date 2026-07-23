document.addEventListener("DOMContentLoaded", () => {

    // Wait until chatbot.html has been loaded
    const waitForChatbot = setInterval(() => {

        const chatWindow = document.getElementById("chat-window");

        if (!chatWindow) return;

        clearInterval(waitForChatbot);

        initializeChatbot();

    }, 100);

});


function initializeChatbot() {

    const toggleBtn = document.getElementById("chat-toggle");
    const closeBtn = document.getElementById("close-chat");

    const sendBtn = document.getElementById("send-message");

    const input = document.getElementById("user-input");

    const messages = document.getElementById("chat-messages");

    const typing = document.getElementById("typing-indicator");

    const quickButtons = document.querySelectorAll(".quick-question");

    const chatWindow = document.getElementById("chat-window");


    // ===========================
    // Open Chat
    // ===========================

    toggleBtn.addEventListener("click", () => {

        chatWindow.style.display = "flex";

        toggleBtn.style.display = "none";

    });


    // ===========================
    // Close Chat
    // ===========================

    closeBtn.addEventListener("click", () => {

        chatWindow.style.display = "none";

        toggleBtn.style.display = "flex";

    });


    // ===========================
    // Enter Key
    // ===========================

    input.addEventListener("keypress", (e) => {

        if (e.key === "Enter") {

            sendMessage();

        }

    });


    // ===========================
    // Send Button
    // ===========================

    sendBtn.addEventListener("click", sendMessage);


    // ===========================
    // Quick Questions
    // ===========================

    quickButtons.forEach(button => {

        button.addEventListener("click", () => {

            input.value = button.innerText;

            sendMessage();

        });

    });


    // ===========================
    // Send Message
    // ===========================

    async function sendMessage() {

        const text = input.value.trim();

        if (text === "") return;

        addUserMessage(text);

        input.value = "";

        typing.style.display = "block";

        scrollBottom();

        try {

            const response = await fetch("http://127.0.0.1:8000/api/v1/chat/", {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    message: text

                })

            });


            if (!response.ok) {

                throw new Error("Server Error");

            }

            const data = await response.json();

            typing.style.display = "none";

            addBotMessage(data.reply);

        }

        catch (error) {

            typing.style.display = "none";

            addBotMessage("⚠ Sorry, I couldn't connect to the server.");

            console.error(error);

        }

    }


    // ===========================
    // User Bubble
    // ===========================

    function addUserMessage(text) {

        const div = document.createElement("div");

        div.className = "user-message";

        div.innerHTML = text;

        messages.appendChild(div);

        scrollBottom();

    }


    // ===========================
    // Bot Bubble
    // ===========================

    function addBotMessage(text) {

        const div = document.createElement("div");

        div.className = "bot-message";

        div.innerHTML = text.replace(/\n/g, "<br>");

        messages.appendChild(div);

        scrollBottom();

    }


    // ===========================
    // Auto Scroll
    // ===========================

    function scrollBottom() {

        messages.scrollTop = messages.scrollHeight;

    }

}