from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "base/home.html")

def executives(request):
    executives_data = {
        "Presidents": [
            {"name": "Connor Lin", "role": "President"},
            {"name": "Khaleel Pardhan", "role": "President"},
        ],
        "Executive Team": [
            {"name": "Jacob Lee", "role": "Executive of Marketing & Outreach"},
            {"name": "Manmeet Badh", "role": "Executive of Marketing & Outreach"},
            {"name": "Nadar Gujral", "role": "Executive of Leadership"},
        ],
        "Core Team": [
            {"name": "Ahnaf Kamal", "role": "Treasurer"},
            {"name": "Qasim Pardhan", "role": "Secretary"},
        ],
        "Finance": [
            {"name": "Allie Wong", "role": "Trainer"},
        ],
        "Marketing": [
            {"name": "Manmeet Badh", "role": "Trainer"},
        ],
        "Business Admin": [
            {"name": "Eeshan Agarwal", "role": "Trainer"},
            {"name": "Connor Lin", "role": "Trainer"},
        ],
        "Hospitality": [
            {"name": "Jacob Lee", "role": "Trainer"},
        ]
    }

    return render(request, "base/executives.html", {"executives": executives_data})

def sponsors(request):
    return render(request, "base/sponsors.html")