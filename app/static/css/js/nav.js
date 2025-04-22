const hamburger = document.querySelector('.hamburger');
const navMenu = document.getElementById('nav-menu');

hamburger.addEventListener('click', () => {
  const expanded = hamburger.getAttribute('aria-expanded') === 'true';
  hamburger.setAttribute('aria-expanded', !expanded);
  navMenu.hidden = !navMenu.hidden;
  navMenu.classList.toggle('active');
});