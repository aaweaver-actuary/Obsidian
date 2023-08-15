## Event loop
* handles callback functions
* allows async

### phases of the event loop
[https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/) 
## callback queue
- first in first out

## when is it best to use `node.js`
- not:
	- video processing
	- ML
		- these are blocking ops 
	- possible but no advantage over other languages/runtimes
- very good for servers:
	- querying data
	- when main performance problem is input/output rather than calculations
	- eg netflix uses node to send video files from DB to client

## observer design pattern

## node `events` module
- [https://nodejs.org/api/events.html#events_events](https://nodejs.org/api/events.html#events_events) 