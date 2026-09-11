const revealItems = document.querySelectorAll('.reveal');

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

revealItems.forEach((item) => observer.observe(item));


// Certificate lightbox
const certificateModal = document.getElementById('certificateModal');
const certificateModalImage = document.getElementById('certificateModalImage');
const certificateModalTitle = document.getElementById('certificateModalTitle');
const certificateButtons = document.querySelectorAll('.cert-view-button');
const closeCertificate = () => {
  if (!certificateModal) return;
  certificateModal.classList.remove('is-open');
  certificateModal.setAttribute('aria-hidden', 'true');
  document.body.classList.remove('modal-open');
  if (certificateModalImage) certificateModalImage.src = '';
};

certificateButtons.forEach((button) => {
  button.addEventListener('click', () => {
    if (!certificateModal || !certificateModalImage) return;
    certificateModalImage.src = button.dataset.certificate || '';
    certificateModalTitle.textContent = button.dataset.certificateTitle || '';
    certificateModal.classList.add('is-open');
    certificateModal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('modal-open');
  });
});

document.querySelectorAll('[data-close-certificate]').forEach((element) => {
  element.addEventListener('click', closeCertificate);
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && certificateModal?.classList.contains('is-open')) {
    closeCertificate();
  }
});
