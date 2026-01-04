/* ---------------------------
   PRODUCTS
--------------------------- */

async function searchProducts(query) {
    const res = await fetch(`/api/items?search=${query}`);
    const data = await res.json();
    renderProducts(data);
}

async function filterByPrice(order) {
    const res = await fetch(`/api/items?sort=${order}`);
    const data = await res.json();
    renderProducts(data);
}

/* ---------------------------
   CART
--------------------------- */

async function addToCart(itemId) {
    await fetch("/api/cart/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ item_id: itemId })
    });
    alert("Added to cart");
}

async function removeFromCart(itemId) {
    await fetch("/api/cart/remove", {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ item_id: itemId })
    });
    location.reload();
}

async function loadCart() {
    const res = await fetch("/api/cart");
    const data = await res.json();
    renderCart(data);
}

/* ---------------------------
   AUTH
--------------------------- */

async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const res = await fetch("/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    });

    if (res.ok) window.location.href = "/";
    else alert("Login failed");
}

/* ---------------------------
   RENDER HELPERS
--------------------------- */

function renderProducts(items) {
    const container = document.querySelector(".products");
    container.innerHTML = "";

    items.forEach(item => {
        container.innerHTML += `
            <div class="product">
                <img src="${item.item_image}">
                <h3>${item.item_name}</h3>
                <p>₹${item.item_value}</p>
                <button onclick="addToCart('${item._id}')">Add to Cart</button>
            </div>
        `;
    });
}

function renderCart(data) {
    const container = document.querySelector(".cart-items");
    const total = document.getElementById("total");

    container.innerHTML = "";
    total.innerText = data.total;

    data.items.forEach(item => {
        container.innerHTML += `
            <div class="cart-item">
                <span>${item.item_name}</span>
                <span>₹${item.item_value}</span>
                <button onclick="removeFromCart('${item._id}')">Remove</button>
            </div>
        `;
    });
}
