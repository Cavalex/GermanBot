const Discord = require('discord.js');

const client = new Discord.Client(); // the bot

//const prefix = '!';
// space in front of ger for the prefix
const prefix = '!g ';

const fs = require('fs');

// create a collection
client.commands = new Discord.Collection();

// read only js files
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));
for(const file of commandFiles){
    const command = require(`./commands/${file}`);

    client.commands.set(command.name, command);
}

client.once('ready', () => {
    console.log('O German está vivo, yey!');
})

client.on('message', message => {
    client.user.setActivity('aziando no lol')

    if((!message.content.startsWith(prefix)) || message.author.bot) return;
    if (message.author.bot) return;

    const args = message.content.slice(prefix.length).split(/ +/); // Ignore spaces (???)
    const command = args.shift().toLowerCase();
    // A switch or a for would be better but I'm lazy and idk js
    if(command === 'ping'){
        client.commands.get('ping').execute(message, args)
    }
    else if(command === 'gay'){
        client.commands.get('gay').execute(message, args)
    }
    else if(command === 'pong'){
        client.commands.get('pong').execute(message, args)
    }
    else if(command === 'comida'){
        client.commands.get('comida').execute(message, args)
    }
    else if(command === 'lol'){
        client.commands.get('lol').execute(message, args)
    }
    else if(command === 'boracs'){
        client.commands.get('boracs').execute(message, args)
    }
    else if(command === 'boralol'){
        client.commands.get('boralol').execute(message, args)
    }
    else if(command === 'help'){
        client.commands.get('help').execute(message, args)
    }
});




// must stay on the last line
// don't mess with this code
client.login('NzY3ODg3ODUxNzkwMjcwNDY0.X44dSg.4ySVPvKKESk4BbZvHNapu9qY2vI');
