let pingCount = 0;

module.exports = {
    name: 'ping',
    description: "this is a ping command!",
    execute(message, args){ 
        pingCount += 1;
        if(pingCount % 4 == 0){
            message.channel.send("LEVAS UMA LASTÍBIA, COLO-TE A PUTA DA CARA AO CU!");
        }
        else if(pingCount % 4 == 3){
            message.channel.send('PONG CARALHO! QUERES QUE EU REPITA ESTA MERDA MAIS VEZES?')
        }
        else if(pingCount % 4 == 2){
            message.channel.send('PONG!');
        }
        else{
            message.channel.send('pong!');
        }
    }
}