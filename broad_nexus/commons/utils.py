import random
from account.models import UserAccountActivationKey
def get_random_key(size):
    alphabets = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    key = ''
    for _ in range(size):
        key += random.choice(alphabets)
    return key

def get_base_url(request):
    return "".join([f'{request.scheme}://', f'{request.get_host()}/'])

def send_account_activation_mail(request, user):
    key = get_random_key(50)
    base_url = get_base_url(request)
    full_url = "".join([base_url, "account/activate/", f'{user.username.hex}/', f'{key}/'])
    subject = "User Account Activation"
    message = f"""
    hello {user.get_full_name()}.Please click on this link to activate your account 
    {full_url}
    """
    from_email = "nishanrai@gmail.com"
    user.email_user(subject=subject, message=message, from_email=from_email)
    UserAccountActivationKey.objects.create(user=user, key=key)



def is_profile_complete(user):
    try:
        profile = user.userprofile
    except:
        return False
    return all([user.account_activated, profile.phone_number, profile.address, profile.resume])