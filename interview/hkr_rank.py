def find(br, agg):
    for i, a in enumerate(agg):
        if a[0] >= br[0] or a[1] >= br[0]:
            return i
    return None

def insert(br, agg, i):
    lr = agg[i]
    brl = sum(br)
    if(lr[0] <= br[0]):
        agg[i] = (lr[0], max(lr[1], brl))
    elif(lr[0] > br[0]):
        if (brl >= lr[0]):
            agg[i] = (br[0], max(lr[1], brl))
        else:
            agg.insert((br[0], brl))
            i += 1
    li = len(agg)
    while i < li:
        crr = agg[i]
        nxt = agg[i+1]
        if nxt[0] <= crr[1]:
            agg[i] = (crr[0], max(crr[1], nxt[1]))
            del agg[i+1]
            li -= 1
        else:
            i +=1
    
def merge(br, agg):
    loc = find(br, agg)
    if (loc):
        insert(br, agg, loc)
    else:
        agg.append((br[0], sum(br)))


n = int(raw_input())
barriers = [ map(int, raw_input().split())[::2] for _ in xrange(n) ]
agg_barrier = []
for k in barriers:
    merge(k, agg_barrier)

counter = 0
for x in agg_barrier:
    counter += x[1] - x[0] + 1
print counter