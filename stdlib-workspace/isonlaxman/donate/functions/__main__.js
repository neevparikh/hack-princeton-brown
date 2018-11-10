// var stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);

/**
* A basic Hello World function
* @param {string} token
* @returns {string}
*/
module.exports = (token, context, callback) => {

  const charge = stripe.charges.create({
    amount: 25,
    currency: 'usd',
    source: token,
    receipt_email: 'inos1199@gmail.com',
  });

  callback(null, charge);
};
