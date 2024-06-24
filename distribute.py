from collections.abc import Callable, Iterable
from typing import TypeVar
import data
import random

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
    return True


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


def sort_with_pointer(
    users: list[data.LeadUser], pointer: int
) -> list[data.LeadUser]: ...


def get_available_users(users: list[data.User]):
    return filter(is_user_available, users)


def distribute(
    lead_batch: list[data.LeadUser],
    users: list[data.User],
    assigned_map: dict[int, int],
) -> tuple[dict[int, int], dict[int, int], list[data.LeadUser]]:
    """
    ### Before distribute is called
    - available `users` must be filtered out and sorted in ascending order but starting
      from the `pointer`

    The responsibility of managing pointers and the users accordingly will be out of scope
    for this function.
    It will just store the last assigned user by updating the POINTER
    """
    metrics = DistributeMetrics()
    lead_user_map: dict[int, int] = {}
    left_over_lead: list[data.LeadUser] = []
    for lead in lead_batch:
        potential_user = pick_til_defined(
            users,
            lambda user: can_assign(user, assigned_map),
        )
        if potential_user is None:
            print("Cannot assign to users...")
            left_over_lead.append(lead)
            continue
        user, index = potential_user
        lead_user_map[user["id"]] = lead["id"]
        assigned_map[user["id"]] += 1
        metrics.pointer = index
    # INFO: Store the last assigned users
    return lead_user_map, assigned_map, left_over_lead


def distribute_rec(
    lead_batch: list[data.LeadUser],
    users: list[data.User],
    assigned_map: dict[int, int],
    user_lead_map: dict[int, int] = {},
) -> tuple[dict[int, int], dict[int, int], list[data.LeadUser]]:
    if len(lead_batch) == 0:
        return user_lead_map, assigned_map, []
    if len(users) == 0:
        print("No more users left")
        return user_lead_map, assigned_map, lead_batch
    first_lead = lead_batch[0]
    first_user = users[0]
    if can_assign(first_user, assigned_map):
        user_lead_map[first_user["id"]] = first_lead["id"]
        assigned_map[first_user["id"]] += 1
        lead_batch.pop(0)
        distribute_rec(lead_batch, users, assigned_map, user_lead_map)
    else:
        users.pop(0)
        distribute_rec(lead_batch, users, assigned_map, user_lead_map)
    return user_lead_map, assigned_map, lead_batch
