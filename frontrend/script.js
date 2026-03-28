console.log("JS loaded");

const form = document.getElementById("open-account-form");
const message = document.getElementById("message");

if (form) {
  form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const password = document.getElementById("password").value;
    const rePassword = document.getElementById("re-password").value;

    if (password !== rePassword) {
      message.textContent = "Passwords do not match";
      return;
    }

    const data = {
      user_id: document.getElementById("idNumber").value,
      first_name: document.getElementById("firstName").value,
      last_name: document.getElementById("lastName").value,
      email: document.getElementById("email").value,
      phone_number: document.getElementById("phone-number").value,
      address: document.getElementById("address").value,
      country: document.getElementById("country").value,
      state: document.getElementById("state").value,
      zip_code: document.getElementById("zip").value,
      password: password
    };

    console.log("Sending to backend:", data);

    try {
      const response = await fetch("http://127.0.0.1:8000/users/add", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
      });

      const result = await response.json();

      if (response.ok) {
        message.textContent = "User created successfully";
        console.log("Success:", result);
        form.reset();
      } else {
        if (result.detail && result.detail.length > 0){
            message.textContent = result.detail[0].msg;
        } else {
            message.textContent = "Something went wrong. Try again later"
        }
        console.log("Backend error:", result);
      }
    } catch (error) {
      message.textContent = "Cannot connect to backend";
      console.error("Network error:", error);
    }
  });
}