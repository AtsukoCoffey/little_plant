/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Take the text value from .text=> text format slice-off [0], take [1] to last ""
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);

// Set up stripe - create a variable using 'stripe public key'
var stripe = Stripe(stripe_public_key);

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