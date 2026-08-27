from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


def robots_txt(request):
    # This is the API host (api.parhaikrlo.com) — no page here is meant to
    # be crawled or indexed; the real robots.txt/sitemap live on the
    # frontend (www.parhaikrlo.com). Blanket-disallow so bots stop wasting
    # crawl budget (and hits) probing this host for /.env etc.
    return HttpResponse("User-agent: *\nDisallow: /\n", content_type="text/plain")


urlpatterns = [
    path('robots.txt', robots_txt),
    path('admin/founder/', include('founder.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/content/', include('content.urls')),        # ← NEW
    path('api/quiz/', include('quiz.urls')),
    path('api/ai/', include('ai_tutor.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )