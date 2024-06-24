from typing import TypedDict
import random


class LeadUser(TypedDict):
    id: int
    name: str
    email: str
    phone: str


class User(TypedDict):
    id: int
    name: str
    email: str
    phone: str
    daily_max: int


def get_currently_assigned_count(user: list[User]) -> dict[int, int]:
    return {u["id"]: random.randint(0, u["daily_max"]) for u in user}


lead_list: list[LeadUser] = [
    {
        "id": 1,
        "name": "lead1",
        "email": "lead1@lead1",
        "phone": "11111111111",
    },
    {
        "id": 2,
        "name": "lead2",
        "email": "lead2@lead2",
        "phone": "22222222222",
    },
    {
        "id": 3,
        "name": "lead3",
        "email": "lead3@lead3",
        "phone": "33333333333",
    },
    {
        "id": 4,
        "name": "lead4",
        "email": "lead4@lead4",
        "phone": "44444444444",
    },
    {
        "id": 5,
        "name": "lead5",
        "email": "lead5@lead5",
        "phone": "55555555555",
    },
    {
        "id": 6,
        "name": "lead6",
        "email": "lead6@lead6",
        "phone": "66666666666",
    },
    {
        "id": 7,
        "name": "lead7",
        "email": "lead7@lead7",
        "phone": "77777777777",
    },
    {
        "id": 8,
        "name": "lead8",
        "email": "lead8@lead8",
        "phone": "88888888888",
    },
    {
        "id": 9,
        "name": "lead9",
        "email": "lead9@lead9",
        "phone": "99999999999",
    },
    {
        "id": 10,
        "name": "lead10",
        "email": "lead10@lead10",
        "phone": "10101010101",
    },
]

user_list: list[User] = [
    {
        "id": 1,
        "name": "user1",
        "email": "user1@user1",
        "phone": "11111111111",
        "daily_max": 3,
    },
    {
        "id": 2,
        "name": "user2",
        "email": "user2@user2",
        "phone": "22222222222",
        "daily_max": 2,
    },
    {
        "id": 3,
        "name": "user3",
        "email": "user3@user3",
        "phone": "33333333333",
        "daily_max": 4,
    },
    {
        "id": 4,
        "name": "user4",
        "email": "user4@user4",
        "phone": "44444444444",
        "daily_max": 1,
    },
    {
        "id": 5,
        "name": "user5",
        "email": "user5@user5",
        "phone": "55555555555",
        "daily_max": 6,
    },
]
