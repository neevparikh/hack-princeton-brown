var stripe = require("stripe");

/**
* A basic Hello World function
* @param {string} secret_key Who you're saying hello to
* @returns {string}
*/
module.exports = (secret_key, context, callback) => {
  log("TAKE 2");

  stripe = stripe(secret_key);

  log("TAKE 3");
  
  const charge = stripe.charges.create({
    amount: 999,
    currency: 'usd',
    source: 'tok_visa',
    receipt_email: 'inos1199@gmail.com',
  });

  callback(null, charge);

};
