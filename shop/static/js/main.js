// ==========================================
// АНИМАЦИЯ ПОЯВЛЕНИЯ ПРИ СКРОЛЛЕ (SCROLL REVEAL)
// ==========================================
document.addEventListener('DOMContentLoaded', function() {
    
    // Находим все элементы с классом animate-on-scroll
    const animElements = document.querySelectorAll('.animate-on-scroll');
    
    // Функция проверки, виден ли элемент на экране
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        const windowHeight = window.innerHeight || document.documentElement.clientHeight;
        // Элемент считается видимым, если его верхняя часть находится в нижних 80% экрана
        return rect.top < windowHeight * 0.85;
    }

    // Функция добавления класса, когда элемент появляется
    function checkAnimations() {
        animElements.forEach(el => {
            if (isElementInViewport(el)) {
                el.classList.add('animated');
            }
        });
    }

    // Запускаем проверку при загрузке
    setTimeout(checkAnimations, 100);
    
    // Запускаем проверку при скролле
    window.addEventListener('scroll', checkAnimations);
});


// ==========================================
// CSRF ТОКЕН ДЛЯ AJAX ЗАПРОСОВ
// ==========================================
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// Пример запроса к API (для демонстрации)
async function loadProductsAPI() {
    try {
        const response = await fetch('/api/products/');
        if (!response.ok) throw new Error('Ошибка загрузки');
        const data = await response.json();
        console.log('Товары загружены через API:', data);
    } catch (error) {
        console.error('Ошибка API:', error);
    }
}
// Раскомментируй строчку ниже, чтобы загрузить данные при старте
// loadProductsAPI();