/**
* A basic Hello World function
* @param {string} city Who you're saying hello to
* @returns {string}
*/
module.exports = (city = '', context, callback) => {
  if (city == '') {
    callback(null, JSON.stringify({
      status: 400,
      message: null
    }));
  } else {
    // Write code here to get the data
    callback(null, `hello ${name}`);
  }
};
