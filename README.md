[![michaeljgarlotteii](https://circleci.com/gh/michaeljgarlotteii/personalFlaskBlog.svg?style=svg)](https://github.com/MichaelJGarlotteII/personalFlaskBlog/tree/feature/circle-ci)

HOW THIS WAS MADE
---
This Github repository is the home of the michaeljgarlotteii.com blog/portfolio site created
in python and Flask. In this repository you can find all of the open source code for the site
as well as some detail as to how the site came to be.

I started work on this site to give myself something to do during the worldwide standstill created
by the COVID-19 crisis. I wanted to get more practice with Full-Stack Web Development so I decided
build and host my own web server with python and Flask. I initially followed a YouTube tutorial to
learn many of the basics and get the framework of the site built. That series can be found at the
following url:

[Tutorial Link Here](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)

Once I got the framework built, I wanted to host it. However, I had no previous experience with
domain's or cloud hosting. That sent me to my friend James, who you will see as a collaborator in
this repository. We hosted the site on GCP(Google Cloud Platform) and I got a very cheap domain from
GoDaddy. Before we could get it up and running however, we decided we should Dockerize the web server
so I could get more experience with Docker. After some trials, we got it running and connected to the
domain that it currently resides at, michaeljgarlotteii.com:5000.


SITE DETAILS:
---
- .gitignore: The .gitignore file was a new concept for me in the sense that I had never made one before. I
            quickly learned how it woks after a few mistakes and having to delete unnecessary files every time
            I pushed to a branch.

- dockerfile: This file was interesting to build as we got going on the Dockerization of the server. I contents are
            pretty self-explanatory. This files runs in Docker when you build the server.

- requirements.txt: The requirements text file contains all of the required add-ons for pythons meant to be used when
                  Dockerizing the server. Docker downloads all of the add-ons, then implements them for every build.

- run.py: This file runs the web server and is run locally with Flask run after specifying the Environment Variable
        as run.py. All of that is contained in the dockerfile and run during the Docker side creation of the server.

- flaskBlog directory
      - __init__.py: This file initializes all of the python-side Flask related variables as well as variables from some of the
                   packages we downloaded.

      - forms.py: This file allows all of the forms to function on the site. It's passed to nearly every page where data is taken
                from the user.

      - models.py: This file creates the database models used to enter user data, post data, and upvote data.

      - routes.py: This file is the way Flask organizes the web server. All new pages must have a route otherwise Flask will throw
                 an error if you try to navigate to it. All created pages are currently accounted for in this file.

      - static directory:

           - frontend.js: This is the JavaScript file that does the frontend visuals to display the upvotes on each post.

           - main.css: This is the CSS file created by the author of the YouTube tutorial from above. No changes have been made to this as of yet.

           - profile_pics directory:
               - This directory contains all profile pics that get saved to the site by users. It will be static on GitHub since GitHub doesn't receive new data from the server.

      - templates directory:

           - This directory contains all of the HTML files for the site. layout.html is the detailed layout file for the site
              and is applied to every page to maintain cohesiveness. From there a code block in python/Flask is added and connected
              to every other HTML file to allow them to use the layout code and avoid redundant lines of code.
