from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    #Main
    url(r'^$', 'main.views.index', name='home'),
    url(r'^settings/', 'main.views.settings', name='settings'),
    url(r'^network/', 'main.views.networkviews', name='network view'),
    url(r'^notifications/', 'main.views.notifications', name='Notification History'),
    url(r'^plugins/', 'main.views.plugins', name='plugins'),
    url(r'^hostcheck/', 'main.views.hostcheck', name='netview'),
    url(r'^netview/', 'main.views.netview', name='netview'),
    url(r'^netctrl/(\w+)/', 'main.views.netctrl', name='netctrl'),
    url(r'^config/(\w+)/', 'main.views.conf', name='configure'),
    
        #Command Load Pages
    url(r'^startpwn/(\w+)/', 'main.views.startpwn', name='start'),
    url(r'^stoppwn/', 'main.views.stoppwn', name='stop'),
    url(r'^resetpwn/', 'main.views.resetpwn', name='resetdb'),
    url(r'^gate/', 'main.views.gate', name='getgateway'),
    
        #Modules
    url(r'^builder/', 'modules.views.builder', name='getgateway'),
    url(r'^create/', 'modules.views.create', name='getgateway'),
    url(r'^wpad.dat', 'modules.views.wpad', name='WPAD'),
    
)
