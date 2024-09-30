const button = document.getElementById('myButton');

button.addEventListener('click', () => {
  // Přepínání třídy 'centered' pro změnu pozice tlačítka
  button.classList.toggle('centered');
});
