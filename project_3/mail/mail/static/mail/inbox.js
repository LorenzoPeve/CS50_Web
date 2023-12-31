document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.getElementById('send-email').addEventListener('click', send_email);


  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#single-email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#single-email-view').style.display = 'none';

  display_emails(mailbox);
}

function send_email() {

  // Get values from form
  let recipients = document.getElementById('compose-recipients').value;
  let subject = document.getElementById('compose-subject').value;
  let body = document.getElementById('compose-body').value;

  // POST request. Display alert in case of failed request
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
    })
  })
  .then(response => {    
    
    if (!response.ok) {
      return response.text().then(text => { throw new Error(text) })
    }
    else {      
      return response.json();
    }
  })
  .catch(error => {
    alert(error.message);
  });
}

function display_emails(mailbox) {
  
  get_emails_from_mailbox(mailbox).then(emails => {

    const container = document.getElementById("emails-view");  
    container.innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
    
    // Handle empty mailbox
    if (emails.length == 0) {
      let mailbox_name = mailbox.charAt(0).toUpperCase() + mailbox.slice(1)
      const no_emails_alert = document.createElement("div");
      no_emails_alert.className = "alert alert-dark";
      no_emails_alert.innerHTML = `No emails in <strong> ${mailbox_name}</strong>.`;
      container.append(no_emails_alert);
      return
    }

    emails.forEach(email => {

      // Distinguish TO/FROM
      if (mailbox == 'inbox' || mailbox == 'archived') {
        header_preffix = 'From';
        person = email.sender;
      }
      else {
        header_preffix = 'To';
        person = email.recipients;
      }

      // Create card for email
      const emailCard = document.createElement("div");
      emailCard.addEventListener('click', () => load_email(email.id))
      emailCard.className = "card w-75 shadow-0 border rounded-3 mb-3";
      emailCard.style.cursor = 'pointer';

      // Card header with sender and timestamp
      const cardHeader = document.createElement("div");
      cardHeader.className = "card-header mb-0 bg-secondary text-white d-flex justify-content-between";
      cardHeader.innerHTML = `
        <p class="mb-0"><small><strong>${header_preffix}:</strong> ${person}</small></p>
        <p class="mb-0"<small>${email.timestamp}</small></p>
      `;

      // Card Body
      const cardBody = document.createElement("div");
      cardBody.className = "card-body"
      cardBody.innerHTML = `
        <p class="card-title mb-0"><small><strong>Subject:</strong> ${email.subject}</small></p>
        <p class="card-text mb-0"><small>${email.body.substring(0,100) + ' ...'}</small> </p>
      `;

      // Read vs Unread messages
      if (email.read && mailbox != 'sent') {
        cardBody.style.backgroundColor = "#cacfcd";
      } else {
        cardBody.style.backgroundColor = "white";
      }
    
      emailCard.append(cardHeader);
      emailCard.append(cardBody);
      container.append(emailCard);
    })
  })
}

function get_emails_from_mailbox(mailbox) {

  const url = `/emails/${mailbox}`;
  let emails = fetch(url)
    .then(response => response.json());

  return emails
}


function load_email(email_id) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#single-email-view').style.display = 'block';

  const container = document.getElementById("single-email-view");
  container.style.border = "1px solid #ddd";
  container.style.padding = "20px";
  container.style.backgroundColor = "#b5bfc4";
  container.style.borderRadius = "10px";
  
  fetch(`/emails/${email_id}`)
    .then(response => response.json())
    .then(email => {
        
      container.innerHTML = `
      <p class="mb-0"><small><strong>From:</strong> ${email.sender}</small></p>
      <p class="mb-0"><small><strong>To:</strong> ${email.recipients}</small></p>
      <p class="mb-0"><small><strong>Subject:</strong> ${email.subject}</small></p>
      <p class="mb-0"><small><strong>Datetime:</strong> ${email.timestamp}</small></p>
      <br>
      <p class="mb-0"><small>${email.body}</small></p>
    `;
     return email
    })
    .then( email => {

      if (email.read != true) {
        fetch(`/emails/${email_id}`, {
          method: 'PUT',
          body: JSON.stringify({
              read: true
        })})
      }
      return email
      })
      .then(email => {  // Add Archive/Remove from archive buttons

        // Only add button for received emails
        let logged_in_user = document.querySelector('#logged-in-user').textContent;
        if (logged_in_user == email.sender) {return};
       
        const element = document.createElement('button');

        if (email.archived == true) {          
          element.innerHTML = 'Remove from Archive';
          element.addEventListener('click', () => unarchive_email(email.id));
        }
        else {
          element.innerHTML = 'Archive';
          element.addEventListener('click', () => archive_email(email.id));
        };

        element.className = "btn btn-secondary btn-sm btn-muted mt-3";
        container.append(element);
      
        return email     
      })
      .then(email => {
        let logged_in_user = document.querySelector('#logged-in-user').textContent;
        if (logged_in_user == email.sender) {return};
        const reply = document.createElement('button');
        reply.innerHTML = 'Reply';
        reply.className = "btn btn-secondary btn-sm btn-muted mt-3 mx-3";
        reply.addEventListener('click', () => compose_reply_email(email));
        container.append(reply);
      });
}


function archive_email (email_id) {

  fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({
        archived: true
  })
  }).
  then(() => load_mailbox('inbox'));
}

function unarchive_email (email_id) {

  fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({
        archived: false
  })
  }).
  then(() => load_mailbox('inbox'));
}

function compose_reply_email(email) {


  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#single-email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  document.querySelector('#compose-recipients').value = email.sender;

  let subject = email.subject
  if (!subject.startsWith("Re: ")) {
    subject = "Re: " + subject;
  }

  document.querySelector('#compose-subject').value = subject;
  document.querySelector('#compose-body').value = `On: ${email.timestamp}\nFrom: ${email.sender}\n\n${email.body}`

}