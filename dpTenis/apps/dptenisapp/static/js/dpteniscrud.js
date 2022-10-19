setTimeout(() => {
  const alert = document.getElementById("alert-message")
  if(alert) alert.style.display='none';
},5000);

(function() {
  'use strict'

  const btnEliminar = document.querySelectorAll(".btnEliminar");

  btnEliminar.forEach(e => {
    e.addEventListener('click', (evt) => {
      const confirma = confirm("¿Seguro que desea eliminar el registro?");
      if(!confirma) evt.preventDefault();
        
    });
  });

})();

(function() {
  'use strict'

  const forms = document.querySelectorAll('.needs-validation');

  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false);
  });
})();