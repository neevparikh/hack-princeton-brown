
/**
* A basic Hello World function
* @param {string} zipcode Who you're saying hello to
* @param {string} time
* @returns {string}
*/
module.exports = (zipcode = '', time = '', context, callback) => {
  // var { PythonShell } = require('python-shell');
  console.log("HELLLO");
  // return "HELLO";
  // if (zipcode == '') {
  //   return JSON.stringify({
  //     status: 400,
  //     message: null
  //   });
  // } else {
  // Write code here to get the data
  // Use ajax requests to execute python requests? 

  // let options = {
  //   pythonPath: 'C:\\Users\\Laxman\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe', //replace with own
  //   pythonOptions: ['-u'],
  //   scriptPath: '../../../../scraper',
  //   // args: []
  // };

  // await PythonShell.run('zipcode_extractor.py', options);

  var data = require('./helper.js');
  data = JSON.parse(data());

  callback(null, data[zipcode][time]);
}
