const form = document.getElementById("leadForm");
const result = document.getElementById("formResult");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = new FormData(form);

    const payload = {
        name: formData.get("name"),
        phone: formData.get("phone"),
        message: formData.get("message") || ""
    };

    result.textContent = "Отправляем...";

    try {
        const response = await fetch("/api/lead", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();
        result.textContent = data.message || "Заявка отправлена";
        form.reset();
    } catch (error) {
        result.textContent = "Ошибка отправки. Позвоните по номеру на сайте.";
    }
});
