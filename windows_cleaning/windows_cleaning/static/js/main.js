const burger = document.querySelector('.burger');

const handleClick = () => {
    burger.classList.toggle('burger--active');
}

burger.addEventListener('click', handleClick);