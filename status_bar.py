from i3pystatus import Status

status = Status()

status.register("clock",
                format="%a %-d %b %X KW%V")

status.register("pulseaudio",
    format="♪{volume}",)

status.register("load")

status.run()
