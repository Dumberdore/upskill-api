from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.db import get_session
from app.domain.course import CourseCreate, CourseRead
from app.repositories.courses import CourseRepository

router = APIRouter(prefix="/api/v1/courses", tags=["courses"])


def get_course_repository(session: Annotated[Session, Depends(get_session)]) -> CourseRepository:
    return CourseRepository(session)


@router.get("", response_model=list[CourseRead])
def list_courses(
    repository: Annotated[CourseRepository, Depends(get_course_repository)],
) -> list[CourseRead]:
    return [CourseRead.model_validate(course) for course in repository.list()]


@router.post("", response_model=CourseRead, status_code=status.HTTP_201_CREATED)
def create_course(
    course_in: CourseCreate,
    repository: Annotated[CourseRepository, Depends(get_course_repository)],
) -> CourseRead:
    return CourseRead.model_validate(repository.create(course_in))


@router.get("/{course_id}", response_model=CourseRead)
def get_course(
    course_id: UUID,
    repository: Annotated[CourseRepository, Depends(get_course_repository)],
) -> CourseRead:
    course = repository.get(course_id)
    if course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return CourseRead.model_validate(course)
