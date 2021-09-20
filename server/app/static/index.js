const socket = io();
const textarea = document.getElementById("textarea1");
const post = document.getElementById("post");
const collections = document.getElementById("collections");

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
  const feed = textarea.value;
  if (feed !== "") {
    const data = { text: feed };
    socket.emit("feed", data);
    textarea.value = "";
    scrollSmoothToBottom("feeds");
  }
};
