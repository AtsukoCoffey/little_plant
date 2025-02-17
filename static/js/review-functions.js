/**
 * Review and Rating function
 */

// Create review - Open the form input modal and submit
const reviewInput = document.getElementById("review-input-button");
const dataDismiss = document.getElementsByClassName("data-dismiss");
const closeButton = document.getElementsByClassName("btn-close");


reviewInput.addEventListener("click", (e) => {
    document.getElementById("review-overlay").style.display = "block";
});

for (let button of dataDismiss) {
    button.addEventListener("click", (e) => {
        document.getElementById("review-overlay").style.display = "none";
        deleteModal.hide();
    });
}
for (let button of closeButton) {
    button.addEventListener("click", (e) => {
        document.getElementById("review-overlay").style.display = "none";
        deleteModal.hide();
    });
}

// Edit functions - Open the same form modal and update
const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_review_body");
const reviewForm = document.getElementById("reviewForm");  // Form element
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        // We need to send slug value too
        let dataId = e.target.getAttribute("data-id");
        let slug = e.target.getAttribute("data-slug");
        document.getElementById("review-overlay").style.display = "block";

        let reviewContent = document.getElementById(
            `review${dataId}`).innerText;
            reviewText.value = reviewContent;
        submitButton.innerText = "Update";
        reviewForm.setAttribute("action", `/products/${slug}/edit_review/${dataId}/`);
    });
}


// Delete functions - Open Delete modal and submit
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let datatId = e.target.getAttribute("data-id");
      let slug = e.target.getAttribute("data-slug");
      deleteConfirm.href = `/products/${slug}/delete_review/${datatId}/`;
      deleteModal.show();
    });
}
