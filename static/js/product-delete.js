/**
 * Deletion function
 * This is used for Admin's product delete & users review delete function
 * 1. Identify the data for products or for reviews
 * 2. Open Delete modal
 * 3. Submit - delete
 */ 
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



