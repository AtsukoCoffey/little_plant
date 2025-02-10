/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Take the text value from .text=> text format slice-off [0], take [1] to last ""
// Changed the variable names to puthon variables
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// Set up stripe - create a variable using 'stripe public key'
var stripe = Stripe(stripePublicKey);

//  Create an instance of stripe elements.
var elements = stripe.elements();

var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Then use elements to create a card element.
var card = elements.create('card', {style: style});

// Stripe is placed at id: #card-element in checkout.html
card.mount('#card-element');


// Handle realtime validation errors on the card element
// change event listener: checks errors everytime it changes
card.addEventListener('change', function (event) {

    var errorDiv = document.getElementById('card-errors');

    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});


// Handle form submit 
var form = document.getElementById('payment-form');

// function - 'stripe.confirmCardPayment()' in here
form.addEventListener('submit', function(ev) {

    ev.preventDefault();  // Default action is POST
    // card button and submission to prevent multiple submissions
    card.update({ 'disabled': true});  

    $('#submit-button').attr('disabled', true);
    // Using python variables in JavaScript 
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            // We'll want to re-enable the card element and the submit button to allow the user to fix it.
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
