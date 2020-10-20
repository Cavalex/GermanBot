
const Discord = require('discord.js'); 
const fs = require("fs");

module.exports = {
    name: 'help',
    description: 'Lists available commands',
    execute(message, args){
        message.channel.send(
`Comandos:
!g help
!g comida
!g boracs
!g boralol
!g lol
!g ping
!g pong
!g gay
**e mais a chegar!**`);
        /*
        fs.readdir("./commands/", (err, files) => {
            if(err) console.error(err);

            let jsfiles = files.filter(f => f.split(".").pop() === "js");
            if(jsfiles.length <= 0) {
                console.log("No commands to load!");
                return;
            }

            var namelist = "";
            var desclist = "";
            var usage = "";
            
            let result = jsfiles.forEach((f, i) => {
                let props = require(`./${f}`);
                namelist = props.help.name;
                desclist = props.help.description;
                usage = props.help.usage;
            
                // send help text
                message.author.send(`**${namelist}** \n${desclist}`);
            });
        })
        */
    }
}