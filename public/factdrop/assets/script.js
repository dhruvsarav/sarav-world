(function () {
  // ---- Clipboard Helper (handles secure & non-secure / file:// contexts) ----
  function copyToClipboard(text, onSuccess) {
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(onSuccess).catch(function () {
        fallbackCopy(text, onSuccess);
      });
    } else {
      fallbackCopy(text, onSuccess);
    }
  }

  function fallbackCopy(text, onSuccess) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.style.position = "fixed";
    ta.style.left = "-9999px";
    ta.style.top = "-9999px";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.focus();
    ta.select();
    try {
      var ok = document.execCommand("copy");
      if (ok && onSuccess) onSuccess();
    } catch (e) {
      console.warn("Fallback copy failed", e);
    }
    document.body.removeChild(ta);
  }

  // ---- native share + copy link ----
  var nativeBtn = document.getElementById("share-native");
  if (nativeBtn && navigator.share) {
    nativeBtn.hidden = false;
    nativeBtn.addEventListener("click", function () {
      navigator.share({
        title: "Fact Drop",
        text: nativeBtn.dataset.text || document.title,
        url: nativeBtn.dataset.url || window.location.href
      }).catch(function () {});
    });
  }

  var copyBtn = document.getElementById("share-copy");
  if (copyBtn) {
    copyBtn.addEventListener("click", function () {
      var url = copyBtn.dataset.url || window.location.href;
      copyToClipboard(url, function () {
        copyBtn.classList.add("copied");
        var labelEl = copyBtn.querySelector(".btn-label");
        var original = labelEl ? labelEl.textContent : copyBtn.textContent;
        if (labelEl) labelEl.textContent = "Copied!";
        else copyBtn.textContent = "Copied!";
        setTimeout(function () {
          copyBtn.classList.remove("copied");
          if (labelEl) labelEl.textContent = original;
          else copyBtn.textContent = original;
        }, 1500);
      });
    });
  }

  // ---- footer popups: privacy / terms / disclaimer / about ----
  // Generic wiring: any button with data-modal-target="X" opens #X.
  // Any .modal-overlay closes via its own .modal-close, clicking the
  // dimmed backdrop, or Escape.
  document.querySelectorAll("[data-modal-target]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var modal = document.getElementById(btn.dataset.modalTarget);
      if (modal) modal.hidden = false;
    });
  });
  document.querySelectorAll(".modal-overlay").forEach(function (modal) {
    var closeBtn = modal.querySelector(".modal-close");
    if (closeBtn) closeBtn.addEventListener("click", function () { modal.hidden = true; });
    modal.addEventListener("click", function (e) {
      if (e.target === modal) modal.hidden = true;
    });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    document.querySelectorAll(".modal-overlay").forEach(function (modal) {
      modal.hidden = true;
    });
  });

  // ---- like button ----
  // Calls the Cloudflare Pages Function at /api/likes/:slug (same origin,
  // no CORS needed). If that function isn't deployed yet, the fetch just
  // fails quietly and the button shows "–" instead of a number — it
  // never blocks or breaks the rest of the page.
  var likeBtn = document.querySelector(".like-btn");
  if (likeBtn) {
    var slug = likeBtn.dataset.slug;
    var countEl = likeBtn.querySelector(".like-count");
    var likedKey = "factdrop_liked_" + slug;

    fetch("/api/likes/" + slug)
      .then(function (r) { return r.json(); })
      .then(function (data) { countEl.textContent = data.count; })
      .catch(function () { countEl.textContent = "0"; });

    if (localStorage.getItem(likedKey)) {
      likeBtn.classList.add("liked");
    }

    likeBtn.addEventListener("click", function () {
      if (localStorage.getItem(likedKey)) return; // one like per browser, v1
      likeBtn.classList.add("liked");
      var current = parseInt(countEl.textContent, 10) || 0;
      countEl.textContent = current + 1; // optimistic update
      fetch("/api/likes/" + slug, { method: "POST" })
        .then(function (r) { return r.json(); })
        .then(function (data) {
          countEl.textContent = data.count;
          localStorage.setItem(likedKey, "1");
        })
        .catch(function () {
          // request failed — roll back the optimistic bump
          countEl.textContent = current;
          likeBtn.classList.remove("liked");
        });
    });
  }
})();
