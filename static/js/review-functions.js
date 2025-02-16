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





// reviewInput.addEventListener("click", (e) => {
//     document.getElementById("reviewModal").style.display = "block";
//     document.getElementById("reviewModal").style.z-index = 99999;
//     console.log("OK");
// });



// Assign Edit functions
const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_review_body");
const reviewtForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");
// Assign Delete functions
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


