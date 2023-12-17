from applications.home.models import Home

# Proceso para recuperar telefono y correo del registro
def home_contact(request):
    try:
        home = Home.objects.latest('created')
    except Home.DoesNotExist:
        home = None

    if home:
        return {
            'phone': home.phone,
            'correo': home.contact_email,
            'youtube': home.youtube,
            'tiktok': home.tiktok,
        }
    else:
        return {
            'phone': 'Valor predeterminado para teléfono',
            'correo': 'Valor predeterminado para correo',
            'youtube': 'Valor predeterminado para youtube',
            'tiktok': 'Valor predeterminado para tiktok',
        }
