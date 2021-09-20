const socket = io();
const textarea = document.getElementById("textarea1");
const post = document.getElementById("post");
const collections = document.getElementById("collections");

function removeHTML(message) {
  if (message.includes("<") || message.includes(">")) {
    const lt = "&lt;";
    const gt = "&gt;";
    while (true) {
      if (message.includes("<")) {
        message = message.replace("<", lt);
      } else if (message.includes(">")) {
        message = message.replace(">", gt);
      } else {
        break;
      }
    }
  }
  return message;
}

function scrollSmoothToBottom(id) {
  var div = document.getElementById(id);
  $("#" + id).animate(
    {
      scrollTop: div.scrollHeight - div.clientHeight,
    },
    500
  );
}

socket.on("feed-update", function (data) {
  const li = document.createElement("LI");
  li.className = "collection-item";
  li.innerHTML = data.text;
  collections.appendChild(li);
  scrollSmoothToBottom("feeds");
});

post.onclick = function () {
  let feed = textarea.value;
  if (feed !== "") {
    feed = removeHTML(feed);
    const data = { text: feed };
    socket.emit("feed", data);
    textarea.value = "";
    scrollSmoothToBottom("feeds");
  }
};
