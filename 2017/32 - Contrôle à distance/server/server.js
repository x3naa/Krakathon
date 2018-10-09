var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var path = require('path')

app.use(express.static('public'))

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

app.post('/', function(req,res){
  send_vibrate();
  res.sendFile(__dirname + '/index.html');
});

app.get('/app', function(req, res){
  res.sendFile(__dirname + '/app.html')
})

io.on('connection', function(socket){
  console.log('a user connected');
});

http.listen(80, function(){
  console.log('listening on *:80');
});

function send_vibrate(){
  console.log('sending vibrate')
  io.emit('message')
}