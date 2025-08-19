async function makeRequest(url, method='GET'){
    let response = await fetch(url, { method: method });
    if (response.ok){
        return await response.json();
    } else {
        throw new Error("Ошибка: " + response.status);
    }
}

async function onClick(event){
    event.preventDefault();
    let a = event.currentTarget;
    let url = a.href;
    let response = await makeRequest(url);

    if (response.action === "liked") {
    a.textContent = "Unlike";
    } else {
    a.textContent = "Like";
    }

    if (a.dataset.articleId){
        let counter = document.getElementById(`likes-count-${a.dataset.articleId}`);
        counter.textContent = response.likes_count;
    }
    if (a.dataset.commentId){
        let counter = document.getElementById(`comment-likes-count-${a.dataset.commentId}`);
        counter.textContent = response.likes_count;
    }
}

function onLoad(){
    let links = document.querySelectorAll('[data-like]');
    for (let link of links){
        link.addEventListener('click', onClick);
    }
}

window.addEventListener("load", onLoad);

