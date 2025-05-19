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

main();
