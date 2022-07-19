from django.core.management.base import BaseCommand, CommandError
from main.models import Employee 
from faker import Faker
from django.contrib.auth import get_user_model
import random


User  = get_user_model()

class Command(BaseCommand):
    help = 'Create employee objects'

    

    def handle(self, *args, **options):
        user = User.objects.first()
        
        fake = Faker()
        depts = ["security", "marketing", "tech", "finance"]
        
        for _ in range(10):
            Employee.objects.create(
                name = fake.name(),
                salary = fake.random_number(digits=6),
                linkedin = fake.url(),
                supervisor = user,
                department = random.choice(depts),
                employee_num = fake.random_number(digits=4)
                
            )
        
        
        self.stdout.write(self.style.SUCCESS('Successfully created 10 employees'))