/**
 * Review and Rating function
 */
const reviewInput = document.getElementById("review-input-button");
const dataDismiss = document.getElementById("data-dismiss");


reviewInput.addEventListener("click", (e) => {
    document.getElementById("review-overlay").style.display = "block";
});
dataDismiss.addEventListener("click", (e) => {
    document.getElementById("review-overlay").style.display = "none";
});


// Assign Edit functions
const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_review_body");
const reviewForm = document.getElementById("reviewForm");  // Form element
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let dataId = e.target.getAttribute("data-id");
        let reviewContent = document.getElementById(
          `review${dataId}`).innerText;
          reviewText.value = reviewContent;
        submitButton.innerText = "Update";
        reviewForm.setAttribute("action", `edit_review/${dataId}/`);
    });
}








// Assign Delete functions
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


