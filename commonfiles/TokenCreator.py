from rest_framework_simplejwt.tokens import AccessToken


def generate_token(user):
    token=AccessToken(user)
    return token
    