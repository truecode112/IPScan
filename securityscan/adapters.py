from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        
        # Save the email from the social account to the user model
        if sociallogin.account.provider == 'github':
            user.email = sociallogin.account.extra_data.get('email')
            user.save()
            
        return user
