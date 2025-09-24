const form = document.getElementById("myForm");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const formData = new FormData(form);

  const protocol = formData.get("protocol");

  fetch(`http://127.0.0.1:8000/upload/${protocol}`, {
    //method: "GET",
    method: "POST",
    body: formData,
  })
    .then((res) => res.json())
    .then((res) => console.log(res));
});
