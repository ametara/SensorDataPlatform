from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('syndash.syndash_sqlite.views',
    (r'^datapoints', 'datapoints'),
    (r'^datapoints/(?P<datapoint_id>\d+)$', 'datapoint'),
    #(r'^datapoints/(?P<datapoint_id>\d+)/measurement', 'measurement')
)
