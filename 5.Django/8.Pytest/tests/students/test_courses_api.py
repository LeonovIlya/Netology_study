import pytest
from django.urls import reverse
from students.models import Course


@pytest.mark.django_db
def test_get_course(api_client, course_factory, student_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=2, students=students)
    url = reverse('courses-detail', args=(courses[0].id,))
    response = api_client.get(url)
    data = response.json()

    assert response.status_code == 200
    assert courses[0].id == data.get('id')
    assert courses[0].name == data.get('name')


@pytest.mark.django_db
def test_get_courses(api_client, course_factory):
    course_factory(_quantity=10)
    url = reverse('courses-list')
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 10


@pytest.mark.django_db
def test_filters_courses_id(api_client, course_factory):
    courses = course_factory(_quantity=5)
    url = reverse('courses-list')
    response = api_client.get(url, data={'id': courses[0].id})
    data = response.json()

    assert response.status_code == 200
    assert courses[0].id == data[0].get('id')


@pytest.mark.django_db
def test_filters_courses_name(api_client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse('courses-list')
    response = api_client.get(url, data={'name': courses[0].name})
    data = response.json()

    print(data)

    assert response.status_code == 200
    assert courses[0].name == data[0].get('name')


@pytest.mark.django_db
def test_create_course(api_client):
    data = {'name': 'Python'}
    url = reverse('courses-list')
    response = api_client.post(url, data=data)

    assert response.status_code == 201
    assert response.data['name'] == 'Python'


@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    data = {'name': 'PHP'}
    courses = course_factory(_quantity=1)
    url = reverse('courses-detail', args=(courses[0].id,))
    response = api_client.patch(url, data=data)

    assert response.status_code == 200
    assert response.data['name'] == 'PHP'


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    courses = course_factory(_quantity=10)
    counts_objects = Course.objects.count()

    url = reverse('courses-detail', args=(courses[0].id,))
    response = api_client.delete(url)

    assert response.status_code == 204
    assert counts_objects - 1 == Course.objects.count()

