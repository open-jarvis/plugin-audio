"""
Copyright (c) 2021 Philipp Scheer
"""


from jarvis_sdk import Router

from endpoints.Audio import Audio


@Router.on("info")
def get_audio_info():
    return Audio.info().json()
