# Student Enrollment API

#### Calls

#### Student
GET All Students
>    GET /student/

GET Student By ID
>    GET /student/<int:id>

POST Student (Create Student)
> POST /student/\
> body - {name: <student_name>}

PUT Student (Update Student)
> PUT /student/<int:id>\
> body - {name: <student_name>}

DELETE Student (Delete Student)
> DELETE /student/<int:id>


#### Course
GET All Courses
>    GET /course/

GET Course By ID
>    GET /course/<int:id>

POST Course (Create Course)
> POST /course/\
> body - {title: <course_title>}

PUT Course (Update Course)
> PUT /course/<int:id>\
> body - {title: <course_title>}

DELETE Course (Delete Course)
> DELETE /course/<int:id>


#### Enrollment
GET All Enrollments (Students in Courses)
>    GET /enroll/

GET Enrollment By ID
>    GET /enroll/<int:id>

POST Enrollment (Create Enrollment)
> POST /enroll/\
> body - {student_id: <student_id>, course_id: <course_id>}

PUT Enrollment (Update Enrollment)
> PUT /enroll/<int:id>\
> body - {student_id: <student_id>, course_id: <course_id>}

DELETE Enrollment (Delete Enrollment)
> DELETE /enroll/<int:id>

#### Search
GET Student By Name
>   GET /student/search/
>   Parameters - {name: <student_name>}

GET Course By Title
>   GET /course/search/
>   Parameters - {title: <course_title>}

GET Course By Start Date
>   GET /course/search/
>   Parameters - {start_date: <course_start_date>}

GET Enrollments by Student ID (All Courses Student is Enrolled in)
>   GET /enroll/search/
>   Parameters - {student: <student_id>}

GET Enrollments by Course ID (All Students Enrolled in Course)
>   GET /enroll/search/
>   Parameters - {course: <course_id>}