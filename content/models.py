from django.db import models


class Exam(models.Model):
    """Top of the content hierarchy. MDCAT, ECAT, NUMS, etc.

    This platform is entry-test-only — Matric/FSc board-curriculum content
    lives on a separate site, not here.
    """

    BOARD_CHOICES = [
        ('PMDC', 'PMDC (Pakistan Medical & Dental Council)'),
        ('FBISE', 'Federal Board'),
        ('Punjab', 'Punjab Board'),
        ('Sindh', 'Sindh Board'),
        ('KP', 'KP Board'),
        ('Cambridge', 'Cambridge International'),
        # Entry tests run by the admitting body itself, not a curriculum
        # board — NUMS, ECAT, and individual university admission tests
        # (10+ planned alongside MDCAT/NUMS/ECAT) all land here.
        ('University', 'University / Admitting Body'),
    ]

    LEVEL_CHOICES = [
        ('entry-test', 'Entry Test'),
        ('o-level', 'O-Level'),
        ('a-level', 'A-Level'),
    ]

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    board = models.CharField(max_length=20, choices=BOARD_CHOICES, blank=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Subject(models.Model):
    """A subject inside an exam. e.g. Biology under MDCAT."""

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name='subjects',
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    # For MDCAT dashboards / question distribution.
    # Biology=34, Chemistry=27, Physics=27, English=9, Logical Reasoning=3.
    weight_percent = models.PositiveSmallIntegerField(default=0)

    # Number of questions this subject contributes in the real exam.
    # Bio=68, Chem=54, etc.
    question_count = models.PositiveSmallIntegerField(default=0)

    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['exam', 'order', 'name']
        unique_together = [('exam', 'slug'), ('exam', 'name')]

    def __str__(self):
        return f"{self.exam.name} — {self.name}"


class Topic(models.Model):
    """A topic inside a subject. e.g. Genetics under Biology."""

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='topics',
    )
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['subject', 'order', 'name']
        unique_together = [('subject', 'slug'), ('subject', 'name')]

    def __str__(self):
        return f"{self.subject.name} — {self.name}"


class Subtopic(models.Model):
    """A subtopic inside a topic. e.g. Mendelian Inheritance under Genetics."""

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='subtopics',
    )
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['topic', 'order', 'name']
        unique_together = [('topic', 'slug'), ('topic', 'name')]

    def __str__(self):
        return f"{self.topic.name} — {self.name}"


class PastPaper(models.Model):
    """A past exam paper. e.g. MDCAT 2023."""

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name='past_papers',
    )
    name = models.CharField(max_length=100)  # e.g. "MDCAT 2023"
    slug = models.SlugField(max_length=100)
    year = models.PositiveSmallIntegerField()

    # Free papers are accessible on the free tier and get free AI explanations.
    is_free = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['exam', '-year']
        unique_together = [
            ('exam', 'slug'),
            ('exam', 'year', 'name'),
        ]

    def __str__(self):
        return f"{self.exam.name} — {self.name}"


class Question(models.Model):
    """One MCQ. Attached to a Subtopic (required) and optionally a PastPaper."""

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    CORRECT_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    # Content hierarchy — Subtopic gives us Topic, Subject, Exam by walking up.
    subtopic = models.ForeignKey(
        Subtopic,
        on_delete=models.PROTECT,
        related_name='questions',
    )

    # Nullable — practice-only questions don't belong to a paper.
    past_paper = models.ForeignKey(
        PastPaper,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='questions',
    )

    question_text = models.TextField()
    option_a = models.CharField(max_length=500)
    option_b = models.CharField(max_length=500)
    option_c = models.CharField(max_length=500)
    option_d = models.CharField(max_length=500)
    correct_answer = models.CharField(
        max_length=1,
        choices=CORRECT_CHOICES,
    )

    # Original question number/order inside the past paper.
    # Example: MDCAT 2014 Biology starts at 133 and ends at 220.
    # Practice-only questions can leave this blank.
    paper_order = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        db_index=True,
    )

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default='medium',
    )

    # Cached AI explanation — filled on first "Explain" tap, reused forever after.
    # Layers 1+2 come from ONE Groq call returning
    # {short, long, trick} JSON; we split it into three fields
    # for easy admin editing + partial invalidation.
    explanation_short = models.TextField(
        blank=True,
        default='',
    )  # Layer 1 — margin note (~40 words)

    explanation_long = models.TextField(
        blank=True,
        default='',
    )  # Layer 2 — full breakdown (~120 words)

    explanation_trick = models.TextField(
        blank=True,
        default='',
    )  # Layer 2 — mnemonic / memory trick

    explanation_generated_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    # Layer 3 — per-option breakdown: why each of a/b/c/d is right or wrong.
    # {"a": "...", "b": "...", "c": "...", "d": "..."}
    # Generated + cached in the same Groq call as short/long/trick.
    explanation_options = models.JSONField(
        blank=True,
        default=dict,
    )

    # Content verifier tutor flips this to True after reviewing.
    # Frontend only serves is_verified=True questions
    # to real students in production.
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_visual_required = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(
                fields=['subtopic', 'difficulty'],
            ),
            models.Index(
                fields=['past_paper'],
            ),
            models.Index(
                fields=['past_paper', 'paper_order'],
            ),
        ]

    def __str__(self):
        return f"[{self.subtopic}] {self.question_text[:60]}..."

    @property
    def has_cached_explanation(self):
        """True if we've already generated + cached the AI explanation."""
        return bool(
            self.explanation_short
            and self.explanation_long
            and self.explanation_options
            and all(
                self.explanation_options.get(letter)
                for letter in ('a', 'b', 'c', 'd')
            )
        )


class QuestionImage(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='images',
    )

    image = models.ImageField(
        upload_to='question_images/',
    )

    source_name = models.CharField(
        max_length=200,
        blank=True,
    )

    source_year = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    page_number = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'Image for Question {self.question_id}'


class ConceptNote(models.Model):
    """A short syllabus note per Topic. Feeds the Syllabus tab AND the RAG index.

    Kept at Topic level (not Subtopic) — matches how MDCAT students think
    about revision ('read the Genetics note') and keeps the RAG corpus
    at a reasonable size.
    """

    topic = models.OneToOneField(
        Topic,
        on_delete=models.CASCADE,
        related_name='concept_note',
    )
    title = models.CharField(max_length=200)

    # Markdown allowed — rendered on frontend, chunked + embedded for RAG.
    body = models.TextField()

    # Bumped whenever body is edited — used to invalidate the RAG embedding.
    version = models.PositiveIntegerField(default=1)

    # True once embedded into FAISS.
    is_indexed = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['topic__subject', 'topic__order']

    def __str__(self):
        return f"Note: {self.topic}"
    