const menuBtn = document.querySelector('.btn-menu__burger--js');

menuBtn.addEventListener('click', () => {
    menuBtn.classList.toggle('btn-menu__burger--open');
});