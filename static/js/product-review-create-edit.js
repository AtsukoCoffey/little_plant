/**
 * Review function - Create
 * For first time reviewer, display empty form to create first review.
 * To ensure one review per product, this "review-input-button" works
 * like edit function for reviewer who already did before  
 * 1. Open review modal
 * 2. If the button has "data-id" attribute, prefill the review text box
 * 3. Submit - send to product_detail view
 */
const reviewInput = document.getElementById("review-input-button");
const reviewText = document.getElementById("id_review_body");

reviewInput.addEventListener("click", (e) => {
    document.getElementById("review-overlay").style.display = "block";
    if (e.target.getAttribute("data-id")) {
        let dataId = e.target.getAttribute("data-id");

        let reviewContent = document.getElementById(
            `review${dataId}`).innerText;
            reviewText.value = reviewContent;
    }
});


/**
 * Review function - Edit
 * This is called from each review's edit buttons, display same modal form
 * But receive the wach review's id to prefill the review text and ratings
 * 1. Open review modal and change button text to "Update"
 * 2. This submission destination is "review_edit" views, we need slug value & id
 * 3. Submit - send to "review_edit" view
 */
// Edit functions - Open the same form modal and update
const editButtons = document.getElementsByClassName("btn-edit");
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


/**
 * Close buttons function for review
 */
const reviewCloseButton = document.getElementsByClassName("review-btn-close");

for (let button of reviewCloseButton) {
    button.addEventListener("click", (e) => {
        document.getElementById("review-overlay").style.display = "none";
    });
}