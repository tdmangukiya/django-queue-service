from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^qs/', include('qs.foo.urls')),
    (r'^createqueue/', 'qs.queue.views.create_queue'), #post 'name' of queue
    (r'^deletequeue/', 'qs.queue.views.delete_queue'), #post 'name' of queue
    (r'^purgequeue/', 'qs.queue.views.purge_queue'),   #post 'name' of queue
    (r'^listqueues/', 'qs.queue.views.list_queues'),
    
    (r'^q/(?P<queue_name>\w+)/put/', 'qs.queue.views.put'),
    (r'^q/(?P<queue_name>\w+)/clearexpire/', 'qs.queue.views.clear_expirations'),
    (r'^q/(?P<queue_name>\w+)/count/json/', 'qs.queue.views.count', {"response_type":"json"}),
    (r'^q/(?P<queue_name>\w+)/count/', 'qs.queue.views.count', {"response_type":"text"}),
    (r'^q/(?P<queue_name>\w+)/delete/$', 'qs.queue.views.delete'), #post 'message_id' of msg
    (r'^q/(?P<queue_name>\w+)/json/', 'qs.queue.views.get', {"response_type":"json"}),
    (r'^q/(?P<queue_name>\w+)/', 'qs.queue.views.get', {"response_type":"text"}),
    
    # Uncomment this for admin:
    # (r'^admin/', include('django.contrib.admin.urls')),
)