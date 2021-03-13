module.exports = {
    name: 'comida',
    description: "this is a comida command!",
    execute(message, args){ 
        // The ideal would be to put this/ese sentences in an array and randomly select one, but again I'm lazy and idk js
        message.channel.send( `<@${'636682510188675093'}>` + ' qual é a comida mais logo paizinho?');
    }
}
