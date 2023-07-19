document.addEventListener('DOMContentLoaded', function() {
  const nav = document.querySelector('#main');
  let topOfNav = nav.offsetTop;

  function fixNav() {
    if (window.scrollY >= topOfNav) {
      document.body.style.paddingTop = nav.offsetHeight + 'px';
      document.body.classList.add('fixed-nav');
    }
    else {
      document.body.classList.remove('fixed-nav');
      document.body.style.paddingTop = 0;
    }
  }

  window.addEventListener('scroll', fixNav);

  function openModal() {
    document.getElementById("myModal").style.display = "block";
  }

  function closeModal() {
    document.getElementById("myModal").style.display = "none";
  }

  var slideIndex = 1;
  showSlides(slideIndex);

  function plusSlides(n) {
    showSlides(slideIndex += n);
  }

  function currentSlide(n) {
    showSlides(slideIndex = n);
  }

  function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    // var dots = document.getElementsByClassName("demo");
    var captionText = document.getElementById("caption");

    if (n > slides.length) {
      slideIndex = 1}
    if (n < 1) {
      slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    // for (i = 0; i < dots.length; i++) {
    //     dots[i].className = dots[i].className.replace(" active", "");
    // }

    slides[slideIndex-1].style.display = "block";

    // dots[slideIndex-1].className += " active";

    captionText.innerHTML = dots[slideIndex-1].alt;
  }
})