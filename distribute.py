from collections.abc import Callable, Iterable
from typing import TypeVar
import data
import random
import time

BATCH_SIZE = 4
POINTER = 0


class DistributeMetrics:
    _pointer = 0

    @property
    def pointer(self):
        return self._pointer

    @pointer.setter
    def pointer(self, value):
        self._pointer = value

    def reset(self):
        self._pointer = 0


def is_user_available(user: data.User):
    return random.random() < 0.5


def can_assign(user: data.User, assigned_map: dict[int, int]):
    return assigned_map[user["id"]] < user["daily_max"]


def choose_user(users: list[data.User], assigned: dict[int, int], pointer: int):
    index = (pointer + 1) % len(users)
    user = users[index]
    if not is_user_available(user):
        return None
    if not can_assign(user, assigned):
        return None
    return user, index


T = TypeVar("T")


def pick_til_defined(
    iterable: Iterable[T], cb: Callable[[T], bool]
) -> tuple[T, int] | None:
    for index, item in enumerate(iterable):
        if cb(item):
            return item, index
    return None


def distribute(
    lead_batch: list[data.LeadUser],
    users: list[data.User],
    assigned_map: dict[int, int],
) -> tuple[dict[int, int], dict[int, int], list[data.LeadUser]]:
    metrics = DistributeMetrics()
    lead_user_map: dict[int, int] = {}
    left_over_lead: list[data.LeadUser] = []
    for lead in lead_batch:
        potential_user = pick_til_defined(
            users,
            lambda user: is_user_available(user) and can_assign(user, assigned_map),
        )
        if potential_user is None:
            print("Cannot assign to users...")
            left_over_lead.append(lead)
            continue
        user, index = potential_user
        lead_user_map[user["id"]] = lead["id"]
        assigned_map[user["id"]] += 1
        metrics.pointer = index
    return lead_user_map, assigned_map, left_over_lead


def batch_data(lead: list[data.LeadUser], size: int):
    return random.choices(lead, k=size)


if __name__ == "__main__":
    batch = batch_data(data.lead_list, BATCH_SIZE)
    start = time.time()
    lead_user_map, assigned_map, left_over_lead = distribute(
        batch, data.user_list, data.get_currently_assigned_count(data.user_list)
    )
    print(
        f"Lead user map: {lead_user_map}\nLeft over lead: {left_over_lead}\nAssigned map: {assigned_map}"
    )
    end = time.time()
    print(f"Time taken: {end - start}")
