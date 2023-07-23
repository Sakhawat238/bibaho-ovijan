from django.db import models
from AUTH.UserAuthentication.models import User


class MaritalStatus(models.TextChoices):
    NEVER_MARRIED = "Never Married"
    MARRIED = "Married"
    WIDOWED = "Widowed"
    AWAITING_DIVORCE = "Awaiting Divorce"
    DIVORCED = "Divorced"
    ANULLED = "Anulled"

class ReligionType(models.TextChoices):
    MUSLIM = "Muslim"
    HINDU = "Hindu"
    CHRISTIAN = "Christian"
    BUDDHIST = "Biddhist"
    OTHER = "Other"

class ComplexionType(models.TextChoices):
    FAIR = "Fair"
    VERY_FAIR = "Very Fair"
    WHEATISH = "Wheatish"
    BROWN = "Brown"
    DARK = "Dark"

class ResidentialStatus(models.TextChoices):
    CITIZEN = "Citizen"
    PERMANENT_RESIDENT = "Permanent Resident"
    WORK_PERMIT = "Work Permit"
    STUDENT_VISA = "Student Visa"

class EmploymentType(models.TextChoices):
    GOVERNMENT = "Government"
    PRIVATE = "Private"
    BUSINESS = "Business"
    DEFENCE = "Defence"
    SELF_EMPLOYED = "Self Employed"
    NOT_WORKING = "Not Working"

class FamilyType(models.TextChoices):
    JOINT = "Joint"
    NUCLEAR = "Nuclear"

class FamilyStatus(models.TextChoices):
    LOWER_CLASS = "Lower Class"
    MIDDLE_CLASS = "Middle Class"
    UPPER_MIDDLE_CLASS = "Upper-Middle Class"
    UPPER_CLASS = "Upper Class"

class FamilyValue(models.TextChoices):
    TRADITIONAL = "Traditional"
    MODERATE = "Moderate"
    LIBERAL = "Liberal"

class BodyType(models.TextChoices):
    SLIM = "Slim"
    ATHLETIC = "Athletic"
    AVERAGE = "Average"
    HEAVY = "Heavy"

class EatingHabit(models.TextChoices):
    VEGETARIAN = "Vegetarian"
    VEGAN = "Vegan"
    NON_VEGETARIAN = "Non Vegetarian"

class DrinkingHabit(models.TextChoices):
    NO = "No"
    YES = "Yes"
    OCCASIONALLY = "Occasionally"

class SmokingHabit(models.TextChoices):
    NO = "No"
    YES = "Yes"
    OCCASIONALLY = "Occasionally"


class Profile(models.Model):
    code = models.CharField(max_length=20,null=False,unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    is_archived = models.BooleanField(default=False)
    
    def __str__(self):
        return self.code

    class Meta:
        db_table = 'matrimony_profile'


class BasicInformation(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50, default="")
    date_of_birth = models.DateField(null=True)
    place_of_birth = models.CharField(max_length=20, default="")
    height = models.CharField(max_length=20, default="")
    weight_kg = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    weight_lbs = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    complexion = models.CharField(max_length=15, choices=ComplexionType.choices, default=ComplexionType.FAIR)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='matrimony/profile/')
    physical_status = models.CharField(max_length=10,default="Normal")
    marital_status = models.CharField(max_length=20,choices=MaritalStatus.choices, default=MaritalStatus.NEVER_MARRIED)
    children_count = models.PositiveIntegerField(default=0)
    mother_tongue = models.CharField(max_length=10,default="Bengali")
    religion = models.CharField(max_length=10, choices=ReligionType.choices, default=ReligionType.MUSLIM)
    blood_group = models.CharField(max_length=10,default="Not Know")
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = 'matrimony_profile_basicinformation'


class ProfileImage(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    location = models.ImageField(null=True, blank=True, upload_to='matrimony/profile/')
    label = models.CharField(max_length=100,default="")
    is_private = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.profile.code

    class Meta:
        db_table = 'matrimony_profile_profileimage'


class Citizenship(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    country = models.CharField(max_length=20,default="Bangladesh")
    status = models.CharField(max_length=20, choices=ResidentialStatus.choices, default=ResidentialStatus.CITIZEN)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.profile.code

    class Meta:
        db_table = 'matrimony_profile_citizenship'


class Location(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.CharField(max_length=20,default="Dhaka")
    state = models.CharField(max_length=20,default="Dhaka")
    country = models.CharField(max_length=20,default="Bangladesh")
    category = models.CharField(max_length=10, default="Present")
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.profile.code

    class Meta:
        db_table = 'matrimony_profile_location'


class Profession(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    employment_type = models.CharField(max_length=15, choices=EmploymentType.choices, default=EmploymentType.PRIVATE)
    occupation = models.CharField(max_length=20, default="")
    occupation_details = models.CharField(max_length=500, default="")
    organization = models.CharField(max_length=100, default="")
    annual_income = models.PositiveIntegerField(null=True)
    currency = models.CharField(max_length=10,default="BDT")
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.profile.code

    class Meta:
        db_table = 'matrimony_profile_profession'


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default="")
    institution = models.CharField(max_length=100, default="")
    passing_year = models.PositiveIntegerField(null=True)
    details = models.CharField(max_length=250, default="")
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.profile.code

    class Meta:
        db_table = 'matrimony_profile_education'


class Family(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=100, default="")
    father_occupation = models.CharField(max_length=50, default="")
    mother_name = models.CharField(max_length=100, default="")
    mother_occupation = models.CharField(max_length=50, default="")
    no_of_brothers = models.PositiveIntegerField(default=0)
    no_of_brothers_married = models.PositiveIntegerField(default=0)
    no_of_sisters = models.PositiveIntegerField(default=0)
    no_of_sisters_married = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=10, choices=FamilyType.choices, default=FamilyType.NUCLEAR)
    status = models.CharField(max_length=20, choices=FamilyStatus.choices, default=FamilyStatus.MIDDLE_CLASS)
    culture = models.CharField(max_length=15, choices=FamilyValue.choices, default=FamilyValue.MODERATE)
    location = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=250, default="")
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.profile.code

    class Meta:
        db_table = 'matrimony_profile_family'


class ExtraInformation(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    body_type = models.CharField(max_length=20, choices=BodyType.choices, default=BodyType.AVERAGE)
    eating_habit = models.CharField(max_length=20, choices=EatingHabit.choices, default=EatingHabit.NON_VEGETARIAN)
    drinking_habit = models.CharField(max_length=20, choices=DrinkingHabit.choices, default=DrinkingHabit.NO)
    smoking_habit = models.CharField(max_length=20, choices=SmokingHabit.choices, default=SmokingHabit.NO)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.profile.code

    class Meta:
        db_table = 'matrimony_profile_extrainformation'


class Preference(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    age_range = models.CharField(max_length=10, default="25-35")
    height_range = models.CharField(max_length=15, default="155-185")
    complexion = models.CharField(max_length=15, choices=ComplexionType.choices, default=ComplexionType.FAIR)
    marital_status = models.CharField(max_length=20,choices=MaritalStatus.choices, default=MaritalStatus.NEVER_MARRIED)
    mother_tongue = models.CharField(max_length=10,default="Bengali")
    religion = models.CharField(max_length=10, choices=ReligionType.choices, default=ReligionType.MUSLIM)
    city = models.CharField(max_length=20,default="Dhaka")
    country = models.CharField(max_length=20,default="Bangladesh")
    residential_status = models.CharField(max_length=20, choices=ResidentialStatus.choices, default=ResidentialStatus.CITIZEN)
    highest_education = models.CharField(max_length=20, default="")
    employment_type = models.CharField(max_length=15, choices=EmploymentType.choices, default=EmploymentType.PRIVATE)
    annual_income = models.PositiveIntegerField(null=True)
    currency = models.CharField(max_length=10,default="BDT")
    family_type = models.CharField(max_length=10, choices=FamilyType.choices, default=FamilyType.NUCLEAR)
    family_status = models.CharField(max_length=20, choices=FamilyStatus.choices, default=FamilyStatus.MIDDLE_CLASS)
    family_culture = models.CharField(max_length=15, choices=FamilyValue.choices, default=FamilyValue.MODERATE)
    eating_habit = models.CharField(max_length=20, choices=EatingHabit.choices, default=EatingHabit.NON_VEGETARIAN)
    drinking_habit = models.CharField(max_length=20, choices=DrinkingHabit.choices, default=DrinkingHabit.NO)
    smoking_habit = models.CharField(max_length=20, choices=SmokingHabit.choices, default=SmokingHabit.NO)
    description = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.profile.code

    class Meta:
        db_table = 'matrimony_profile_preference'


class FilterConfiguration(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    strict_age = models.BooleanField(default=False)
    strict_height = models.BooleanField(default=False)
    strict_complexion = models.BooleanField(default=False)
    strict_marital_status = models.BooleanField(default=False)
    strict_religion = models.BooleanField(default=False)
    strict_city = models.BooleanField(default=False)
    strict_employment_type = models.BooleanField(default=False)
    strict_family_type = models.BooleanField(default=False)
    strict_family_status = models.BooleanField(default=False)
    strict_family_culture = models.BooleanField(default=False)
    strict_eating_habit = models.BooleanField(default=False)
    strict_drinking_habit = models.BooleanField(default=False)
    strict_smoking_habit = models.BooleanField(default=False)

    def __str__(self):
        return self.profile.code

    class Meta:
        db_table = 'matrimony_profile_filterconfiguration'

