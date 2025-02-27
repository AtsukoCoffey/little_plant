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


/**
 * Close buttons function for review
 */
const reviewCloseButton = document.getElementsByClassName("review-btn-close");

for (let button of reviewCloseButton) {
    button.addEventListener("click", (e) => {
        document.getElementById("review-overlay").style.display = "none";
    });
}