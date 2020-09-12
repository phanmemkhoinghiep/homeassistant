# """
# A component which allows you to parse an RSS feed into a sensor
# For more details about this component, please refer to the documentation at
# https://github.com/custom-components/sensor.feedparser
# Following spec from https://validator.w3.org/feed/docs/rss2.html
# """
import asyncio
import re
import feedparser
import logging
import voluptuous as vol
from datetime import timedelta
from dateutil import parser
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import (PLATFORM_SCHEMA)
from homeassistant.const import (CONF_NAME)

__version__ = '0.1.1'
_LOGGER = logging.getLogger(__name__)

REQUIREMENTS = ['platform']

CONF_FEED_URL = 'feed_url'

DEFAULT_SCAN_INTERVAL = timedelta(hours=1)

# COMPONENT_REPO = 'https://github.com/custom-components/sensor.feedparser/'
SCAN_INTERVAL = timedelta(hours=1)
ICON = 'mdi:rss'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME): cv.string,
    vol.Required(CONF_FEED_URL): cv.string,
})


@asyncio.coroutine
def async_setup_platform(hass, config, async_add_devices, discovery_info=None):
    async_add_devices([FeedParserSensor(
        feed=config[CONF_FEED_URL],
        name=config[CONF_NAME]
        )], True)


class FeedParserSensor(Entity):
    def __init__(self, feed: str, name: str):
        self._feed = feed
        self._name = name
        self._state = None
        self._entries = []
    def update(self):
        parsedFeed = feedparser.parse(self._feed)
        if not parsedFeed:
            return False
        else:
            self._entries = []
            for entry in parsedFeed.entries[:self._state]:
                entryValue = ''            
                clean = re.compile('<.*?>')
                clean_content= re.sub(clean, '', entry.summary)
                entryValue ='Tiêu đề: '+entry.title+', nội dung: '+clean_content+'. '
                self._entries.append(entryValue)


    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return ICON

    @property
    def device_state_attributes(self):
        return {
            'entries': self._entries
        }
