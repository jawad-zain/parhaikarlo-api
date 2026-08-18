from django.db import models

@property
def has_cached_explanation(self):
    return bool(
        self.explanation_short
        and self.explanation_long
        and self.explanation_trick
    )
