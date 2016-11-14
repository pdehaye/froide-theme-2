# -*- coding: utf-8 -*-
import os

from froide.settings import Base, ThemeBase, HerokuPostmark, HerokuPostmarkS3, SSLSite  # noqa


class CustomThemeBase(ThemeBase):
    FROIDE_THEME = 'froide_theme.theme'

    SITE_NAME = "PersonalData.IO"
    SITE_EMAIL = "5d126ec739b2be09ae96e716db80649c@inbound.postmarkapp.com"
    SITE_URL = 'http://beta.PersonalData.IO'

    SECRET_URLS = {
        "admin": "admin-theme",
        "postmark_inbound": "postmark_inbound",
        "postmark_bounce": "postmark_bounce"
    }

    @property
    def LOCALE_PATHS(self):
        return list(super(CustomThemeBase, self).LOCALE_PATHS.default) + [
            os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', "locale")
            )
        ]

    LANGUAGES = (
        ('en', 'English'),
    )


class Dev(CustomThemeBase, Base):
    pass


class ThemeHerokuPostmark(CustomThemeBase, HerokuPostmark):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    
class ThemeSSLHerokuPostmark(ThemeHerokuPostmark, SSLSite):
    SECRET_URLS = {
        "admin": "admin-theme-ssl-heroku-postmark",
        "postmark_inbound": "postmark_inbound",
        "postmark_bounce": "postmark_bounce"
    }

class ThemeHerokuPostmarkS3(CustomThemeBase, HerokuPostmarkS3):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    SECRET_URLS = {
        "admin": "admin-theme-heroku-postmark-s3",
        "postmark_inbound": "postmark_inbound",
        "postmark_bounce": "postmark_bounce"
    }

class ThemeSSLHerokuPostmarkS3(CustomThemeBase, HerokuPostmarkS3, SSLSite):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    SECRET_URLS = {
        "admin": "admin-theme-ssl-heroku-postmark-s3",
        "postmark_inbound": "postmark_inbound",
        "postmark_bounce": "postmark_bounce"
    }


try:
    from .local_settings import *  # noqa
except ImportError:
    pass
