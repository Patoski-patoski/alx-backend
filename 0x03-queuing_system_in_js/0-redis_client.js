import { createClient } from 'redis'

const err_message = 'Redis client not connected to the server: ERROR_MESSAGE: ';
const connect_message = 'Redis client connected to the server';

const client = createClient();
client.on('error', err => console.log(err_message, err));
client.on('connect', () => console.log(connect_message));
