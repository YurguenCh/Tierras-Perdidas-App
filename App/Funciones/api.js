const FiveM = require("fivem-server-api");

const options = {
    timeout: 5000,
    errmsg: 'Error Occured',
};

const server = new FiveM.Server('199.127.62.247:30120', options);

async function fetchData() {
    try {
        const [serverStatus, players] = await Promise.all([server.getServerStatus(), server.getPlayers(), server.getMaxPlayers()]);
        console.log(JSON.stringify({ serverStatus, players }));
    } catch (error) {
        console.error(error);
    }
}

fetchData();
