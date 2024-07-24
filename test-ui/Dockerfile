# Use a base image with a web server (Nginx in this example)
FROM nginx:alpine

# Copy your application files to the web server's root directory
COPY index.html /usr/share/nginx/html/
COPY gstwebrtc-api-2.0.0.min.js /usr/share/nginx/html/
COPY gstwebrtc-api-2.0.0.min.js.map /usr/share/nginx/html/

# Expose port 80 (or whichever port your signaling server is listening on)
EXPOSE 80
