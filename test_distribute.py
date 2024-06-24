import data
import distribute


def generate_users(size: int) -> list[data.User]:
    users: list[data.User] = []
    for i in range(size):
        users.append(
            {
                "id": i,
                "name": f"user{i}",
                "email": f"email{i}",
                "phone": f"phone{i}",
                "daily_max": 1,
            }
        )
    return users


def generate_leads(size: int) -> list[data.LeadUser]:
    leads: list[data.LeadUser] = []
    for i in range(size):
        leads.append(
            {
                "id": i,
                "name": f"lead{i}",
                "email": f"email{i}",
                "phone": f"phone{i}",
            }
        )
    return leads


SIZE = 100


def test_should_distribute():
    users = generate_users(SIZE)
    leads = generate_leads(SIZE)
    assigned_map = {user["id"]: 0 for user in users}
    user_lead_map, res_assigned_map, left_over_lead = distribute.distribute(
        leads, users, assigned_map
    )
    assert user_lead_map == {i: i for i in range(SIZE)}
    assert len(left_over_lead) == 0


def test_should_distribute_rec():
    users = generate_users(SIZE)
    leads = generate_leads(SIZE)
    assigned_map = {user["id"]: 0 for user in users}
    user_lead_map, res_assigned_map, left_over_lead = distribute.distribute_rec(
        leads, users, assigned_map
    )
    assert user_lead_map == {i: i for i in range(SIZE)}
    assert len(left_over_lead) == 0
