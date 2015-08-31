var fs = require('fs');
var express = require('express');
    app = express(),
    server = require('http').createServer(app),
    io = require('socket.io').listen(server);

server.listen(8009);
console.log("server inicio en puerto 8009");

app.use(express.static(__dirname +'/js'));

app.get("/",function(req,res){
    res.sendfile(__dirname +'/index.html');
});

var mensajesnuevoscant = 0;

io.sockets.on('connection', function(socket){
    setInterval(function(){
        var contenido = fs.readFileSync("mensajes.json");
        
        var jsoncontenido = JSON.parse(contenido);
        var cantidadmensajes = jsoncontenido.cantidadmsg;
        
        if(mensajesnuevoscant!=cantidadmensajes){

            mensajesnuevoscant = cantidadmensajes;
            var metada = {
                tipomsg: jsoncontenido.tipomsg,
                nick: jsoncontenido.nick,
                msg:jsoncontenido.msg
            };
            socket.emit('date',metada);
        }
    },100);
});