/*
    This is the server-side of things: Python bot is ran by express, minimalistic web framework, and
    also uses exec-sh to execute shell script. It has this server thing set up because the host
    I'm using has Node.js engine and it does not support Python.
*/

var express = require('express');
var app = express();
const cmd = require("node-cmd");
const crypto = require("crypto");
 
app.get('/', function (req, res) {
  	res.send('Hello World')
})

app.post('/git', (req, res) => {

	let hmac = crypto.createHmac("sha1", process.env.SECRET);
  	let sig  = "sha1=" + hmac.update(JSON.stringify(req.body)).digest("hex");
	
	if (req.headers['x-github-event'] == "push" && sig == req.headers['x-hub-signature']) {
		cmd.run('chmod 777 git.sh'); /* :/ Fix no perms after updating */
		cmd.get('./git.sh', (err, data) => {  // Run our script
		  if (data) console.log(data);
		  if (err) console.log(err);
		});
		cmd.run('refresh');  // Refresh project
	  
		let commits = req.body.head_commit.message.split("\n").length == 1 ?
              		  req.body.head_commit.message :
                      req.body.head_commit.message.split("\n").map((el, i) => i !== 0 ? "                       " + el : el).join("\n");
		console.log(`> [GIT] Updated with origin/master\n` + 
            		`        Latest commit: ${commits}`);
	}
  
	return res.sendStatus(200); // Send back OK status
});

app.listen(3000)
deletePictures()
startWeedbot()

function startWeedbot() {
	
	console.log("== Starting the Weedbot via start.sh ==")
	try {
		var execSh = require('exec-sh')
		execSh("bash ./start.sh")
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