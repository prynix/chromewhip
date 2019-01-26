# noinspection PyPep8
# noinspection PyArgumentList

"""
AUTO-GENERATED BY `scripts/generate_protocol.py` using `data/browser_protocol.json`
and `data/js_protocol.json` as inputs! Please do not modify this file.
"""

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

class Cast(PayloadMixin):
    """ A domain for interacting with Cast, Presentation API, and Remote Playback API
functionalities.
    """
    @classmethod
    def enable(cls,
               presentationUrl: Optional['str'] = None,
               ):
        """Starts observing for sinks that can be used for tab mirroring, and if set,
sinks compatible with |presentationUrl| as well. When sinks are found, a
|sinksUpdated| event is fired.
Also starts observing for issue messages. When an issue is added or removed,
an |issueUpdated| event is fired.
        :param presentationUrl: 
        :type presentationUrl: str
        """
        return (
            cls.build_send_payload("enable", {
                "presentationUrl": presentationUrl,
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Stops observing for sinks and issues.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def setSinkToUse(cls,
                     sinkName: Union['str'],
                     ):
        """Sets a sink to be used when the web page requests the browser to choose a
sink via Presentation API, Remote Playback API, or Cast SDK.
        :param sinkName: 
        :type sinkName: str
        """
        return (
            cls.build_send_payload("setSinkToUse", {
                "sinkName": sinkName,
            }),
            None
        )

    @classmethod
    def startTabMirroring(cls,
                          sinkName: Union['str'],
                          ):
        """Starts mirroring the tab to the sink.
        :param sinkName: 
        :type sinkName: str
        """
        return (
            cls.build_send_payload("startTabMirroring", {
                "sinkName": sinkName,
            }),
            None
        )

    @classmethod
    def stopCasting(cls,
                    sinkName: Union['str'],
                    ):
        """Stops the active Cast session on the sink.
        :param sinkName: 
        :type sinkName: str
        """
        return (
            cls.build_send_payload("stopCasting", {
                "sinkName": sinkName,
            }),
            None
        )



class SinksUpdatedEvent(BaseEvent):

    js_name = 'Cast.sinksUpdated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 sinkNames: Union['[]', dict],
                 ):
        if isinstance(sinkNames, dict):
            sinkNames = [](**sinkNames)
        self.sinkNames = sinkNames

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')


class IssueUpdatedEvent(BaseEvent):

    js_name = 'Cast.issueUpdated'
    hashable = []
    is_hashable = False

    def __init__(self,
                 issueMessage: Union['str', dict],
                 ):
        if isinstance(issueMessage, dict):
            issueMessage = str(**issueMessage)
        self.issueMessage = issueMessage

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
