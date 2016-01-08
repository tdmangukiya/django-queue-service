# Introduction #

The queue service is intended to be a lightweight, open-source queueing mechanism along the lines of the [Amazon Simple Queue Service](http://www.amazon.com/Simple-Queue-Service-home-page/b?ie=UTF8&node=13584001). The concepts are based off that API, and the implementation is using the Django web framework (python). The queue is intended to be used through a REST interface. In effect, this project is an open source clone of that work.

## Purpose ##

The question often comes up on the [Django Users mailing list](http://groups.google.com/group/django-users) : _how I do I arrange for background processing?_ Some times you'd like to queue up something that'll take a little while (longer than you'd want to hold up an http request for anyway), and then have another process running that deals with it. This queue project is intended for exactly that need. It is written using the [Django](http://djangoproject.com/) web framework, but it can be used from anything over it's REST interface.

## Linkage ##

  * BackgroundHistory
  * MovingForward
  * HowToUseDjangoQueueService

## Email ##
  * Discussion http://groups.google.com/group/django-queue-service/topics
    * [django-queue-service@googlegroups.com](mailto:django-queue-service@googlegroups.com)
  * Commits http://groups.google.com/group/django-queue-server-commits

## Feeds ##
  * [Last 15 Commits](http://groups.google.com/group/django-queue-server-commits/feed/rss_v2_0_msgs.xml) (RSS)
  * [All Commits](http://groups.google.com/group/django-queue-server-commits/feeds) (Atom/RSS)