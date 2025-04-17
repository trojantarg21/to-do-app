import pytest
from app import app  # Import the Flask app

# Test Client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test Home Route (index)
def test_home(client):
    """Test if the homepage loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Buy groceries' in response.data  # Check if a task exists on the page

# Test adding a task
def test_add_task(client):
    """Test if a new task is added correctly"""
    response = client.post('/add', data={'newTask': 'Learn Docker'}, follow_redirects=True)
    assert response.status_code == 200  # Should successfully load the page after redirect
    assert b'Learn Docker' in response.data  # Check if the new task is in the list


# Test completing a task (this deletes it in your code)
def test_complete_task(client):
    """Test if a task is marked as completed (deleted)"""
    client.post('/add', data={'newTask': 'Complete Testing'})
    response = client.post('/complete', data={'taskCheckbox': ['1']})  # Assuming the task 'Complete Testing' is first
    assert response.status_code == 302
    assert b'Complete Testing' not in response.data  # Task should be deleted

# Test deleting a task
def test_delete_task(client):
    """Test if a task is deleted"""
    client.post('/add', data={'newTask': 'Attend meeting'})
    response = client.post('/delete', data={'taskCheckbox': ['1']})  # Delete the first task
    assert response.status_code == 302
    assert b'Attend meeting' not in response.data  # Task should be deleted

# Test that tasks are listed correctly on the homepage
def test_tasks_list(client):
    """Ensure tasks are displayed on the homepage"""
    client.post('/add', data={'newTask': 'Do Laundry'})
    response = client.get('/')
    assert b'Do Laundry' in response.data  # Check if the task is listed on the homepage
