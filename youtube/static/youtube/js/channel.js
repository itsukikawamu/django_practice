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

const subscribeButton = document.getElementById("subscribeButton");
const subscribersCount = document.getElementById("subscribersCount");

subscribeButton.addEventListener("click", async function(){
    const url = subscribeButton.dataset.url;
   
    try{
        const responce = await fetch(url, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCsrfToken(),
                "Content-Type": "application/json"
            },
            body: JSON.stringify({})
        })
        const data = await responce.json();

        if (data.success){
            subscribersCount.textContent = data.subscribers_number;
        }
    } catch (error){
        console.error("エラーが発生しました:", error);
    }
})