def unique_users(events):
    unique_users_set = set()
    for event in events:
        unique_users_set.add(event.user_id)
    return unique_users_set