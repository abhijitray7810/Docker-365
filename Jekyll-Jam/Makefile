up:
\tdocker compose up --build
down:
\tdocker compose down
new:
\tmkdir -p site && docker run --rm -v $$PWD/site:/srv/jekyll jekyll/jekyll jekyll new . --skip-bundle
clean:
\trm -rf site/_site site/.jekyll-cache
