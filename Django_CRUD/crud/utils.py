from .models import ParcelList,DriverList


def decide_compartment(parcel_postcode):
    try:

        compartment = DriverList.objects.filter(min_postcode__lte=parcel_postcode).filter(max_postcode__gte=parcel_postcode).values_list('compartment', flat=True)
        destination = DriverList.objects.filter(min_postcode__lte=parcel_postcode).filter(max_postcode__gte=parcel_postcode).values_list('zone', flat=True)

        compartment = int(compartment[0])
        destination = str(destination[0])

    except:
        compartment = 0
        destination = str("OTHERS")

    return compartment,destination
