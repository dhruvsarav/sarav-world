document.addEventListener('DOMContentLoaded', function () {
  // --- Legal modals (Privacy / Terms / Disclaimer / About) ---
  var overlay = document.getElementById('modal-overlay');
  var body = document.getElementById('modal-body');
  var closeBtn = document.getElementById('modal-close');
  if (overlay && body) {
    function openModal(name) {
      var tpl = document.getElementById('tpl-' + name);
      if (!tpl) return;
      body.innerHTML = '';
      body.appendChild(tpl.content.cloneNode(true));
      overlay.classList.add('open');
      document.body.classList.add('modal-locked');
      closeBtn.focus();
    }
    function closeModal() {
      overlay.classList.remove('open');
      document.body.classList.remove('modal-locked');
    }
    document.addEventListener('click', function (e) {
      var trigger = e.target.closest('[data-modal]');
      if (trigger) {
        e.preventDefault();
        openModal(trigger.getAttribute('data-modal'));
        return;
      }
      if (e.target === overlay) closeModal();
    });
    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && overlay.classList.contains('open')) closeModal();
    });
  }

  // --- Share row ---
  var nativeBtn = document.getElementById('share-native');
  if (nativeBtn) {
    if (navigator.share) {
      nativeBtn.hidden = false;
      nativeBtn.addEventListener('click', function () {
        navigator.share({
          title: 'Temples of Tamil Gods',
          text: nativeBtn.getAttribute('data-text'),
          url: nativeBtn.getAttribute('data-url')
        }).catch(function () {});
      });
    }
  }
  var copyBtn = document.getElementById('share-copy');
  if (copyBtn) {
    copyBtn.addEventListener('click', function () {
      var url = copyBtn.getAttribute('data-url');
      var done = function () {
        copyBtn.classList.add('copied');
        setTimeout(function () { copyBtn.classList.remove('copied'); }, 1500);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(done).catch(function () {});
      } else {
        var ta = document.createElement('textarea');
        ta.value = url;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand('copy'); done(); } catch (e) {}
        document.body.removeChild(ta);
      }
    });
  }
});
