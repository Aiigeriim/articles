async function makeRequest(url, method='GET'){
    let response = await fetch(url, { method: method });
    if (response.ok){
        return await response.json();
    } else {
        let error = await response.json();
        throw new Error(error.message);
    }
}

async function onClick(event){
    event.preventDefault();
    let a = event.target;
    let url = a.href;
    let response = await makeRequest(url);

    // Обновляем текст кнопки
    a.textContent = response.action === "liked" ? "Unlike" : "Like";

    // Обновляем счётчик
    let articleId = a.dataset.articleId;
    let counter = document.getElementById(`likes-count-${articleId}`);
    counter.textContent = response.like_users.count;
}

function onLoad(){
    let links = document.querySelectorAll('[data-like="like_article"]');
    for (let link of links){
        link.addEventListener('click', onClick);
    }
}

window.addEventListener("load", onLoad);
