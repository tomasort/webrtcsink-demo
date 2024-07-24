FROM python:3.9.19-alpine3.20
WORKDIR /app

# Enable the 'edge' repository for newer packages
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && apk update

# Install GStreamer and its plugins (including WebRTC and Python bindings)
RUN apk add --no-cache \
    gstreamer \
    gst-plugins-base \
    gst-plugins-good \
    gst-plugins-bad \
    gst-plugins-ugly \
    gst-rtsp-server \
    gst-libav \
    musl-dev \
    cairo-dev \
    pkgconf \
    gcc \
    gst-plugins-rs \
    python3-dev \
    gobject-introspection-dev \
    gstreamer-tools \
    gstreamer-dev \
    g++ \
    libffi-dev

RUN apk add --no-cache libnice-gstreamer

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . /app

CMD ["python3", "test.py"]