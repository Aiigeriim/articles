async function makeRequest(url, method='GET'){
    let response = await fetch(url, {"method": method})
    if (response.ok){
        return await response.json();
    }
    else{
        let error = await response.json()
        throw new Error(error.message)
    }
}


async function onClick(event){
    event.preventDefault();
    let a = event.target;
    let url = a.href;
    let response = await makeRequest(url);
    let articleId = a.dataset['articleId']
    let idUrl = `/article/${articleId}/test/`
    let countId = await makeRequest(idUrl)
    console.log(countId)

    let p = a.parentElement.getElementsByClassName("testJs")[0];
    p.innerHTML = response.test;
}

function onLoad(){
    let links = document.querySelectorAll('[data-like="like_article"]');
    for (let link of links){
        link.addEventListener('click', onClick);
    }
}

window.addEventListener("load", onLoad)




