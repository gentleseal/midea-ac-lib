Updated home-assistant component for hass version 0.96 and the "climate-1.0" changes.

Last tested with hass version 0.110.x

## Installation

### HACS [![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)
1. Search the HACS Store for Midea
2. Install the Midea Aircon component
3. Add configuration to your yaml, as shown here: https://github.com/NeoAcheron/midea-ac-py/wiki/Installing-to-Home-Assistant

### Manual
1. Clone this repo
1. Place the `custom_components/midea` folder into your `custom_components` folder
1. Add configuration to your yaml, as shown here: https://github.com/NeoAcheron/midea-ac-py/wiki/Installing-to-Home-Assistant

## Fan Only Workaround
There is an optional workaround to avoid reading the device's state on initial connection, since for some reason the update method causes my device to turn on and be set to fan only mode. (This is a bug to be fixed in [andersonshatch/midea-ac-lib](https://github.com/andersonshatch/midea-ac-lib)... if only I knew how.)

With this workaround enabled, it restores state from home-assistant's previous state.
This should work okay as long as you only alter the state of your device using home-assisant.

If you find this component turns your device on and to fan_only every time home-assistant updates it (once a minute by default), you probably want to turn on the workaround with this config property:
```
use_fan_only_workaround: true
```

Original Readme:
```# midea-ac-py 

This is a library to allow communicating to a Midea AC via the Midea Cloud.

This is a very early release, and comes without any guarantees. This is still an early work in progress and simply serves as a proof of concept.

This library would not have been possible if it wasn't for the amazing work done by @yitsushi and his Ruby based command line tool. 
You can find his work here: https://github.com/yitsushi/midea-air-condition
The reasons for me converting this to Python is that this library also serves as a platform component for Home Assistant.

## Wiki
Please visit the Wiki for device support and instruction on how to use this component: https://github.com/NeoAcheron/midea-ac-py/wiki 
```

This is an updated version of the library component only, from the repo at [NeoAcheron/midea-ac-py](https://github.com/NeoAcheron/midea-ac-py).

So far, the only changes are to handle the session timeout properly. It should recover from an invalidated session or use of your account on another device.

It is used by the home-assistant custom component at [andersonshatch/midea-ac-py](https://github.com/andersonshatch/midea-ac-py)

Original Readme:
# midea-ac-py 

This is a library to allow communicating to a Midea AC via the Midea Cloud.

This is a very early release, and comes without any guarantees. This is still an early work in progress and simply serves as a proof of concept.

This library would not have been possible if it wasn't for the amazing work done by @yitsushi and his Ruby based command line tool. 
You can find his work here: https://github.com/yitsushi/midea-air-condition
The reasons for me converting this to Python is that this library also serves as a platform component for Home Assistant.

## Wiki
Please visit the Wiki for device support and instruction on how to use this component: https://github.com/NeoAcheron/midea-ac-py/wiki 
