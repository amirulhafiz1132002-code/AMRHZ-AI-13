async function send() {
  const input = document.getElementById("input").value;
  const res = await fetch("http://localhost:8000/chat?prompt=" + input, {
    method: "POST"
  });
  const data = await res.json();
  document.getElementById("output").innerText = data.response;
}