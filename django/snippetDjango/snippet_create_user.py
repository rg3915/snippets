class Student(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    exstudent = models.BooleanField('ex-aluno', default=False)
    team = models.ForeignKey(Team, null=True, blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_model_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
