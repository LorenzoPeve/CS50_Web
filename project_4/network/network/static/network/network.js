document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll('.like-button').forEach((button) => {
        button.addEventListener('click', () => like_post(button));
    });

});

function like_post(button) {

    let post_id = button.dataset.postid;
    fetch('http://127.0.0.1:8000/likeunlikepost', {
        method: 'POST',
        body: JSON.stringify({
            post_id: post_id
      })  
    })
    .then(response => response.json())
    .then(result => {

        let parentDiv = button.parentElement.parentElement;
        let likeCounter = parentDiv.getElementsByClassName("like-counter")[0];
        let current_count = Number(likeCounter.innerHTML);

        if (result == 'like') {
            likeCounter.innerHTML = current_count + 1;
        }
        else {
            likeCounter.innerHTML = current_count - 1;
        }
    })
};
