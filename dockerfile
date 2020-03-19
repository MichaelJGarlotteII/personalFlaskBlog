FROM python
COPY . /blog
WORKDIR /blog
RUN pip install -r requirements.txt
ENV FLASK_APP='run.py'
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]