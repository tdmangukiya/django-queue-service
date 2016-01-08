# Introduction #

The results are all from my laptop - 2GHz Intel Core Duo, 2GB RAM. Running python 2.5 and the current trunk of Django (0.97-pre-SVN-6668).

The benchmarking script is written with httplib2, making direct HTTP calls against the server. For the Nov 11 results, I was benchmarking using the WSGIserver we ship with the project. A few light runs against the development server showed that it was a tad slower. I haven't tested this against any other combinations - although the data would be useful in the future.

The benchmarking script has two tests embedded.

The first test times the "add a message" function and the "get and delete a message" combination functions over time with the queue just getting worked. I set this up so that we could measure the impact of indexes getting wonked or just noticing something slowly going bad over time.

Following that, the next test runs through the timing for adding messages into the queue and getting/deleting messages from the queue, scaling the queue size from 0 to 25,000 items.

  * The results from Joe's laptop, Nov 11, 2007 are available at http://django-queue-service.googlecode.com/svn/branches/unstable/docs/DQS_BENCHMARK.xls