import kue from 'kue';

const push_notification_code = kue.createQueue();
const job = push_notification_code.create('job', {
    phoneNumber: '080292929',
    message: 'Please accept my congratulations!',
}).save(err => {
    if (!err) {
        console.log(`Notification job created: ${job.id}`);
    }
});

job.on('completed', ()=> console.log(`Notification job completed`));
job.on('failed', ()=> console.log(`Notification job failed`));
