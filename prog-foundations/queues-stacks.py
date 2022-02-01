# Queue ---- >  FIFO
import queue

q = queue.Queue()

for i in range(3):
    q.put('bag'+str(i))

print(q)

print(q.get())
print(q.get())


# q.empty()
# q.full()
# q  = queue.Queue(Max_Length)

# Stack --- > LIFO
