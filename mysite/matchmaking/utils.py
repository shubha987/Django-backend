def calculate_similarity(user1, user2):
    # Split the comma-separated strings and convert to sets
    interests1 = set(user1.interests.split(','))
    interests2 = set(user2.interests.split(','))
    preferences1 = set(user1.partner_preferences.split(','))
    preferences2 = set(user2.partner_preferences.split(','))
    events1 = set(user1.event_preferences.split(','))
    events2 = set(user2.event_preferences.split(','))

    # Calculate interests similarity
    common_interests = len(interests1.intersection(interests2))
    total_interests = len(interests1.union(interests2))
    interests_similarity = common_interests / total_interests if total_interests != 0 else 0

    # Calculate partner preferences similarity
    common_preferences = len(preferences1.intersection(preferences2))
    total_preferences = len(preferences1.union(preferences2))
    preferences_similarity = common_preferences / total_preferences if total_preferences != 0 else 0

    # Calculate event preferences similarity
    common_events = len(events1.intersection(events2))
    total_events = len(events1.union(events2))
    events_similarity = common_events / total_events if total_events != 0 else 0

    # Define weights
    interests_weight = 0.4
    preferences_weight = 0.3
    events_weight = 0.3

    # Calculate total compatibility score
    compatibility_score = (
        interests_similarity * interests_weight +
        preferences_similarity * preferences_weight +
        events_similarity * events_weight
    )

    return compatibility_score