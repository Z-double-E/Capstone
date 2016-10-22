from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser

DIFFICULTY_CHOICES = (
    ("", ""),
    ("EASY", "Easy"),
    ("MEDIUM", "Medium"),
    ("HARD", "Hard"),
)

STATUS = (
    ("", ""),
    ("MODIFIED", "Modified"),
    ("ORIGINAL", "Original"),
)

PRO_SOL_PARA = (
    ("", ""),
    ("Complete Search","Complete Search"),
    ("Divide and Conquer","Divide and Conquer"),
    ("Dynamic Programming","Dynamic Programming"),
    ("Greedy","Greedy"),
)

DATA_STRUCTURES = (
    ("", ""),
    ("Linear DS", "Linear DS"),
    ("Non-Linear DS", "Non-Linear DS"),
)

TYPE_CHOICES = (
    ("", ""),
    ("Computational Geometry", (
            ("Basic Gemometry Objects","Basic Gemometry Objects"),
            ("Algorithm on Polygon","Algorithm on Polygon"),
        )
    ),
    ("Graph",  (
            ("Graph Traversal","Graph Traversal"),
            ("Minimum Spanning Tree","Minimum Spanning Tree"),
            ("Shortest Paths","Shortest Paths"),
            ("Network Flow","Network Flow"),
            ("Special Graph","Special Graph"),

        )
    ),
    ("Mathematics",  (
            ("Ad Hoc Maths Problem","Ad Hoc Maths Problem"),
            ("Combinatorics","Combinatorics"),
            ("Probability","Probability"),
            ("Cycle-Finding","Cycle-Finding"),
            ("Number Theory","Number Theory"),
            ("Game Theory","Game Theory"),
        )
    ),
    ("String Processing",  (
            ("Ad Hoc String Problem","Ad Hoc String Problem"),
            ("String Matching","String Matching"),
            ("Suffix Trie/Tree/Array","Suffix Trie/Tree/Array"),
        )
    ),
)


##Problem class
class Problem(models.Model):
    
    name = models.CharField(max_length=255)

    url = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='')
    problemSP = models.CharField(max_length=255, choices=PRO_SOL_PARA, default='')
    wused = models.CharField(max_length=255)
    surl = models.CharField(max_length=255)
    dp = models.CharField(max_length=255, choices=DATA_STRUCTURES, default='')
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default='')
    created = models.DateField(default=timezone.now)
    hasSolution = models.BooleanField(default = False)
    Noviews = models.IntegerField(default = 0)

    #method to set date created automaticlly
    def save(self, *args, **kwargs):
        auto_now = kwargs.pop('update_auto_now', True)
        if auto_now:
            self.updated = timezone.now()
        super(Problem,self).save(*args, **kwargs)

    #method to ruturn name of problem as a string
    def __str__(self):
        return self.name


#Problem set classes
class ProblemSet(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateField(default=timezone.now) # date created which is set to automaticaly on the day problem was added.
    problems = models.ManyToManyField(Problem)
    Noviews = models.IntegerField(default = 0)
    wused = models.CharField(max_length=255)

    #method to set date created automaticlly
    def save(self, *args, **kwargs):
        auto_now = kwargs.pop('update_auto_now', True)
        if auto_now:
            self.updated = timezone.now()
        super(ProblemSet,self).save(*args, **kwargs)
    
    #method to ruturn name of problemSet as a string
    def __str__(self):
        return self.name