def unique_users(rows):
    unique_users_set = {}
    for row in rows:
        unique_users_set.add(row[1])
    return unique_users_set