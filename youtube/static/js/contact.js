const contactForm = document.getElementById('contactForm');
const submitButton = document.getElementById('submitButton');
function handleSubmit(event){
    event.preventDefault();
    submitButton.disabled = true;
    submitButton.textContent = '送信中...';
    function temp(){contactForm.submit();}
    setTimeout(temp, 1000);
}
contactForm.addEventListener('submit', handleSubmit);
