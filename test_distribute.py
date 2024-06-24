import data
import distribute
import rich


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


def test_should_distribute():
    users = generate_users(10)
    leads = generate_leads(5)
    assigned_map = {user["id"]: 0 for user in users}
    user_lead_map, res_assigned_map, left_over_lead = distribute.distribute(
        leads, users, assigned_map
    )
    rich.print(
        f" INPUT: \n {users=} {leads=} \n\n OUTPUT: \n {user_lead_map=} {res_assigned_map=}"
    )
    assert user_lead_map == {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    assert len(left_over_lead) == 0
