document.addEventListener('DOMContentLoaded', function () {
  var dataEl = document.getElementById('explore-data');
  if (!dataEl) return;
  var temples = JSON.parse(dataEl.textContent);

  var searchInput = document.getElementById('explore-search');
  var chipsWrap = document.getElementById('explore-chips');
  var circuitChipsWrap = document.getElementById('circuit-chips');
  var resultsWrap = document.getElementById('explore-results');
  var countEl = document.getElementById('explore-count');
  var emptyEl = document.getElementById('explore-empty');
  var activeCat = 'all';
  var activeCircuit = null;

  function cardHtml(t) {
    var badges = '';
    if (t.categories && t.categories.length > 0) {
      badges = '<span class="card-badges">' + t.categories
        .map(function (c) { return '<span class="also-in-badge small">' + c + '</span>'; })
        .join('') + '</span>';
    }
    var circuitBadge = t.circuit ? '<span class="circuit-tag">' + t.circuit + '</span>' : '';
    var subshrine = t.is_subshrine ? '<span class="card-badges"><span class="also-in-badge small subshrine">sub-shrine</span></span>' : '';
    
    return '<a class="mini temple-card" href="../temple/' + t.id + '/">' +
      '<div class="card-top-row">' +
        '<span class="n">' + t.name_ta + '</span>' +
        circuitBadge +
      '</div>' +
      '<span class="t-en">' + t.name_en + '</span>' +
      badges + subshrine +
      '</a>';
  }

  function render() {
    var q = (searchInput.value || '').trim().toLowerCase();
    var filtered = temples.filter(function (t) {
      var matchesCat = activeCat === 'all' || (t.categories && t.categories.indexOf(activeCat) !== -1);
      if (!matchesCat) return false;

      var matchesCircuit = !activeCircuit || (t.circuit && t.circuit.indexOf(activeCircuit) !== -1);
      if (!matchesCircuit) return false;

      if (!q) return true;
      var qMatch = (t.name_en && t.name_en.toLowerCase().indexOf(q) !== -1) ||
                   (t.name_ta && t.name_ta.indexOf(q) !== -1) ||
                   (t.subgroup && t.subgroup.toLowerCase().indexOf(q) !== -1) ||
                   (t.circuit && t.circuit.toLowerCase().indexOf(q) !== -1);
      return qMatch;
    });

    countEl.textContent = 'Showing ' + filtered.length + ' of ' + temples.length + ' temples';
    resultsWrap.innerHTML = filtered.map(cardHtml).join('');
    emptyEl.hidden = filtered.length !== 0;
  }

  if (searchInput) {
    searchInput.addEventListener('input', render);
  }

  if (chipsWrap) {
    chipsWrap.addEventListener('click', function (e) {
      var chip = e.target.closest('.chip');
      if (!chip) return;
      chipsWrap.querySelectorAll('.chip').forEach(function (c) { c.classList.remove('active'); });
      chip.classList.add('active');
      activeCat = chip.getAttribute('data-cat');
      render();
    });
  }

  if (circuitChipsWrap) {
    circuitChipsWrap.addEventListener('click', function (e) {
      var chip = e.target.closest('.chip-circuit');
      if (!chip) return;
      if (chip.classList.contains('active')) {
        chip.classList.remove('active');
        activeCircuit = null;
      } else {
        circuitChipsWrap.querySelectorAll('.chip-circuit').forEach(function (c) { c.classList.remove('active'); });
        chip.classList.add('active');
        activeCircuit = chip.getAttribute('data-circuit');
      }
      render();
    });
  }

  render();
});
