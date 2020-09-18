from apscheduler.schedulers.blocking import BlockingScheduler
from automessaging import automessaging


sched = BlockingScheduler()

sched.add_job(automessaging, 'interval', seconds=1)

sched.start()