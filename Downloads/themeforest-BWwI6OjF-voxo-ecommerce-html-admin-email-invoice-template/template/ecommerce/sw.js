var cacheName = 'Voxo';
var filesToCache = [
  './',
  './index.html',
  './assets/css/vendors/font-awesome/brands.css',
  './assets/css/vendors/font-awesome/fontawesome.css',
  './assets/css/vendors/font-awesome/regular.css',
  './assets/css/vendors/font-awesome/solid.css',
  './assets/css/vendors/font-awesome/v4-shims.css',
  './assets/css/vendors/slick/slick-theme.css',
  './assets/css/vendors/slick/slick.css',
  './assets/css/vendors/animate.css',
  './assets/css/vendors/bootstrap.css',
  './assets/css/vendors/bootstrap.rtl.css',
  './assets/css/vendors/feather-icon.css',
  './assets/css/vendors/font-awesome.css',
  './assets/css/vendors/ion.rangeSlider.min.css',
  './assets/css/vendors/slick.css',
  './assets/css/demo1_dark.css',
  './assets/css/demo1.css',
  './assets/css/demo2_dark.css',
  './assets/css/demo2.css',
  './assets/css/demo3_dark.css',
  './assets/css/demo3.css',
  './assets/css/demo4_dark.css',
  './assets/css/demo4.css',
  './assets/css/demo5_dark.css',
  './assets/css/demo5.css',
  './assets/css/demo6_dark.css',
  './assets/css/demo6.css',
  './assets/css/element-banner.css',
  './assets/css/element-category.css',
  './assets/css/element-deal-banner.css',
  './assets/css/element-header.css',
  './assets/css/magnific-popup.css',
  './assets/js/bootstrap/bootstrap-notify.min.js',
  './assets/js/bootstrap/bootstrap.bundle.min.js',
  './assets/js/bootstrap/popper.min.js',
  './assets/js/feather/feather-icon.js',
  './assets/js/feather/feather.min.js',
  './assets/js/slick/custom_slick.js',
  './assets/js/slick/slick-animation.min.js',
  './assets/js/slick/slick.js',
  './assets/js/touchspin/input-groups.min.js',
  './assets/js/touchspin/touchspin.js',
  './assets/js/touchspin/vendors.min.js',
  './assets/js/add-remove.js',
  './assets/js/ajax-custom.js',
  './assets/js/cart_modal_resize.js',
  './assets/js/changing-word.js',
  './assets/js/check-box-select.js',
  './assets/js/count-down-timer.js',
  './assets/js/custome-threesixty.js',
  './assets/js/filter.js',
  './assets/js/filter-menu.js',
  './assets/js/flip-clock.js',
  './assets/js/pwa.js',
  './assets/js/home-script.js',
  './assets/js/infinite-scroll.js',
  './assets/js/ion.rangeSlider.min.js',
  './assets/js/isotope.pkgd.min.js',
  './assets/js/jquery.elevatezoom.js',
  './assets/js/jquery.magnific-popup.min.js',
  './assets/js/jquery.parallax.min.js',
  './assets/js/jquery-3.5.1.min.js',
  './assets/js/lazysizes.min.js',
  './assets/js/newsletter.js',
  './assets/js/order-success.js',
  './assets/js/portfolio.js',
  './assets/js/portfolio-grid.js',
  './assets/js/price-filter.js',
  './assets/js/script.js',
  './assets/js/sticky-cart-bottom.js',
  './assets/js/theme-setting.js',
  './assets/js/threesixty.js',
  './assets/js/timer.js',
  './assets/js/timer1.js',
  './assets/js/timer2.js',
  './assets/js/timer2-0.js',
  './assets/js/timer3.js',
  './assets/js/typeahead.bundle.min.js',
  './assets/js/typeahead.jquery.min.js',
  './assets/js/zoom-filter.js',
];

/* Start the service worker and cache all of the app's content */
self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(cacheName).then(function (cache) {
      return cache.addAll(filesToCache);
    })
  );
  self.skipWaiting();
});

/* Serve cached content when offline */
self.addEventListener('fetch', function (e) {
  e.respondWith(
    caches.match(e.request).then(function (response) {
      return response || fetch(e.request);
    })
  );
});