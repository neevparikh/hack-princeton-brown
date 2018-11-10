// var stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);

/**
* A basic Hello World function
* @param {string} token
* @returns {string}
*/
module.exports = async (token, context) => {

  const charge = await stripe.charges.create({
    amount: 25,
    currency: 'usd',
    source: token,
    receipt_email: 'inos1199@gmail.com',
  });

  return charge;
};
