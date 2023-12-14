# signals.py

import logging
from django.db.models.signals import post_save,pre_delete,post_delete
from django.dispatch import receiver
from modelType.models import Lesson

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Lesson)
def lesson_created_handler(sender, instance, **kwargs):
    # Check if the instance is newly created
    if kwargs.get('created', False):
        course_name = instance.course.name
        success_message = f"Lesson '{instance.title}' created for course '{course_name}'."
        logger.info(success_message)


@receiver(post_delete,sender=Lesson)
def post_delete(sender,**kwargs):
    print(f'You deleted {Lesson.title}')



# Basically postsave and presave chai kaile use huncha vanda after save chai k garni vanera function dina paryo and also pre save ma function define garna milcha