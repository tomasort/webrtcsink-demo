import sys
import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstWebRTC', '1.0')
from gi.repository import Gst, GstWebRTC, GLib

Gst.init(None)

def create_pipeline():
    # Create the pipeline directly with a multiline string
    pipeline = Gst.parse_launch("""
        uridecodebin uri=file:///app/test.mp4 name=demux 
        webrtcsink signaller::uri=ws://signaling-server:8443 name=ws meta="meta,name=gst-stream"
        demux. ! queue ! videoconvert ! video/x-raw ! queue ! ws. 
        demux. ! queue ! audioconvert ! audioresample ! audio/x-raw ! queue ! ws.
    """)

    # Set up bus message handling
    loop = GLib.MainLoop()
    bus = pipeline.get_bus()
    bus.add_signal_watch()
    bus.connect("message", bus_call, loop)

    # Start playing the pipeline
    pipeline.set_state(Gst.State.PLAYING)
    try:
        loop.run()
    except KeyboardInterrupt:  # Catch Ctrl+C for graceful exit
        pass
    finally:
        pipeline.set_state(Gst.State.NULL)  # Ensure pipeline cleanup

# Bus message callback
def bus_call(bus, message, loop):
    t = message.type
    if t == Gst.MessageType.EOS:
        print("End-of-stream")
        loop.quit()
    elif t == Gst.MessageType.ERROR:
        err, debug = message.parse_error()
        print(f"Error: {err} {debug}")
        loop.quit()
    return True

# Main execution
if __name__ == '__main__':
    create_pipeline()
