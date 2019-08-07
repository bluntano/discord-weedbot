/*
    This is the server-side of things: Python bot is ran by express, minimalistic web framework, and
    also uses exec-sh to execute shell script. It has this server thing set up because the host
    I'm using has Node.js engine and it does not support Python.
*/

var express = require('express');
var app = express();
var cmd = require('node-cmd');
const exec = require('exec-sh');

 
app.get('/', function (req, res) {
  	res.send('Hello World')
})

app.post('/git', (req, res) => {
	// If event is "push"
	if (req.headers['x-github-event'] == "push") {
		cmd.run('chmod 777 ./git.sh');
		cmd.run('sh ./git.sh');
		console.log("> [GIT] Updated with origin/master");
	}
  
	return res.sendStatus(200); // Send back OK status
});

app.listen(3000)
deletePictures()
startWeedbot()

function startWeedbot() {
	
	console.log("== Starting the Weedbot via start.sh ==")
	exec("bash ./start.sh");
	return
}

function deletePictures(isDelete = true) {
	
	if (isDelete === true) {
		console.log("== Deleting pictures ==")
		var fs = require("fs-extra")
		try {
			fs.removeSync('./weedbot/upload-pictures')
		}
		catch (err) {
			console.log("Deletion failed: " + err)
		}
	} else if (isDelete == false) {
		return
	}
	return
}