function getCsrfToken(){
    let csrfToken = null;
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++){
        const cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')){
            csrfToken = cookie.substring('csrftoken='.length);
            break;
        }
    }
    return csrfToken;
}


const likeButton = document.getElementById("likeButton");
const likeCount = document.getElementById("likeCount");

likeButton.addEventListener("click", async function(){
    const url = likeButton.dataset.url;
    try{
        const response = await fetch(url,
            {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCsrfToken(),
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({})
            });
        const data =await response.json();
        if (data.success) {
            likeCount.textContent = data.like_count;  
        }
    }
    catch (error){
        console.error("error", error);
    }
});

const commentForm=document.getElementById("commentForm")

commentForm.addEventListener("submit", async function(event){
    console.log("clicked");
    const url = commentButton.getAttribute("data-url");

    if (!commentInput.value.trim()){
        console.log("no comment here.");
        return ;
    }
    console.log("comment input:", JSON.stringify({commentText: commentInput.value}));
    try{
        const responce = await fetch(url,
            {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCsrfToken(),
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({commentText: commentInput.value})
            });
        console.log("posted");

        const data =await responce.json();
        if (data.success) {
            let newComment = document.createElement("li");
            newComment.classList.add("list-group-item");
            newComment.textContent = data.newCommentText;
            commentList.appendChild(newComment);
            commentInput.value = "";
        }
    }
    catch(error){
        console.log("error",error);
    }
    });

