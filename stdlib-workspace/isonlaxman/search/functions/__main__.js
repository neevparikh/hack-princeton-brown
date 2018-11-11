
/**
* A basic Hello World function
* @param {string} zipcode Who you're saying hello to
* @returns {string}
*/
module.exports = async (zipcode = '', context) => {
  var { PythonShell } = require('python-shell');
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

  let options = {
    pythonPath: 'C:\\Users\\Laxman\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe', //replace with own
    pythonOptions: ['-u'],
    scriptPath: '../../../../python',
    // args: []
  };

  var result = await PythonShell.run('neural-net.py', options);
  console.log('results: %j', results);
  return JSON.stringify(result);
}
