// let slider = document.querySelector('.slider');
// let slides = document.querySelectorAll('.slide');

// let currentSlide = 0;
// const slideWidth = slides[0].clientWidth;

// function nextSlide() {
//   currentSlide = (currentSlide + 1) % slides.length;
//   updateSlider();
// }

// function prevSlide() {
//   currentSlide = (currentSlide - 1 + slides.length) % slides.length;
//   updateSlider();
// }

// function updateSlider() {
//   slider.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
// }

// setInterval(nextSlide, 1500); // Change slide every 5 seconds

const images = document.querySelectorAll('.image-container img');
let currentImageIndex = 0;

function showNextImage() {
  images[currentImageIndex].classList.remove('active');
  currentImageIndex = (currentImageIndex + 1) % images.length;
  images[currentImageIndex].classList.add('active');
}

setInterval(showNextImage, 4000); 
