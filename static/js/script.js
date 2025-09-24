const form = document.getElementById("myForm");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  const protocol = formData.get("protocol");

  fetch(`http://127.0.0.1:8000/upload/${protocol}`, {
    method: "POST",
    body: formData,
  })
    .then((res) => {
      if (!res.ok) {
        throw new Error(`Erro: ${res.status}`);
      }
      return res.json();
    })
    .then((data) => {
      alert(data.message || JSON.stringify(data));
    })
    .catch((err) => {
      alert(`Falha ao enviar: ${err}`);
    });
});
