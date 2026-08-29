(function () {
  // ---- native share + copy link (existing) ----
  var nativeBtn = document.getElementById("share-native");
  if (nativeBtn && navigator.share) {
    nativeBtn.hidden = false;
    nativeBtn.addEventListener("click", function () {
      navigator.share({
        title: "Fact Drop",
        text: nativeBtn.dataset.text,
        url: nativeBtn.dataset.url
      }).catch(function () {});
    });
  }
  var copyBtn = document.getElementById("share-copy");
  if (copyBtn) {
    copyBtn.addEventListener("click", function () {
      navigator.clipboard.writeText(copyBtn.dataset.url).then(function () {
        var original = copyBtn.textContent;
        copyBtn.textContent = "Copied!";
        setTimeout(function () { copyBtn.textContent = original; }, 1500);
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
