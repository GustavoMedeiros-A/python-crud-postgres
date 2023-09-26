# import pytest
# from app import create_app


# @pytest.fixture
# def app():
#     app = create_app()
#     client = app.test_client()
#     yield client


# def test_get_all_users(app):
#     response = app.get('/api/users')
#     assert response.status_code == 200

# def test_create_user(app):
#     user_data = {
#         "name": "mario",
#         "email": "mario@gmail.com",
        
#     }
