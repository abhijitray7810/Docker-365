FROM jekyll/jekyll:4

# Set working directory inside the container
WORKDIR /srv/jekyll

# Cache gems for faster builds
#COPY site/Gemfile site/Gemfile.lock* ./ || true
COPY site/Gemfile* ./ 
RUN bundle install || true

# Default command (overridden by docker-compose for dev)
CMD ["jekyll", "serve", "--livereload", "--host", "0.0.0.0", "--drafts"]
