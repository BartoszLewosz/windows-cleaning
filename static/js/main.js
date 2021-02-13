const burger = document.querySelector('.burger');
const topNav = document.querySelector('.top-nav__list--js');
const topNavHeader = document.querySelector('.top-nav__header--js');

const handleClick = () => {
    topNavHeader.classList.toggle('top-nav__header--hide');
    burger.classList.toggle('burger--active');
    topNav.classList.toggle('top-nav__list--active');
}

burger.addEventListener('click', handleClick);