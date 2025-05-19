function main() {
  initSplide();
  initBackToTopButton();
}

function initSplide() {
  new Splide('#splide', {
    type: 'loop',
    perPage: 1,
    autoplay: true,
    arrows: true,
    pagination: true,
  }).mount();
}

function initBackToTopButton() {
  const backToTopButton = document.querySelector('.back-to-top');

  if (backToTopButton) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        backToTopButton.classList.add('visible');
      } else {
        backToTopButton.classList.remove('visible');
      }
    });
    window.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth',
      });
    });
  }
}

main();
