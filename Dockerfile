FROM snehithaithu/python3_ubuntu18_gpu

COPY . /app
WORKDIR /app/Exam

RUN pip install -r ../requirements.txt

RUN bash ../.env && python manage.py migrate && python manage.py makemigrations && python manage.py migrate

EXPOSE 8000

# ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# docker run -p 8000:8000 -it snehithaithu/exam_portal_django /bin/bash -c "source ../.env ; python manage.py runserver 0.0.0.0:8000"
