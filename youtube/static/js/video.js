function getCsrfToken(){
    let CSRFToken = null;
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++){
        const cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')){
            CSRFToken = cookie.substring('csrftoken='.length);
            break;
        }
    }
    return CSRFToken;
}


const likeButton = document.getElementById("likeButton");
const likeCount = document.getElementById("likeCount");

likeButton.addEventListener("click", async function(){
    const url = likeButton.getAttribute("data-url");
    try{
    const responce = await fetch(url,
        {
            method: "POST",
            headers: {
                "X-CSRFToken": getCsrfToken(),
                "Content-Type": "application/json"
            },
            body: JSON.stringify({})
        });
    const data =await responce.json();
    if (data.success) {
        likeCount.textContent = data.likes;  
    }
    }
    catch (error){
        console.log("error", error);
    }
});

const commentForm = document.getElementById("commentForm");
const commetntInput = document.getElementById("commentInput");

commentForm.addEventListener("submit", async function(){

    });

