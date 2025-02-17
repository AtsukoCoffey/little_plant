/**
 * Admin page Product & Site user Review - deletion function
 */
// Delete functions - Open Delete modal and submit
// Identify the data for products or for reviews
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let datatId = e.target.getAttribute("data-id");
        let productId = e.target.getAttribute("data-product-id");
        let slug = e.target.getAttribute("data-slug");
        if (productId) {
            deleteConfirm.href = `/products/delete/${productId}/`;
            deleteModal.show();
        } else {
            deleteConfirm.href = `/products/${slug}/delete_review/${datatId}/`;
            deleteModal.show();
        }
    });
}


/**
 * Close buttons function for review
 */
const reviewCloseButton = document.getElementsByClassName("review-btn-close");

for (let button of reviewCloseButton) {
    button.addEventListener("click", (e) => {
        document.getElementById("review-overlay").style.display = "none";
    });
}
/**
 * Close buttons function for Deletion
 */
const dataDismiss = document.getElementsByClassName("data-dismiss");
const closeButton = document.getElementsByClassName("btn-close");

for (let button of dataDismiss) {
    button.addEventListener("click", (e) => {
        deleteModal.hide();
    });
}
for (let button of closeButton) {
    button.addEventListener("click", (e) => {
        deleteModal.hide();
    });
}


/**
 * Review function
 */
// Create review - Open the form input modal and submit
const reviewInput = document.getElementById("review-input-button");

reviewInput.addEventListener("click", (e) => {
    document.getElementById("review-overlay").style.display = "block";
});


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

