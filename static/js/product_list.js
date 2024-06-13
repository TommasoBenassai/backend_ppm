// Aggiungi la classe "has-scrollbar" alle righe con la barra di scorrimento
document.addEventListener('DOMContentLoaded', function() {
  var rows = document.querySelectorAll('.product-row');

  function checkScrollbar(row) {
    if (row.scrollWidth > row.clientWidth) {
      row.classList.add('has-scrollbar');
    } else {
      row.classList.remove('has-scrollbar');
    }
  }

  function checkAllScrollbars() {
    rows.forEach(function(row) {
      checkScrollbar(row);
    });
  }

  checkAllScrollbars();

  window.addEventListener('resize', function() {
    checkAllScrollbars();
  });
});

function menuOnClick() {
    document.getElementById("menu-bar").classList.toggle("change");
    document.getElementById("nav").classList.toggle("change");
    document.getElementById("menu-bg").classList.toggle("change-bg");
    document.getElementById("blurr").classList.toggle("change-blurr");

}



document.addEventListener('DOMContentLoaded', function() {
  const searchIcon = document.getElementById('search-icon');
  const searchInput = document.getElementById('search-input');

  // Aggiungi un ascoltatore di eventi per l'evento keyup sul campo di input
  searchInput.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
      performSearch();
    }
  });

  // Aggiungi un ascoltatore di eventi per l'evento click sull'icona di ricerca
  searchIcon.addEventListener('click', function() {
    performSearch();
  });

  function performSearch() {
    const searchTerm = searchInput.value.trim();

    if (searchTerm !== '') {
      // Effettua una richiesta AJAX per ottenere l'URL dei dettagli del prodotto corrispondente al termine di ricerca
      const xhr = new XMLHttpRequest();
      xhr.open('GET', '/search-product?search=' + encodeURIComponent(searchTerm), true);
      xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
          const response = JSON.parse(xhr.responseText);
          const productDetailURL = response.productDetailURL;

          if (productDetailURL) {
            // Reindirizza l'utente alla pagina dei dettagli del prodotto
            window.location.href = productDetailURL;
          } else {
            // Stampa un messaggio se il prodotto non esiste
            alert('Il prodotto cercato non esiste.');
          }
        } else if (xhr.readyState === 4) {
          // Stampa un messaggio se si verifica un errore durante la richiesta
          alert('Si è verificato un errore durante la richiesta.');
        }
      };
      xhr.send();
    }
  }
});
