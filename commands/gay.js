const Discord = require('discord.js'); // yup this line is in the main file too
const attachment1 = new Discord.MessageAttachment("././images/HA.gif");

module.exports = {
    name: 'gay',
    description: "this is a gay command!",
    execute(message, args){ 
        message.channel.send(attachment1);
    }
}