"use strict";
document.querySelectorAll("[data-email-form]").forEach((form) => {
  form.querySelector("button[type=submit]").disabled = false;
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const data = new FormData(form);
    const body = `Name: ${data.get("name")}\nReply email: ${data.get("email")}\n\n${data.get("message")}`;
    const url = `mailto:foundersfla@gmail.com?subject=${encodeURIComponent(data.get("subject"))}&body=${encodeURIComponent(body)}`;
    form.querySelector("[data-form-status]").textContent = "Your email app should open a draft. Review and send it there. If it does not open, use the email address below.";
    window.location.href = url;
  });
});
