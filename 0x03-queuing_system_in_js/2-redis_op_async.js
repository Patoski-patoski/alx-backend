import redis from 'redis';
import { promisify } from "util";

// Create a new Redis client
const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error}`);
});

const getAsync = promisify(client.get).bind(client);
client.connect();

/**
 * Set a new school in the Redis database.
 *
 * @param {string} schoolName - The name of the school which serves as the key.
 * @param {string} value - The value to set for the school.
 */

function setNewSchool(schoolName, value) {
        client.set(schoolName, value, redis.print);
}

/**
 * Display the value of a school from the Redis database.
 *
 * @param {string} schoolName - The name of the school.
 */
async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (err) {
        console.error('Error fetching value:', err);
    }
}

(async () => {
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();
