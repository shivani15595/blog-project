# blog-project
Blog web application

This is a Blogging Application to view/create/update and delete blog posts.

The home page shows list view of posts, with Title, Body, Author and an auto generated Date field.
The About page gives a brief about the Blog.
We can view the post details and update the fields or delete the post, by clicking on Post details button.
We can also create new posts by clicking on the 'Create New Post' option.

-------------------------------------------------------------------------------------------------------------------------------------
To run application using Docker :

Clone the project in a directory.
In terminal, go to the directory (<directory_path>/blog-project/mysite).
Run command : docker-compose up
Open 0.0.0.0:8000 in the browser, once the docker build is completed.

To stop the project :
Use Command : docker-compose down

----------------------------------------------------------------------------------------------------------------------------------------

To view the app without docker :

Clone/Download Repository.
Open Terminal and go to the correct folder (/blog-project/mysite)
In the terminal, type : 
mysite>python manage.py runserver
The application will start in browser at http://127.0.0.1:8000/ by default.

We can change the server as such :
python manage.py runserver 8080

 
