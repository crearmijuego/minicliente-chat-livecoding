(function($){
    var socket = io.connect();
    socket.on("date",function(data){

        if(data.tipomsg=='msg'){
            if(data.msg!=''){
                $('#mensajeschat').append('<li>'+data.nick+' : '+ data.msg+'</li>');
            }
        }
        if(data.tipomsg=='conectado'){
            if(data.msg!=''){
                $('#mensajeschat').append('<li>'+data.nick+' : '+ data.msg+'</li>');
            }
        }

        $('#mensajeschat').scrollTop($('#mensajeschat').prop('scrollHeight'));
    });
})(jQuery);