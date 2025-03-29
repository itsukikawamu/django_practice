const contactForm = document.getElementById('contactForm');
const submitButton = document.getElementById('submitButton');

function getCSRFToken() {
    const csrfInput = document.querySelector('[name=csrfmiddlewaretoken]');
    return csrfInput ? csrfInput.value : '';
}

function handleSubmit(event){
    event.preventDefault();
    submitButton.disabled = true;
    submitButton.textContent = '送信中...';
    
    setTimeout(function(){
        contactForm.submit();}, 2000);
}

contactForm.addEventListener('submit', handleSubmit);
