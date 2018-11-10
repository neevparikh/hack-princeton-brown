const PythonShell = require('python-shell');

/**
* A basic Hello World function
* @param {string} zipcode Who you're saying hello to
* @returns {string}
*/
module.exports = (zipcode = '', context, callback) => {
  if (zipcode == '') {
    callback(null, JSON.stringify({
      status: 400,
      message: null
    }));
  } else {
    // Write code here to get the data
    // Use ajax requests to execute python requests? 
    let options = {
      pythonPath: '/Users/ryanchoi/miniconda3/bin/python', //replace with own
      pythonOptions: ['-u'],
      scriptPath: '../../../../python/',
      args: ['zipcode']
    };

    PythonShell.run('./../../../neural-net.py', options, function(err, results) {
    if(err) callback(null, err);
    console.log('results: %j', results);
    callback(null, results);
    });

  }
};
