from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests

def is_stream_online(username):
    """
    Returns True if the Twitch stream is online, False otherwise.
    Uses the public frontend Client-ID (no OAuth).
    """
    url = f"https://www.twitch.tv/{username}"
    headers = {
        "Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko",  # Publicly known Client-ID
    }
    resp = requests.get(url, headers=headers)
    return "isLiveBroadcast" in resp.text

with SB(uc=True, test=True) as ryute:

    if True:
        url = "https://kick.com/brutalles"
        ryute.uc_open_with_reconnect(url, 5)
        ryute.uc_gui_click_captcha()
        ryute.sleep(1)
        ryute.uc_gui_handle_captcha()
        ryute.sleep(1)
        if ryute.is_element_present('button:contains("Accept")'):
            ryute.uc_click('button:contains("Accept")', reconnect_time=4)
        if ryute.is_element_visible('#injected-channel-player'):
            yrfht = ryute.get_new_driver(undetectable=True)
            yrfht.uc_open_with_reconnect(url, 5)
            yrfht.uc_gui_click_captcha()
            yrfht.uc_gui_handle_captcha()
            ryute.sleep(10)
            if yrfht.is_element_present('button:contains("Accept")'):
                yrfht.uc_click('button:contains("Accept")', reconnect_time=4)
            while ryute.is_element_visible('#injected-channel-player'):
                ryute.sleep(10)
            ryute.quit_extra_driver()
    ryute.sleep(1)
    if is_stream_online("brutalles"):
        url = "https://www.twitch.tv/videos/2490289749"
        ryute.uc_open_with_reconnect(url, 5)
        ryute.uc_gui_click_captcha()
        ryute.sleep(10)
        ryute.uc_gui_handle_captcha()
        ryute.sleep(10)
        if ryute.is_element_present('button:contains("Accept")'):
            ryute.uc_click('button:contains("Accept")', reconnect_time=4)
        url = "https://www.twitch.tv/brutalles"
        ryute.uc_open_with_reconnect(url, 5)
        if ryute.is_element_present('button:contains("Accept")'):
            ryute.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            yrfht = ryute.get_new_driver(undetectable=True)
            yrfht.uc_open_with_reconnect(url, 5)
            ryute.sleep(10)
            if yrfht.is_element_present('button:contains("Accept")'):
                yrfht.uc_click('button:contains("Accept")', reconnect_time=4)
            while ryute.is_element_visible(input_field):
                ryute.sleep(10)
            ryute.quit_extra_driver()
    ryute.sleep(1)

