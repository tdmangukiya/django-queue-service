# Introduction #

For setting up an instance of the queue service, see RunningQueueService.

When it's running standalone, you communicate with it via http
requests. There are setup calls that you'd likely use once (or just
put the data into the fixtures) to create a queue. Once you had a
queue created, the time to insert something into the queue is the
latency of making that http request and getting a response. Inserting
into the queue (current release) is an HTTP Post, with the data being
a string. If you want to toss around slightly more complex data
structures, I'd recommend using JSON.

Something like the following:

```
import httplib2
client = httplib2.Http()
body_string = "message=%s" % (message_to_be_inserted_in_queue,)
(response,content) =
client.request(uri='http://dqshost:8000/q/queue_name_here/put',
method='POST', body=body_string)
if response['status'] != 200:
  print "Queue didn't accept the input"
```

The DQS architecture is based on Amazon's SQS, so removing a item from
a queue is actually a two step process. You ask for the item at the
top of the queue, and just asking for it makes it "invisible" to
others for a certain timeout (our default is 5 minutes). If you don't
come back and invoke an explicit "delete" on that item, it will become
visible again for another process to pop it off the queue.

The component that drives that "every 5 minutes clear things up" isn't
automatic, so in practice asking for something off the queue will make
it invisible forever unless you implement the clearing of expirations
as well. In practice, something like the following in a cron job
running every 5 minutes works fine:
`curl -i http://dqshost:8000/q/queue_name_here/clearexpire/`

While we've been working on the unstable branch and making this thing
more REST like (as opposed to my bastard REST/RPC initial
implementation), I put together a benchmark script to see how fast
things were going - basically to make sure we didn't bork anything in
the process of development. That script
(http://django-queue-service.googlecode.com/svn/trunk/benchmark.py)
has a bunch of reasonably well encapsulated example calls to the DQS
using urllib2 like the example above. Check it out for examples of
getting something from the queue and deleting that item from the queue
- the code should be pretty self-evident.


# Details #

Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages