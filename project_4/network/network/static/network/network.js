document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll('.like-button').forEach((button) => {
        button.addEventListener('click', () => like_post(button.dataset.postid));
    });

});


function like_post(post_id) {

    fetch('http://127.0.0.1:8000/likeunlikepost', {
        method: 'POST',
        body: JSON.stringify({
            post_id: post_id
      })  
    })
    .then(response => response.json())
    .then(result => console.log(result));
};
