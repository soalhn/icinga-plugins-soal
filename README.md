# icinga-plugins-soal

Custom Icinga/Nagios plugins

## Available plugins

### check_activemq.py

Icinga/Nagios plugin to check ActiveMQ instance, by subscribing
to a queue, sending and reading a message.

#### Dependencies

The plugin needs module [Stompest](http://nikipore.github.io/stompest/index.html)

#### Installation

Copy the plugins you need to Icinga/Nagios' plugins location, usually:
/usr/lib/nagios/plugins

### Authors
Soal (@soalhn)

### Credits
Based on the perl version from [Nagios Exchange](http://exchange.nagios.org/directory/Plugins/Java-Applications-and-Servers/check_activemq/details)

