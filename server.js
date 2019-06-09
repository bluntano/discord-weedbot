/*
    This is the server-side of things: Python bot is ran by express, minimalistic web framework, and
    also uses exec-sh to execute shell script. It has this server thing set up because the host
    I'm using has Node.js engine and it does not support Python.
*/

var express = require('express');
var app = express();
 
app.get('/', function (req, res) {
  res.send('Hello World')
})
 
app.listen(3000)
deletePictures()
startWeedbot()

function startWeedbot() {
	
	console.log("== Starting the Weedbot via start.sh ==")
	try {
		var execSh = require('exec-sh')
		execSh("sh start.sh")
	}
	catch(err) {
		console.log("Failed to start: " + err)
	}
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