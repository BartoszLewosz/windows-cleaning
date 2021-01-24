const burger = document.querySelector('.burger');
const topNav = document.querySelector('.top-nav__list--js');

const handleClick = () => {
    burger.classList.toggle('burger--active');
    topNav.classList.toggle('top-nav__list--active');
}

burger.addEventListener('click', handleClick);