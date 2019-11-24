# bell-controller
### Simple python script to turn on and off a relay

The goal of this script is to provide an easy method of controlling a relay via GPIO on a Raspberry Pi. In conjunction with this, we'll be using a crontab GUI like [cronkeep/cronkeep](https://github.com/cronkeep/cronkeep) or [alseambusher/crontab-ui](https://github.com/alseambusher/crontab-ui) to allow for anyone (with authentication) to manage when the relay is triggered.

The command line args for the script are as follows

`python main.py off` or

`python main.py on [time in seconds]`

By default, the `on` command will not allow you to leave the relay on forever, you must specify some float number of seconds until the relay turns off. Therefore, the `off` command will probably rarely be used.

Similar systems cost upwards of a few hundred dollars, but I already have the hardware to make it work without extra costs.
