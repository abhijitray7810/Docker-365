FROM nginx:alpine

# Remove the default nginx index.html
RUN rm /usr/share/nginx/html/index.html

# Copy your index.html to the nginx html directory
COPY index.html /usr/share/nginx/html/index.html