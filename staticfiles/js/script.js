document.addEventListener('DOMContentLoaded', function () {
    const nav = document.querySelector('.navbar');

    // Toggle background color once user scrolls 50px
    document.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    });
});