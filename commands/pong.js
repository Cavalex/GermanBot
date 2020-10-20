let pongCount = 0;

module.exports = {
    name: 'pong',
    description: "this is a pong command!",
    execute(message, args){ 
        pongCount += 1;
        if(pongCount % 4 == 0){
            message.channel.send("LEVAS UMA LASTÍBIA, COLO-TE A PUTA DA CARA AO CU!");
        }
        else if(pongCount % 4 == 3){
            message.channel.send('PING CARALHO! QUERES QUE EU REPITA ESTA MERDA MAIS VEZES?')
        }
        else if(pongCount % 4 == 2){
            message.channel.send('PING!');
        }
        else{
            message.channel.send('ping!');
        }
    }
}