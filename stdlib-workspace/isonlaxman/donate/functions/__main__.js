var stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);
var lib = require("../../../../website/lib");

/**
* A basic Hello World function
* @returns {string}
*/
module.exports = (context, callback) => {
  const charge = stripe.charges.create({
    amount: 999,
    currency: 'usd',
    source: 'tok_visa',
    receipt_email: 'inos1199@gmail.com',
  });

  callback(null, charge);

};
