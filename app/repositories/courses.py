from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.course import Course, CourseCreate


class CourseRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def list(self) -> list[Course]:
        return list(self.session.scalars(select(Course).order_by(Course.created_at.desc())))

    def get(self, course_id: UUID) -> Course | None:
        return self.session.get(Course, course_id)

    def create(self, course_in: CourseCreate) -> Course:
        course = Course(
            title=course_in.title,
            description=course_in.description,
            level=course_in.level.value,
        )
        self.session.add(course)
        self.session.commit()
        self.session.refresh(course)
        return course
