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

var execSh = require('exec-sh')
execSh("sh start.sh")