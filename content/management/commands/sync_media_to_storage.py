"""
One-time (or repeatable) backfill: upload every local file under MEDIA_ROOT
to whatever storage backend Django is currently configured with — i.e. the
Backblaze B2 bucket, once USE_S3_MEDIA=True and the B2_* vars are set in
.env. Safe to re-run: it skips any file that already exists remotely, and
never touches or deletes anything on local disk.

    python manage.py sync_media_to_storage            # do it
    python manage.py sync_media_to_storage --dry-run  # just list what would upload
"""
import os

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Upload every local file under MEDIA_ROOT to the configured default_storage backend (e.g. Backblaze B2).'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run', action='store_true',
            help='List what would be uploaded without touching the remote storage.',
        )

    def handle(self, *args, **options):
        if not getattr(settings, 'USE_S3_MEDIA', False):
            raise CommandError(
                'USE_S3_MEDIA is not enabled in settings — set the B2_* vars and '
                'USE_S3_MEDIA=True in .env first. Otherwise this would just walk '
                'local disk with local disk as the destination too.'
            )

        media_root = settings.MEDIA_ROOT
        if not os.path.isdir(media_root):
            raise CommandError(f'MEDIA_ROOT does not exist locally: {media_root}')

        dry_run = options['dry_run']
        uploaded = skipped = 0

        for dirpath, _dirnames, filenames in os.walk(media_root):
            for filename in filenames:
                local_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(local_path, media_root).replace(os.sep, '/')

                if default_storage.exists(rel_path):
                    skipped += 1
                    continue

                if dry_run:
                    self.stdout.write(f'Would upload: {rel_path}')
                    uploaded += 1
                    continue

                with open(local_path, 'rb') as fh:
                    default_storage.save(rel_path, ContentFile(fh.read()))
                self.stdout.write(f'Uploaded: {rel_path}')
                uploaded += 1

        self.stdout.write(self.style.SUCCESS(
            f'Done. Uploaded {uploaded}, skipped {skipped} (already present remotely).'
        ))
