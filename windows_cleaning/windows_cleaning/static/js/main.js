const burger = document.querySelector('.burger');
const topNav = document.querySelector('.top-nav__list--js');
const testJs = document.querySelector('.top-nav__header--js');

const handleClick = () => {
    testJs.classList.toggle('top-nav__header--hide');
    burger.classList.toggle('burger--active');
    topNav.classList.toggle('top-nav__list--active');
    topNavHeader.toggle('top-nav__header--active');
}

burger.addEventListener('click', handleClick);