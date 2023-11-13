


let commentButton = document.querySelector(".commentsSubmit");

commentButton.addEventListener("click", (e) => {
  e.preventDefault();
  let response = confirm(
    "Your update has been submitted and is pending approval"
  );

  if (response) {
    let form = document.querySelector(".comment-form");
    form.requestSubmit();
  }
});
