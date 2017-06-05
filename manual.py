import time
from tasks import add
result = add.delay(2,3)
time.sleep(1)
print result.get()
