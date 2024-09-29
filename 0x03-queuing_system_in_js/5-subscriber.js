import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('connect', () => {
    console.log("Redis client connected to the server");
});

subscriber.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
});

let channel = 'holberton school channel';

subscriber.subscribe(channel, (message, channel) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe(channel);
        process.exit(0);
    }
});

subscriber.connect();
