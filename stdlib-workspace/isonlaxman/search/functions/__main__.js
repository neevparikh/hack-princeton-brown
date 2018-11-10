const PythonShell = require('python-shell');

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
    // Use ajax requests to execute python requests? 
    callback(null);
  }
};
