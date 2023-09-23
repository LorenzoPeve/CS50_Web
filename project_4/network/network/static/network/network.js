document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll('.like-button').forEach((button) => {
        button.addEventListener('click', () => like_post(button));
    });

    document.querySelectorAll('.editpost').forEach((button) => {
        button.addEventListener('click', () => edit_post(button));
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

function edit_post(button) {

    let post_id = button.dataset.postid;
    let card = button.parentElement.parentElement; // <div class="card mb-2 post">
    let post = card.getElementsByClassName('card-text')[0];

    // Replace post content with a textarea
    const textarea = document.createElement('textarea');
    textarea.value = post.textContent.trim();
    textarea.style.width = '100%';
    textarea.style.minHeight = '100px';
    textarea.style.verticalAlign = 'top';
    textarea.style.textAlign = 'left';
    post.replaceWith(textarea);

    // Add a "Save" button
    const saveButton = document.createElement('button');
    saveButton.textContent = 'Save';
    saveButton.className = 'btn btn-primary';
    button.parentElement.appendChild(saveButton);

    // Hide Edit button
    button.style.display = 'none';

    // Save Event
    saveButton.addEventListener('click', function () {

        // Create new card-text with updated text
        const newpost = document.createElement('p');
        newpost.className = 'card-text';
        let newtext = textarea.value;
        newpost.textContent = newtext;
        textarea.replaceWith(newpost);
        saveButton.remove();
        button.style.display = 'block';

        fetch('http://127.0.0.1:8000/update_post', {
        method: 'POST',
        body: JSON.stringify({
            post_id: post_id,
            content: newtext,
        })  
        })
        .then(response => response.json())
        })
    };