# models.py
from django.db import models
from django.contrib.auth.hashers import make_password


class Facility(models.Model):
    """
    Model representing a facility type (either government or private owned).
    """
    FACILITY_CHOICES = [
        ('government', 'Government-Owned'),
        ('private', 'Private-Owned'),
    ]
    
    facility_type = models.CharField(
        max_length=20,
        choices=FACILITY_CHOICES,
        default='private',  # Default to private if not selected
    )

    def __str__(self):
        return self.facility_type


class FacilityInput(models.Model):
    """
    Model representing the facility input details, including information
    about the director, location, and generated facility codes.
    """
    class FacilityType(models.TextChoices):
        HOSPITAL = 'hospital', 'Hospital'
        DENTAL_CLINIC = 'dental_clinic', 'Dental Clinic'
        CLINIC = 'clinic', 'Clinic'
        PHARMACY = 'pharmacy', 'Pharmacy'
        LABORATORY = 'laboratory', 'Laboratory'

    class DirectorTitle(models.TextChoices):
        MEDICAL_DIRECTOR = 'Medical Director', 'Medical Director'
        MATRON = 'Matron', 'Matron'
        PATRON = 'Patron', 'Patron'

    class State(models.TextChoices):
        ABIA = 'abia', 'Abia'
        ADAMAWA = 'adamawa', 'Adamawa'
        AKWA_IBOM = 'akwa_ibom', 'Akwa Ibom'
        ANAMBRA = 'anambra', 'Anambra'
        BAUCHI = 'bauchi', 'Bauchi'
        BAYELSA = 'bayelsa', 'Bayelsa'
        BENUE = 'benue', 'Benue'
        BORNO = 'borno', 'Borno'
        CROSS_RIVER = 'cross_river', 'Cross River'
        DELTA = 'delta', 'Delta'
        EBONYI = 'ebonyi', 'Ebonyi'
        EDO = 'edo', 'Edo'
        EKITI = 'ekiti', 'Ekiti'
        ENUGU = 'enugu', 'Enugu'
        GOMBE = 'gombe', 'Gombe'
        IMO = 'imo', 'Imo'
        JIGAWA = 'jigawa', 'Jigawa'
        KADUNA = 'kaduna', 'Kaduna'
        KANO = 'kano', 'Kano'
        KATSINA = 'katsina', 'Katsina'
        KEBBI = 'kebbi', 'Kebbi'
        KOGI = 'kogi', 'Kogi'
        KWARA = 'kwara', 'Kwara'
        LAGOS = 'lagos', 'Lagos'
        NASARAWA = 'nasarawa', 'Nasarawa'
        NIGER = 'niger', 'Niger'
        OGUN = 'ogun', 'Ogun'
        ONDO = 'ondo', 'Ondo'
        OSUN = 'osun', 'Osun'
        OYO = 'oyo', 'Oyo'
        PLATEAU = 'plateau', 'Plateau'
        RIVERS = 'rivers', 'Rivers'
        SOKOTO = 'sokoto', 'Sokoto'
        TARABA = 'taraba', 'Taraba'
        YOBE = 'yobe', 'Yobe'
        ZAMFARA = 'zamfara', 'Zamfara'
        FCT = 'fct', 'Federal Capital Territory (Abuja)'

    class LGA(models.TextChoices):
        ABAK = 'abak', 'Abak'
        EASTERN_OBOLO = 'eastern_obolo', 'Eastern Obolo'
        EKET = 'eket', 'Eket'
        ESIT_EKET = 'esit_eket', 'Esit Eket'
        ESSIEN_UDIM = 'essien_udim', 'Essien Udim'
        ETIM_EKPO = 'etéim_ekpo', 'Etim Ekpo'
        ETINAN = 'etéinan', 'Etinan'
        IBENO = 'ibeno', 'Ibeno'
        IBIONO_IBOM = 'ibiono_ibom', 'Ibiono Ibom'
        IKA = 'ika', 'Ika'
        IKONO = 'ikono', 'Ikono'
        IKOT_ABASI = 'ikot_abasi', 'Ikot Abasi'
        IKOT_EKPENE = 'ikot_ekpene', 'Ikot Ekpene'
        INI = 'ini', 'Ini'
        ITU = 'itu', 'Itu'
        MBO = 'mbo', 'Mbo'
        MKPAT_ENIN = 'mkpat_enin', 'Mkpat Enin'
        NSIT_ATAI = 'nsit_atai', 'Nsit Atai'
        NSIT_IBOM = 'nsit_ibom', 'Nsit Ibom'
        NSIT_UBIUM = 'nsit_ubium', 'Nsit Ubium'
        OBOT_AKARA = 'obot_akara', 'Obot Akara'
        OKOBO = 'okobo', 'Okobo'
        ONNA = 'onna', 'ONNA'
        ORON = 'oron', 'Oron'
        UDUNG_UKO = 'udung_uko', 'Udung Uko'
        UKANAFUN = 'ukanafun', 'Ukanafun'
        URUAN = 'uruan', 'Uruan'
        URUE_OFFONG_ORUKO = 'urue_offong_oruko', 'Urue-Offong/Oruko'
        UYO = 'uyo', 'Uyo'
        OTHER_STATE_LOCAL_GOVERNMENT_AREA = 'other_state_local_government_area', 'Other State Local Government Area'

    FACILITY_CODES = {
        'hospital': 'HAKS',
        'dental_clinic': 'DAKS',
        'clinic': 'CAKS',
        'pharmacy': 'PAKS',
        'laboratory': 'LATS',
    }

    # Added the `facility_ownership` field
    FACILITY_OWNERSHIP_CHOICES = [
        ('government', 'Government-Owned'),
        ('private', 'Private-Owned'),
    ]
    
    facility_ownership = models.CharField(
        max_length=20,
        choices=FACILITY_OWNERSHIP_CHOICES,
        default='private',  # Default to private if not selected
    )
    
    facility_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    state = models.CharField(max_length=100, choices=State.choices)
    lga = models.CharField(max_length=100, choices=LGA.choices)
    director_title = models.CharField(max_length=50, choices=DirectorTitle.choices)
    director_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    nin = models.CharField(max_length=11, unique=True)
    facility_type = models.CharField(max_length=50, choices=FacilityType.choices)
    password = models.CharField(max_length=255)
    serial_code = models.CharField(max_length=20, unique=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Override save method to:
        1. Generate serial_code if not provided.
        2. Hash the password before saving to database.
        """
        if not self.serial_code:
            # Generate serial code based on facility type and count
            facility_code = self.FACILITY_CODES.get(self.facility_type, 'GEN')  # Default to 'GEN'
            count = FacilityInput.objects.filter(facility_type=self.facility_type).count() + 1
            self.serial_code = f"{facility_code}{count:04d}"

        # Hash password before saving to ensure security
        self.password = make_password(self.password)

        # Call the parent save method
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.facility_name} - {self.serial_code}"