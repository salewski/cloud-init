import abc
import logging

import six

from cloudinit.registry import DictRegistry


@six.add_metaclass(abc.ABCMeta)
class ReportingHandler(object):
    """Base class for report handlers.

    Implement :meth:`~publish_event` for controlling what
    the handler does with an event.
    """

    @abc.abstractmethod
    def publish_event(self, event):
        """Publish an event to the ``INFO`` log level."""


class LogHandler(ReportingHandler):
    """Publishes events to the cloud-init log at the ``INFO`` log level."""

    def publish_event(self, event):
        """Publish an event to the ``INFO`` log level."""
        logger = logging.getLogger(
            '.'.join(['cloudinit', 'reporting', event.event_type, event.name]))
        logger.info(event.as_string())


available_handlers = DictRegistry()
available_handlers.register_item('log', LogHandler)
