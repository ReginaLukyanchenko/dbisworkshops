INSERT INTO "STUDENT_PRESENCE" (
    lesson_id,
    student_id,
    presence_date,
    presence,
    teacher_id
) VALUES (
    (select lesson_id from lesson
    where lesson.discipline_number = (select discipline_number from discipline
    where discipline_name = 'English' ) and week_day = '5'),
    (select student_id from student
    where student.id_code = (select id_code from check_in_user
    where last_name = 'Lukianchenko' and first_name = 'Rehina')),
    TO_DATE('2018-11-23 00:00:00', 'YYYY-MM-DD HH24:MI:SS'),
    '0',
    '4'
);
