// Array de productos (fácil de personalizar para un emprendimiento real)
const products = [
    {
        name: "DriftMaster X1",
        description: "Carro RC de drift con motor brushless, ideal para principiantes y expertos. Incluye batería de litio y control remoto.",
        price: "$150",
        image: "https://via.placeholder.com/300x200?text=DriftMaster+X1",
        buyLink: "#" // Reemplaza con enlace a sistema de pago real
    },
    {
        name: "SpeedDrift Pro",
        description: "Modelo avanzado con suspensión ajustable y neumáticos de goma para máxima adherencia en pistas de drift.",
        price: "$200",
        image: "https://via.placeholder.com/300x200?text=SpeedDrift+Pro",
        buyLink: "#"
    },
    {
        name: "NightDrift Elite",
        description: "Carro RC con luces LED neón, perfecto para sesiones nocturnas. Resistente y de alto rendimiento.",
        price: "$250",
        image: "https://via.placeholder.com/300x200?text=NightDrift+Elite",
        buyLink: "#"
    }
];

// Función para generar el catálogo dinámicamente
function loadProducts() {
    const grid = document.getElementById('products-grid');
    products.forEach(product => {
        const card = document.createElement('div');
        card.className = 'product-card';
        card.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>${product.description}</p>
            <p class="price">${product.price}</p>
            <a href="${product.buyLink}" class="buy-button">Comprar</a>
        `;
        grid.appendChild(card);
    });
}

// Función para menú móvil
function toggleMenu() {
    const nav = document.querySelector('.nav-list');
    nav.classList.toggle('active');
}

// Event listeners
document.addEventListener('DOMContentLoaded', loadProducts);
document.getElementById('hamburger').addEventListener('click', toggleMenu);