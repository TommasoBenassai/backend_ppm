// Aggiungi la classe "has-scrollbar" alle righe con la barra di scorrimento
document.addEventListener('DOMContentLoaded', function() {
    var rows = document.querySelectorAll('.product-row');
    rows.forEach(function(row) {
        if (row.scrollWidth > row.clientWidth) {
            row.classList.add('has-scrollbar');
        }
    });
});

