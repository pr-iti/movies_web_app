from rest_framework.throttling import UserRateThrottle

class ReviewCreateThrottle(UserRateThrottle):
    """
    Custom throttle for review creation
    Limits users to 3 review creations per day
    """
    scope = 'review-create'

class ReviewListThrottle(UserRateThrottle):
    """
    Custom throttle for review listing
    """
    scope = 'review-list'
