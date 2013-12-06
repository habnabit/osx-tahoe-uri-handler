#!/usr/bin/python

import struct
import webbrowser

from objc import signature
from PyObjCTools import AppHelper
from Foundation import NSAppleEventManager, NSObject
from AppKit import NSApplication


class AppDelegate(NSObject):
    def applicationWillFinishLaunching_(self, notification):
        man = NSAppleEventManager.sharedAppleEventManager()
        man.setEventHandler_andSelector_forEventClass_andEventID_(
            self,
            "openURL:withReplyEvent:",
            struct.unpack(">i", "GURL")[0],
            struct.unpack(">i", "GURL")[0])
        man.setEventHandler_andSelector_forEventClass_andEventID_(
            self,
            "openURL:withReplyEvent:",
            struct.unpack(">i", "WWW!")[0],
            struct.unpack(">i", "OURL")[0])

    @signature('v@:@@')
    def openURL_withReplyEvent_(self, event, replyEvent):
        keyDirectObject = struct.unpack(">i", "----")[0]
        url = (event.paramDescriptorForKeyword_(keyDirectObject)
               .stringValue().decode('utf8'))
        url = 'https://peq.io/' + url
        webbrowser.open(url)


def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    app.setDelegate_(delegate)
    AppHelper.runEventLoop()


if __name__ == '__main__':
    main()
