// Price tabs
function switchTab(event, tab) {
  document.querySelectorAll('.price-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.price-panel').forEach(p => p.classList.remove('active'));
  if (event && event.target) { event.target.classList.add('active'); }
  document.getElementById('tab-' + tab).classList.add('active');
}

// Mobile menu
function toggleMenu() {
  document.getElementById('mobileMenu').classList.toggle('open');
}

// Scroll reveal
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

// Set min date for booking
const dateInput = document.querySelector('input[type="date"]');
if (dateInput) {
  const today = new Date().toISOString().split('T')[0];
  dateInput.min = today;
}
