"""API tests using Playwright's built-in request context.
No browser needed for these -- same CRUD validation approach used
with Postman, just automated and version-controlled.
"""
from playwright.sync_api import APIRequestContext


BASE_URL = "https://reqres.in/api"


def test_get_users_returns_200_and_data(request_context: APIRequestContext):
    response = request_context.get(f"{BASE_URL}/users?page=2")
    assert response.ok
    body = response.json()
    assert len(body["data"]) > 0
    assert "email" in body["data"][0]


def test_get_single_user_returns_correct_id(request_context: APIRequestContext):
    response = request_context.get(f"{BASE_URL}/users/2")
    assert response.status == 200
    body = response.json()
    assert body["data"]["id"] == 2


def test_get_nonexistent_user_returns_404(request_context: APIRequestContext):
    response = request_context.get(f"{BASE_URL}/users/23")
    assert response.status == 404


def test_create_user_returns_201(request_context: APIRequestContext):
    response = request_context.post(
        f"{BASE_URL}/users",
        data={"name": "Devansh", "job": "QA Automation Engineer"},
    )
    assert response.status == 201
    body = response.json()
    assert body["name"] == "Devansh"
    assert "id" in body


def test_update_user_returns_200(request_context: APIRequestContext):
    response = request_context.put(
        f"{BASE_URL}/users/2",
        data={"name": "Devansh", "job": "Senior QA Engineer"},
    )
    assert response.status == 200
    body = response.json()
    assert body["job"] == "Senior QA Engineer"


def test_delete_user_returns_204(request_context: APIRequestContext):
    response = request_context.delete(f"{BASE_URL}/users/2")
    assert response.status == 204
