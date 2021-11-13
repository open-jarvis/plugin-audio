"""
Copyright (c) 2021 Philipp Scheer
"""


import pyaudio

from jarvis_sdk import Storage
from jarvis_sdk.struct.Controls import AudioDevice, AudioInformation


pa = pyaudio.PyAudio()


class Audio:
    @staticmethod
    def mapDevice(dev) -> AudioDevice:
        return AudioDevice(
                type="input" if dev["maxInputChannels"] > 0 else "output",
                index=dev["index"],
                name=dev["name"],
                channels=dev["maxInputChannels"] if dev["maxInputChannels"] > 0 else dev["maxOutputChannels"],
                rate=dev["defaultSampleRate"]
            )

    @staticmethod
    def getAvailableInputs() -> list:
        devs: list = []
        for i in range(pa.get_device_count()):
            devs.append(Audio.mapDevice(pa.get_device_info_by_index(i)))
        return [_ for _ in devs if _.type == "input"]
    
    @staticmethod
    def getAvailableOutputs() -> list:
        devs: list = []
        for i in range(pa.get_device_count()):
            devs.append(Audio.mapDevice(pa.get_device_info_by_index(i)))
        return [_ for _ in devs if _.type == "output"]

    @staticmethod
    def setDefaultInput(index: int):
        Storage.set("default-input", index)

    @staticmethod
    def getDefaultInput() -> AudioDevice:
        index = Storage.get("default-input", None)
        if index is None:
            try:
                return Audio.mapDevice(pa.get_default_input_device_info())
            except OSError: # no default input device available
                return None
        return Audio.mapDevice(pa.get_device_info_by_index(index))

    @staticmethod
    def setDefaultOutput(index: int):
        Storage.get("default-output", index)

    @staticmethod
    def getDefaultOutput() -> list:
        index = Storage.get("default-output", None)
        if index is None:
            try:
                return Audio.mapDevice(pa.get_default_output_device_info())
            except OSError: # no default input device available
                return None
        return Audio.mapDevice(pa.get_device_info_by_index(index))

    @staticmethod
    def info() -> AudioInformation:
        return AudioInformation(
            available_inputs=Audio.getAvailableInputs(),
            default_input=Audio.getDefaultInput(),
            available_outputs=Audio.getAvailableOutputs(),
            default_output=Audio.getDefaultOutput()
        )

