import kue from 'kue';

const queue = kue.createQueue();
/**
 * 
 * @param {Array} jobs 
 * @param {queue} queue 
 */
function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error(' Jobs is not an array');
    }
    jobs.forEach(job => {
        const new_job = queue.create('push_notification_code_3', {
            phoneNumber: job.phoneNumber,
            message: job.message,
        }).save(err => {
            if (!err) {
                console.log(`Notification job created: ${new_job.id}`);
            }
        });
        new_job.on('progress', progress => {
            console.log(`Notification job ${new_job.id} ${progress}% complete`);
        });
        new_job.on('complete', () => {
            console.log(`Notification job ${new_job.id} completed`);
        });
        new_job.on('failed', err => {
            console.error(`Notification job ${new_job.id} failed: ${err}`);
        });
    });
}

export default createPushNotificationsJobs;
