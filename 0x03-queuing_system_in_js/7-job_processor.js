import kue from 'kue';

const blackListed = [4153518780, 4153518781];
const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);
    if (blackListed.includes(phoneNumber)) {
        done(Error(`Phone number ${phoneNumber} is blacklisted`));
    } else {
        job.progress(50, 100);
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
        done();
    }
}

queue.process('push_notification_code_2', (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});
